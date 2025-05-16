
# 📚 読書ログアプリ（Flask × SQLite）

このアプリは Flask と SQLite を用いて開発された、簡単な読書ログ管理ツールです。  
本のタイトル、著者、感想を登録・編集・削除できます。

---

## 📌 主な機能

- 本の登録（タイトル / 著者 / 感想）
- 本の一覧表示
- 本の編集
- 本の削除（確認ダイアログあり）
- Bootstrap による簡単なスタイリング

---

## 🛠 使用技術

- Python 3.x
- Flask
- SQLite
- HTML (Jinja2 テンプレート)
- Bootstrap 5

---

## 🚀 起動方法（ローカル環境）

1. このリポジトリをクローン  
   ```bash
   git clone https://github.com/Joyful-c/booklog-flask.git
   cd booklog-flask
   ```

2. 仮想環境（任意）を作成・有効化  
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows の場合
   ```

3. Flask をインストール  
   ```bash
   pip install flask
   ```

4. 初期データベースを作成  
   ```bash
   python init_db.py
   ```

5. アプリを起動  
   ```bash
   python app.py
   ```

6. ブラウザでアクセス  
   → http://localhost:5000

---

## 📁 ディレクトリ構成

```
booklog-flask/
│
├─ templates/
│   ├─ index.html        # 一覧ページ
│   ├─ add.html          # 登録フォーム
│   └─ edit.html         # 編集フォーム
│
├─ app.py                # メインアプリ
├─ init_db.py            # 初期DB作成スクリプト
├─ .gitignore
└─ README.md             # このファイル
```

---

## 🔒 補足

- `.gitignore` により `books.db` は Git に含まれていません。  
  初回実行時に `python init_db.py` で自動作成されます。
- このアプリは学習・ポートフォリオ目的で作成されています。
- ---

## 🗒 制作メモ

このアプリは、Flask・Git・GitHub の学習を目的として、プログラミング初学者が一から作成したものです。  
小さな機能を少しずつ積み重ねながら、Web開発の基礎を学びました。


---

## 👤 作者

**Joyful-c**  
GitHub: https://github.com/Joyful-c
