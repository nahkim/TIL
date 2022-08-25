# JOIN

- 관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능
- 일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를 저장하는 것이 아니라 여러 테이블로 나누어 저장하게 된다. -> 여러 테이블을 결함(Join)하여 활용
- 일반적으로 레코드는 기본키(PK)나 외래키(FK) 값의 관계에 의해 결합함



## JOIN 종류

- INNER JOIN
- OUTER JOIN
- CROSS JOIN



[SQL Joins Visualizer](https://sql-joins.leopard.in.ua)



TABLE 생성

```sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  name TEXT,
  role_id INT
);

INSERT INTO users VALUES
  (1, '관리자', 1),
  (2, '김철수', 2),
  (3, '이영희', 2);

CREATE TABLE role(
  id INT PRIMARY KEY,
  title TEXT
);

INSERT INTO role VALUES
	(1, 'admin'),
	(2, 'staff'),
	(3, 'student');

CREATE TABLE articles(
	id INT PRIMARY KEY,
  title TEXT,
  content TEXT,
  user_id INT
);

INSERT INTO articles VALUES
(1, '1번글', '111', 1),
(2, '2번글', '222', 2),
(3, '3번글', '333', 1),
(4, '4번글', '444', NULL);

-- 확인
.mode column
SELECT * FROM users;
SELECT * FROM role;
SELECT * FROM articles;

```



```sql
-- INNER JOIN (INNER 생략 가능)
SELECT *
FROM 테이블1 [INNER] JOIN 테이블2
	ON 테이블1.칼럼 = 테이블2.칼럼;

-- 실습
SELECT *
FROM users INNER JOIN role
	ON users.id = role.id;
	
SELECT *
FROM users INNER JOIN role
	ON users.id = role.id
WHERE role.id = 2;

SELECT *
FROM users INNER JOIN role
	ON users.id = role.id
ORDER BY users.name DESC;

-- OUTER JOIN
SELECT *
FROM 테이블1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2
	ON 테이블1.칼럼 = 테이블2.칼럼;

-- 실습
SELECT *
FROM articles LEFT OUTER JOIN users
	ON articles.user_id = users.id;

SELECT *
FROM articles LEFT OUTER JOIN users
	ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;

SELECT *
FROM articles FULL OUTER JOIN users
	ON users.id = articles.user_id;
-- SQLite는 외부 조인의 경우 왼쪽 외부 조인(LEFT OUTER JOIN)절에서만 지원한다.
-- 확인 필요

-- CROSS JOIN
SELECT *
FROM 테이블1 CROSS JOIN 테이블2;

-- 실습
SELECT *
FROM users CROSS OUTER JOIN role;
```



```sql
Error: in prepare, RIGHT and FULL OUTER JOINs are not currently supported (1)
Error: in prepare, ambiguous column name: InvoiceId (1)
```

