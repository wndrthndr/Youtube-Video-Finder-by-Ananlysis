# title_analyzer.py — OpenAI SDK v1.13.3 compliant

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_titles(query, videos):
    titles = [f"{i+1}. {video['title']}" for i, video in enumerate(videos)]
    formatted_titles = "\n".join(titles)

    prompt = f"""You are a helpful assistant. A user searched for "{query}" on YouTube.
Here are 20 video titles found:

{formatted_titles}

Based on clarity, relevance, and usefulness, which ONE title is the best? Just return the number and title.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4o"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    return response.choices[0].message.content.strip()
