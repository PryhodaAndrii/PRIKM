import yt_dlp as youtube_dl
import os 
import logging


FORMAT = '%(asctime)-15s %(name)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.basicConfig(level=logging.ERROR, format=FORMAT)
logger = logging.getLogger()


path= os.path.join(os.path.dirname(__file__), f"_videos/")

def ytdl(link = None):
  print
  ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

  dl_ops = {
        'outtmpl': f'{path}%(title)s.%(ext)s',
        'format_sort': ['res:1080', 'ext:mp4:m4a']
      }

  with youtube_dl.YoutubeDL(dl_ops) as ydl:
      logger.error(f"link is: {link}")
      ydl.download(link)
      info = ydl.extract_info(link, download=False)
      file_path = ydl.prepare_filename(info)
      return file_path
