## Django

### framework == meal-kit

서비스 개발에 필요한 기능들을 미리 구현해서 모아놓은 것

내가 만들고자 하는 본질에 집중하는 것

⇒ 소프트웨어의 **생산성과 품질**을 높임

## WWW

### World Wide Web

전 세계에 퍼져있는 거미줄같은 연결망

## 클라이언트와 서버

### 클라이언트 - 서버 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a152fc7-af73-4e06-9d81-6daac0be67dd/Untitled.png)

**클라이언트**

- 웹 사용자의 인터넷에 연결된 장치 (예를 들어 wi-fi에 연결된 컴퓨터 또는 모바일)
- Chrome 또는  Firefox같은 웹 브라우저
- 서비스를 요청하는 주체

**서버**

- 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
- 클라이언트가 웹페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
- 요청에 대해 서비스를 응답하는 주체

## 웹 브라우저와 웹 페이지

### 웹 브라우저

페이지와 페이지를 하이퍼링크로 연결해놓은 것

웹 페이지 파일을 우리가 보는 화면으로 바꿔주는 (rendering)프로그램

### 웹 페이지

**정적 웹 페이지**

- ex) 최초의 웹 사이트

[http://info.cern.ch](http://info.cern.ch)

- 누가 들어오든 똑같은 사이트

**동적 웹 페이지**

- ex) 백준 홈페이지(아이디가 다름)
- 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
- 웹 페이지의 내용을 바꿔주는 주체 == **서버**
    - 사용자의 요청을 받아서 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임 워크가 바로 **Django**

### 3줄 정리

1. 프레임 워크가 뭔가요? == 밀키트
2. 웹 : 서버(문서를 보여준다) - 클라이언트(웹 브라우저가 하는 일)
3. 정적 페이지 vs 동적 페이지

## MTV Design Pattern

### **디자인 패턴이란?**

하나의 일반화된 공법

- ‘클라이언트 - 서버 구조’도 디자인 패턴 중 하나

### MVC 소프트웨어 디자인 패턴(Model-View-Controller)

**Model** 데이터와 관련된 로직을 관리

**View** 사람들에게 보여지는 것

**Controller** 명령을 model과 view 부분으로 연결 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/272b3c36-23c0-4997-808f-e633ea154ad2/Untitled.png)

그냥 용어만 바뀌었을 뿐, 다른 점은 없음

### MTV 디자인 패턴(Django)

**Model**

- MVC - **Model**
- 데이터와 관련된 로직을 관리
- 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
- ex) 사용자, 영화 정보

**Template**

- MVC - **View**
- 레이아웃과 화면을 처리
- 사용자 인터페이스 구조와 레이아웃을 정의

**View**

- MVC - **Controller**
- 화면과 데이터를 연결
- 클라이언트 요청에 대해 처리
- 동작 예시
    - 데이터가 필요하면 model에서 데이터를 가져오고, 가져온 데이터를 template로 보내 화면을 구성하고, 구성된 화면을 응답으로 만들어 클라이언트에게 반환
    

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ce6bf060-c9ea-4e3b-8e25-692bb2e2de58/Untitled.png)

### 3줄 정리

1. 디자인 패턴
2. MVC
3. Django - MTV

## Django Quick Start

1. VSC 코드 열기
2. 설치 2개
3.  세팅에 코드 추가
4. 가상환경 만들기 : `$ python -m venv venv` 
5. 가상환경 활성화 : `$ source venv/Scripts/activate` 
    - 비활성화 : `$ deactivate`
6. 설치된 프로그램 보기 : `$ pip list` 
7. Django 설치하기 : `$ pip install django==3.2.13` 
8. 업데이트할 때마다 덮어씌우기 : `$ pip freeze > requirements.txt` 
    - *참고사항*
    - `$ pip install -r requirements.txt` : 집에가서 한꺼번에 requirements.txt에 있는 파일 설치

1. 장고 프로젝트 생성(현재 폴더 기준으로) : `$ django-admin startproject firstpjt .` 
2. `$ python [manage.py](http://manage.py/) runserver` 하고 나서 밑에 URL을 `ctrl` 누르고 클릭 ⇒ 장고 킨거

1. application으로 각각의 기능을 나눠담는다

`$ python [manage.py](http://manage.py/) startapp articles` : ‘아티클’ 앱 생성

1. settings.py를 열어서 INSALLED_APPS 리스트 맨 위에 `‘articles’,` 추가 ⇒ **반드시 생성 후 등록**

