import os
import json
import random

try:
    import requests as _requests
    _USE_REQUESTS = True
except ImportError:
    import urllib.request
    _USE_REQUESTS = False

BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8",
}

def download_pexels_background(keyword, output_path="pipeline_bg.jpg"):
    pexels_api_key = os.environ.get("PEXELS_API_KEY", "").strip()

    if not pexels_api_key:
        print("PEXELS_API_KEY not set - using default dark background.")
        return None

    search_url = (
        "https://api.pexels.com/v1/search"
        "?query=" + keyword.replace(" ", "+") +
        "&orientation=portrait&per_page=10"
    )
    auth_headers = dict(BROWSER_HEADERS)
    auth_headers["Authorization"] = pexels_api_key

    try:
        if _USE_REQUESTS:
            r = _requests.get(search_url, headers=auth_headers, timeout=10)
            r.raise_for_status()
            data = r.json()
        else:
            req = urllib.request.Request(search_url, headers=auth_headers)
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))

        photos = data.get("photos", [])
        if not photos:
            print("Pexels: no results for keyword, using default background.")
            return None

        photo = random.choice(photos)
        img_url = photo["src"]["large2x"]

        if _USE_REQUESTS:
            img_resp = _requests.get(img_url, headers=BROWSER_HEADERS, timeout=30)
            img_resp.raise_for_status()
            with open(output_path, "wb") as f:
                f.write(img_resp.content)
        else:
            req2 = urllib.request.Request(img_url, headers=BROWSER_HEADERS)
            with urllib.request.urlopen(req2) as ir:
                with open(output_path, "wb") as f:
                    f.write(ir.read())

        size_kb = os.path.getsize(output_path) // 1024
        print(f"Pexels 4K background downloaded: {output_path} ({size_kb}KB)")
        return output_path

    except Exception as e:
        print(f"Pexels download failed ({e}), using default background.")
        return None
