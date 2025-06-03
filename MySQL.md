# MySQL 기초문법  
# 1. SELECT

```sql
SELECT name, age 
FROM users 
WHERE age > 20 
ORDER BY age DESC 
LIMIT 5;
```

# 2. WHERE

 비교 연산자 

`=` `!=` `<` `>` `<=` `>=` 

여러 값 중 포함 여부 

`IN (a, b, ..)`

범위 포함

`BETWEEN a AND b` 

패턴 매칭 

`LIKE` `NOT LIKE` 

- 와일드카드
    
    %: 0개 이상의 모든 문자 (문자열 전체)
    
    _: 정확히 1개의 문자 
    
    ```sql
    -- 'kim'으로 시작하는 이름
    SELECT * FROM users
    WHERE name LIKE 'kim%';
    
    -- 'son'으로 끝나는 이름
    SELECT * FROM users
    WHERE name LIKE '%son';
    
    -- 두 번째 글자가 'a'인 이름
    SELECT * FROM users
    WHERE name LIKE '_a%';
    
    -- 'park'이 포함되지 않은 이름
    SELECT * FROM users
    WHERE name NOT LIKE '%park%';
    ```
    

NULL 여부 확인 

`IS NULL` `IS NOT NULL` 

# 3. JOIN

```sql
-- INNER JOIN (교집합)
SELECT *
FROM A
JOIN B ON A.id = B.a_id;

-- LEFT JOIN (A는 전부, B는 NULL일 수 있음)
SELECT *
FROM A
LEFT JOIN B ON A.id = B.a_id;

-- RIGHT JOIN, FULL JOIN 
-- (MySQL은 FULL JOIN 없음 → UNION으로 처리)
```

# 4. GROUP BY, 집계함수

```sql
SELECT dept_id, COUNT(*) AS cnt
FROM employees
GROUP BY dept_id
HAVING cnt > 5;
```

집계함수 종류

- `COUNT(*)`, `SUM(컬럼)`, `AVG(컬럼)`, `MAX()`, `MIN()`

# 5. 서브쿼리 (Subquery)

```sql
-- WHERE 안에서 사용
SELECT name
FROM employees
WHERE dept_id IN (
    SELECT id FROM departments WHERE name = 'IT'
);
```

# 6. CASE WHEN (조건 분기)

```sql
SELECT name,
       CASE 
           WHEN score >= 90 THEN 'A'
           WHEN score >= 80 THEN 'B'
           ELSE 'C'
       END AS grade
FROM students;

```

# 7. 문자열 함수

문자열 연결

`CONCAT(a, b)`

부분 문자열 추출

`SUBSTRING(s, 시작위치, 길이)` 

```sql
SELECT SUBSTRING('HELLO', 2, 3);  -- 'ELL'

-- 이메일 도메인 추출 예시 
-- kim@gmail.com -> gmail.com
SELECT SUBSTRING(email, INSTR(email, '@') + 1) AS domain
FROM users;

INSTR(전체 문자열, 찾고 싶은 문자열) 
-- 반환값: 찾은 위치, 없으면 0 
```

왼쪽 n글자, 오른쪽 n글자

`LEFT(s, n)` `RIGHT(s, n)`

문자열 길이

`LENGTH(s)`

글자 수 

`CHAR_LENGTH(s)`

문자열 치환

`REPLACE(s, a, b)`

소/대문자 변환

`LOWER()` `UPPER()`

# 8. 날짜/시간 함수

현재 시간

`NOW()`

오늘 날짜, 현재 시간

`CURDATE()` `CURTIME()`

날짜 차이 (a-b)

`DATEDIFF(a, b)`

날짜 포맷 지정 (%Y-%m-%d)

`DATE_FORMAT(date, format)`

연, 월, 일 추출

`YEAR(date)` `MONTH()` `DAY()` 

# 9. 윈도우 함수 (MySQL 8 이상)

```sql
SELECT *,
       RANK() OVER (PARTITION BY category ORDER BY score DESC) AS ranking
FROM table;
```

## ROW_NUMBER() - 고유 순위 (무조건 1, 2, 3)

- 동점자 없이 순위를 매김
- 같은 값이여도 무조건 1, 2, 3 …

```sql
SELECT name, score,
       ROW_NUMBER() OVER (ORDER BY score DESC) AS rnum
FROM students;
```

| name | score | rnum |
| --- | --- | --- |
| A | 95 | 1 |
| B | 95 | 2 |
| C | 90 | 3 |

## RANK() vs DENSE_RANK()

- 동일한 값은 같은 순서 부여
- OVER (ORDER BY …) 로 정렬 기준 지정

| 함수 | 동점 다음 순위가 | 예시 순위 |
| --- | --- | --- |
| `RANK()` | 점프함 (건너뜀) | 1, 1, 3 |
| `DENSE_RANK()` | 연속됨 (순서대로) | 1, 1, 2 |

```sql
SELECT name, score,
       RANK() OVER (ORDER BY score DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rank
FROM students;
```

| name | score | rank | dense_rank |
| --- | --- | --- | --- |
| A | 95 | 1 | 1 |
| B | 95 | 1 | 1 |
| C | 90 | 3 | 2 |

## 윈도우 집계함수

SUM() OVER (…), AVG() OVER (…)

- GROUP BY 없이도 집계 가능
- OVER() 안에 PARTITION BY 넣으면 부분 집계
- ORDER BY 넣으면 누적합/이동평균도 가능

