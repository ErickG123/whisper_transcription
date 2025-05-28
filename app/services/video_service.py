import subprocess
import os

def render_video_with_subtitles(input_video, subtitles_file, output_video):
    subtitles_file_escaped = subtitles_file.replace("\\", "/").replace(":", "\\:")

    cmd = [
        "ffmpeg",
        "-i", input_video,
        "-vf", f"subtitles='{subtitles_file_escaped}'",
        "-c:a", "copy",
        output_video
    ]

    print("Comando:", " ".join(cmd))

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print("Erro no ffmpeg:")
        print(e.stdout)
        print(e.stderr)
        raise
