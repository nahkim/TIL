# Database

---



- 체계화된 데이터의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 (하나 이상의) 자료의 모음으로
  그 내용을 고도로 구조화 함으로써 검색과 생신의 효율화를 도모함
- 즉, 몇 개의 자료 파일을 조직적으로 통합하여
  자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체



- 데이터베이스의 장점
  - 데이터 중복 최소화
  - 데이터 무결성 (정확한 정보를 보장)
  - 데이터 일관성
  - 데이터 독립성 (물리적 / 논리적)
  - 데이터 표준화
  - 데이터 보안 유지



## 관계형 데이터베이스 (RDB, Relational Database)

---



- 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
- 키와 값들의 관계를 표형태로 정리한 데이터베이스



- 스키마 (Schema)
  - 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것
- 테이블 (table)
  - 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합
- 열 (column)
  - 각 열에 고유한 데이터 형식 지정
- 행 (row)
  - 실제 데이터가 저장되는 형태
- 기본키 (Primary Key)
  - 각 행(레코드)의 고유 값



## 관계형 데이터베이스 관리 시스템 (RDBMS)

---



- 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미
  - MySQL
  - SQLite
  - PostgreSQL
  - ORACLE
  - SQL Server



### SQLite

---



- 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨
- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능



- Data Type
  1. NULL
  2. INTEGER
     - 크기에 따라 0, 1, 2, 3, 4, 6, 또는 8바이트에 저장된 부호있는 정수
  3. REAL
     - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
  4. TEXT
  5. BLOB
     - 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)



- Sqlite Type Affinity (1/2)

  - 특정 컬럼에 저장하도록 권장하는 데이터 타입

  1. INTEGER
  2. TEXT
  3. BLOB
  4. REAL
  5. NUMERIC





|      Example Typenames From The CREATE TABLE Statement       | Resulting Affinity |
| :----------------------------------------------------------: | :----------------: |
| INT<br />INTEGER<br />TINYINT<br />SMALLINT<br />MEDIUMINT<br />BIGINT<br />UNSIGNED BIG INT<br />INT2<br />INT8 |      INTEGER       |
| CHARACTER(20)<br />VARCHAR(255)<br />VARYING CHARACTER(255)<br />NCHAR(55)<br />NATIVE CHARACTER(70)<br />NVARCHAR(100)<br />TEXT<br />CLOB |        TEXT        |
|              BLOB<br />(no datatype specified)               |        BLOB        |
|      REAL<br />DOUBLE<br />DOUBLE PRECISION<br />FLOAT       |        REAL        |
| NUMERIC<br />DECIMAL(10, 5)<br />BOOLEAN<br />DATE<br />DATETIME |      NUMERIC       |





## SQL (Structured Query Language)

---



- 관계형 데이터베이스 관리시스템의 데이터관리를 위해 설계된 특수 목적의 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리



| 분류                                                     | 개념                                                         | 예시                                        |
| -------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| DDL - 데이터 정의 언어<br />(Data Definition Language)   | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE<br />DROP<br />ALTER                 |
| DML - 데이터 조작 언어<br />(Data Manipulation Language) | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어        | INSERT<br />SELECT<br />UPDATE<br />DELETE  |
| DCL - 데이터 제어 언어<br />(Data Control Language)      | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어       | GRANT<br />REVOKE<br />COMMIT<br />ROLLBACK |





- SQL Keywords - Data Manipulation Language
  - INSERT : 새로운 데이터 삽입
  - SELECT : 저장되어있는 데이터 조회
  - UPDATE : 저장되어있는 데이터 갱신
  - DELETE : 저장되어있는 데이터 삭제



- 명령어

'.'은 sqlite에서 활용되는 명령어임



Database 생성

```sqlite
$ sqlite3 tutorial.sqlite3
sqlite> .database
```



csv 파일을 table로 만들기

```sqlite
.mode csv
.import hellodb.csv examples
.tables
examples
```



SELECT

```sqlite
SELECT * FROM examples;
```

SELECT문은 특정 테이블의 레코드(행) 정보를 반환함



