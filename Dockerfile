FROM python:3.10-slim

RUN apt update && \
    apt install -y ffmpeg && \
    pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
