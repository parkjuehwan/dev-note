import requests
from bs4 import BeautifulSoup
import os
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage

# 카테고리별 URL
CATEGORIES = {
    "커피": "https://m.hollys.co.kr/menu/menuList.do",
    "라떼/초콜릿/티": "https://m.hollys.co.kr/menu/menuList.do?menuDiv=SIGNATURE",
    "할리치노/빙수": "https://m.hollys.co.kr/menu/menuList.do?menuDiv=HOLLYCCINO",
    "스무디/주스": "https://m.hollys.co.kr/menu/menuList.do?menuDiv=JUICE",
    "스파클링": "https://m.hollys.co.kr/menu/menuList.do?menuDiv=TEA"
}

data = []
IMG_DIR = "hollys_images"
os.makedirs(IMG_DIR, exist_ok=True)

def get_menu_list(category, url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    # 여러 ul.menu_list를 모두 순회
    menu_uls = soup.find_all("ul", class_="menu_list")
    if not menu_uls:
        menu_uls = soup.find_all("ul", class_="menu_list line")
    for menu_ul in menu_uls:
        for li in menu_ul.find_all("li"):
            a = li.find("a")
            if not a:
                continue
            detail_url = "https://m.hollys.co.kr" + a["href"] if a.has_attr("href") else ""
            img_tag = a.find("img")
            img_url = img_tag["src"] if img_tag and img_tag.has_attr("src") else ""
            name_tag = a.find("span", class_="name")
            name = name_tag.text.strip() if name_tag else ""
            get_menu_detail(category, name, img_url, detail_url)

def get_menu_detail(category, name, img_url, detail_url):
    res = requests.get(detail_url)
    soup = BeautifulSoup(res.text, "html.parser")
    # 메뉴명, 영문명, 설명
    h3 = soup.find("h3")
    kor_name = name
    eng_name = ""
    if h3:
        spans = h3.find_all("span")
        if spans:
            eng_name = spans[0].text.strip()
    desc = soup.find("p", class_="menu_txt")
    desc_text = desc.text.strip() if desc else ""
    # 사이즈 종류
    size_info = soup.find("span", class_="stit")
    size_text = size_info.text.strip() if size_info else ""
    # 영양정보 테이블
    nutrition = {"칼로리": "", "당류": "", "단백질": "", "포화지방": "", "나트륨": "", "카페인": ""}
    table = soup.find("div", class_="tableType01")
    if table:
        for tr in table.find_all("tr"):
            th = tr.find("th")
            tds = tr.find_all("td")
            if th and tds and th.text.strip() in nutrition:
                nutrition[th.text.strip()] = {
                    "HOT": tds[0].text.replace("HOT : ", "").strip(),
                    "ICED": tds[1].text.replace("ICED : ", "").strip() if len(tds) > 1 else ""
                }
    # 이미지 다운로드
    img_path = ""
    if img_url:
        try:
            img_data = requests.get(img_url).content
            ext = os.path.splitext(img_url)[-1]
            safe_name = kor_name.replace("/", "_").replace(" ", "_")
            img_path = os.path.join(IMG_DIR, f"{safe_name}{ext}")
            with open(img_path, "wb") as f:
                f.write(img_data)
        except Exception as e:
            img_path = ""
    data.append({
        "카테고리": category,
        "메뉴명": kor_name,
        "영문명": eng_name,
        "사이즈종류": size_text,
        "이미지경로": img_path,
        "설명": desc_text,
        "칼로리(HOT)": nutrition["칼로리"].get("HOT", ""),
        "칼로리(ICED)": nutrition["칼로리"].get("ICED", ""),
        "당류(HOT)": nutrition["당류"].get("HOT", ""),
        "당류(ICED)": nutrition["당류"].get("ICED", ""),
        "단백질(HOT)": nutrition["단백질"].get("HOT", ""),
        "단백질(ICED)": nutrition["단백질"].get("ICED", ""),
        "포화지방(HOT)": nutrition["포화지방"].get("HOT", ""),
        "포화지방(ICED)": nutrition["포화지방"].get("ICED", ""),
        "나트륨(HOT)": nutrition["나트륨"].get("HOT", ""),
        "나트륨(ICED)": nutrition["나트륨"].get("ICED", ""),
        "카페인(HOT)": nutrition["카페인"].get("HOT", ""),
        "카페인(ICED)": nutrition["카페인"].get("ICED", "")
    })

if __name__ == "__main__":
    for category, url in CATEGORIES.items():
        print(f"크롤링 중: {category}")
        get_menu_list(category, url)
    # openpyxl로 엑셀 저장
    wb = Workbook()
    ws = wb.active
    ws.title = "메뉴정보"
    # 헤더
    headers = [
        "카테고리", "메뉴명", "영문명", "사이즈종류", "이미지", "설명",
        "칼로리(HOT)", "칼로리(ICED)", "당류(HOT)", "당류(ICED)",
        "단백질(HOT)", "단백질(ICED)", "포화지방(HOT)", "포화지방(ICED)",
        "나트륨(HOT)", "나트륨(ICED)", "카페인(HOT)", "카페인(ICED)"
    ]
    ws.append(headers)
    # 데이터 행 추가
    for idx, row in enumerate(data, start=2):
        values = [
            row["카테고리"], row["메뉴명"], row["영문명"], row["사이즈종류"], "", row["설명"],
            row["칼로리(HOT)"], row["칼로리(ICED)"], row["당류(HOT)"], row["당류(ICED)"],
            row["단백질(HOT)"], row["단백질(ICED)"], row["포화지방(HOT)"], row["포화지방(ICED)"],
            row["나트륨(HOT)"], row["나트륨(ICED)"], row["카페인(HOT)"], row["카페인(ICED)"]
        ]
        ws.append(values)
        # 이미지 삽입
        img_path = row["이미지경로"]
        if img_path and os.path.exists(img_path):
            img = XLImage(img_path)
            img.width = 80
            img.height = 80
            ws.add_image(img, f"E{idx}")
    wb.save("hollys_menu_with_images.xlsx")
    print("엑셀 저장 완료: hollys_menu_with_images.xlsx")
