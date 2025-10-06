import requests
import os
import sys

def download_audio():
    """Download audio file and save it as test_audio.mp3 in the same directory as index.html"""
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the audio file path
    audio_file_path = os.path.join(script_dir, "test_audio.mp3")
    
    # URL of the audio file to download
    # Using the same SoundHelix sample audio from your HTML player
    audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    
    try:
        print("Downloading audio file...")
        
        # Make the request to download the audio
        response = requests.get(audio_url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Save the file
        with open(audio_file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Audio downloaded successfully!")
        print(f"Saved as: {audio_file_path}")
        
        # Verify the file exists and get its size
        if os.path.exists(audio_file_path):
            file_size = os.path.getsize(audio_file_path)
            print(f"File size: {file_size / 1024:.2f} KB")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading audio: {e}")
        return False
    except IOError as e:
        print(f"Error saving file: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def check_index_html():
    """Check if index.html exists in the same directory"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(script_dir, "index.html")
    
    if os.path.exists(index_path):
        print("✓ index.html found in the same directory")
        return True
    else:
        print("⚠ Warning: index.html not found in the same directory")
        print(f"Looking for: {index_path}")
        return False

if __name__ == "__main__":
    print("Audio Downloader Script")
    print("=" * 30)
    
    # Check if index.html exists
    check_index_html()
    print()
    
    # Download the audio
    success = download_audio()
    
    if success:
        print("\n✅ Download completed successfully!")
        print("You can now update your index.html to use 'test_audio.mp3' as the audio source.")
    else:
        print("\n❌ Download failed!")
        sys.exit(1)