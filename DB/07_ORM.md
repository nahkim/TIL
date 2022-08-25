# ORM

---

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술
- 파이썬에서는 SQLAlchemy, peewee 등 라이브러리가 있으며, Django 프레임워크에서는 내장 Django ORM을 활용



**객체(object)로 DB를 조작한다**

```sqlite
Genre.objects.all()
=
SELECT * FROM Genre;
```



- 모델 설계 및 반영

1. 클래스를 생성하여 내가 원하는 DB 구조를 만든다

```sqlite
## ERD를 가지고 DB를 생성하기 위한 DB SQL구문
CREATE TABLE genres(
	id PRIMARY KEY,
	name TEXT
);
```

파이썬

```python
class Genre(models.Model):
  name = models.CharField(max_length=30)	# varchar(30)을 뜻함
```



2. 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 자동 생성한다.

```python
python manage.py makemigrations
```



3. DB에 migrate한다.

```python
python manage.py migrate
```



- Migration (마이그레이션)
  - Model에 생긴 변화를 DB에 반영하기 위한 방법
    - 클래스 생성 -> 테이블 생성
    - 필드 변경(수정, 삭제, 추가) -> 클래스 수정 -> makemigration -> migrate
  - 마이그레이션 파일을 만들어 DB 스키마를 반영한다.
  - 명령어
    - makemigrations : 마이그레이션 파일 생성
    - migrate : 마이그레이션을 DB에 반영



- 트랜잭션 (BEGIN, COMMIT)

모든 마이그레이션이 성공적으로 완료 되었을 때 적용됨, 오류시 롤백

```python
BEGIN;
CREATE TABLE "db_genre" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" varchar(30) NOT NULL
);
COMMIT;
```



- 데이터베이스 조작(Database API)

```python
Genre.objects.all()
# Genre : Class Name
# objects : Manager
# all() : QuerySet API
```



## ORM 기본 조작

---

- Create

  - ```python
    # 방법1. create 메서드 활용
    Genre.objects.create(neme='발라드')
    
    # 방법2. 인스턴스 조작
    genre = Genre()
    genre.name = '인디밴드'
    genre.save()
    
    # 방법2-1. 여러개일 경우 for문 사용
    genres = ['팝', '인디밴드', '발라드']
    for genre_name in genres:
      genre = Genre()
      genre.name = genre_name
      genre.save()
    ```

    

- Read

  - ```python
    # 방법1. 전체 데이터 조회
    Genre.objects.all()
    # <QuerySet [<Genre: Genre object (1)>, <Genre: Genre object (2)>]>
    
    # 방법1. 특정 데이터 조회, for문 사용도 가능
    Genre.objects.all()[0]
    # <Genre: Genre object (1)>
    
    # 방법2. 일부 데이터 조회(get) 단일 객체(반드시 하나) -> 없거나 많으면 오류
    # PK 바탕으로 찾을 경우 사용
    Genre.objects.get(id=1)
    # <Genre: Genre objects (1)>
    
    # 방법3. 일부 데이터 조회(filter) 반드시 QuerySet(일종의 리스트)
    # where 쓰는것은 filter 사용
    Genre.objects.filter(id=1)
    # <QuerySet [<Genre: Genre object (1)>]>
    ```

    

- Update

  - ```python
    # 1. genre 객체 활용
    genre = Genre.objects.get(id=1)
    # 2. genre 객체 속성 변경
    genre.name = '트로트'
    # 3. genre 객체 저장
    genre.save()
    ```

    

- Delete

  - ```python
    # 1. genre 객체 활용
    genre = Genre.objects.get(id=1)
    # 2. genre 객체 삭제
    genre.delete()
    
    # 1 2 합치기 가능
    Genre.objects.get(id=1).delete()
    ```



파이썬의 경우 datetime.date(2022, 8, 24)와 '2022-8-24' 문자열과 같다.

DB에는 그대로 저장하지만 꺼내올 때 자동으로 날짜형식으로 준다.



[django 데이터 필드 레퍼런스](https://docs.djangoproject.com/en/4.1/ref/models/fields/)



1. ORM은 파이썬(객체)을 조작해서 데이터베이스를 관리함

2. 데이터베이스를 관리할 때 모델링, 쿼리로 테이블 조작
   - 모델링 - 클래스 생성, 마이그레이션 생성 후 반영

3. 까마귀 관계 모델 - 객체를 조작