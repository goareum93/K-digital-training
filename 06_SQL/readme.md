# Data Understanding  (DataBase)

이 자료는 정준수 강사님의 강의를 바탕으로 작성한 것입니다.

강의날짜 : 2021.6.14 ~ 6.15



*The goal of a model is to privde a simple low-dimensional summary of dataset - Hadley Wickham*



## 데이터베이스

데이터베이스는 여러사람에 의해 공유되어 사용할 목적으로 통합하여 관리되는 데이터의 집합, 줄여서 DB라고 말함

관계형 데이터베이스(RDBMS)는 데이터를 로우(Row : 행), 컬럼(Colume : 열)과 같이 일종의 표 형태로 저장하고 종속성은 관계(Relation)로 표현함

컬럼의 구조와 데이터의 관계가 테이블 스키마(Schema)로 사전 정의되고, SQL(구조화 질의 언어)에 의해서 정교한 검색 쿼리를 제공하며 상상하는 거의 모든 방식으로 데이터를 다룰 수 있게 됨



## SQL

- 2차원의 정형데이터를 다루는 가장 효율적인 언어
- Data의 처리 과정을 기술하는 방법이 아닌 원하는 Data의 요건을 기술하는 방식
- Data의 요건이 기술된 요건 정의서 형태이므로 요건의 변경시 적은 수정으로 요건을 반영할 수 있음



### 기본 문법

'SQL로 맛보는 데이터 전처리 분석' 교재 기준으로 기술



#### SELECT

- SELECT : 선택하고자 하는 속성목록을 기술

  SELECT 칼럼, 계산값

  ```sql
  # 쿼리란 데이터베이스에 정보를 요청하는 것
  
  ## SELECT
  
  # 칼럼조회
  SELECT customerNumber FROM classicmodels.customers;
  
  # 집계함수
  SELECT SUM(AMOUNT),COUNT(checkNumber) FROM classicmodels.payments;
  
  # *(모든결과조회)
  SELECT * FROM classicmodels.payments;
  SELECT productName, productLine FROM classicmodels.products;
  
  # AS 칼럼 명을 변경해 조회
  SELECT count(productCode) AS N_PRODUCTS, 
  COUNT(productCode) N_PRODUCTS 
  FROM classicmodels.products;
  
  # DISTINCT 중복을 제외하고 데이터 조회
  SELECT DISTINCT orderNumber FROM classicmodels.orderDetails;
  ```



#### FROM

- FROM : Source Data Set을 기술

  FROM 테이블 명

  ```sql
  ## FROM 테이블명
  # 두가지 방식으로 사용
  # 1) SELECT 계산식 또는 칼럼 명 FROM DB 명.SALES;
  # 2) USE DB 명; SELECT 계산식 또는 칼럼 명 FROM SALES;
  ```



#### WHERE

- WHERE: 선택하고자 하는 행의 조건의 목록을 기술

  WHERE 조건

  ```sql
  ## WHERE 조건
  SELECT customerNumber FROM classicmodels.customers where country='USA';
  SELECT * FROM classicmodels.customers where country='USA';
  
  # BETWEEN 시작점 AND 끝점
  SELECT * FROM classicmodels.orderdetails WHERE priceEach BETWEEN 30 AND 50;
  
  # 대소 관계 표현
  SELECT * FROM classicmodels.orderdetails WHERE priceEach >= 30;
  
  # IN (값, 값2) => 값1 또는 값2 출력
  SELECT customerNumber FROM classicmodels.customers WHERE country IN ('USA', 'Canada');
  
  # NOT IN (값1, 값2)
  SELECT customerNumber FROM classicmodels.customers WHERE country NOT IN ('USA', 'Canada');
  
  # IS NULL 결측치(NULL) 처리
  SELECT employeeNumber FROM classicmodels.employees WHERE reportsTo IS NULL;
  SELECT employeeNumber FROM classicmodels.employees WHERE reportsTo IS NOT NULL; # NULL이 아닌 것만 출력하고 싶을 때
  
  # LIKE '%TEXT%' TEXT가 들어간 데이터를 조회하고 싶을때
  SELECT addressLine1 FROM classicmodels.customers WHERE addressLine1 LIKE '%ST%';
  ```



#### GROUP BY

