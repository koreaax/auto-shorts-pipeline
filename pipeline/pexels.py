import os
import urllib.parse
import urllib.request
import json
import random

def download_pexels_background(keyword, output_path="pipeline_bg.jpg"):
    """
    Pexels 무료 API를 이용해 AI 대본 키워드에 맞는 고화질 4K 배경 이미지를 자동 다운로드합니다.
    """
    pexels_api_key = os.environ.get("PEXELS_API_KEY", "").strip()

    if not pexels_api_key:
        print("⚠️ PEXELS_API_KEY 없음 - 기본 다크 배경으로 진행합니다.")
        return None

    search_url = f"https://api.pexels.com/v1/search?query={urllib.parse.quote(keyword)}&orientation=portrait&per_page=10"
    headers = {"Authorization": pexels_api_key}

    try:
        req = urllib.request.Request(search_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            photos = data.get("photos", [])
            if not photos:
                return None
            photo = random.choice(photos)
            img_url = photo["src"]["large2x"]
            urllib.request.urlretrieve(img_url, output_path)
            print(f"📸 [Pexels] 4K 배경 이미지 다운로드 완료: {output_path}")
            return output_path
    except Exception as e:
        print(f"Pexels 이미지 다운로드 실패 ({e}), 기본 배경으로 대체합니다.")
        return None
