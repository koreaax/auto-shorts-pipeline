import os
import json
import asyncio
import urllib.request
import edge_tts

def load_env_file():
    """ .env 파일이 존재하면 환경변수로 자동 로드합니다. """
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip()

async def generate_edge_tts(text, output_audio_path="pipeline_audio.mp3"):
    VOICE = "ko-KR-SunHiNeural"
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_audio_path)
    print(f"TTS 음성 저장 완료: {output_audio_path}")

def generate_script_and_audio(product=None):
    """
    OpenAI API로 숏폼 대본 생성 + Edge-TTS 음성 합성.
    product: {"name": "제품명", "category": "카테고리", "link": "URL"} or None
    product 있을 때: IT지식 -> 공감 -> 제품 연결 3단계 구조
    product 없을 때: 순수 IT 지식 대본
    """
    load_env_file()
    print("[Step 1/3] OpenAI GPT-4o-mini가 오늘 숏폼 대본을 작성하고 있습니다...")

    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        print("OPENAI_API_KEY 없음 - 샘플 대본으로 진행합니다.")
        script_text = "컴퓨터 버그의 진짜 유래를 아시나요? 1947년 세계 최초의 버그는 진짜 나방이었습니다. 컴퓨터 기계 사이에 나방이 끼어 고장이 났던 것이죠!"
    else:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        if product:
            system_prompt = (
                "너는 IT 지식과 테크 제품을 자연스럽게 연결하는 100만 쇼츠 작가야. "
                "시청자가 지식을 얻는 동시에 제품에 매력을 느끼도록 다음 3단계 구조로 "
                "딱 30초 분량(총 4문장, 130자 내외)의 한국어 대본을 작성해줘.\n\n"
                "1단계: 호기심 유발 (IT/개발 관련 가장 충격적이거나 흥미로운 비하인드 스토리 1문장)\n"
                "2단계: 현실 공감 (그 지식과 연결되는 개발자/직장인의 킹받는 일상 고충 1문장)\n"
                "3단계: 제품 연결 (문제를 한방에 해결해 줄 추천 제품 언급 및 고정댓글 확인 유도 2문장)\n\n"
                "[주의사항]\n"
                "- 문장은 무조건 짧고 호흡이 빠르게 작성할 것.\n"
                "- 어조는 유튜브 쇼츠 특유의 경쾌하고 트렌디한 반말 또는 '요'체로 작성할 것.\n"
                "- 괄호, 화면 설명, 지시문, 기호는 절대 넣지 말고 오직 말하는 나레이션만 출력할 것."
            )
            user_prompt = (
                f"오늘의 추천 제품: [{product['name']}]\n"
                f"이 제품과 기가 막히게 연결되는 IT/개발 지식 비하인드 스토리 대본을 짜줘."
            )
        else:
            system_prompt = (
                "너는 전 세계 흥미로운 IT 비하인드를 알려주는 숏폼 대본 작가야. "
                "시청자가 듣자마자 스크롤을 멈추고 끝까지 보게 만드는 대본을 작성해줘.\n\n"
                " 구조:\n"
                "1단계: 대중이 잘 모르는 개발자/IT 관련 흥미로운 비하인드 스토리 (2문장)\n"
                "2단계: 다음 편 기대감 조성 및 자연스러운 구독 유도 CTA (1문장)\n\n"
                "[주의사항]\n"
                "- 총 3문장, 100자 내외로 매우 짧고 임팩트 있게 작성할 것.\n"
                "- 괄호, 해설, '1단계' 같은 표시 없이 오직 목소리로 읽을 나레이션만 출력할 것."
            )
            user_prompt = "개발자나 IT 지식 관련 흥미로운 비하인드 스토리 하나를 작성해줘."


        # if product:
        #     system_prompt = (
        #         "너는 IT 지식과 테크 제품을 자연스럽게 연결하는 스타 쇼츠 작가야. "
        #         "시청자가 지식을 얻는 동시에 제품에 매력을 느끼도록 다음 3단계 구조로 "
        #         "40초 분량(총 4~5문장)의 한국어 대본을 작성해줘.\n\n"
        #         "1단계: 호기심 유발 (IT/개발자 관련 흥미로운 지식이나 비하인드 스토리 2문장)\n"
        #         "2단계: 현실 공감 (그 지식과 관련된 개발자/직장인의 일상적 고충이나 문제점 1문장)\n"
        #         "3단계: 제품 연결 (문제를 해결해 줄 추천 제품 언급 및 고정 댓글 유도 1~2문장)\n\n"
        #         "[주의사항]\n"
        #         "- 어조는 경쾌하고 트렌디하게 작성할 것.\n"
        #         "- 나레이션만 출력하고, 불필요한 해설이나 기호, 괄호 등은 아예 생략할 것."
        #     )
        #     user_prompt = (
        #         f"오늘의 추천 제품: [{product['name']}]\n"
        #         f"이 제품과 기가 막히게 연결되는 IT/개발 지식 비하인드 스토리 대본을 짜줘."
        #     )
        # else:
        #     system_prompt = (
        #         "너는 흥미진진한 숏폼 대본 작가야. "
        #         "30초 분량으로 사람들의 호기심을 자극하는 한 줄 지식을 한국어로 경쾌하게 작성해줘."
        #     )
        #     user_prompt = "개발자나 IT 지식 관련 흥미로운 비하인드 스토리 하나를 3 문장 이내로 작성해줘."

        data = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.7,
        }

        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                res_body = json.loads(response.read().decode("utf-8"))
                script_text = res_body["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"API 호출 실패 ({e}), 샘플 대본으로 대체합니다.")
            script_text = "개발자가 자판기를 만난 순간 최고의 자동화가 시작됩니다. 매일 아침 커피 한 잔의 여유를 주는 AI 파이프라인의 세계!"

    print(f"AI 대본:\n\"{script_text}\"\n")

    output_audio_path = "pipeline_audio.mp3"
    asyncio.run(generate_edge_tts(script_text, output_audio_path))

    return script_text, output_audio_path

if __name__ == "__main__":
    generate_script_and_audio()
