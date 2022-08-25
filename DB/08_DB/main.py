import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

# 3
directors = [
    ("봉준호","1993-01-01","KOR"),
    ("김한민","1999-01-01","KOR"),
    ("최동훈","2004-01-01","KOR"),
    ("이정재","2022-01-01","KOR"),
    ("이경규","1992-01-01","KOR"),
    ("한재림","2005-01-01","KOR"),
    ("Joseph Kosinski","1999-01-01","KOR"),
    ("김철수","2022-01-01","KOR"),
]

for director in directors:
    name_ = director[0]
    debut_ = director[1]
    country_ = director[2]
    Director.objects.create(name=name_, debut=debut_, country=country_)

genres = ["액션","드라마","사극","범죄","스릴러","SF","무협","첩보","재난"]

for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()

# 4
director_ = Director.objects.get(name = '봉준호')
print(f'id : {director_.id}')
print(f'name : {director_.name}')
print(f'debut : {director_.debut}')
print(f'country : {director_.country}')

# 5
genre_ = Genre.objects.get(title = '드라마')
print(f'id : {genre_.id}')
print(f'title : {genre_.title}')

# 6
# 모델 Director와 Genre의 인스턴스 생성
director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')

# Moive 모델의 인스턴스 movie 생성
movie = Movie()

# 인스턴스(변수) movie의 director 필드에 Director 모델의 인스턴스 저장
movie.director=director_

# 인스턴스(변수) movie의 genre 필드에 Genre 모델의 인스턴스 저장
movie.genre=genre_
movie.title='기생충'
movie.opening_date='2019-05-30'
movie.running_time=132
movie.screening=False

# movie 인스턴스 저장 -> 데이터베이스에 행 추가(INSERT)
movie.save()

# 7
movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for movie in movies:
  movie_ = Movie()
  
  director_ = Director.objects.get(name = movie[0])
  genre_ = Genre.objects.get(title = movie[1])
  
  movie_.director = director_
  movie_.genre = genre_
  movie_.title = movie[2]
  movie_.opening_date = movie[3]
  movie_.running_time = movie[4]
  movie_.screening = movie[5]
  movie_.save()

# 8
movie_list = Movie.objects.all()

for movie in movie_list:
  print(
    movie.director,	# movie의 director 필드 출력
    movie.genre,		# movie의 genre 필드 출력
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 9
movie_list = Movie.objects.all()

for movie in movie_list:
  print(
    movie.director.name,	# movie의 director 필드의 name 필드 출력
    movie.genre,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 10
movie_list = Movie.objects.all()

for movie in movie_list:
  print(
    movie.director.name,
    movie.genre.title,			# movie의 genre 필드의 title 필드 출력
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 11
movies = Movie.objects.order_by('-opening_date')	# 개봉일 기준 내림차순으로 정렬해서 조회
for movie in movies:
  print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 12
movies = Movie.objects.order_by('opening_date')[0]
print(
  movies.director.name,
  movies.genre.title,
  movies.title,
  movies.opening_date,
  movies.running_time,
  movies.screening
)

# 13
movie_list = Movie.objects.filter(screening = True).order_by('opening_date')
for movie in movie_list:
  print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 14
director_ = Director.objects.get(name = '봉준호')
movie_list = Movie.objects.filter(director = director_).order_by('opening_date')

for movie in movie_list:
  print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 15
director_ = Director.objects.get(name = '봉준호')
movie = Movie.objects.filter(director = director_).order_by('opening_date')[1]

print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 16
movie_list = Movie.objects.filter(running_time__gt = 119).order_by('running_time')

for movie in movie_list:
  print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 17
movie_list = Movie.objects.filter(running_time__gte = 119).order_by('running_time')

for movie in movie_list:
  print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 18
movie_list = Movie.objects.filter(opening_date__gt = '2022-01-01').order_by('opening_date')

for movie in movie_list:
  print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 19
# 각각 name이 봉준호인 Director 인스턴스 director_와 title이 드라마인 Genre 인스턴스 genre_ 생성
director_ = Director.objects.get(name = '봉준호')
genre_ = Genre.objects.get(title = '드라마')

# director가 director_ 이고, genre가 genre_인 Movie 데이터 탐색
movie_list = Movie.objects.filter(director = director_, genre = genre_).order_by('opening_date')

for movie in movie_list:
  print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )

# 20
director_ = Director.objects.get(name = '봉준호')

movie_list = Movie.objects.exclude(director = director_).order_by('opening_date')

for movie in movie_list:
  print(
    movie.director.name,
    movie.genre.title,
    movie.title,
    movie.opening_date,
    movie.running_time,
    movie.screening
  )