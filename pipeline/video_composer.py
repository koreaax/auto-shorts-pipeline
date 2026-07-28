import os


def compose_video(image_path, audio_path, output_path="pipeline_output.mp4"):
    """
    PNG 정지 이미지 + MP3 오디오를 합쳐 실제 YouTube Shorts 규격 MP4를 생성합니다.
    moviepy.ImageClip(duration=오디오길이) + AudioFileClip → write_videofile

    YouTube Shorts 요구사항:
    - 해상도: 1080x1920 (9:16)
    - 포맷: MP4 (H.264 + AAC)
    - 최대 길이: 60초
    """
    try:
        from moviepy import ImageClip, AudioFileClip  # moviepy 2.x
    except ImportError:
        try:
            from moviepy.editor import ImageClip, AudioFileClip  # moviepy 1.x fallback
        except ImportError:
            print("❌ moviepy 미설치. pip install moviepy 후 재시도 하세요.")
            return None

    print("\n🎬 [MP4 합성] 이미지 + 오디오 → MP4 변환 시작...")

    if not os.path.exists(image_path):
        print(f"❌ 이미지 파일 없음: {image_path}")
        return None

    if not os.path.exists(audio_path):
        print(f"❌ 오디오 파일 없음: {audio_path}")
        return None

    try:
        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration

        # 정지 이미지를 오디오 길이만큼 재생되는 비디오 클립으로 변환 (moviepy 2.x API)
        video_clip = ImageClip(image_path).with_duration(duration).with_fps(30)
        video_clip = video_clip.with_audio(audio_clip)

        video_clip.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac",
            temp_audiofile="temp_audio.m4a",
            remove_temp=True,
            logger=None,   # moviepy 진행 바 숨김
        )

        audio_clip.close()
        video_clip.close()

        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"✅ MP4 생성 완료: {output_path} ({duration:.1f}초, {size_mb:.1f}MB)")
        return output_path

    except Exception as e:
        print(f"❌ MP4 합성 실패: {e}")
        return None


if __name__ == "__main__":
    result = compose_video("pipeline_frame.png", "pipeline_audio.mp3")
    if result:
        print(f"🎥 출력 파일: {result}")
