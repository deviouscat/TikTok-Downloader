import requests
import os
import re

def get_video_url(link):
    r = requests.get(
        "https://www.tikwm.com/api/",
        params={"url": link},
        headers={"User-Agent": "Mozilla/5.0"}
    )
    j = r.json()
    return j["data"]["play"] if j.get("data") else None

def clean_name(text):
    text = re.sub(r"[^a-zA-Z0-9]+", "_", text)
    return text[:40] if len(text) > 40 else text

def download_video(url, name):
    os.makedirs("Tiktoks", exist_ok=True)
    path = f"Tiktoks/{name}.mp4"
    v = requests.get(url, stream=True)
    with open(path, "wb") as f:
        for chunk in v.iter_content(1024 * 1024):
            f.write(chunk)
    return path

link = input("Enter TikTok link: ").strip()
print("\nFetching video…")

video_url = get_video_url(link)

if not video_url:
    print("Could not fetch video.")
else:
    name = clean_name(link)
    file_path = download_video(video_url, name)
    print(f"\nSaved to: {file_path}")
    print("Done.\n")
