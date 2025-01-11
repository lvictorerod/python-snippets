import argparse
import os
from moviepy.editor import *

VALID_EXTENSIONS = [".mp4", ".mov", ".avi"]  # Added more extensions

def convert_to_wav(video_path, output_path):
    """Converts a video file to .wav audio."""
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(output_path, bitrate="320k")
        # Log success
    except Exception as e:
        # Log error
        print(f"Error processing {video_path}: {e}")

def main(input, output, overwrite=False):
    # Check if the paths are valid
    if not os.path.isdir(input):
        print(f"Error: {input} is not a valid path.")
        return
    if not os.path.isdir(output):
        print(f"Error: {output} is not a valid path.")
        return

    # Traverse the path and find video files
    for root, dirs, files in os.walk(input):
        for file in files:
            if any(file.lower().endswith(ext) for ext in VALID_EXTENSIONS):
                output_path = os.path.join(output, f"{os.path.splitext(file)[0]}.wav")
                if os.path.exists(output_path) and not overwrite:
                    # Log skipping
                    continue
                convert_to_wav(os.path.join(root, file), output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert video files to .wav audio format")
    parser.add_argument("input", type=str, help="Local path of the folder containing the video files")
    parser.add_argument("output", type=str, help="Local path of the folder where the .wav audio files will be saved")
    args = parser.parse_args()

    main(args.input, args.output)
