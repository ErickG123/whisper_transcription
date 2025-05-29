# 🎥 Whisper Subtitle Generator

Este projeto utiliza o modelo **Whisper (medium)** da OpenAI para gerar legendas automáticas a partir de áudios de vídeos. As legendas são extraídas, salvas nos formatos `.txt`, `.srt` e `.ass`, e posteriormente inseridas no próprio vídeo de forma automática.

O projeto é desenvolvido com **Python**, **FastAPI** para a API REST e **FFmpeg** para manipulação de vídeos.

## 🧠 Tecnologias Utilizadas

- [OpenAI Whisper](https://github.com/openai/whisper) — Reconhecimento de voz
- [FFmpeg](https://ffmpeg.org/) — Processamento de vídeo e áudio
- [FastAPI](https://fastapi.tiangolo.com/) — API rápida e moderna
- Python 3.11.X

## 🚀 Funcionalidades

- 🎧 Extração de áudio de vídeos
- 📝 Geração de legendas automáticas com Whisper
- 💾 Exportação das legendas em:
  - `.txt` (texto simples)
  - `.srt` (legenda padrão)
  - `.ass` (legenda avançada)
- 🎬 Inserção da legenda automaticamente no vídeo
