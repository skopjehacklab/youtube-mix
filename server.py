from flask import Flask, render_template, request
import os
import subprocess
app = Flask(__name__, static_url_path='/static')
app.debug = True

@app.route("/")
def home():
    return render_template("index.html", title = 'Index')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/generate", methods=["POST"])
def generate():
	playlist = request.form["playlist"]

	

	try:
		os.makedirs('./Music/')
	except OSError:
		pass

	playlist_txt = open("Music/playlist.txt",'w')
	playlist_txt.write(playlist)
	playlist_txt.close()

	subprocess.call(["youtube-dl", "--output", "Music/%(autonumber)s.%(ext)s", "--extract-audio", "--audio-format", "mp3", "--audio-quality", "9", "--add-metadata", "--no-overwrites", "--continue", "--batch-file", "Music/playlist.txt"])

	songs_txt = open("Music/songs.txt",'a')
	songs_txt.close()
	

	return "Hello from generate"

if __name__ == "__main__":
    app.run('localhost', 5001)
