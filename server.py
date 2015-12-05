from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')



@app.route("/")
def home():
    return render_template("index.html", title = 'Index')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run('localhost', 5001)