- GROUP BY: 집계하고자 하는 기준속성목록을 기술

  GROUP

  BY 그룹화

  ```sql
  ## GROUP BY 그룹화
  
  # 집계함수 활용 => 집계함수 AVG(), COUNT(), SUM()
  SELECT country, city, count(customerNumber) N_COUSTOMERS FROM classicmodels.customers GROUP BY country, city;
  
  # 집계 함수에 CASE WHEN 구문 사용
  select sum(case when country = 'USA' then 1 else 0 end) N_USA, sum(case when country = 'USA' then 1 else 0 end)/count(*) USA_PORTION
  from classicmodels.customers;
  
  # 교재 외 연습내용
  use classicmodels;
  show tables;
  select * from employees;
  select firstName from employees;
  select firstName, lastName from employees;
  select employeeNumber, firstName, lastName from employees where employees.employeeNumber >= 1300;
  select * from offices;
  select city from offices where offices.officeCode='1';
  select city, phone from offices where offices.officeCode='1';
  ```



#### JOIN

- JOIN => 테이블 결합함수

  ```sql
  # LEFT JOIN => FROM 절의 테이블 기준으로 매칭되는 정보 호출
  select a.orderNumber, b.country from classicmodels.orders A LEFT JOIN classicmodels.customers B ON a.customerNumber = b.customerNumber
  select a.orderNumber, b.country from classicmodels.orders A LEFT JOIN classicmodels.customers B ON a.customerNumber = b.customerNumber
  where b.country = 'USA';
  
  # INNER JOIN => 교집합만 출력
  select a.orderNumber, b.country from classicmodels.orders A INNER JOIN classicmodels.customers B ON a.customerNumber = b.customerNumber
  where b.country = 'USA';
  
  # FULL JOIN => 거의 사용하지 않음
  ```

  

#### CASE WHEN

- SELECT CASE WHEN 조건 1 TEHN 결과1

  WHEN 조건 2 THEN 결과 2 ELSE 결과 3 END

  FROM 데이터베이스.테이블 명;

  ```sql
  ## CASE WHEN
  select country, case when country in ('USA', 'Canada') then 'North Ameria' else 'Others' end as region from classicmodels.customers;
  
  select case when country in ('USA', 'Canada') then 'North Ameria' 
  else 'Others' end as region, 
  count(customerNumber) N_customer 
  from classicmodels.customers
  group
  by case when country in ('USA', 'Canada') then 'North Ameria' else 'Others' end;
  
  select case when country in ('USA', 'Canada') then 'North Ameria' 
  else 'Others' end as region, 
  count(customerNumber) N_customer 
  from classicmodels.customers
  group
  by 1;
  ```

  

## 데이터 분석을 위한 파이썬 연동 SQL 사용 실습  

### MySQL DB 모듈 설치

Python에서 MySQL 데이터베이스를 사용하기 위해 우선 Python DB API 표준을 따르는 MySQL DB 모듈을 다운받아 설치한다.

MySQL DB 모듈 중 하나인 **PyMySql 모듈**을 Anaconda Powershell Prompt (anaconda3)에서 설치한다.

```shell
$ pip install PyMySQL
```



### MySql 사용 절차

1. PyMySql 모듈을 import 한다.

   ```python
   import pymysql.cursors
   ```

   

2. pymysql.connect() 메소드를 사용하여 MySQL에 Connect 한다. 호스트명, 로그인, 암호, 접속할 DB 등을 파라미터로 지정한다.

   ```python
   connection = pymysql.connect(host='localhost',
           user='root',
           password='1234',
           db='tip',
           charset='utf8',
           cursorclass=pymysql.cursors.DictCursor)
   ```

3. DB 접속이 성공하면, Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져온다. DB 커서는 Fetch 동작을 관리하는데 사용되는데, 만약 DB 자체가 커서를 지원하지 않으면, Python DB API에서 이 커서 동작을 Emulation 하게 된다.

4. Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 보낸다. SQL 쿼리의 경우 Cursor 객체의 fetchall(), fetchone(), fetchmany() 등의 메서드를 사용하여 데이타를 서버로부터 가져온 후, Fetch 된 데이터를 사용한다.

   ```python
   try:
       with connection.cursor() as cursor:
           sql = "SELECT total_bill FROM tip.tips where tip >= 7;"
           cursor.execute(sql)
   
           result = cursor.fetchone()
           print(result)
   ```

5. Connection 객체의 close() 메서드를 사용하여 DB 연결을 닫는다.

   ```python
   finally:
       connection.close()
   ```



source : 

- sql_basic.sql
- python_db.ipynb
- tips.csv



Reference : http://pythonstudy.xyz/python/article/202-MySQL-%EC%BF%BC%EB%A6%AC



### SQL과 python 비교 예시

Reference : https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#compare-with-sql



실습 파일 : tips_pandas.ipyn

source : 

- tips.csv

