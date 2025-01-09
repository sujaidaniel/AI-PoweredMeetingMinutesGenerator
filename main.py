# Import necessary libraries and modules
import os
import openai
from dotenv import load_dotenv

# Import custom modules for sentiment analysis, transcription, and document saving
from sentiment_analysis import (
    abstract_summary_extraction,
    key_points_extraction,
    action_item_extraction,
    sentiment_analysis
)
from transcription import transcribe_audio
from save_as_docx import save_as_docx

# Load environment variables from a .env file
load_dotenv()

# Set up the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to generate meeting minutes
def generate_meeting_minutes(transcription_text):
    return {
        'abstract_summary': abstract_summary_extraction(transcription_text),
        'key_points': key_points_extraction(transcription_text),
        'action_items': action_item_extraction(transcription_text),
        'sentiment': sentiment_analysis(transcription_text)
    }

# Path to the audio file
audio_file = "./audio/ClientMeet.wav"

# Transcribe audio using OpenAI's API
transcription_result = transcribe_audio(audio_file, openai)

# Generate meeting minutes from the transcription
meeting_minutes = generate_meeting_minutes(transcription_result)

# Print the generated meeting minutes
print(meeting_minutes)

# Save the meeting minutes to a Word document
save_as_docx(meeting_minutes, 'meeting_minutes.docx')
