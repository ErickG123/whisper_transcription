from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import subtitles

app = FastAPI(
    title="AutoSub API",
    description="API para gerar legendas automáticas e renderizar vídeos com IA",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(subtitles.router, prefix="/subtitles", tags=["Subtitles"])
