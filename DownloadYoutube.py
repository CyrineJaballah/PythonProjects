from pytube import YouTube
import subprocess

def download_youtube_audio(url):
    # Download the YouTube video
    youtube = YouTube(url)
    video = youtube.streams.filter(only_audio=True).first()
    video.download()

    # Convert the video to MP3 using ffmpeg
    video_filename = video.default_filename
    audio_filename = video_filename.replace(".mp4", ".mp3")
    subprocess.run(['ffmpeg', '-i', video_filename, audio_filename])

    print("Download completed. Audio saved as:", audio_filename)

# Example usage
url = input("Enter YouTube video URL: ")
download_youtube_audio(url)
