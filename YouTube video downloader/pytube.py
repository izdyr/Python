from pytube import YouTube

# Ask user for the YouTube video URL
url = input("Please type the YouTube video URL: ")

# Create an instance of the YouTube class and get the video stream
yt = YouTube(url)
video = yt.streams.first()

# Download the video
print("Downloading video...")
video.download()

print("Video downloaded successfully!")
