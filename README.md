# api server #
1. ## 개요 ##
	- Django framework를 사용하여 재료 정보와 요리 레시피를 Create, Read, Update, Delete 할 수 있는 REST API server를 구현
		- 개인 Project
	1. ### 수행기간 ###
		- 2022.01.25(1일)
	2. ### 사용언어 ###
		- Python3
	3. ### 목적 ###
		- 요리, 쇼핑 서비스에서 클라이언트에게 기본적으로 제공되며 데이터를 수집하여 활용할 수 있는 MSA 형태의 백엔드를 구현
	4. ### 주요내용 ###
		- Django 활용 API server 구현
		- RDB를 ORM을 사용하여 효율적으로 이용할 수 있도록 학습
		- Data의 Relation에 따라 발생할 수 있는 한계점을 탐색, 최소화
2. ## 계획 ##
	1. ### 과제 범위 확인 ###
		- 구현 기능 설정
		- 필요 라이브러리 탐색 및 스터디
		- 요구사항 목록 작성[재료 추가, 조회, 수정, 삭제, 레시피 추가, 조회, 수정, 삭제]
		- 요구사항 정의서 작성[요구사항분류 및 번호, 명칭, 유형, 상세설명, 산출물]
	2. ### 기존 문제점 탐색 ###
		- 재료 업데이트에 따라 레시피의 원가 정보 업데이트, 재료의 삭제가 기존 레시피에 영향이 없도록 설정
3. ## 설계 ##
	1. ### API 설계 ###
		- Singlton 또는 Collection, Sub Resource에 따라 URI를 일관성있게 작성
		- Resource의 Type에 따라 document, collection, store, controller로 Subdivision하여 설정 
		- 매개변수를 포함한 API 명세서 작성
	2. ### ERD / 테이블 정의 ###
		- TABLE "Ingredient" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "category" varchar(32) NOT NULL, "name" varchar(64) NOT NULL, "stock" integer unsigned NOT NULL CHECK ("stock" >= 0), "price" integer unsigned NOT NULL CHECK ("price" >= 0), "deleted_data" bool NOT NULL)
		- TABLE "Sandwich" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "bread_id" integer NOT NULL REFERENCES "Ingredient" ("id") , "cheese_id" integer NOT NULL REFERENCES "Ingredient" ("id") , "sauce_id" integer NOT NULL REFERENCES "Ingredient" ("id") , "deleted_data" bool NOT NULL, "price" integer unsigned NOT NULL CHECK ("price" >= 0), "sauce2_id" integer NULL REFERENCES "Ingredient" ("id") , "topping2_id" integer NULL REFERENCES "Ingredient" ("id") , "topping_id" integer NOT NULL REFERENCES "Ingredient" ("id"))
	3. ### 개발 표준 / 테스트 시나리오 ###
		- 함수 및 변수명 작성 규칙, 예외처리에 대한 부분, 주석 형식(작성일자, 작성자, Input, Output)
		- Serializer 사용 Data 직렬화
		- 단위 테스트, 통합 테스트 시나리오 작성
4. ## 구현 ##
	- 환경
		- 운영체제:Windows
		- python==3.8.8rc1
		- asgiref==3.5.0
		- backports.zoneinfo==0.2.1
		- Django==4.0.1
		- djangorestframework==3.13.1
		- pytz==2021.3
		- sqlparse==0.4.2
		- tzdata==2021.5
5. ## 테스트 ##
	- 개발 기능 별 단위 테스트 병행(Postman)
	- 테스트 시나리오 보완
	- 서버 환경(AWS EC2) 테스트
	- 프로젝트 완료 보고서 작성

_woodnlowkey(woojin choi, vxrs3310@gmail.com)_
=====
- 관계형 데이터베이스를 실무적으로 활용하기 위해 구체적으로 기능을 설계 및 구현하면서 발생할 수 있는 문제점을 경험할 수 있었고 해결을 위해 관련 정보를 학습했습니다.
- 보다 직관적이고 단순하며 클라이언트의 구조에 맞는 API를 설계하기 위해 찾아보고 고민해 볼 수 있었습니다.
