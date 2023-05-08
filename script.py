import pytube

links = ["paste yt link here", "more if you need"]

for link in links:
    try:
        yt = pytube.YouTube(link)
        video = yt.streams.get_highest_resolution()
        filename = video.default_filename
        video.download()
        print(f"{filename} downloaded successfully from {link}.")
    except pytube.exceptions.RegexMatchError:
        print(f"Could not download {link}. Invalid URL.")
    except pytube.exceptions.VideoUnavailable:
        print(f"Could not download {link}. Video is unavailable.")
    except OSError as e:
        print(f"Could not download {link}. {e}")
