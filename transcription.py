def transcribe_audio(audio_file_path, openai):
    """
    Converts audio content into text using the Whisper ASR model.
    
    Args:
        audio_file_path (str): Path to the audio file.
        openai (module): OpenAI module instance for API interaction.

    Returns:
        str: Transcribed text from the audio file.
    """
    with open(audio_file_path, 'rb') as audio_file:
        result = openai.Audio.transcribe("whisper-1", audio_file)
    return result['text']
