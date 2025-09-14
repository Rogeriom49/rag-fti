import io
import tempfile
from pytube import YouTube
import whisper
import yt_dlp
from pathlib import Path
from docling.document_converter import DocumentConverter
from Classes.AudioTranscription import AudioTranscription

url = 'https://www.youtube.com/watch?v=nzPjuaYS5X0'

# audio = AudioTranscription().transcribe(url)

ydl_options = {
    'format':'bestaudio/best',
    'outtmpl':'-'
}

converter = DocumentConverter()

with yt_dlp.YoutubeDL(ydl_options) as ydl:
    info = ydl.extract_info(url=url, download=False)
    # print(info.keys())
    url_audio = info['url']
    # model = whisper.load_model("turbo")
    # transcricao = model.transcribe(url_audio, language='pt')
    audio_result = converter.convert(url_audio)
    transcript = audio_result.document.export_to_markdown()
    
    # result = converter.convert_string(transcricao['text'])
    # doc = result.document
    print(transcript)



    
