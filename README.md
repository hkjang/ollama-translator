# AI Ollama Translator

| 항목 | 설명 |
|------|------|
| 이름 | Ollama 기반 웹 번역기 |
| 목적 | LLM을 이용한 다국어 텍스트 번역 웹 앱 제공 |
| 기술 스택 | Flask, HTML/CSS, Bootstrap, Ollama API |

---

### 📄 `README.md`

```markdown
# Ollama 번역기

Ollama LLM API를 이용한 Flask 기반 웹 번역기입니다. 사용자는 입력한 텍스트를 다양한 언어로 번역할 수 있습니다.

## 🧩 주요 기능

- 다양한 언어(20개 이상) 지원
- EasyMDE 기반의 마크다운 편집기 UI
- Ollama LLM API 연동
- 번역 결과 시각적 출력

## 🚀 실행 방법

### 1. 환경 설정

```bash
git clone https://github.com/hkjang/ollama-translator.git
cd ollama-translator
python -m venv venv
source venv/bin/activate  # Windows는 venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 환경 변수 설정 (.env)

`.env` 파일 생성 후 다음 내용 입력:

```
OLLAMA_API_URL=http://localhost:11434
OLLAMA_MODEL_NAME=llama3
OLLAMA_TRANSLATE_PROMPT=You are a professional translator. Translate the following text into {lang}. Maintain the tone, context, and style of the original text. Do not explain. Only output the translated text.:
```

### 3. 서버 실행

```bash
python app.py
```

브라우저에서 `http://localhost:5000` 접속

## 🖼️ 화면 구성

- 좌측: 번역할 텍스트 입력
- 우측: 번역된 결과 출력
- 언어 선택: 상단 드롭다운

## 🌐 지원 언어 목록

- 영어, 한국어, 일본어, 중국어, 스페인어, 프랑스어, 독일어, 포르투갈어, 러시아어, 아랍어, 힌디어, 벵골어, 우르두어, 이탈리아어, 터키어, 베트남어, 태국어, 네덜란드어, 인도네시아어, 폴란드어

## 📁 디렉터리 구조

```
ollama-translator/
├── app.py
├── templates/
│   └── index.html
├── static/
├── .env
└── requirements.txt
```

## 📦 의존 패키지 (requirements.txt)

```
Flask
flask-cors
python-dotenv
requests
```

## ⚠️ 주의사항

- Ollama API 서버가 사전에 실행되어 있어야 합니다.
- 언어 이름은 Ollama 모델이 이해할 수 있는 명칭으로 지정해야 합니다.

## 📜 라이선스

MIT License
```

---

필요 시 `Mermaid`로 구성 흐름도도 추가해드릴 수 있습니다. 시각적으로 표현하시겠습니까?