```sql
SELECT department, name, salary,
       SUM(salary) OVER (PARTITION BY department) AS dept_total
FROM employees;
```

| department | name | salary | dept_total |
| --- | --- | --- | --- |
| Sales | John | 3000 | 9000 |
| Sales | Jane | 3000 | 9000 |
| Sales | Jack | 3000 | 9000 |
| HR | Alice | 4000 | 8000 |
| HR | Bob | 4000 | 8000 |

누적합

```sql
SELECT name, month, sales,
       SUM(sales) OVER (ORDER BY month) AS cumulative_sales
FROM monthly_sales;
```

| name | month | sales | cumulative_sales |
| --- | --- | --- | --- |
| Kim | Jan | 100 | 100 |
| Kim | Feb | 150 | 250 |
| Kim | Mar | 200 | 450 |

# 10. 기타

중복 제거

`DISTINCT` 

페이징 

`LIMIT` `OFFSET`

- LIMIT
    
    최대 몇 개의 행을 가져올지
    
- OFFSET
    
    앞에서 몇 개의 행을 건너뛸지 
    

```sql
SELECT * FROM 테이블
ORDER BY 컬럼
LIMIT 10 OFFSET 20;
-- 21번째-30번째 행 조회
```

정렬 제거

`ORDER BY NULL`

NULL 처리

`IFNULL(expr1, expr2)`

나머지 연산

`MOD(a, b)`

반올림, 내림

`FLOOR()` `CEIL()` `ROUND()`

# 11. NULL 처리

IFNULL(expr1, expr2)

- expr1이 NULL이면 expr2를 반환, NULL이 아니면 expr1 반환
    
    ```sql
    SELECT IFNULL(phone, '없음') AS phone_number FROM users;
    ```
    

COALESCE(expr1, expr2, …, exprN)

- 가장 먼저 NULL이 아닌 값을 반환
    
    ```sql
    SELECT COALESCE(nickname, username, 'guest') FROM users;
    ```
    

CASE WHEN … THEN … ELSE … END 

```sql
SELECT 
  CASE 
    WHEN email IS NULL THEN '이메일 없음'
    ELSE email
  END AS email_info
FROM users;
```

IS NULL, IS NOT NULL

```sql
SELECT * FROM orders WHERE delivery_date IS NULL;
SELECT * FROM users WHERE phone IS NOT NULL;
```

`= NULL`, `!= NULL`은 안됨. 반드시 `IS` 키워드 사용해야 함

NULLIF(a, b)

- a와 b가 같으면 NULL 반환
    
    ```sql
    SELECT NULLIF(score, 0) AS result
    FROM tests;
    ```
    

집계 함수에서 NULL 처리 

| 함수 | NULL 포함 여부 |
| --- | --- |
| `COUNT(*)` | 모든 행 수 (NULL 포함) |
| `COUNT(column)` | NULL 제외 |
| `SUM()`, `AVG()` | NULL 제외하고 계산 |

# 12. 비트 연산자

| 연산자 | 이름 | 설명 |
| --- | --- | --- |
| `&` | AND | 둘 다 1일 때만 1 |
| `\|`   | OR | 둘 중에 하나라도 1이면 1  |
| `^` | XOR | 서로 다르면 1, 같으면 0 |
| `~` | NOT | 비트를 반전 (1 → 0, 0 → 1) ※ MySQL에서는 부호 포함이라 주의 필요 |

```sql
-- AND: 공통 비트 확인
SELECT 6 & 3;   -- 110 & 011 = 010 → 2

-- OR: 모든 비트를 포함
SELECT 6 | 3;   -- 110 | 011 = 111 → 7

-- XOR: 서로 다른 비트만 남김
SELECT 6 ^ 3;   -- 110 ^ 011 = 101 → 5

-- NOT: 비트 반전 (MySQL은 부호 반전까지 포함)
SELECT ~6;      -- -7 (이진수로 보면 -6-1과 같음)
```

## 예제

https://school.programmers.co.kr/learn/courses/30/lessons/276034

1. 특정 스킬을 가진 개발자 찾기 (AND)
    
    SKILL_CODE는 여러 스킬을 2의 제곱수로 더해 표현한 값이다.
    
    Python(256) 또는 C#(1024) 스킬을 가진 개발자의 이메일을 조회하라.
    
    ```sql
    SELECT EMAIL
    FROM DEVELOPERS
    WHERE SKILL_CODE & 256 > 0 OR SKILL_CODE & 1024 > 0;
    ```
    

1. OR 비트 연산을 통해 모든 기술을 합치기 
    
    세 명의 개발자가 가진 기술을 모두 합쳐보자.
    
    ```sql
    SELECT BIT_OR(SKILL_CODE) AS TOTAL_SKILL_CODE
    FROM DEVELOPERS;
    ```
    
    `BIT_OR()`는 MySQL 내장 함수로 다수 행의 OR 연산 결과를 계산
    

1. 두 개발자의 기술 비교: 서로 다른 기술 구하기 (XOR)
    
    개발자 A와 B가 가진 기술 중 서로 다른 기술만 구분하고 싶다.
    
    ```sql
    SELECT A.ID AS A_ID, B.ID AS B_ID, 
           (A.SKILL_CODE ^ B.SKILL_CODE) AS DIFF_SKILL_CODE
    FROM DEVELOPERS A
    JOIN DEVELOPERS B ON A.ID < B.ID;
    ```
