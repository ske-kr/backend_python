# 장고의 구조

- MVT 구조

MVC구조와는 무엇이 다를까?



# 장고의 구성

- urls

뷰 함수에 대한 매핑을 통해 특정한 url에 대한 view를 매핑시켜준다.

- views

HTTP request를 수신하고 원하는 결과를 return 하는 핵심적인 부분

- models

model이라는 파이썬 객체를 통해 data를 관리. 그러나 database와 직접소통하는 방식이 아니다.
직접적 제어가 아닌 model 객체를 통해 명령을 내리면 장고가 db에 관한 작업을 처리하는 방식

ps- 아주 기본내용만 적어놓았고 상세한 복습은 코드를 통해 진행

# asgi.py // wsgi.py

- 8.27내 기입완료할것