# Model

Django는 Model을 이용하여 데이터베이스를 처리한다.

보통 데이터베이스에 데이터를 저장하고 조회하기 위해서 SQL 쿼리문을 이용해야 하지만 장고의 Model을 사용하면 쉽게 데이터를 처리할 수 있다.

## Database

체계화된 데이터의 모임

데이터 검색을 잘 하기 위해서 잘 정리해서 저장해둔다

### 기본구조

1. 스키마
2. 테이블

### 스키마

데이터베이스의 뼈대(Structure)

데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

== 데이터의 요약본

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ec2f2d6-01fa-49ca-97c5-99b7ebc69307/Untitled.png)

### 테이블

필드와 레코드를 사용해 조직된 데이터 요소들의 집합

관계(Relation)라고도 부름

1. **필드**
    - 속성, 컬럼(Column)
    - 각 필드에는 고유한 데이터 형식(Type)이 지정됨
        - INT, TEXT
2. **레코드**
    - 튜플, 행(Row)
    - 테이블의 데이터는 레코드에 저장됨
    - 실제 데이터, 4개

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f565c26d-219b-4689-9366-9276be4af251/Untitled.png)

**PK(Primary Key)**

- 기본 키
- 각 레코드의 고유한 값 (식별자로 사용)
- 기술적으로 다른 항목과 절대로 중복되어 나타날 수 없는 단일 값(unique)을 가짐
- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용됨

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/06cd5f4f-62a6-4f07-a405-bcbc79c9e199/Untitled.png)

- 예시 : 주민등록번호

**쿼리 (Query)**

- 데이터를 조회하기 위한 명령어를 일컫음
    - “나 이 데이터 줘”
- Query를 날린다 ⇒ 데이터베이스를 조작한다
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어 (주로 테이블형 자료구조에서)

## Model

사용하는 데이터들의 필수적인 필드(Column)을 정의하고 동작(method)들을 포함하고

그 둘을 통해서 데이터베이스의 구조를 작성한다

모델 클래스 1개 == 데이터베이스 테이블 1개

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/38ab5a1d-9f3f-4a80-a4f5-111ca3a559ca/Untitled.png)

모델 ≠ 데이터베이스

독립적으로 있는 데이터베이스와 모델을 통해 소통하는 것!

**클래스를 만들어보자(**파이썬 OOP쪽 공부하기!)

```python
# articles/models.py

# models의 Model 클래스를 상속받을 것(각 모델은 상속을 받아야 온전한 기능 가능)
**class Article(models.Model):**
    # 상속받은 것을 그대로 이용한다
    # 우리는 테이블만 정의(column)

    # 클래스 변수가 하나의 필드가 된다
    # 필드 이름 = 타입 -> 스키마를 만들어 보자(설계도)
		# models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의
    **title = models.CharField(max_length=10)**  # max_length=가 필수 인자
    **content = models.TextField()**  # 길이가 더 길게 가능(글자 수가 많을 때 사용)
```

 **<스키마>**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8aa1384a-3e99-4ccd-9bb1-faaeafed1ef4/Untitled.png)

⇒ 그래서 이 뼈대를 가지고 실제 데이터베이스에 어떻게 반영할 것인가?

## Migrations

Django가 모델에 생긴 변화(models.py)를 실제 데이터베이스에 반영하는 방법

모델에 대한 청사진을 만들고 이를 통해 테이블을 생성하는 일련의 과정

### 1. makemigrations

모델의 변경사항에 대한 새로운 migration(**설계도**)을 만들 때 사용

`$ python [manage.py](http://manage.py/) makemigration`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8a7f649e-0ce5-44dc-a42e-82ce5391b4cd/Untitled.png)

⇒ 아직 DB에는 보내지 않음

### 2. migrate

makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정

결과적으로 **모델의 변경사항**과 데이터베이스를 **동기화**

`$ python [manage.py](http://manage.py) migrate`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d7f578e6-a286-4462-9825-117277bac257/Untitled.png)

테이블을 만들 때 **‘앱이름_클래스이름’**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/021272fe-525b-4e08-9c2f-e435950d7fda/Untitled.png)

### [참고] 기타 명령어

1. showmigrations

`$ python [manage.py](http://manage.py/) showmigrations`

migrations 파일들이 migrate 됐는지 확인하는 용도

1. sqlmigrate

`$ python [manage.py](http://manage.py) sqlmigrate 앱이름 설계도번호`

