import click
from . import lib
from .log import log
from . import config

@click.group()
def cli():
    pass

@click.command()
@click.option('--language', default="en", help='language code')
def list_voices(language):
    """List voices"""
    lib.list_voices(language)

@click.command()
@click.argument('textfile')
@click.option('--voice', "-v", default="en-US-Wavenet-D", help='Voice to synthesize with')
@click.option('--output', "-o", default="audio", help='Output file to save audio as')
def synth(textfile,voice, output):
    """Synthesize text file to audiobook"""
    
    # Load input text
    chunks = lib.load_chunks(textfile)

    # Synthesize
    log.info(f"Synthesizing {len(chunks)} chunks with {voice}")

    for i, chunk in enumerate(chunks):
        lib.text_to_wav(voice, chunk, filename=f"{output}_{i}")

    # Combine
    lib.combine(output, 0, len(chunks), fmt="ogg")


cli.add_command(list_voices)
cli.add_command(synth)