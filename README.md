# AI-PoweredMeetingMinutesGenerator

**Description**  
This project leverages OpenAI's Whisper ASR and GPT-4 models to streamline the creation of meeting minutes by automating transcription, summarization, and extraction of key points from audio recordings. It also identifies action items and performs sentiment analysis.  

Built using Python, this application efficiently transcribes audio, generates concise summaries, and organizes insights into actionable formats.  

**Requirements**  
Basic knowledge of Python and an OpenAI API key is required. Obtain your API key [here](https://platform.openai.com/signup/). The project uses Python 3.11.5.  


**Usage**  
- **Audio Transcription:** Use `transcription.py` with Whisper ASR to convert audio to text.  
- **Summary and Analysis:** Summarize transcripts and extract insights using GPT-4 in `sentiment_analysis.py`.  
- **Key Points and Action Items:** Identify crucial points and tasks using `sentiment_analysis.py`.  
- **Generate Meeting Minutes:** Format and compile insights into minutes using `meeting_minutes.py`.  
- **Export to Word Document:** Save results as a Word document using `save_as_docx.py`.  

**Optimization and Further Development**  
- Enhance Whisper ASR's accuracy by fine-tuning with custom datasets.  
- Explore prompt engineering to improve GPT-4’s performance.  
- Refine system messages for better contextual responses from GPT-4.  
