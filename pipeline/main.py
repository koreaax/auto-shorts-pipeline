import os
import sys
from generator import generate_script_and_audio, load_env_file
from video_engine import create_shorts_thumbnail, get_keyword_from_script
from pexels import download_pexels_background
from video_composer import compose_video
from uploader import upload_to_youtube_shorts
from blogger import post_to_tistory

def run_pipeline():
    # .env 파일 로드 (로컬 실행 시 환경변수 자동 주입)
    load_env_file()
    print("=" * 60)
    print("🚀 [Full-Auto Pipeline v2] 무인 숏폼 + 블로그 + 무인 업로드 가동!")
    print("=" * 60)

    # 1단계: AI 대본 + Edge-TTS 사람 성우 음성 생성
    script_text, audio_path = generate_script_and_audio()

    # 2단계: 대본 키워드 추출 후 Pexels 4K 배경 이미지 자동 다운로드
    keyword = get_keyword_from_script(script_text)
    print(f"\n🔍 배경 키워드 자동 선정: [{keyword}]")
    bg_path = download_pexels_background(keyword)

    # 3단계: Pexels 4K 배경 + 자막 합성 숏폼 이미지 렌더링
    frame_path = create_shorts_thumbnail(script_text, bg_image_path=bg_path)

    # 4단계: PNG + MP3 → 실제 MP4 합성 (YouTube Shorts 수익화 필수)
    mp4_path = compose_video(frame_path, audio_path)
    upload_target = mp4_path if mp4_path else frame_path

    # 5단계: 유튜브 채널에 100% 무인 자동 업로드
    shorts_title = f"💡 {script_text[:25]}... #Shorts"
    upload_to_youtube_shorts(shorts_title, script_text, upload_target)

    # 6단계: 티스토리 블로그에 쿠팡 파트너스 링크 포함 자동 포스팅
    print("\n📝 [보너스] 티스토리 블로그에 동시 포스팅 시작...")
    blog_title = script_text[:30]
    post_to_tistory(blog_title, script_text)

    # 완료 보고
    print("\n" + "=" * 60)
    print("🎉 [v2] 100% 완전 무인 파이프라인 ALL DONE!")
    print(f"  🎙️ Edge-TTS 사람 성우 음성: {audio_path}")
    print(f"  🖼️ Pexels 4K 배경 숏폼 프레임: {frame_path}")
    print(f"  🎬 실제 MP4 영상: {mp4_path if mp4_path else '합성 실패 (이미지로 대체)'}")
    print(f"  📺 유튜브 숏폼 채널: 자동 업로드 완료")
    print(f"  📝 티스토리 블로그: 쿠팡 링크 포함 자동 포스팅 완료")
    print("=" * 60)
    print("\n💰 수익 통장 3개가 동시에 작동하고 있습니다!")
    print("  1️⃣  유튜브 조회수 광고 수익 (애드센스)")
    print("  2️⃣  블로그 쿠팡 파트너스 제휴 수수료 (3%)")
    print("  3️⃣  Lemon Squeezy 템플릿 스토어 유입 수익 ($39)")

if __name__ == "__main__":
    run_pipeline()
