from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
import os
from app.services import whisper_service, subtitles_service, video_service
from app.core.config import STATIC_DIR

router = APIRouter()

@router.post("/generate")
def generate_subtitles(file: UploadFile = File(...), language: str = Form("pt")):
    filename = file.filename
    file_path = os.path.join(STATIC_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    result = whisper_service.transcribe_audio(file_path, language)

    base_name = os.path.splitext(filename)[0]

    txt_path = os.path.join(STATIC_DIR, f"{base_name}.txt")
    srt_path = os.path.join(STATIC_DIR, f"{base_name}.srt")
    ass_path = os.path.join(STATIC_DIR, f"{base_name}.ass")
    output_video_path = os.path.join(STATIC_DIR, f"{base_name}_subtitled.mp4")

    subtitles_service.save_as_txt(result, txt_path)
    subtitles_service.save_as_srt(result, srt_path)
    subtitles_service.save_as_ass(result, ass_path)

    video_service.render_video_with_subtitles(file_path, ass_path, output_video_path)

    return {
        "txt": txt_path,
        "srt": srt_path,
        "ass": ass_path,
        "video": output_video_path
    }

@router.get("/download")
def download_file(file_path: str):
    return FileResponse(file_path)
