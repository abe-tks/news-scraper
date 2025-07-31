# ニュース見出し収集ツール

このツールはPythonで作成したシンプルなWebスクレイピングツールです。  
Yahoo!ニュースの見出しを取得してCSVファイルに保存します。

---

## 動作環境

- Python 3.x  
- ライブラリ: requests, beautifulsoup4

---

## インストール方法

必要なライブラリをインストールしてください。

```bash
pip install requests beautifulsoup4
使い方
ターミナルやコマンドプロンプトでプロジェクトフォルダに移動します。

以下のコマンドを実行してニュースの見出しを取得します。

bash

python news_scraper.py
実行後、news_headlines.csv というファイルが作成されます。
そこに最新のニュース見出しとURLが保存されます。

