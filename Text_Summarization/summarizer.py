import click
from ollama_api import OllamaAPI  # Assuming you've set up Ollama API

@click.command()
@click.option('-t', '--text', type=click.STRING, help='Input text or path to a text file')
def summarize(text):
    """Summarizes input text."""
    if text:
        if text.endswith('.txt'):
            # Read text from file
            with open(text, 'r', encoding='utf-8') as file:
                input_text = file.read()
        else:
            input_text = text

        # Use Ollama API (Qwen2 0.5B model) for summarization
        summary = OllamaAPI.summarize(input_text)

        click.echo(f".Summary of {text}.\n\n{summary}")
    else:
        click.echo("Please provide input text or a valid text file.")

if __name__ == '__main__':
    summarize()
