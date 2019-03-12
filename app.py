from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<thml>Hi 八幡平!</html>"


@app.route("/hachimantai")
def hello_hachimantai():
    return "<html>スパルタキャンプ in八幡平</html>"


"""
課題
http://127.0.0.1:5000/goodbye というURL を入力したら、「Good Bye!」 と表示されるようにして下さい

"""


@app.route("/goodbye")
def goodbye():
    return "<html>Good Bye!</html>"


if __name__ == '__main__':
    app.run(debug=True)
