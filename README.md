# youtube-to-mp3
A simple script to donwload your musics from youtube

![Alt Text](https://github.com/GuilhermeVBeira/youtube-to-mp3/raw/main/example.gif)
## requirements 
  - [ffmpeg](https://ffmpeg.org/download.html)
  - python > 3.7

## How to use
fill up the music.txt with the links videos from youtube and run the scrip
```bash
python downloader.py
```

## copy to your usb-stick
if you want download and copy all the content directly to your usb-stick you can run this command

```bash
python downloader.py &&  cp -n * /media/$USER/<USB-STICK-NAME>
```
