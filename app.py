from pytube import YouTube
from moviepy.editor import *


def download_video(url, output_path=None):
    
    try:
        print("Downloading video...")
        yt = YouTube(url)

        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if output_path is None:
            output_path = video_stream.default_filename

        video_stream.download(output_path)
        print("Download concluded!")
        return output_path
    
    except Exception as e:
        print("An error has ocurred:", e)
        
        
def mp4_to_mp3(mp4, mp3):
    mp4 = AudioFileClip(mp4)
    mp4.write_audiofile(mp3)
    mp4.close()
    

if __name__ == "__main__":
    video_url = input("Video URL: ")
    output_path = download_video(video_url)
    
    mp4_path = f"{output_path}/{output_path}"
    mp3_path = f"{output_path}/{output_path[:-4]}.mp3"
    
    mp4_to_mp3(mp4_path, mp3_path) 