1.  [urls.p](http://urls.pt)y에 path 등록 → `path('index/', views.index),` + `from articles import views`

```python
# urls.py

**from articles import views

urlpatterns = [
		path('admin/', admin.site.urls),
		path('index/', views.index),
]**
```

1. articles > [views.py](http://views.py) > 함수생성

```python
**def index(request):
    return render(request, 'index.html')**
					# 화면에 렌더링하는 함수

# request : 응답을 생성하는 데 사용되는 요청 객체
# template_name : 템플릿 이름의 경로
# context : 템플릿에서 사용할 데이터(딕셔너리 타입)
```

1. template 생성
    - articles(앱) > templates 폴더 생성 > index.html 파일 생성
    
    ```html
    # 상속시
    
    **{% extends 'base.html' %}
    
    {% block content %}
      <h1 class="text-danger">홈 화면</h1>
    {% endblock %}**
    ```
    

< 동작 예시 > 

사용자가 요청          ➡️     **URLs**       ➡️     index

                                       ⬇️

(Class 1개) **Model**    ↔️      **Views**       ➡️     **Templates**     ➡️ 사용자에게 반환( ➡️html/Json)로 응답) 

        (ORM) ↕                      

                    **DB**      

             (테이블 1개)

**반드시 이 순서대로 진행**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/da50537d-1053-486c-96c0-434e01737813/Untitled.png)

**[참고]**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3d08c99f-620c-4706-a342-34ecd15a48f2/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c260b630-3941-4e14-9b03-cc41984e02e9/Untitled.png)

## URLs.py

페이지 요청이 발생하면 가장 먼저 호출되는 파일로 URL과 view함수 간의 mapping을 정의한다.

urls.py에 mapping을 추가한다

`from 앱이름 import views`

```python
from articles import views

urlpatterns = [
		path('articles/', views.index),
		# articles/ url이 요청되면 views.index를 호출하라

# 참고 : 마지막에 /를 붙여주면 알아서 /를 붙여준다
```

## App URL mapping

앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법을 이해하기

하나의 프로젝트에 여러 앱이 존재한다면, 각각의 앱 안에 [urls.py](http://urls.py)를 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁할 수 있음

```python
# project/urls.py

from django.urls import path, include
~~from articles import views~~

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
		# articles/로 시작하는 페이지를 요청하면 articles/urls.py의 매핑정보를 읽어서 처리
]
```

```python
# articles/urls.py

from django.urls import path
from .(현재) import views

urlpatterns = [
		path('', views.index),
		# ''인 이유 : 이미 projet/urls.py에서 articles/로 매핑되어서''만 해줘도
		# articles/로 처리된다
]
```

 

이제 메인 페이지의 주소는 이렇게 바뀌었음

[`http://127.0.0.1:8000/index`](http://127.0.0.1:8000/index) → `http://127.0.0.1:8000/articles/index`

### include()

다른 URLconf(app1/urls.py)들을 참조할 수 있도록 돕는 함수

함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/96a74261-ed59-4232-960a-1c9bb00c3bb0/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2535984e-2abf-402d-8411-23462b9bfb0e/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/baeb0cd7-408d-481c-9e93-52482a73965b/Untitled.png)

## Views.py

views.py에 함수 추가해준다

```python
from django.shortcuts import render
							

def index(request):
    return render(request, 'index.html')
					# 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수

# request : 응답을 생성하는 데 사용되는 요청 객체
# template_name : 템플릿 이름의 경로
# context : 템플릿에서 사용할 데이터(딕셔너리 타입)
```

## Django Template

데이터 표현을 제어하는 도구이자 표현에 관련된 로직

### Django Template Language(DTL)

django template에서 사용하는 built-in template system

### DTL Syntax

- Variable
- Filters
- Tags
- Comments

## Variable

`{{ variable }}`

render()의 세번째 인자로 {’key’: value}와 같이 딕셔너리 형태로 넘겨주며, key가 변수명이 된다.

**context 사용을 권장**

```python
# views.py

def 함수명(request):
		food = ['apple', 'banana', 'coconut']
		
		context = {
				'food' : food
		}
		
		return render(request, 'food.html', context)
		# context 데이터를 food.html 파일(템플릿)에 적용하여 html을 생성

# 템플릿 파일은 html 파인과 비슷하지만 파이썬 데이터를 읽어서 사용할 수 있는 html 파일이다
```

`{{ 객체.속성 }}`

## Filters

`{{ variable|filter }}`

표시할 변수를 수정할 때 사용

## Tag

`{% tag %}`

for문이나 if문 등

### if문

```html
{% if 조건문1 %}
    <p>조건문1에 해당되는 경우</p>
{% elif 조건문2 %}
    <p>조건문2에 해당되는 경우</p>
{% else %}
    <p>조건문1, 2에 모두 해당되지 않는 경우</p>
{% endif %}
```

### 반복문

```html
{% for item in list %}
    <p>순서: {{ forloop.counter }} </p>
    <p>{{ item }}</p>
{% endfor %}
```

| forloop 속성 | 설명 |
| --- | --- |
| forloop.counter | 루프내의 순서로 1부터 표시  |
| forloop.counter0 | 루프내의 순서로 0부터 표시 |
| forloop.first | 루프의 첫 번째 순서인 경우 True |
| forloop.last | 루프의 마지막 순서인 경우 True |

## Comments

`{# 한 줄 주석 #}`

```html
**{% comment %}
여러줄 주석
여러줄 주석
{% endcomment %}**
```

## Template inheritance

블럭을 갈아끼듯이 원하는 것을 넣고 원하는 것을 뺀다

1. settins.py에서 수정

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/669766cc-a601-4d4f-bdcb-cc7f0c860c22/Untitled.png)

