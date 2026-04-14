# 1. 가벼운 Python 이미지 선택
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 시스템 패키지 설치 (MySQL 클라이언트 라이브러리 등)
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 4. 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 애플리케이션 소스 코드 복사
COPY app/ .

# 6. FastAPI 실행 포트 노출
EXPOSE 8000

# 7. 실행 명령어 (Uvicorn 사용)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]