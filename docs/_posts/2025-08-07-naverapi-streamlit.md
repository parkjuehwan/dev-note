---
layout: post
title: "네이버 데이터랩 API 연동 및 Streamlit 대시보드 구축"
date: 2025-08-07
---

## 개요

이 포스트에서는 네이버 데이터랩 오픈 API를 활용하여 특정 키워드의 검색 트렌드를 수집하고,  
이를 Streamlit을 통해 대시보드 형태로 시각화하는 과정을 다룬다.  
분석 대상은 계절별 인기 레저 키워드(예: 계곡, 해수욕장, 스키장, 온천)이며,  
실시간 데이터 수집, 인터랙티브 그래프, 통계 분석 기능을 포함한다.

---

## 1. 네이버 데이터랩 API 등록 방법

1. [네이버 개발자 센터](https://developers.naver.com/main/)에 접속
2. 애플리케이션 > 애플리케이션 등록 메뉴로 이동
3. 애플리케이션 이름 입력 후, 사용 API 항목에서  
   "Search > 데이터랩 검색어 트렌드" 선택
4. 등록 완료 후 발급된 Client ID와 Client Secret을 확인

> 참고: 실제 운영 시에는 해당 키를 코드에 직접 노출하지 않고 환경 변수로 관리하는 것이 권장된다.

<img width="1375" height="887" alt="image" src="https://github.com/user-attachments/assets/644d31a9-b417-4a8e-8a8e-a7e58bd93eea" style="width: 100%; height: auto;" />


---

## 2. Streamlit 대시보드 구성

사용한 주요 파일은 다음과 같다:

- `streamlit_dashboard.py`: 대시보드 실행용 Streamlit 앱
- `seasonal_trends_notebook.ipynb`: 사전 분석 과정을 정리한 Jupyter 노트북

대시보드는 다음과 같은 기능을 제공한다:

- 시작일, 종료일, 주기 설정 (일/주/월 단위)
- 키워드 다중 선택 기능
- 네이버 데이터랩 API 호출을 통한 검색 트렌드 수집
- Plotly 또는 Matplotlib을 이용한 시각화 출력
- 평균값, 최대값, 계절별 비교 등 통계 분석
- 분석 결과 CSV 다운로드

<img width="1379" height="845" alt="image" src="https://github.com/user-attachments/assets/dd24af57-1fed-4349-9a82-9ee0628e2da5" style="width: 100%; height: auto;" />


---

## 3. 주요 코드 설명

Streamlit 앱은 다음과 같은 방식으로 동작한다:

- 사용자 입력을 기반으로 API 요청 페이로드 생성
- `requests.post()`를 통해 API 호출
- 결과를 JSON으로 받아 DataFrame으로 변환
- 키워드별 평균값, 최대값 계산 및 시각화
- 탭을 이용해 그래프 / 데이터 테이블 / 통계 정보를 분리

```python
url = "https://openapi.naver.com/v1/datalab/search"
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
    "Content-Type": "application/json"
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
```

---

## 4. 실행 예시

Streamlit 앱은 다음 명령어로 실행할 수 있다:

```bash
streamlit run streamlit_dashboard.py
```

앱이 실행되면 브라우저에서 다음 정보를 확인할 수 있다:

- 선택된 키워드들의 시간대별 검색 트렌드  
- 각 키워드의 평균 및 최대 검색 지수  
- 월별 데이터를 바탕으로 한 계절별 검색량 분석  
- 데이터 테이블 및 다운로드 기능  

<img width="1584" height="830" alt="image" src="https://github.com/user-attachments/assets/d56eb24a-fcf0-49ef-b853-5d803772e4ae" style="width: 100%; height: auto;" />
<img width="1518" height="608" alt="image" src="https://github.com/user-attachments/assets/2ab3b7fd-f257-4606-8739-bb04c5b6f144" style="width: 100%; height: auto;" />
<img width="1010" height="371" alt="image" src="https://github.com/user-attachments/assets/3a042eb1-5c09-469a-8f58-94c111a35c06" style="width: 100%; height: auto;" />


---

## 후기

이 외에도 KBO 10개 구단 검색량을 알아보려 했지만, 검색 대상은 한번에 5개씩 밖에 안되며,
API가 절대적인 검색횟수를 제공하는 것이 아니라, 검색 비율로 나오기때문에 10개 구단을 한번에 비교하기는 힘들었다.
(물론 구단 1개씩 겹치게 3번정도 돌려서 직접 계산할 수는 있지만 귀찮다...)

또한 유저들이 '기아 타이거즈'나 '삼성 라이온즈'를 그냥 '기아', '삼성'으로 검색할 수도 있는데
이게 야구를 검색하는지 자동차를 검색하는지 핸드폰을 검색하는지 알 수가 없다.
키워드를 어떻게 잡아야 할지 좀 머리가 아프다