1. 내가 바꿀 내용만 수정

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9340c18a-09ca-4bad-8a6d-e7e5b2cfbfe9/Untitled.png)

```html
**{% extends '' %}**
# 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
# 반드시 템플릿 최상단에 작성

**{% block content %}**
# 여기에 내용 작성
**{% endblock content %}**
```

## Sending and Retrieving form data

데이터 보내고 가져오기

<form> 을 이용해서 데이터 전송

                           클라이언트       데이터를 담아서(form에) 요청

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/08e99e9e-b0bd-44b8-843d-f7ce80a16b26/Untitled.png)

                                                              응답 (장고, MTV)                          서버

### Sending form data(Client)

데이터가 전송되는 방법을 정의

웹에서 사용자 정보를 입력하는 여러 방식을 제공하고, **사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당**

“데이터를 어디(action)로 어떤 방식(method)으로 보낼지”

### action = url : 어디에 전송?

입력 데이터가 전송될 URL을 지정

데이터를 어디로 보낼 것인지 지정

### method = GET, POST : 어떻게 전송?

데이터를 어떻게 보낼 것인지 정의

입력 데이터의 HTTP request methods를 지정

GET과 POST 방식이 있다

```html
# articles/templates/throw.html

**{% extends '' %}

{% block content %}
  <h1>Throw<h1>
  <form action="/catch/" method="GET">
		<label for="message">Throw</label>
		<input type="text" id="message" name="message">
		<input type="submit">
	</form>
{% endblock content %}**
```

### GET

서버로부터 정보를 **조회**하는데 사용

**데이터를 가져올 때** 사용

### Retrieving the data(Server)

데이터 가져오기(검색하기)

서버는 클라이언트로 받은 key-value쌍의 목록과 같은 데이터를 받게 됨

throw 페이지의 form이 보낸 데이터는 어디에 들어있는걸까?

catch 페이지의 url 확인 `http://127.0.0.1:8000/catch/?message=데이터`

데이터 가져오기

모든 요청 데이터는 view 함수의 첫번째 인자 request에 들어있다

```python
# views.py

def catch(request):
		message = request.GET.get('message'}
		context = {
				'message': message,
		}
		return render(request, 'catch.html', context)
```

```html
# articles/templates/catch.html

{% extends '' %}

{% block content %}
  <h1>Catch<h1>
  <hw>여기서 {{ message }}를 받았어!!<h2>
	<a href="/throw/">다시 던지러</a>
{% endblock content %}
```

## Variable routing

우리가 해야할 일 : 중복을 없애고 재사용성을 높이는 것

URL 주소를 변수로 사용

URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

변수는 <>에 정의하며 view 함수의 인자로 할당됨

1. str (작성하지 않을 경우 기본값)
2. int

```python
# urls.py

urlpatterns = [
		path('<int:id>/', views.hello)
				
'''
http://127.0.0.1:8000/fruits/2/ 페이지가 요청되면
http://127.0.0.1:8000/fruits/<int:pk>/가 적용되어 pk에 2가 저장되고
views.hello 함수 실행
''' 	

]
```

```python
def hello(request, id):
		article = Article.objects.dget(id=id)
		context = {
				'article': article,
		}
		return render(request, 'articles/hello.html', context)

# hello 함수 호출 시 전달되는 매개변수가 request외에 id가 추가되었다.
# 매개변수 id에는 URL 매핑시 저장된 id가 전달된다
# http://127.0.0.1:8000/fruits/2/ 페이지가 요청되면 매개변수 id에 2가 세팅되어 hello 함수가 실행
```

## Naming URL patterns

링크의 주소 대신에 url 별칭 사용하려면 URL 매핑에 name 속성 부여

링크에 URL을 직접 작성하는 것이 아니라 path() 함수의 name 인자를 정의하여 사용

DTL Rag중 하나인 URL 태그를 사용해서 path() 함수에 작성한 name을 사용할 수 있음

url이름을 바꿔도 모든 이름을 다 바꿔줄 필요 없음

```python
# articles/urls.py

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('show/<name>/', views.show, name='show'),
]
```

### Built-in-tag-”url”

`{% url '' %}`

주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환

```html
# index.html

**{% extends '' %}

{% block content %}
  ...
	<a href="{% url 'throw' %}">다시 던지러</a>
{% endblock content %}**
 
```

## Name Space

### URL namespace

```python
# articles/urls.py

app_name = 'articles'

urlpatterns = [

]
```

**url tag**

`**{% url 'index' %}`  ⇒  `{% url 'articles:index' %}`**

app_name : url_name 형태로 사용해야 함

### Templater namespace

`app_name/templates/app_name/index.html`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/610c7f03-01c9-4448-aaa6-cc895e142085/Untitled.png)

`app이름/url이름`