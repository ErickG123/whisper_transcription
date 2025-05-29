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

## 🚀 Como rodar este projeto

### 📦 Pré-requisitos

- Python 3.10 ou superior instalado
- Git instalado
- Gerenciador de pacotes `pip` (geralmente já vem com o Python)

### 🔧 Instalação

Clone o repositório:
```bash
git clone https://github.com/ErickG123/whisper_transcription
cd whisper_transcription
```

### Crie e ative um ambiente virtual (recomendado):
### No Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### No macOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```

### Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 🚀 Rodando o projeto
Execute o seguinte comando para iniciar o servidor:
```bash
uvicorn app.main:app --reload
```
