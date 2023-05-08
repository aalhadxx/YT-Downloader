# Download YouTube Videos with Python and Pytube Library

Learn how to use the **Pytube library** in Python to download YouTube videos. This code uses exception handling to handle errors and provides informative output messages.

## How to Use

1. **Configure a virtual environment** by running `python3 -m venv myenv` in the command line. Activate the virtual environment by running `source myenv/bin/activate` on Linux or macOS, or `myenv\Scripts\activate` on Windows.
2. **Clone the repository** to your local machine.
3. **Install the Pytube library** using `pip install pytube`.
4. **Add the YouTube video links** that you want to download to the `links` list in the `script` file.
5. **Run the `script.py` file.**
6. The videos will be downloaded to your default download folder.

## Code Description

This Python code shows how to download YouTube videos using the Pytube library. The code takes in a list of YouTube video links and iterates through each link to download the video with the highest resolution. The code uses **exception handling** to catch any errors that may occur during the download process, such as invalid URLs or unavailable videos. **Informative output messages** are displayed to inform the user of the status of each download.
