# Instructions for Running the YouTube Channel Audio Downloader

## macOS and Linux

1. Open Terminal
2. Navigate to the project directory:
   ```
   cd path/to/youtube_channel_downloader
   ```
3. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
5. Install FFmpeg (if not already installed):
   - macOS (using Homebrew):
     ```
     brew install ffmpeg
     ```
   - Linux (Ubuntu/Debian):
     ```
     sudo apt-get update
     sudo apt-get install ffmpeg
     ```
6. Run the script:
   ```
   python main.py
   ```

## Windows

1. Open Command Prompt or PowerShell
2. Navigate to the project directory:
   ```
   cd path\to\youtube_channel_downloader
   ```
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
5. Install FFmpeg:
   - Download the FFmpeg build from https://ffmpeg.org/download.html
   - Extract the archive and add the `bin` folder to your system PATH
6. Run the script:
   ```
   python main.py
   ```

## Google Colab

1. Create a new Colab notebook
2. Run the following cells:

```python
!pip install yt-dlp

import os

# Create the main.py file
%%writefile main.py
# Paste the contents of main.py here

# Run the script
!python main.py

# Download the results
from google.colab import files
!zip -r downloaded_videos.zip downloaded_videos
files.download('downloaded_videos.zip')
```

Note: You may need to modify the script to use a specific output path that works with Colab's file system.
