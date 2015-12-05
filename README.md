# Youtube Mix

Takes a list of Youtube videos, concatenates them into a mix.

## The process

* The user pastes a list of Youtube links into an HTML form, clicks "Submit"
* The server downloades the files using `yt-download`
* Then, it concatenates them using FFmpeg
* The file download beigins

### yt-download command

`youtube-dl --output '%(autonumber)s.%(ext)s' --extract-audio --audio-format mp3 --audio-quality 9 --add-metadata --no-overwrites --continue --batch-file playlist.txt`

### ffmpeg concat

`songs.txt`:

```
# this is a comment
file '/path/to/file1'
file '/path/to/file2'
file '/path/to/file3'
```

Command:

`ffmpeg -f concat -i mylist.txt -c copy output`

## Things to consider:

* How many songs do we allow in a playlist?
* What happens if some songs are really long?
* Where will we host it? Some Youtube videos are banned in some countries. Proxy?
* We're executing shell commands. Security concerns? Review yt-download source code.
* Processor / RAM / disk memory / bandwidth limits and concerns?
* How can we improve the GUI?
   