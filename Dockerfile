FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    xvfb curl ca-certificates unzip \
    libglib2.0-0 libnss3 libfontconfig1 \
    libxss1 libgtk-3-0 libasound2 libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -m playwright install --with-deps

CMD ["sh", "-c", "Xvfb :99 -screen 0 1920x1080x24 & export DISPLAY=:99 && pytest --alluredir=/app/allure-results"]