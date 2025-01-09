import openai

def extract_abstract_summary(transcription):
    """
    Generates a concise abstract summary of the provided transcription.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an advanced AI skilled in summarizing text into a coherent abstract. "
                    "Summarize the following text into a single paragraph that captures the most "
                    "important points, avoiding unnecessary details or tangential information."
                )
            },
            {"role": "user", "content": transcription}
        ]
    )
    return response['choices'][0]['message']['content']

def extract_key_points(transcription):
    """
    Extracts and lists the main points discussed in the provided transcription.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI specialized in identifying key points from text. Extract the main ideas, "
                    "topics, or findings from the following text and present them as a concise list of key points."
                )
            },
            {"role": "user", "content": transcription}
        ]
    )
    return response['choices'][0]['message']['content']

def extract_action_items(transcription):
    """
    Identifies and extracts actionable tasks or assignments from the transcription.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI with expertise in extracting actionable tasks from conversations. "
                    "Analyze the following text and list any tasks, assignments, or actions that need to be performed. "
                    "Clearly and concisely present the action items."
                )
            },
            {"role": "user", "content": transcription}
        ]
    )
    return response['choices'][0]['message']['content']

def analyze_sentiment(transcription):
    """
    Analyzes the overall sentiment of the provided transcription, categorizing it as positive, negative, or neutral.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI expert in sentiment analysis. Review the following text and determine the overall tone, "
                    "categorizing it as positive, negative, or neutral. Provide brief reasoning to support your analysis."
                )
            },
            {"role": "user", "content": transcription}
        ]
    )
    return response['choices'][0]['message']['content']
