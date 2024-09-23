import json
import os
from typing import List

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field


# 環境変数の読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEYが設定されていません。.envファイルを確認してください。")

# OpenAIクライアントの初期化
client = OpenAI(api_key=api_key)


class Ingredient(BaseModel):
    name: str
    amount: str
    unit: str


class Step(BaseModel):
    description: str
    time_minutes: int = Field(ge=0)


class Recipe(BaseModel):
    title: str
    description: str
    servings: int = Field(gt=0)
    ingredients: List[Ingredient]
    steps: List[Step]
    total_time_minutes: int = Field(ge=0)
    difficulty: str = Field(pattern="^(簡単|中級|難しい)$")


def generate_recipe(prompt: str) -> Recipe:
    try:
        completion = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system",
                 "content": "あなたは創造的なシェフで、ユーザーの要望に基づいてレシピを生成します。"
                 "レシピはJSON形式で出力してください。"},
                {"role": "user",
                 "content": f"以下の要望に基づいてレシピを生成し、JSON形式で返してください：{prompt}"}
            ],
            response_format={"type": "json_object"},
            functions=[{
                "name": "create_recipe",
                "description": "ユーザーの要望に基づいてレシピを生成し、JSON形式で返します。",
                "parameters": Recipe.model_json_schema()
            }],
            function_call={"name": "create_recipe"}
        )
        recipe_data = json.loads(
            completion.choices[0].message.function_call.arguments)
        return Recipe(**recipe_data)
    except Exception as e:
        print(f"レシピの生成中にエラーが発生しました: {e}")
        return None


def print_recipe(recipe: Recipe):
    print(f"\n{'=' * 40}")
    print(f"レシピ: {recipe.title}")
    print(f"{'=' * 40}")
    print(f"説明: {recipe.description}")
    print(f"難易度: {recipe.difficulty}")
    print(f"調理時間: {recipe.total_time_minutes}分")
    print(f"材料 ({recipe.servings}人分):")
    for ing in recipe.ingredients:
        print(f"- {ing.name}: {ing.amount} {ing.unit}")
    print("\n調理手順:")
    for i, step in enumerate(recipe.steps, 1):
        print(f"{i}. {step.description} (所要時間: {step.time_minutes}分)")


def main():
    while True:
        user_prompt = input("どんなレシピを生成しますか？（終了するには 'q' を入力）: ")
        if user_prompt.lower() == 'q':
            print("プログラムを終了します。")
            break

        recipe = generate_recipe(user_prompt)
        if recipe:
            print_recipe(recipe)

            # JSON形式でも出力するオプション
            json_output = input("JSONフォーマットでも出力しますか？ (y/n): ").lower()
            if json_output == 'y':
                print(json.dumps(recipe.dict(), indent=2, ensure_ascii=False))

        print("\n")  # レシピ間の空行


if __name__ == "__main__":
    main()
