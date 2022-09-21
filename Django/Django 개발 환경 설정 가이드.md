### 가상 환경



가상환경 생성

```bash
# python -m venv [가상 환경 이름]
python -m venv server-venv
```



가상환경 실행

```bash
# window
source server-venv/Scripts/activate

# mac
source server-venv/bin/activate
```



가상환경 종료

```bash
deactivate
```



장고 설치 및 확인

```bash
# 가상 환경에 접속하여 명령어 실행
pip list

pip install django==3.2.13
```



Django 프로젝트 생성

```bash
# django-admin [명령어]

django-admin startproject [프로젝트 이름] [시작경로]
```



서버 구동

```bash
python manage.py runserver
```



접속 방법

localhost:8000



터미널

```bash
/ : root 경로

~ : home 경로
```

