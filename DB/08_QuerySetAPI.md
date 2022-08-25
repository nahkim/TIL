환경

- Shell_Plus -파이썬 REPL환경

- .py - 파이썬 / 한줄한줄 코드를 돌림 

- $ - 터미널 / 완성된 코드를 돌림



# QuerySet API

---

메서드

- gt (초과)

  - ```python
    Entry.objects.filter(id__gt=4)
    #Entry.objects.filter(필드이름__메서드)
    ```

  - ```python
    # 쿼리문
    SELECT ... WHERE id > 4;
    ```

- gte (이상)

  - ```python
    # 쿼리셋
    Entry.objects.filter(id__gte=4)
    ```

  - ```python
    # 쿼리문
    SELECT ... WHERE id >= 4;
    ```

- lt (미만), lte(이하)

  - ```python
    # less then
    
    ```

- in

- startswith

- istartswith (대소문자 구분 안함)

- contains (포함 유무)

- range (범위)



- 복합 활용
  - 서브쿼리
- 활용
  - 범위일경우 limit offset 이용





쿼리 출력이 안됨

파이썬의 본질 : 개별 인스턴스라 쿼리 출력이 안된다



QuerySet : 개별 오브젝트의 모음

쿼리 출력이 된다



## 1:N ORM 확장

이름 = models.ForeignKey('클래스이름', on_delete=models.CASCADE)

-> 이름_id 로 만들어진다

옵션 on_delete=models.CASCADE : 글이 삭제됐을 경우 댓글을 지워야한다

PROTECT : 댓글이 있으면 글을 지우지 못한다 ex) 댓글 포인트 제도



soft delete : 삭제를 하지 않았지만 삭제를 한것처럼

필드를 만들고 is_delete, is_active(1, 0)



- Foreign Key



- 1:N 관계에서의 Create



ORM

---

파이썬으로 DB를 조작

1. 테이블 생성 -> 클래스 정의 - makemigrations - migrate
2. 쿼리 (SQL)
   - CRUD



ORM의 장단점

- 데이터베이스를 고민할 필요 없음(쿼리를 바꿀 필요 없음)
- 유지보수 관리가 편함
- 복잡한 형태의 쿼리들은 제약사항이 있어 직접 작성해야한다



DB-ORM-master에서 DB 전부 삭제하는법

db.sqlite3 파일 삭제