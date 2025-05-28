import whisper
import os

model = whisper.load_model("small")

def transcribe_audio(file_path: str, language="pt") -> dict:
    result = model.transcribe(file_path, language=language)
    return result
