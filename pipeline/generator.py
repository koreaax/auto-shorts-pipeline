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
    """
    Microsoft Edge-TTS를 사용해 100% 사람과 똑같은 초고품질 한국어 AI 성우 음성을 생성합니다.
    Voice: ko-KR-SunHiNeural (자연스러운 여성 성우) 또는 ko-KR-InJoonNeural (경쾌한 남성 성우)
    """
    VOICE = "ko-KR-SunHiNeural"
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_audio_path)
    print(f"🎙️ [Edge-TTS] 사람 같은 초고품질 AI 성우 음성 저장 완료: {output_audio_path}")

def generate_script_and_audio():
    """
    OpenAI API를 통해 숏폼용 재미있는 지식/IT 비하인드 대본을 생성하고,
    Edge-TTS로 사람 같은 음성을 만듭니다.
    """
    load_env_file()
    print("🤖 [Step 1/3] OpenAI GPT-4o-mini가 오늘 숏폼 대본을 작성하고 있습니다...")
    
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("⚠️ OPENAI_API_KEY가 설정되지 않아 샘플 테스트 대본으로 진행합니다.")
        script_text = "컴퓨터 버그의 진짜 유래를 아시나요? 1947년 세계 최초의 버그는 진짜 나방이었습니다. 컴퓨터 기계 사이에 나방이 끼어 고장이 났던 것이죠!"
    else:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        data = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": "너는 흥미진진한 숏폼 대본 작가야. 30초 분량으로 사람들의 호기심을 자극하는 한 줄 지식을 한국어로 경쾌하게 작성해줘."
                },
                {
                    "role": "user",
                    "content": "개발자나 IT 지식 관련 흥미로운 비하인드 스토리 하나를 3 문장 이내로 작성해줘."
                }
            ]
        }
        
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                res_body = json.loads(response.read().decode('utf-8'))
                script_text = res_body['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"API 호출 실패 ({e}), 샘플 대본으로 대체합니다.")
            script_text = "개발자가 자판기를 만난 순간 최고의 자동화가 시작됩니다. 매일 아침 커피 한 잔의 여유를 주는 AI 파이프라인의 세계!"

    print(f"📜 작성된 실시간 AI 대본:\n\"{script_text}\"\n")

    # 100% 무료 초고품질 Edge-TTS 음성합성 실행
    output_audio_path = "pipeline_audio.mp3"
    asyncio.run(generate_edge_tts(script_text, output_audio_path))

    return script_text, output_audio_path

if __name__ == "__main__":
    generate_script_and_audio()
