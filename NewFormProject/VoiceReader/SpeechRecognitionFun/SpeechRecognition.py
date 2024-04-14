#установи эти шняги
from aiogram.types import Message
from aiogram import F, Bot, Router
import speech_recognition as sr
from pydub import AudioSegment
#импортируй эти шняги
import os 
import stat

from Classes.BotClasses import StepsBots


router_voic_reader = Router()

@router_voic_reader.message(StepsBots.READER_VOICE)
async def voice_recognize(message: Message, bot: Bot):
    AudioSegment.converter = r"AnkeBot\NewFormProject\VoiceReader\SpeechRecognitionFun\ffmpeg.exe" #РАДИ ВСЕГО СВЯТОГО НЕ ПЕРЕМЕЩАЙ ЭТИ ФАЙЛЫ ДАЛЕКО ОТ ИСПОЛНЯЕМОЙ ФУНКЦИИ ПОЖАЛУЙСТА
    AudioSegment.ffprobe   = r"AnkeBot\NewFormProject\VoiceReader\SpeechRecognitionFun\ffprobe.exe"
    os.chmod(r"AnkeBot\NewFormProject\VoiceReader\SpeechRecognitionFun\ffmpeg.exe", stat.S_IEXEC)
    os.chmod(r"AnkeBot\NewFormProject\VoiceReader\SpeechRecognitionFun\ffprobe.exe", stat.S_IEXEC)

# ... rest of your code ...


    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    await bot.download_file(file_path, 'voice.ogg')

    src_filename = 'voice.ogg'
    dest_filename = 'voice.wav'
    sound = AudioSegment.from_ogg(src_filename)
    sound.export(dest_filename, format="wav")
    r = sr.Recognizer()
    try:
        with sr.AudioFile(dest_filename) as source:
        
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="ru-RU")
            await message.reply(text)
    except sr.UnknownValueError:
        await message.reply("Я не понял ваших слов")
    