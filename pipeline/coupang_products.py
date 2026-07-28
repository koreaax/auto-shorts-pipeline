# -*- coding: utf-8 -*-
"""
쿠팡 파트너스 제품 목록 관리
=============================
제품 추가/수정 방법 (Python 코드 수정 없이):

[방법 1] products.json 직접 편집 (권장)
  - GitHub 웹 UI: 레포 -> pipeline/products.json -> 연필 아이콘 -> 수정 -> Commit
  - 로컬: 텍스트 에디터로 pipeline/products.json 수정

[방법 2] Google Sheets 연동 (폰에서도 수정 가능)
  - .env 에 COUPANG_SHEET_CSV_URL 설정
  - Google Sheets -> 파일 -> 공유 -> 웹에 게시 -> CSV 형식 URL 복사
  - 컬럼 순서: name, category, link, active
"""

import os
import json
import datetime

PRODUCTS_JSON = os.path.join(os.path.dirname(__file__), "products.json")


def _load_from_json():
    """pipeline/products.json 에서 활성 제품 목록을 읽어옵니다."""
    if not os.path.exists(PRODUCTS_JSON):
        return []
    with open(PRODUCTS_JSON, encoding="utf-8") as f:
        all_products = json.load(f)
    return [p for p in all_products if p.get("active", True)]


def _load_from_sheets():
    """
    Google Sheets CSV 공개 URL에서 제품 목록을 읽어옵니다.
    .env 의 COUPANG_SHEET_CSV_URL 이 설정된 경우에만 사용됩니다.
    Google Sheets 설정: 파일 -> 공유 -> 웹에 게시 -> CSV
    컬럼 순서: name, category, link, active
    """
    try:
        import urllib.request, csv, io
        csv_url = os.environ.get("COUPANG_SHEET_CSV_URL", "").strip()
        if not csv_url:
            return []
        with urllib.request.urlopen(csv_url, timeout=5) as r:
            content = r.read().decode("utf-8")
        reader = csv.DictReader(io.StringIO(content))
        products = []
        for row in reader:
            if row.get("active", "true").lower() in ("true", "1", "yes", "y"):
                products.append({
                    "name": row.get("name", "").strip(),
                    "category": row.get("category", "").strip(),
                    "link": row.get("link", "").strip(),
                    "active": True,
                })
        return [p for p in products if p["name"]]
    except Exception as e:
        print(f"Google Sheets 로드 실패 ({e}), JSON 파일로 대체합니다.")
        return []


def get_todays_product():
    """
    오늘 날짜 기준으로 제품을 로테이션 선정합니다.
    Google Sheets URL 있으면 Sheets 우선, 없으면 products.json 사용.
    """
    # Google Sheets 우선 시도
    products = _load_from_sheets()

    # 없으면 JSON 파일 사용
    if not products:
        products = _load_from_json()

    if not products:
        # 최후 폴백
        return {
            "name": "개발자 추천 가성비 아이템",
            "category": "기타",
            "link": os.environ.get("COUPANG_AFFILIATE_LINK", "https://link.coupang.com/your-link"),
        }

    day_index = datetime.date.today().toordinal() % len(products)
    product = products[day_index]

    # 링크가 비어있으면 공통 링크 사용
    if not product.get("link") or "your-" in product.get("link", ""):
        product["link"] = os.environ.get(
            "COUPANG_AFFILIATE_LINK",
            product.get("link", "https://link.coupang.com/your-link")
        )

    return product


if __name__ == "__main__":
    from generator import load_env_file
    load_env_file()
    p = get_todays_product()
    print(f"오늘의 제품: {p['name']}")
    print(f"카테고리: {p['category']}")
    print(f"링크: {p['link']}")
