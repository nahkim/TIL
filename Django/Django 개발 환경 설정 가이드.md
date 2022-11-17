### 가상 환경

---



가상환경 생성

```bash
# python -m venv [가상 환경 이름]
python -m venv venv
```



가상환경 실행

```bash
# window
# source [가상 환경 이름]/Scripts/activate
source venv/Scripts/activate

# mac
# . [가상 환경 이름]/bin/activate
. venv/bin/activate
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



---





#### git 에 올릴시

---



1. 가상환경 ignore 생성

(.gitignore에 venv/ 추가)



.gitignore

```bash
venv/
```



2. 패키지 공유 (패키지 목록 생성)

```bash
pip freeze > requirements.txt
```



가상환경 패키지 설치

```bash
pip install -r requirements.txt
```

