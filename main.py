import yt_dlp
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import whisper

def download_progress_hook(d):
    if d['status'] == 'downloading':
        progress = d.get('_percent_str', '0%')
        print(f"\rDownloading: {d['filename']} - {progress}", end='', flush=True)
    elif d['status'] == 'finished':
        print(f"\nFinished downloading: {d['filename']}")

def download_video(video_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'no_warnings': True,
        'quiet': True,
        'progress_hooks': [download_progress_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video_url, download=False)
            filename = ydl.prepare_filename(info)
            ydl.download([video_url])
            return filename.rsplit('.', 1)[0] + '.mp3'
        except Exception as e:
            print(f"Error downloading {video_url}: {str(e)}")
            return None

def get_channel_videos(channel_url):
    ydl_opts = {
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)
        if 'entries' in result:
            return [entry['url'] for entry in result['entries']]
    return []

def download_channel_videos(channel_url, output_path, max_workers=4):
    os.makedirs(output_path, exist_ok=True)
    video_urls = get_channel_videos(channel_url)

    downloaded_files = []
    with tqdm(total=len(video_urls), desc="Overall Progress") as pbar:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(download_video, url, output_path) for url in video_urls]
            for future in as_completed(futures):
                result = future.result()
                if result:
                    downloaded_files.append(result)
                pbar.update(1)
    
    return downloaded_files

def transcribe_audio(audio_file, model):
    result = model.transcribe(audio_file)
    return result["text"]

def transcribe_audios(audio_files, output_path):
    model = whisper.load_model("base")
    with tqdm(total=len(audio_files), desc="Transcription Progress") as pbar:
        for audio_file in audio_files:
            transcript = transcribe_audio(audio_file, model)
            transcript_path = os.path.join(output_path, os.path.splitext(os.path.basename(audio_file))[0] + '.txt')
            with open(transcript_path, 'w', encoding='utf-8') as f:
                f.write(transcript)
            pbar.update(1)

if __name__ == "__main__":
    channel_url = "https://www.youtube.com/@channel_name"  # Replace with the actual channel URL
    output_path = "local-path" # Replace with directory to save the videos
    
    print("Starting video downloads...")
    downloaded_files = download_channel_videos(channel_url, output_path)
    
    print("\nStarting transcription...")
    transcribe_audios(downloaded_files, output_path)
    
    print("All processing completed.")
