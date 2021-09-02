from pytube import YouTube
import os

def main():
    yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n-> ")))
    type_ = input("1- Only Audio \n2- Video + Audio\n-> ")
        
    if type_ == "1":
        video = yt.streams.filter(only_audio=True).first()

        print("\n\nEnter the destination (Hit Enter for current directory)")
        destination = str(input("-> ")) or '.'

        out_file = video.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    elif type_ == "2":
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print("\n\nEnter the destination (Hit Enter for current directory)")
        destination = str(input("-> ")) or '.'
        out_file = video.download(output_path=destination)
    else:
        print("Try again...")
        main()

    print(yt.title + " has been successfully downloaded.")

if __name__ == '__main__':
    main()