해당 migrations 파일이 SQL 문으로 어떻게 해석될지 미리 확인

### 추가 필드

기존의 테이블에 2개의 컬럼이 추가되는 상황

```python
**class Article(models.Model):

    title = models.CharField(max_length=10)
    content = models.TextField()
  
    created_at = models.DateTimeField(auto_now_add=True)** 
# DateTimeFeild() : 날짜 및 시간을 값으로 사용하는 필드
# auto_now_add= : 최초 생성 일자
# 데이터가 실제로 만들어질 때 현재 날짜와 시간으로 자동으로 초기화
    **updated_at = models.DateTimeField(auto_now=True)**
# auto_now= : 최초 수정 일자
# 데이터가 수정될 때마다 현재 날짜와 시간으로 자동 갱신
```

데이터가 변경되었으니 이를 바탕으로 새로운 설계도를 만들어야 함

`python [manage.py](http://manage.py) makemigrations`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e90cfdc8-a089-4a18-95cc-4636c6b35e94/Untitled.png)

장고는 기본적으로 컬럼을 빈값으로 추가할 수 없음

1. 다음 화면으로 넘어가서 새 컬럼의 기본 값을 직접 입력하는 방법
2. 현재 과정에서 나가고 모델 필드에 default 속성을 직접 작성하는 방법

⇒ 1번 선택

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4a8814a7-c4df-4343-b5f7-7e83d6833318/Untitled.png)

django : 엔터 누르면 내가 알아서 해줄게

⇒ enter

후에 동기화

`python [manage.py](http://manage.py) migrate`

### 반드시 기억해야 할 migration 3단계

1. models.py에서 변경사항이 발생하면
2. migrations 파일 생성 (설계도 생성)
    - `makemigrations`
3. DB 반영 (모델과 DB의 동기화)
    - `migrate`

그런데 설계도는 어떻게, 누가 해석할까?

⇒ 중간에 번역하는 친구가 ORM

## ORM

Object-Relational-Mapping

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에 데이터를 변환하는 프로그래밍 기술

(Django ↔ DB)

⇒ SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d7239c4f-7c57-480f-9312-c493f4a6721c/Untitled.png)

**장점**

SQL을 몰라도 객체지향 언어로 DB조작 가능

**단점**

나중에 프로그램이 커졌을 때 ORM만으로는 세밀한 데이터베이스 조작을 구현하기 어려운 경우가 있음

**ORM을 사용하는 이유**

⇒ 생산성

### [참고] Shell

운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램

Shell, 사용자와 운영 체제의 내부사이의 인터페이스를 감싸는 층이기 때문에 이런 이름이 붙음

사용자 ↔ Shell ↔ 운영체제

예시) git Bash

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e0e4e947-e4a3-4f73-bf88-56d7ac04a662/Untitled.png)

### QuerySet API

1. 장고에서 shell 켜기 `$ python [manage.py](http://manage.py/) shell_plus`
2. 전체 데이터 조회 `Article.objects.all()`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bf38b67e-9673-4de2-857b-e0b8122f1f7d/Untitled.png)

                                                                                                              읽기, 조회, 수정 등

### Query

데이터베이스에 특정한 데이터를 보여달라는 요청

`Article.objects.all()` ⇒ ORM ⇒ SQL ⇒ ORM ⇒ 나

### QuerySet

데이터베이스에게서 전달 받은 객체 목록 (데이터 모음, 복수형)

- 순회 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/702bbdb0-de6c-4e63-9842-79914db57edf/Untitled.png)

### CRUD 실습

Create/ Read/ Update/ Delete

## Create

1. model 클래스로 인스턴스 생성
    
    `article = Article()`
    
2. 필드에 맞는 인스턴스 변수 생성
    
    `article.title = '제목'`
    
3. 저장
    
    `article.save()`
    
    객체를 데이터베이스에 저장 ⇒ id값에 1부여
    

```python
# 

from .models import Article

article = Article()  # Article 클래스를 이용해 article 인스턴스 생성

In [5]: article
Out[5]: <Article: Article object (None)>

article.title = 'fisrt'  # article의 title이라는 속성에 'first'값을 넣어준다
article.content = 'django!'

article.save()  # DB에 저장(반영)

In [9]: article
Out[9]: <Article: Article object (1)>  # id(1) 부여
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/95235a45-eb81-4e8d-92f4-4d4d2e3bf15a/Untitled.png)

```python
# 2번. 한 줄로도 가능
article = Article(title='second', content='django!!')

