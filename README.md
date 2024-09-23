# Recipe Generator

このプロジェクトは、OpenAI GPT-4 APIを使用して、ユーザーの入力に基づいてレシピを自動生成するPythonスクリプトです。

## フォルダ構造

```
recipe_generator/
│
├── recipe_generator.py  # メインのPythonスクリプト
├── .env                 # 環境変数ファイル（GitHubにはアップロードしない）
├── .env.example         # .envファイルのサンプル
├── requirements.txt     # 依存関係リスト
├── .gitignore           # Gitの無視リスト
└── README.md            # このファイル
```

## セットアップ

1. このリポジトリをクローンします：
   ```
   git clone https://github.com/yourusername/recipe-generator.git
   cd recipe-generator
   ```

2. 仮想環境を作成し、アクティベートします：
   ```
   python -m venv venv
   source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
   ```

3. 必要なパッケージをインストールします：
   ```
   pip install -r requirements.txt
   ```

4. `.env.example` ファイルを `.env` にコピーし、OpenAI APIキーを設定します：
   ```
   cp .env.example .env
   ```
   そして、`.env` ファイルを編集し、`YOUR_API_KEY_HERE` を実際のAPIキーに置き換えます。

## 使用方法

スクリプトを実行するには：

```
python recipe_generator.py
```

プロンプトが表示されたら、生成したいレシピの種類を入力します。例えば：
- "ベジタリアン向けの簡単な夏のパスタ料理"
- "子供が喜ぶチョコレートケーキ"

'q' を入力するとプログラムが終了します。

## 注意事項

- このスクリプトはOpenAI APIを使用するため、APIの使用量に応じて料金が発生する可能性があります。
- 生成されたレシピは、常に調理前に内容を確認し、安全性を確保してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 貢献

バグの報告や機能の提案は、GitHubのIssueを通じて行ってください。プルリクエストも歓迎します！

```

次に、`.env.example` ファイルの内容を作成しましょう：

```plaintext
# OpenAI API Key
OPENAI_API_KEY=YOUR_API_KEY_HERE

# Optional: OpenAI API Organization ID (if you're using one)
# OPENAI_ORG_ID=your_org_id_here

# Optional: Model name (if you want to change it easily)
# MODEL_NAME=gpt-4-turbo-preview

```

これらのファイルをプロジェクトに追加することで、以下の利点があります：

1. README.md:
   - プロジェクトの概要、セットアップ手順、使用方法を明確に説明します。
   - フォルダ構造を視覚的に示し、各ファイルの目的を説明します。
   - 潜在的な利用者や貢献者にとって、プロジェクトの理解と使用が容易になります。

2. .env.example:
   - 必要な環境変数を示し、ユーザーが自身の `.env` ファイルを正しく設定できるようにします。
   - API キーなどの機密情報をリポジトリに直接含めることを避けつつ、必要な設定を明示できます。

GitHub にアップロードする前の最終確認事項：

1. `.gitignore` ファイルに `.env` が含まれていることを確認し、API キーが誤ってコミットされないようにします。
2. `requirements.txt` ファイルが存在し、必要な全ての依存関係（openai、pydantic、python-dotenv）が列挙されていることを確認します。
3. コードにコメントを追加し、複雑な部分を説明することを検討してください。
4. ライセンスファイル（例：LICENSE）を追加することを検討してください。

これらの準備が整えば、プロジェクトを GitHub にアップロードする準備が整います。コミットする前に、機密情報が含まれていないことを再度確認してください。
