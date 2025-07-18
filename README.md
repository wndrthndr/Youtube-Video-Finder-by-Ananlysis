#YouTube Video Finder with Title Analysis#

This is a smart YouTube automation tool built for the **AI Automations Internship Assignment**. It allows users to search for a topic (in English or Hindi), fetches the top 20 most relevant and recent YouTube videos, and uses **OpenAI GPT** to analyze and recommend the best video based on the title quality.

 Features

✅ Accepts **text input** for video search  
✅ Uses **YouTube Data API** to search and filter videos  
✅ Filters:
- Duration: **4 to 20 minutes**
- Posted: **Within the last 14 days**

✅ Sends the video titles to **OpenAI GPT (gpt-4o)**  
✅ Returns the **best video title** based on clarity, relevance, and usefulness  
✅ Prints all 20 videos + the best suggestion

---

2. 📦 Install Dependencies
pip install -r requirements.txt


3. 🔑 Create .env File
Make a .env file in the root directory with your API keys:

YOUTUBE_API_KEY=your_youtube_api_key
OPENAI_API_KEY=your_openai_api_key

**Sample Output**
YouTube Video Finder with Analysis
Enter your search topic: best coding tutorials

🔎 Top 20 YouTube Videos Found:
1. Learn Python in 10 Minutes → https://youtube.com/xyz
2. Top 5 Coding Bootcamps in 2024 → https://youtube.com/abc
...

✅ Best Suggested Video Based on Title Analysis:
5. "Python Full Course - Beginner to Advanced (2024 Edition)"



