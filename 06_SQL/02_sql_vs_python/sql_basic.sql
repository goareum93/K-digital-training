# SQL로 맛보는 데이터 전처리 분석
# 쿼리란 데이터베이스에 정보를 요청하는 것

## SELECT
# 칼럼조회
-- SELECT customerNumber FROM classicmodels.customers;
# 집계함수
-- SELECT SUM(AMOUNT),COUNT(checkNumber) FROM classicmodels.payments;
# *(모든결과조회)
-- SELECT * FROM classicmodels.payments;
-- SELECT productName, productLine FROM classicmodels.products;
# AS 칼럼 명을 변경해 조회
-- SELECT count(productCode) AS N_PRODUCTS, 
-- COUNT(productCode) N_PRODUCTS 
-- FROM classicmodels.products;
# DISTINCT 중복을 제외하고 데이터 조회
-- SELECT DISTINCT orderNumber FROM classicmodels.orderDetails;

## FROM 테이블명
# 두가지 방식으로 사용
# 1) SELECT 계산식 또는 칼럼 명 FROM DB 명.SALES;
# 2) USE DB 명; SELECT 계산식 또는 칼럼 명 FROM SALES;

## WHERE 조건
-- SELECT customerNumber FROM classicmodels.customers where country='USA';
-- SELECT * FROM classicmodels.customers where country='USA';
# BETWEEN 시작점 AND 끝점
-- SELECT * FROM classicmodels.orderdetails WHERE priceEach BETWEEN 30 AND 50;
# 대소 관계 표현
-- SELECT * FROM classicmodels.orderdetails WHERE priceEach >= 30;
# IN (값, 값2) => 값1 또는 값2 출력
-- SELECT customerNumber FROM classicmodels.customers WHERE country IN ('USA', 'Canada');
# NOT IN (값1, 값2)
-- SELECT customerNumber FROM classicmodels.customers WHERE country NOT IN ('USA', 'Canada');
# IS NULL 결측치(NULL) 처리
-- SELECT employeeNumber FROM classicmodels.employees WHERE reportsTo IS NULL;
-- SELECT customerNumber FROM classicmodels.customers WHERE country IS NULL;
-- SELECT employeeNumber FROM classicmodels.employees WHERE reportsTo IS NOT NULL; # NULL이 아닌 것만 출력하고 싶을 때
# LIKE '%TEXT%' TEXT가 들어간 데이터를 조회하고 싶을때
-- SELECT addressLine1 FROM classicmodels.customers WHERE addressLine1 LIKE '%ST%';

## GROUP BY 그룹화
# 집계함수 활용 => 집계함수 AVG(), COUNT(), SUM()
-- SELECT country, city, count(customerNumber) N_COUSTOMERS FROM classicmodels.customers GROUP BY country, city;
# 집계 함수에 CASE WHEN 구문 사용
-- select sum(case when country = 'USA' then 1 else 0 end) N_USA, sum(case when country = 'USA' then 1 else 0 end)/count(*) USA_PORTION
-- from classicmodels.customers;

# 교재 외 연습내용
-- use classicmodels;
-- show tables;
-- select * from employees;
-- select firstName from employees;
-- select firstName, lastName from employees;
-- select employeeNumber, firstName, lastName from employees where employees.employeeNumber >= 1300;
-- select * from offices;
-- select city from offices where offices.officeCode='1';
-- select city, phone from offices where offices.officeCode='1';

## JOIN
# LEFT JOIN => FROM 절의 테이블 기준으로 매칭되는 정보 호출
-- select a.orderNumber, b.country from classicmodels.orders A LEFT JOIN classicmodels.customers B ON a.customerNumber = b.customerNumber
-- select a.orderNumber, b.country from classicmodels.orders A LEFT JOIN classicmodels.customers B ON a.customerNumber = b.customerNumber
-- where b.country = 'USA';

# INNER JOIN => 교집합만 출력
-- select a.orderNumber, b.country from classicmodels.orders A INNER JOIN classicmodels.customers B ON a.customerNumber = b.customerNumber
-- where b.country = 'USA';
# FULL JOIN => 거의 사용하지 않음

## CASE WHEN
-- select country, case when country in ('USA', 'Canada') then 'North Ameria' else 'Others' end as region from classicmodels.customers;

-- select case when country in ('USA', 'Canada') then 'North Ameria' 
-- else 'Others' end as region, 
-- count(customerNumber) N_customer 
-- from classicmodels.customers
-- group

-- by case when country in ('USA', 'Canada') then 'North Ameria' else 'Others' end;

-- select case when country in ('USA', 'Canada') then 'North Ameria' 
-- else 'Others' end as region, 
-- count(customerNumber) N_customer 
-- from classicmodels.customers
-- group
-- by 1;


# 파이썬 연동 연습

select customers.state, customers.customerName, payments.checkNumber from customers 
left join payments on customers.customerNumber = payments.customerNumber
where payments.paymentDate >= '2004-10-06';
