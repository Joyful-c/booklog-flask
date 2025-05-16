from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# トップページ：一覧表示
@app.route("/")
def index():
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return render_template("index.html", books=books)

# 本の追加
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        memo = request.form["memo"]

        conn = sqlite3.connect("books.db")
        conn.execute("INSERT INTO books (title, author, memo) VALUES (?, ?, ?)",
                     (title, author, memo))
        conn.commit()
        conn.close()

        return '''
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>保存完了</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light py-5">
  <div class="container text-center">
    <h2 class="mb-4">📘 保存完了！</h2>
    <a href="/" class="btn btn-primary">トップページに戻る</a>
  </div>
</body>
</html>
'''
    else:
        return render_template("add.html")

# 編集機能
@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        memo = request.form["memo"]

        conn.execute("UPDATE books SET title=?, author=?, memo=? WHERE id=?",
                     (title, author, memo, book_id))
        conn.commit()
        conn.close()
        return redirect("/")
    else:
        book = conn.execute("SELECT * FROM books WHERE id=?", (book_id,)).fetchone()
        conn.close()
        return render_template("edit.html", book=book)

# 削除機能
@app.route("/delete/<int:book_id>", methods=["POST"])
def delete(book_id):
    conn = sqlite3.connect("books.db")
    conn.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
