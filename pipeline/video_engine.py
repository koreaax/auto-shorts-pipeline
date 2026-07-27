import os
from PIL import Image, ImageDraw, ImageFont

def create_shorts_thumbnail(script_text, output_image_path="pipeline_frame.png"):
    """
    1080x1920 (9:16 숏폼 규격) 다크모드 카드뉴스 배경 프레임을 생성합니다.
    """
    width, height = 1080, 1920
    # 딥 다크 퍼플 배경
    image = Image.new("RGB", (width, height), color=(15, 12, 29))
    draw = ImageDraw.Draw(image)

    # 상단 그래픽 장식 원
    draw.ellipse([width//2 - 300, 200, width//2 + 300, 800], fill=(79, 70, 229))

    # 기본 폰트 또는 커스텀 폰트 로드
    try:
        font_title = ImageFont.truetype("arial.ttf", 60)
        font_body = ImageFont.truetype("arial.ttf", 45)
    except IOError:
        font_title = ImageFont.load_default()
        font_body = ImageFont.load_default()

    # 타이틀
    title_text = "💡 오늘의 1분 IT 지식"
    draw.text((width // 2, 450), title_text, fill=(168, 85, 247), font=font_title, anchor="mm")

    # 본문 자막 (줄바꿈 처리)
    lines = []
    words = script_text.split(" ")
    current_line = ""
    for word in words:
        if len(current_line + word) > 14:
            lines.append(current_line)
            current_line = word + " "
        else:
            current_line += word + " "
    lines.append(current_line)

    y_offset = 800
    for line in lines:
        draw.text((width // 2, y_offset), line.strip(), fill=(255, 255, 255), font=font_body, anchor="mm")
        y_offset += 80

    # 하단 출처 및 브랜딩
    draw.text((width // 2, 1600), "🤖 Automated by GitHub Actions", fill=(148, 163, 184), font=font_body, anchor="mm")

    image.save(output_image_path)
    print(f"🖼️ 숏폼 프레임 이미지 생성 완료: {output_image_path}")

    return output_image_path

if __name__ == "__main__":
    create_shorts_thumbnail("컴퓨터 버그의 진짜 유래를 아시나요? 1947년 세계 최초의 버그는 진짜 나방이었습니다!")
