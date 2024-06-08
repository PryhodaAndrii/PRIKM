FROM python:3.10-slim
WORKDIR /bot
# Install python requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz
COPY . /bot
CMD ["python", "main.py"]