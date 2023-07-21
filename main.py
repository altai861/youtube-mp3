import pytube
import os

url = input('Youtube video link')
video = pytube.YouTube(url)
print('Title: ', video.title)
print("Downloading...")
out_path = video.streams.filter(only_audio=True).first().download()
new_name = os.path.splitext(out_path)
os.rename(out_path, new_name[0]+'.mp3')
print('Done...')