(Optional) 터미널 view 변경하기

```sqlite
.headers on			# 
.mode column		#
```



테이블 생성

CREATE TABLE

```sqlite
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);
```



생성되어 있는 테이블 확인

```sqlite
.tables
```



특정 테이블의 schema 조회

```sqlite
.schema classmates
```





테이블 제거

DROP TABLE

```sqlite
DROP TABLE classmates;
```



- 필드 제약 조건
  - NOT NULL : NULL 값 입력 금지
  - UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 입력 가능)
  - PRIMARY KEY : 테이블에서 반드시 하나. NOT NULL + UNIQUE
  - FOREIGN KEY : 외래키. 다른 테이블의 Key
  - CHECK : 조건으로 설정된 값만 입력 허용
  - DEFAULT : 기본 설정 값





### CRUD

---

|  -   |  구문  |                             예시                             |
| :--: | :----: | :----------------------------------------------------------: |
|  C   | INSERT | **INSERT INTO** 테이블이름 (컬럼1, 컬럼2, ... ) **VALUES** (값1, 값2); |
|  R   | SELECT |       **SELECT** * **FROM** 테이블이름 **WHERE** 조건;       |
|  U   | UPDATE | **UPDATE** 테이블이름 **SET** 컬럼1=값1, 컬럼2=값2 **WHERE** 조건; |
|  D   | DELETE |          **DELETE FROM** 테이블이름 **WHERE** 조건;          |



**CREATE**

- INSERT

  - "insert a single row into a table"

  - 테이블에 단일 행 삽입

    - ```sqlite
      INSERT INTO 테이블_이름 (칼럼1, 칼럼2) VALUES (값1, 값2);
      ```

  - 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력

    - ```sqlite
      INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);
      ```



rowid : SQLite에서 PRIMARY KEY가 없는 경우 자동으로 증가하는 PK 컬럼

```sqlite
SELECT rowid, * FROM classmates;
```



스키마에 직접 id를 작성했을 경우 입력할 column들을 명시하지 않으면 자동으로 입력되지 않는다!

```sqlite
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

INSERT INTO classmates VALUES ('이름');	# ERROR

# 방법1 id를 포함한 모든 value 작성
INSERT INTO classmates VALUES (1, '이름');

# 방법2 각 value에 맞는 column들을 명시적으로 작성
INSERT INTO classmates (name) VALUES ('이름');
```





**READ**

- SELECT
  - "query data from a table"
  - 테이블에서 데이터를 조회
  - SELECT 문은 SQLite에서 가장 기본이 되는 문이면 다양한 절(clause)와 함께 사용
    - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY ...
- LIMIT
  - "constrain the number of rows returned by a query"
  - 쿼리에서 반환되는 행 수를 제한
  - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함
  - OFFSET : 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형(0부터 시작)
- WHERE
  - "specify the search condition for rows returned by the query"
  - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
- SELECT DISTINCT
  - "remove duplicate rows in the result set"
  - 조회 결과에서 중복 행을 제거
  - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함



```sqlite
SELECT DISTINCT 컬럼1, 컬럼2 FROM 테이블이름 LIMIT 숫자1 OFFSET 숫자2;

# 숫자2 + 1번째 행부터 숫자1개 행(컬럼1, 컬럼2)을 중복없이 조회
```



**UPDATE**

- UPDATE

  - "update data of existing rows in the table"

  - 기존 행의 데이터를 수정

  - SET clause에서 테이블의 각 열에 대해 새로운 값을 설정

  - ```sqlite
    UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2 WHERE 조건;
    ```

    

**DELETE**

- DELETE

  - 데이터 삭제

  - "remove rows from a table"

  - 테이블에서 행을 제거

  - ```sqlite
    DELETE FROM 테이블이름 WHERE 조건;
    # 중복 불가능한 (UNIQUE) 값인 rowid를 기준으로 삭제하기
    ```

- AUTOINCREMENT

  - SQLite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지

  - ```sqlite
    CREATE TABLE students(
    	id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL
    );
    ```

    