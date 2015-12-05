from flask import Flask
app = Flask(__name__)

index_html = open("index.html").read()

@app.route("/")
def hello():
    return index_html

if __name__ == "__main__":
    app.run()