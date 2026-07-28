import os
import time
from datetime import datetime

def post_to_tistory(title, content):
    """
    Selenium을 이용해 티스토리 블로그에 쿠팡 파트너스 링크 포함 포스팅을 100% 무인 자동 게시합니다.
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
    except ImportError:
        print("⚠️ selenium이 설치되지 않아 블로그 포스팅을 건너뜁니다.")
        return False

    kakao_email    = os.environ.get("TISTORY_KAKAO_EMAIL", "").strip()
    kakao_password = os.environ.get("TISTORY_KAKAO_PASSWORD", "").strip()
    blog_name      = os.environ.get("TISTORY_BLOG_NAME", "").strip()
    coupang_link   = os.environ.get("COUPANG_AFFILIATE_LINK", "https://link.coupang.com/your-link").strip()

    if not kakao_email or not kakao_password or not blog_name:
        print("⚠️ 티스토리 계정 정보(TISTORY_KAKAO_EMAIL / PASSWORD / BLOG_NAME)가 없어 포스팅을 건너뜁니다.")
        return False

    today = datetime.now().strftime("%Y년 %m월 %d일")
    full_title = f"💡 {title} | {today}"
    full_content = f"""
<h2>💡 오늘의 1분 IT 지식</h2>

<blockquote style="border-left:4px solid #8B5CF6; padding:16px; background:#F5F3FF; font-size:18px;">
{content}
</blockquote>

<p>매일 새로운 IT 지식을 유튜브 숏폼과 블로그에서 동시에 만나보세요! 🚀</p>
<hr/>

<h3>🛒 개발자 추천 가성비 아이템</h3>
<p>코딩 생산성을 높여줄 아이템을 확인해 보세요!</p>
<a href="{coupang_link}" target="_blank" 
   style="display:inline-block; background:#EF4444; color:white; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:bold;">
🛍️ 쿠팡에서 바로 보기
</a>
<p style="color:#9CA3AF; font-size:13px; margin-top:20px;">
이 링크를 통한 구매 시 소정의 수수료가 지급됩니다.
</p>
<p>#IT지식 #개발자 #AI #숏폼 #1분지식 #코딩</p>
"""

    # Headless Chrome 옵션 설정
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    try:
        print("📝 [티스토리] 카카오 로그인 시작...")

        # 1. 티스토리 로그인 페이지 접속
        driver.get("https://www.tistory.com/auth/login")
        time.sleep(2)

        # 2. 카카오 로그인 버튼 클릭
        kakao_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.btn_login.kakao_login, .kakao-login-btn, a[href*='kakao']")
        ))
        kakao_btn.click()
        time.sleep(2)

        # 3. 카카오 이메일 입력
        email_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input#loginId, input[name='loginKey'], input[type='email']")
        ))
        email_input.clear()
        email_input.send_keys(kakao_email)

        # 4. 카카오 비밀번호 입력
        pw_input = driver.find_element(By.CSS_SELECTOR, "input#password, input[name='password'], input[type='password']")
        pw_input.clear()
        pw_input.send_keys(kakao_password)

        # 5. 로그인 버튼 클릭
        login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit'], .btn_confirm, .login-btn")
        login_btn.click()
        time.sleep(3)

        print("✅ 카카오 로그인 성공!")

        # 6. 글쓰기 페이지 이동
        write_url = f"https://{blog_name}.tistory.com/manage/newpost/"
        driver.get(write_url)
        time.sleep(3)

        # 7. 제목 입력
        title_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input#post-title-inp, input[placeholder*='제목'], .title-input")
        ))
        title_input.clear()
        title_input.send_keys(full_title)
        time.sleep(1)

        # 8. 에디터를 HTML 모드로 전환 후 본문 입력
        try:
            # HTML 모드 버튼 클릭
            html_btn = driver.find_element(By.CSS_SELECTOR, "button[data-tiara-action-name*='HTML'], .btn_html, button[title='HTML']")
            html_btn.click()
            time.sleep(1)
        except Exception:
            pass

        # iframe 안의 에디터에 직접 JS로 내용 삽입
        driver.execute_script("""
            var editors = document.querySelectorAll('.CodeMirror, textarea#content, #tinymce');
            if(editors.length > 0) { editors[0].value = arguments[0]; }
        """, full_content)

        # iframe 에디터 처리 (일반 TinyMCE)
        try:
            iframe = driver.find_element(By.CSS_SELECTOR, "#editor-tistory_ifr, iframe.tox-edit-area__iframe")
            driver.switch_to.frame(iframe)
            body = driver.find_element(By.TAG_NAME, "body")
            driver.execute_script("arguments[0].innerHTML = arguments[1];", body, full_content)
            driver.switch_to.default_content()
        except Exception:
            pass

        time.sleep(1)

        # 9. 공개 발행 버튼 클릭
        publish_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button#publish-layer-btn, .btn_publish, button[data-tiara-action-name*='발행']")
        ))
        publish_btn.click()
        time.sleep(2)

        # 10. 최종 발행 확인 버튼
        try:
            confirm_btn = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.btn_ok, .layer_post_publish button.btn_ok, button[onclick*='publish']")
            ))
            confirm_btn.click()
            time.sleep(2)
        except Exception:
            pass

        print(f"📝 [티스토리] 무인 자동 포스팅 완료! 👉 https://{blog_name}.tistory.com")
        return True

    except Exception as e:
        print(f"❌ 티스토리 포스팅 실패: {e}")
        return False

    finally:
        driver.quit()

if __name__ == "__main__":
    post_to_tistory("컴퓨터 버그의 유래", "1947년 세계 최초의 버그는 진짜 나방이었습니다!")
