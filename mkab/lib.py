from google.cloud import texttospeech as tts
from nltk import sent_tokenize
from sys import argv
from os import system

from . import config
from .log import log

def list_languages():
    client = tts.TextToSpeechClient()
    voices = client.list_voices().voices
    languages = unique_languages_from_voices(voices)

    print(f' Languages: {len(languages)} '.center(60, '-'))
    for i, language in enumerate(sorted(languages)):
        print(f'{language:>10}', end='' if i % 5 < 4 else '\n')

def list_voices(language_code=None):
    client = tts.TextToSpeechClient()
    response = client.list_voices(language_code=language_code)
    voices = sorted(response.voices, key=lambda voice: voice.name)

    print(f' Voices: {len(voices)} '.center(60, '-'))
    for voice in voices:
        languages = ', '.join(voice.language_codes)
        name = voice.name
        gender = tts.SsmlVoiceGender(voice.ssml_gender).name
        rate = voice.natural_sample_rate_hertz
        print(f'{languages:<8}',
              f'{name:<24}',
              f'{gender:<8}',
              f'{rate:,} Hz',
              sep=' | ')

def get_voices(language_code=None):
    client = tts.TextToSpeechClient()
    response = client.list_voices(language_code=language_code)
    voices = sorted(response.voices, key=lambda voice: voice.name)
    return [v.name for v in voices]

def unique_languages_from_voices(voices):
    language_set = set()
    for voice in voices:
        for language_code in voice.language_codes:
            language_set.add(language_code)
    return language_set 

def text_to_wav(voice_name, text, filename=""):
    if filename == "":
        filename = voice_name
    language_code = '-'.join(voice_name.split('-')[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name)
    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config)

    filename = f'{filename}.wav'
    with open(filename, 'wb') as out:
        out.write(response.audio_content)
        log.info(f'Audio content written to "{filename}"')

def chunkify(text, chunk_size=1024):

    # Tokenize into sentances.
    sents = sent_tokenize(text)

    # Split into chunks of 1000 chars
    chunks = []
    chunk = ""
    for sent in sents:
        if (len(chunk) + len(sent)) < chunk_size:
            chunk += f" {sent}" 
        else:
            chunks.append(chunk)
            chunk = ""
            chunk += f" {sent}" 

    # Add last chunk
    chunks.append(chunk)
    return chunks

# Combine audio chunks
def combine(basename, start, end, fmt="ogg"):

    # Generate audiofile manifest
    log.debug("Generating audio file manifest...")
    with open('manifest.txt', "w") as manifest:
        for i in range(start, end):
            fname = f"{basename}_{i}.wav"
            manifest.write(f"file '{fname}'\n")  

    # Combine with ffmpeg
    log.debug("Combining audio with ffmpeg...")
    outname = f"{basename}.{fmt}"
 
    # Todo: Check if ffmpeg is installed
    system(f"ffmpeg -f concat -i manifest.txt {outname}")
    log.debug(f"Combined audio saved to {outname}")

def load_chunks(filename):
    log.debug(f"Loading chunks from {filename}")
    chunks = []
    with open(filename) as infile:
        text = infile.read()
        chunks = chunkify(text)
    
    num_chunks = len(chunks)
    log.info(f"Parsed text as {num_chunks} chunks")
    return chunks