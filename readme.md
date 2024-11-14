# YouTube Channel Audio Downloader

This project allows you to download all videos from a YouTube channel and convert them to MP3 format. It uses the `yt-dlp` library to handle the downloading and conversion process.

## Features

- Downloads all videos from a specified YouTube channel
- Converts videos to MP3 format
- Displays progress for each download
- Handles errors gracefully

## Requirements

- Python 3.6+
- yt-dlp
- FFmpeg

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/youtube-channel-downloader.git
   cd youtube-channel-downloader
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Install FFmpeg:
   - On macOS (using Homebrew):
     ```
     brew install ffmpeg
     ```
   - On Windows:
     Download from https://ffmpeg.org/download.html and add it to your system PATH.

## Usage

1. Open `main.py` and replace `CHANNEL_ID_HERE` with the actual YouTube channel ID or full channel URL.
2. Run the script:
   ```
   python main.py
   ```

The downloaded MP3 files will be saved in the `downloaded_videos` directory.

## License

This project is open-source and available under the MIT License.
