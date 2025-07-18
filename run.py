# run.py

from yt_finder import search_youtube_videos
from title_analyzer import analyze_titles

def main():
    print("🎯 YouTube Video Finder with Analysis")
    query = input("Enter your search topic: ")

    videos = search_youtube_videos(query)

    print("\n🔎 Top 20 YouTube Videos Found:")
    for idx, video in enumerate(videos):
        print(f"{idx+1}. {video['title']} → {video['url']}")

    best_video = analyze_titles(query, videos)

    print("\n✅ Best Suggested Video Based on Title Analysis:")
    print(best_video)

if __name__ == "__main__":
    main()
