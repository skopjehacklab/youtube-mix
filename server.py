from flask import Flask, render_template, request, send_from_directory, g
import os
import subprocess
import glob
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
		os.makedirs('./music/')
	except OSError:
		pass
		
	os.chdir('./music')

	playlist_txt = open("playlist.txt",'w')
	playlist_txt.write(playlist)
	playlist_txt.close()

	subprocess.call(["youtube-dl", "--output", "%(autonumber)s.%(ext)s",
		"--extract-audio", "--audio-format", "aac", "--audio-quality", "0",
		"--add-metadata", "--no-overwrites", "--continue", "--batch-file",
		"playlist.txt"])

	is_a_song = lambda p: '.aac' in p and p != 'out.aac'
	songs_filenames = filter(is_a_song, sorted(os.listdir('./')))
	
	ffmpeg_concat = 'concat:' + '|'.join(songs_filenames) # 01.aac|02.aac
	
	subprocess.call(["ffmpeg", "-i", ffmpeg_concat, '-acodec', 'copy', '-y', 'out.aac'])
	
	for f in glob.glob('0*.aac'): # uzhas (tomi)! :D
		os.remove(f)
	os.remove('playlist.txt')
	
	os.chdir('..')

	return send_from_directory('./music', 'out.aac', as_attachment=True)

if __name__ == "__main__":
    app.run('localhost', 5001)
