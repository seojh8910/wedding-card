FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# 필요 패키지 설치 및 종속성 설치
RUN apt-get -y update && apt-get -y install \
    vim \
    pkg-config \
    libmariadb-dev-compat \
    libmariadb-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 소스 코드 추가
COPY . .

# Python 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# MySQL 클라이언트 라이브러리 설치
RUN pip install mysqlclient

# 환경 변수 설정
ENV DJANGO_SETTINGS_MODULE=wedding_card.settings
ENV PYTHONUNBUFFERED=1

# 정적 파일 수집
RUN python manage.py collectstatic --noinput

# 포트 노출 및 Gunicorn 사용하여 애플리케이션 실행
EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "wedding_card.wsgi:application"]
