# 🚀 Startup Quest: 창업가 MBTI (Quest of Founder)

![Startup Quest](https://img.shields.io/badge/Status-Active-brightgreen)
![Tech Stack](https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20Vanilla%20JS-blue)
![Style](https://img.shields.io/badge/Style-8--Bit%20Retro%20%7C%20NES.css-red)

**Startup Quest(창업가 MBTI)**는 8비트 레트로 게임 컨셉의 웹 기반 성향 테스트입니다. 사용자의 의사결정 방식과 비즈니스 스타일을 12개의 질문을 통해 분석하고, 16가지의 고유한 '창업가 페르소나' 중 하나를 결과로 제시합니다.

## ✨ 주요 기능 (Key Features)

*   **🎮 레트로 8비트 UI/UX:** `NES.css`와 CRT 스캔라인 효과를 적용하여 고전 게임을 플레이하는 듯한 몰입감 제공
*   **🧠 4가지 분석 축 (MBTI 스타일):**
    *   **Action (실행):** Field (현장 중심, F) vs Professional (전문성/계획, P)
    *   **Decision (결정):** Data (데이터 기반, D) vs Intuition (직관/인사이트, I)
    *   **Focus (집중):** Target (선택과 집중, T) vs Multi (다각화, M)
    *   **Risk (위험 감수):** Bold (과감한 도전, B) vs Stability (안정 추구, S)
*   **👥 16가지 창업가 페르소나:** '유니콘 헌터', '그로스 해커', '프로덕트 장인' 등 스타트업 씬의 다양한 리더십 유형을 도트 아바타와 함께 제공
*   **🤝 환상의 짝꿍 (Match):** 각 성향과 시너지를 낼 수 있는 이상적인 파트너 유형 추천
*   **📸 결과 화면 캡처:** `html2canvas`를 활용하여 테스트 결과를 이미지 파일(`startup_mbti_result.png`)로 저장하고 공유하는 기능
*   **📖 전체 도감 보기:** 16가지 모든 페르소나의 일러스트와 상세 설명을 확인할 수 있는 갤러리 뷰 제공

## 🛠 기술 스택 (Tech Stack)

*   **Frontend Ccore:** HTML5, CSS3, JavaScript (Vanilla JS)
*   **Styling:** 
    *   [Tailwind CSS](https://tailwindcss.com/) (CDN) - 레이아웃 및 유틸리티 클래스
    *   [NES.css](https://nostalgic-css.github.io/NES.css/) - 8비트 닌텐도 스타일 UI 컴포넌트
*   **Fonts:** 
    *   `Press Start 2P` (Google Fonts) - 영문 픽셀 폰트
    *   `Pretendard` - 가독성을 위한 한글 본문 폰트
*   **Libraries:** [html2canvas](https://html2canvas.hertzen.com/) - 결과 화면 이미지 렌더링

## 📂 프로젝트 구조 (Project Structure)

```text
Founder-Mbti-Test/
├── index.html            # 메인 애플리케이션 파일 (UI 및 로직 포함)
├── assets/               # 정적 파일 디렉토리
│   └── images/           # 16개의 페르소나 도트 아바타 이미지 (.png)
├── (Utilities)           # 에셋 파일 관리를 위한 파이썬 스크립트들
```

## 🚀 실행 방법 (How to Run)

별도의 빌드 과정이나 서버 설정이 필요 없는 정적 웹 페이지입니다.

1.  이 저장소를 클론(Clone)하거나 다운로드합니다.
2.  브라우저에서 `index.html` 파일을 직접 열면 즉시 실행됩니다.
3.  Vercel, GitHub Pages 등을 통해 쉽게 정적 호스팅이 가능합니다. (현재 `vercel.json` 설정 포함)

---
© 2026 Startup Quest. All rights reserved.
made by sangwon
