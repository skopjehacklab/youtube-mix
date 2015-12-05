from flask import Flask
app = Flask(__name__)
app.debug = True

index_html = open("index.html").read()

@app.route("/")
def index():
    return index_html

@app.route("/generate", methods=["POST"])
def generate():
	return "Hello from generate"

if __name__ == "__main__":
    app.run()