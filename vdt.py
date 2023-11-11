from pytube import YouTube
import os 



#Create a downloads directory 
if not os.path.exists('downloads'):
    os.makedirs('downloads')



while True:
    # URL of the YouTube video you want to download
    video_url = input("Enter URL: ")
    print("\033[32mDownloading...........\033[0m")

    if video_url.lower() == 'q' :
        break #Exit the loop if user enter 'q'

    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream (usually the first stream)
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the current working directory
        video_stream.download(output_path='downloads')

        print(f"\033[34mDownloaded\033[0m {yt.title}")

    except Exception as e:
        print("\033[31;1mError Url: " + str(e) + "\033[0m")