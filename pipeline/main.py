import os
import sys
from generator import generate_script_and_audio
from video_engine import create_shorts_thumbnail
from uploader import upload_to_youtube_shorts

def run_pipeline():
    print("=" * 60)
    print("🚀 [100% Full-Auto Pipeline] 무인 숏폼 생성 및 자동 게시 가동!")
    print("=" * 60)

    # 1. AI 대본 및 음성 생성
    script_text, audio_path = generate_script_and_audio()

    # 2. 1080x1920 숏폼 프레임 이미지 생성
    frame_path = create_shorts_thumbnail(script_text)

    # 3. 100% 무인 유튜브 숏폼 자동 업로드 실행!
    shorts_title = f"💡 {script_text[:25]}... #Shorts"
    upload_to_youtube_shorts(shorts_title, script_text, frame_path)

    # 파이프라인 완료 보고
    print("\n" + "=" * 60)
    print("🎉 100% 손대지 않는 무인 파이프라인 프로세스 완료!")
    print(f"- 음성 파일: {audio_path}")
    print(f"- 숏폼 프레임: {frame_path}")
    print(f"- 게시 제목: {shorts_title}")
    print("=" * 60)

if __name__ == "__main__":
    run_pipeline()
