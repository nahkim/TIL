import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 3
directors = [('봉준호', '1993-01-01', 'KOR'),
             ('김한민', '1999-01-01', 'KOR'),
             ('최동훈', '2004-01-01', 'KOR'),
             ('이정재', '2022-01-01', 'KOR'),
             ('이경규', '1992-01-01', 'KOR'),
             ('한재림', '2005-01-01', 'KOR'),
             ('Joseph Kosinski', '1999-01-01', 'KOR'),
             ('김철수', '2022-01-01', 'KOR')
            ]

for director in directors:
  name_ = director[0]
  debut_ = director[1]
  country_ = director[2]
  Director.objects.create(name = name_, debut = debut_, country = country_)

# 4
genres = ["액션","드라마","사극","범죄","스릴러","SF","무협","첩보","재난"]

for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()

# 5
directors = Director.objects.all()
for director in directors:
    print(director.name, director.debut, director.country)

# 6
director = Director.objects.get(id = 1)
print(director.name, director.debut, director.country)

# 7
director = Director.objects.get(country = 'USA')
print(director.name, director.debut, director.country)
# DoesNotExist: Director matching query does not exist.

# 8
# get은 조건에 맞는 것이 존재하지 않는 경우 오류를 발생시킨다.

# 9
director = Director.objects.get(name = 'Joseph Kosinski')
director.country = 'USA'
director.save()

print(director.name, director.debut, director.country)

# 10
directors = Director.objects.get(country = 'KOR')
# MultipleObjectsReturned: get() returned more than one Director -- it returned 7!

# 11
# get은 조건에 맞는 것이 2개 이상일 경우 오류를 발생시킨다.

# 12
directors = Director.objects.filter(country = 'KOR')

for director in directors:
    print(director.name, director.debut, director.country)

# 13
# get : 단일 객체(반드시 하나가 존재해야한다) 없거나 많으면 오류 발생한다.
# filter : 반드시 QuerySet 형태이다. 없거나 많아도 오류가 발생하지 않는다.

# 14
director = Director.objects.get(name = '김철수')
director.delete()