article.save()

In [12]: article
Out[12]: <Article: Article object (2)>
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3787519b-cce9-4843-9fb8-3129c74eaa04/Untitled.png)

```python
# 3. 한 번에 save까지 된다 
Article.objects.create(title='third', content='django!!!')

Out[14]: <Article: Article object (3)>
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/028e05c4-02c7-4002-966f-3481d5189532/Untitled.png)

## ⭐ Read ⭐

Class 모델의 데이터는 Class.objects를 통해서 조회할 수 있다.

1. return new querysets ⇒ 데이터 목록
2. do not return querysets ⇒ 데이터 한 개

### all()

QuerySet return

전체 데이터 조회

```python
from .models import Article

Article.objects.all()
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/59228aa9-5d9e-4818-b9c9-714bf09ba361/Untitled.png)

return된다는 것은 이 값을 어딘가에 담아서 쓸 수 있다는 것

반복 가능한 객체 ⇒ for문이 가능하다

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/055d0985-1620-40d8-b3da-a913dbfeee65/Untitled.png)

### get()

단일 데이터 조회 (반드시 1건의 데이터를 조회할 때 사용)

**primary key와 같이 고유성을 보장하는 조회에서 사용해야 함**

```python
Article.objects.get(id=1)
```

예외

- 객체를 찾을 수 없으면 DoesNotExist
- 둘 이상의 객체 MultipleObjectsReturned

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ae37f1d6-fd6c-4002-93c7-5752be993147/Untitled.png)

**[참고]**

id값 대신 제목 표시가능

```python
# __str__ 메서드를 추가하면 id값 대신 제목을 표시할 수 있따

class Myclass(models.Model):
		...

		def __str__(self):
				return self.subject
```

### filter()

```python
# id값이 1인 Article 데이터를 조회

Article.objects.filter(id=1)

# filter는 조건에 해당되는 데이터를 모두 리턴해준다(QuerySwt 리턴)
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/be3e2c45-fc6b-4166-88d5-ce3a5472ea71/Untitled.png)

없어도 빈 QuerySet

하나여도 Queryset으로 반환

pk를 찾았는데 없는데도 빈 쿼리셋을 줌 ⇒ **부적합 (get으로만 조회한다)**

### Field lookup

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f0276149-86eb-439d-9271-bb3d670c708e/Untitled.png)

## Update

```python
def update(request, pk):

		# id값이 2인 데이터 조회
		article = Article.objects.get(id=2)
		
		# subject 속성을 수정
		aticle.subject = 'update'
		
		# 반드시 저장해줘야함
		article.save()

		return redirect('articles:detail', article.pk)
```

## Delete

```python
def delete(request, pk):

		article = Article.objects.get(id=2)
		article.delete()

		return rendirect('articles:index') 
```

### 총복습

Django == Framework == Meal-kit

사용자 ⇒ 요청 ⇒ URLs

```html
POST 쓸 때
**{% csrf_token %}** # 사용자가 맞는지 유효성 검사
```

```
 request.GET['id']

"GET"요청으로 들어온 id라는 파라미터를 받는 구문입니다.이후 data딕셔너리에 파라미터를 담아 "parameter.html"로 전송
```

render와 redirect의 차이점

[https://velog.io/@ready2start/Django-redirect](https://velog.io/@ready2start/Django-redirect)

path

**route**

URL 패턴을 가진 문자열이다.

**view**

Django 에서 일치하는 패턴을 찾으면, [HttpRequest](https://docs.djangoproject.com/ko/3.0/ref/request-response/#django.http.HttpRequest) 객체를 첫번째 인수로 하고, 경로로 부터 '캡처된' 값을 키워드 인수로하여 특정한 view 함수를 호출.

**kwargs**

임의의 키워드 인수들은 목표한 view 에 사전형으로 전달

**name**

URL 에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조가 가능하다

## admin

- admin 계정 생성

`python [manage.py](http://manage.py) createsuperuser`

```python
사용자 이름: admin
이메일 주소: 
Password:
Password (again):
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
비밀번호가 너무 일상적인 단어입니다.
비밀번호가 전부 숫자로 되어 있습니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

- admin에 모델 클래스 등록

```python
# articles/admin.py

from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

<결과>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2930c205-57df-4b2d-b00b-43869ff22691/Untitled.png)