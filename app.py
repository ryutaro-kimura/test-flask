import pyrebase
from flask import *
 
config = {
    apiKey: "AIzaSyD1zCgL2wBkrHXOsVAo7ao4UsmJ5HA-3Y8",
    authDomain: "test-flask-database.firebaseapp.com",
    projectId: "test-flask-database",
    storageBucket: "test-flask-database.appspot.com",
    messagingSenderId: "708005631553",
    appId: "1:708005631553:web:22cc023dbd1d316f7798c0"
}


firebase = pyrebase.initialize_app(config)

db = firebase.database()
# db.child("names").push({"name":"kota"})
# db.child("names").push({"name":"take"})

# ルートを指定、メソッドはGET、POST
@app.route('/', methods=['GET', 'POST'])

# basic関数を定義
def basic():
    # POSTでリクエストされたら
    if request.method == 'POST':
        # form['submit']のvalueが'add'であれば
        if request.form['submit'] == 'add':
            # formから値を取得
            name = request.form['name']
            # 値をfirebase上のtodoに書き込む
            db.child("todo").push(name)
            # firebaseから値を取得
            todo = db.child("todo").get()
            # toに値を代入
            to = todo.val()
            # index.htmlに 値toを返す
            return render_template('index.html', t=to.values())
        # form['submit']のvalueが'delete'であれば
        elif request.form['submit'] == 'delete':
            # firebaseのdbであるtodoを削除
            db.child("todo").remove()
            # 元のindex.htmlを返す
            return render_template('index.html',)
    # それ以外は、index.htmlを返す
    return render_template('index.html')

if __name__ == '__main__':
    #処理の実行
    app.run(debug=True)