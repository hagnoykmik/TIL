# Model간의 관계

- A many-to-one relationship
- N : 1 (Comment - Article)
- N : 1 (Article - User)
- N : 1 (Comment - User)

## A many-to-one relationship

관계형 데이터 베이스에서의 외래 키 속성을 사용해 모델 간 N:1 관계 설정하기

### RDB (관계형 데이터 베이스)

- 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
- RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만드는데 사용할 수 있음

### 외래 키 (foreign key, FK)

관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키

### 관계

테이블 간의 상호 작용을 기반으로 설정되는 여러 테이블 간의 논리적인 연결

### RDB 에서의 관계

1. 1 : 1
    - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
2. N : 1 (주문 : 고객)
    - 한 테이블(주문 테이블)의 0개 이상의 레코드가 다른 테이블(고객 정보 테이블)의 레코드 한 개와 관련된 경우
3. M : N
    - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
    - 양쪽 모두에서 N : 1관계를 가짐

## Foreign Key

### 개념

- 외래 키 (외부 키)
- 참조되는 테이블의 기본 키(Primary Key)를 가리킴
- 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블(주문)에서 1개의 키에 해당하고, 이는 참조되는 측 테이블(고객)의 기본 키를 가리킴
- 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응됨
- 외래 키를 가지고 있는 쪽(N)이 참조하는 쪽이다
- 참조하는 테이블 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있음

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d94e2604-ff91-476a-a265-3cb5c23906b1/Untitled.png)

### 특징

- 키를 사용하여 부모 테이블(참조되는 테이블)의 유일한 값을 참조 ⇒ 참조 무결성
- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함

### [참고] 참조 무결성

- 데이터 베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
- 외래 키가 선언된 테이블(참조하는)의 외래 키 속성(열) 값은 그 테이블의 부모가 되는 테이블(참조되는)의 기본 키 값으로 존재해야 함

# N : 1 (Comment - Article)

- Comment(N) - Article(1)
- 0개 이상의 댓글은 1개의 게시글에 작성될 수 있음
- 댓글은 게시글에 종속

### 모델 관계 설정

- 스키마

![댓글과 게시글 (몇 번째 게시글의 댓글인지)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e3e5550d-38d9-4da1-a1dc-45d754de7a14/Untitled.png)

댓글과 게시글 (몇 번째 게시글의 댓글인지)

- Comment

![3번 게시글 - 1개의 댓글, 1번 게시글 - 2개의 댓글](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9033c271-67e0-4c6c-8f81-1d7aa489a543/Untitled.png)

3번 게시글 - 1개의 댓글, 1번 게시글 - 2개의 댓글

## Django Relationship fields

1. OneToOneField()
2. ForeignKey() ⇒ N : 1 관계
3. ManyToManyField()

### ForeignKey(to, on_delete, **options)

- N : 1 relationship 을 담당하는 Django의 모델 필드 클래스
- Django 모델에서 관계형 데이터 베이스의 외래 키 속성을 담당
- 필수 위치 인자
    1. to = 참조하는 model class
    2. on_delete = on_delete 옵션

### Comment Model

- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계 없이 필드의 마지막에 작성됨
- ForeignKey() Class의 인스턴스(article) 이름은 참조하는 모델(Article()) 클래스 이름의 소문자로 작성하는 것을 권장

```python
# articles/models.py

from django.db import models

# 스키마 구성 - Class형태로 구성
class Article(models.Model):
    # column = models.타입(ModelFeild)(제약조건(option))
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 댓글을 구성하는 테이블을 만들자!

# models모듈의 Model 클래스를 상속받을 거임
class Comment(models.Model):
									 # ForeignKey(참조하는 모델클래스, on_delete)
		article = models.ForeignKey(Article, on_delete=models.CASCADE)

    content = models.TextField()        # 글자 수 제한 X
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
	# column = models.타입(ModelFeild)(제약조건(option))

    def __str__(self):
        return self.content
```

### ForeignKey(to, on_delete)

- 외래 키가 참조하는 객체(게시글)가 사라졌을 때, 외래 키를 가진 객체(댓글)를 어떻게 처리할 지를 정의
- 데이터 무결성을 위함
- on_delete 옵션값
    - CASCADE : 부모 객체(참조된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
    - PROTECT, SET_NULL, SET_DEFAULT …

### [참고] 데이터 무결성

- 데이터의 정확성과 일관성을 유지하고 보증하는 것
- 데이터 베이스나 RDBMS의 중요한 기능
- 무결성 제한의 유형
    1. 개체 무결성
    2. 참조 무결성
    3. 범위 무결성

### Migration

models.py에 수정이 일어나면 migration과정을 해주어야 한다

1. 설계도를 만든다

`$ python [manage.py](http://manage.py/) makemigrations`

1. database에 넣어라

`$ python [manage.py](http://manage.py/) migrate`

- 정리

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8b27aee4-9aa9-47ae-895e-b25a7b2c7667/Untitled.png)

### [참고] 데이터 베이스로 SQL을 이용해서 넘어가는 것 보기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2a8e14a7-ac47-4ecb-a2e6-8db6591daaa1/Untitled.png)

## 실습

### 댓글 생성 연습하기

1. 댓글 생성
    - 사용자로부터 comment의 content를 인스턴스 변수로 받는다.

![articles_id에 NULL 값이 들어갔다 ⇒ article 변수에 값을 지정해주지 않았다 (어떤 게시글에 달건지) ⇒ comment 인스턴스에 article_id 변수가 비어있음](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a4005a66-9de2-4100-990b-d92bb2f13b33/Untitled.png)

articles_id에 NULL 값이 들어갔다 ⇒ article 변수에 값을 지정해주지 않았다 (어떤 게시글에 달건지) ⇒ comment 인스턴스에 article_id 변수가 비어있음

- 어떤 article에 대해서 참조하고 있는지 알아야 하니까 게시글 생성!

![comment 인스턴스의 article 변수 값에 1번 게시글을(article) 넣어준다. ⇒ 알아서 이 객체의 번호 값을 추출해서 저장해준다. ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6ae48615-7958-4514-a466-658862ff853d/Untitled.png)

comment 인스턴스의 article 변수 값에 1번 게시글을(article) 넣어준다. ⇒ 알아서 이 객체의 번호 값을 추출해서 저장해준다. 

1. 댓글 속성 값 확인

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6b44ddd0-e542-447f-ab8c-d847cb4cac08/Untitled.png)

1. comment 인스턴스를 통한 article 값 접근하기

![article 테이블에 있는 pk를 가져온것임 (값은 같으나 다른 위치)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d75d816c-1b12-4c1f-aa31-30f2e02eb14f/Untitled.png)

article 테이블에 있는 pk를 가져온것임 (값은 같으나 다른 위치)

- 결과

![article 1번에 달린 댓글](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6bab5561-c07a-45e3-ab91-88a586aed78e/Untitled.png)

article 1번에 달린 댓글

1. 두 번째 댓글

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e995f244-c3a2-4a7e-9284-b73be5f77d3a/Untitled.png)

## 관계 모델 참조

### Related manager

- 역참조
    - N : 1 관계에서 외래 키를 없는 친구가 본인을 참조하고 있는 외래 키를 가진 친구를 참조하는 것
    - 1이 N을 참조하는 상황
    - 참조 : Commnet(N) → Article(1)
    - 역참조 : Commnet(N) ← Article(1)
- 이전 모델 생성시 objects라는 매니저를 통해 queryset api를 사용했던 것 처럼 related manager를 통해 queryset api를 사용할 수 있게 됨

### _set 매니저

`article.comment_set.method()`

- Article 모델이 Comment 모델을 참조(역 참조)할 때 사용하는 매니저
- Article 클래스에는 Comment 와의 어떠한 관계도 작성되어 있지 않음
- Django가 역 참조할 수 있는 comment_set manager 를 자동으로 생성해 article.commnet_set 형태로 댓글 객체를 참조할 수 있음
    - `모델명_set`

## 실습

### Related manager 연습하기

1. 1번 게시글 조회하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3e26fa6e-6eab-4368-b2c2-e90f776c2461/Untitled.png)

1. `dir(클래스 객체)` 로 사용할 수 있는 메서드 확인하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/73f95268-ce99-4ce7-bbd8-3341e23ecb2b/Untitled.png)

1. 1번 게시글에 작성된 모든 댓글 조회하기 (역참조)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b32af30b-18d9-4d31-9f17-4982cd83e16b/Untitled.png)

1. 1번 게시글에 작성된 모든 댓글 출력하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b0fc8d10-1e40-47cb-964c-766f5fc7e673/Untitled.png)

### admin site 등록

- 새로 작성한 Comment 모델을 admin site에 등록하기

```python
# articles/admin.py

from django.contrib import admin
from .models import Article, Comment

# Register your models here.
# admin.site에.register해라(Model)을
admin.site.register(Article)
admin.site.register(Comment)
```

## Comment 구현

### ModelForm

- 사용자로부터 받는 데이터가 우리의 Model 필드에 맞춰서 저장된다면 모델을 기반으로 폼을 만들어준다. (필드, 조건)

- 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 작성

```python
# articles/forms.py

from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)

# forms 라이브러리에 있는 ModelForm 클래스 상속
class CommentForm(forms.ModelForm):
    # CommentForm에 대한 정보를 작성하는 곳

    class Meta:
        model = Comment
				fields = '__all__'   # 전체 필드 출력 => 오류 발생
```

- detail 페이지에서 CommentForm 출력 (View)

```python
# articles/views.py

from .forms import AricleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()       # 인스턴스 생성
    context = {
        'article': article,
        'comment_form': comment_form,  # detail 템플릿에서 출력하기위함
    }
    return render(request, 'articles/detail.html', context)
```

- detail 페이지에서 CommentForm 출력 (Template)

```html
# detail.html

{% extends 'base.html' %}

{% block content %}
	...  
  <a href="{% url 'articles:index' %}">뒤로가기</a>
	<hr>
  <form action="#" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
{% endblock content %}
```

- 결과

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a823ed77-c31b-4ef9-b664-d994ba44f8d2/Untitled.png)

- Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요하기 때문에 출력되고 있는 것
- 외래 키 필드는 사용자의 입력으로 받는 것이 아니라 view 함수 내에서 받아 별도로 처리되어 저장되어야 함

- 외래 키 필드를 출력에서 제외 후 확인

```python
# articles/forms.py

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
				~~fields = '__all__'~~ 
        exclude = ('article',)
```

- 출력에서 제외된 외래 키는 어디서 받아와야 할까?
    - detail의 url에 pk가 있음 ⇒ variable routing (url을 통해 변수를 넘김)

`127.0.0.1.8000/articles/1/`

- urls.py

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```

- views.py

```python
# articles/views.py
...

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)             # article의 pk(몇번째 글)를 사용하기 위해 조회
    comment_form = CommentForm(request.POST)         # 사용자가 적은 내용 (request.POST에 들어있다)    
    if comment_form.is_valid():                      # 유효성 검사
				# save 전에 추가적으로 넣은 값이 있으면 인스턴스를 return해줄게
        ~~comment_form.save()~~                          # 저장 취소
				comment = comment_form.save(commit=False)		 # 인스턴스는 생성하되 저장 X
				# 자! 시간 줬으니까 해야될꺼 얼렁해!
		    comment.article = article                    # 몇 번째 게시글에 작성됐는지 
				comment.save()                               # 저장
		return redirect('articles:detail', article.pk)    # 댓글이 써지고나면 댓글이 있는 페이지로
```

- detail.html

```python
# detail.html

{% extends 'base.html' %}

{% block content %}
	...  
  <a href="{% url 'articles:index' %}">뒤로가기</a>
	<hr>
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit"> 
{% endblock content %}
```

### save()

`save(commit=False)`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b101e45e-d823-4845-9d47-8934f3e80f3d/Untitled.png)

- 기본값은 True
- False는 아직 데이터베이스에 저장되지 않은 인스턴스를 생성(반환)해준다
- 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 수 있음

### 댓글 출력

```python
# articles/views.py

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()          # 인스턴스 생성
		comments = article.comment_set.all()  # 게시물에 단 댓글 역참조
    context = {
        'article': article,
        'comment_form': comment_form,  
				'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

```

```html
<!-- articles/details.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h2>{{ article.pk }}번째 글입니다.</h2>
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
  <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
  <hr>

	<h4>댓글 목록	  </h4>
	    <ul>
	      {% for comment in comments %}
	        <li>{{ comment.content }}</li>
	      {% endfor %}
	    </ul>
	
	<hr> <!-- 댓글 작성하는 폼 -->
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

### 댓글 삭제

```python
# articles/urls.py
		
		# 처음에 받을 때 게시물 번호와 댓글 번호 다 받기
		path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comments_delete'), # 댓글 번호만 필요
```

```python
# articles/views.py

from .models import Article, Comment

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)   # 삭제할 댓글 조회
    comment.delete()                               # 댓글 삭제
    return redirect('articles:detail', article_pk) # 게시물로 이동
```

```python
<!-- articles/details.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h2>{{ article.pk }}번째 글입니다.</h2>
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
  <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
  <hr>

	<h4>댓글 목록</h4>
	    <ul>
	      {% for comment in comments %}
	        <li>
          {{ comment.content }}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="delete">  
          </form>
        </li>
	      {% endfor %}
	    </ul>
	
	<hr> <!-- 댓글 작성하는 폼 -->
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

### 댓글 수정을 하지 않는 이유

→ JavaScript 영역

### Comment 추가 사항

1. 댓글 개수 출력하기
    - filter → `length`
        
        `{{ comments|length }}`
        
    - Queryset API → `count()`
        
        `{{ comments.count }}`
        

```html
<!-- articles/details.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h2>{{ article.pk }}번째 글입니다.</h2>
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
  <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
  <hr>

	<h4>댓글 목록</h4>

	{% if comments %}
	  <p>{{ comments|length }}개의 댓글이 있습니다.</p>
  {% endif %}

    <ul>
      {% for comment in comments %}
        <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="delete">  
        </form>
      </li>
      {% endfor %}
    </ul>
	
	<hr> <!-- 댓글 작성하는 폼 -->
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

1. 댓글이 없을 때 댓글 대체어 출력

```html
<!-- articles/details.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h2>{{ article.pk }}번째 글입니다.</h2>
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
  <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
  <hr>

	<h4>댓글 목록</h4>

	{% if comments %}
	  <p>{{ comments|length }}개의 댓글이 있습니다.</p>
  {% endif %}

    <ul>
      {% for comment in comments %} <!--반복가능한 것이 없을 때-->
        <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="delete">  
        </form>
      </li>
			{% empty %}
        <li>댓글이 아직 없어요</li>
      {% endfor %}
    </ul>
	
	<hr> <!-- 댓글 작성하는 폼 -->
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```

# N : 1 (Article - User)

- Article(N) - User(1)
- Article 모델과 User 모델 간 관계 설정
- 0개 이상의 게시글은 1개의 회원에 의해 작성 될 수 있음

## Django 에서 User 모델을 참조하는 방법

1. settings.AUTH_USER_MODEL
2. get_user_model()

### settings.AUTH_USER_MODEL

내장 User 모델을 accounts User 모델로 대체

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/eb8177e5-0fe7-40f1-9fad-99a005f28d9c/Untitled.png)

- 반환 값 : `accounts.User` (문자열)
- User 모델에 대한 외래 키 또는 M:N 관계를 정의 할 때 사용
- models.py의 모델 필드에서 User 모델을 참조할 때 사용

### get_user_model()

- 반환 값 : User Object (객체)
- 현재 활성화된 User 모델을 반환
- 커스터마이징한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User를 반환
- models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용

### User 모델을 참조 할 때 ⭐

- [models.py](http://models.py) 에서는 settings.AUTH_USER_MODEL
- 다른 모든 곳에서는 get_user_model()

## Article과 User간 모델 관계 설정

- Article 모델에 User 모델을 참조하는 외래 키 작성

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/94331e0a-2feb-4edd-adda-62847519c073/Untitled.png)

- 외래 키는 N쪽이 들고 있다

```python
# articles/models.py

from django.conf import settings

class Article(models.Model):
    # 외래키 작성
		# 참조하는 모델의 소문자
	#	user = models.ForeignKey(참조하는 모델)
		user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

## CREATE

- 인증된 회원의 게시글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행

- 문제점 발생 : 외래 키가 같이 출력됨
    - request 객체에서 user 정보를 받아온다

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
      # fields = '__all__'
        exclude = ('user',)  # 외래 키 숨기기
```

```python
# articles/views.py

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
						article = form.save(commit=False)
            article.user = request.user       # article 인스턴스의 user 컬럼에 요청하는 user 정보를 넣는다 (request객체에 user 정보가 들어있음)
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

## DELETE

- 게시글을 아무나 삭제하면 안됨
- 게시글 작성한 user와 현재 삭제를 요청하려는 user를 비교

```python
# articles/views.py

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:  # 인증
        # 현재 삭제를 요청하는 user가 article 작성자 user가 같다면
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail')
```

## UPDATE

```python
@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.user == article.user:

        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            # form = ArticleForm(data=request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)

    else:
        return redirect('articles:index')

    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```

- 게시글 작성자가 아니라면 수정/삭제 버튼도 출력하지 않는다

```html
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h2>{{ article.pk }}번째 글입니다.</h2>
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
    {% endif %}
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
  <hr>
  <h4>댓글 목록</h4>
  {% if comments %}
    <p>{{ comments|length }}개의 댓글이 있습니다.</p>
  {% endif %}
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.content }}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="delete">  
          </form>
        </li>
      {% empty %}
        <li>댓글이 아직 없어요</li>
      {% endfor %}
    </ul>
  <hr>
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
{% endblock content %}
```

## READ

- 각 게시글의 작성자 출력

```html
<!-- index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% endif %}
  <hr>
  {% for article in articles %}
  <p><b>작성자: {{ article.user }}</b></p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
    <hr>
  {% endfor %}
{% endblock content %}
```

```html
<!-- detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h2>{{ article.pk }}번째 글입니다.</h2>
  <hr>
  <p><b>작성자: {{ article.user }}</b></p>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
    {% endif %}
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
  <hr>
  <h4>댓글 목록</h4>
  {% if comments %}
    <p>{{ comments|length }}개의 댓글이 있습니다.</p>
  {% endif %}
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.content }}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="delete">  
          </form>
        </li>
      {% empty %}
        <li>댓글이 아직 없어요</li>
      {% endfor %}
    </ul>
  <hr>
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
{% endblock content %}
```

# N : 1 (Comment - User)

- Comment(N) - User(1)
- Comment 모델과 User 모델 간 관계 설정
- 0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음

## 모델 관계 설정

![Comment에 Article_id 외래 키 하나 더 있음](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0964c899-cc6a-4746-bf9a-a2b031ccef51/Untitled.png)

Comment에 Article_id 외래 키 하나 더 있음

```python
# articles/models.py

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delelte=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()    
		created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

- model에 변동 사항이 생겼기 때문에 migration 진행

## CREATE

- 외래 키 가리기

```python
# articles/forms.py

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'   # 전체 필드 출력
        exclude = ('article', 'user',)
```

- 댓글 작성 시 작성자 정보가 같이 저장될 수 있도록 save commit 옵션 활용

```python
# articles/views.py

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)               # article의 pk(몇번째 글)를 사용하기 위해 조회
    comment_form = CommentForm(request.POST)           # data는 request.POST에 들어있다    
    if comment_form.is_valid():                        # 유효성 검사
        comment = comment_form.save(commit=False)      # 저장하면서 나올 객체를 미리 준다(저장X)
        comment.article = article                      # 몇 번째 게시글에 작성됐는지 
        comment.user = request.user                    # (생성) 요청객체에 유저정보를 넣고
        comment.save()                                 # 저장
        return redirect('articles:detail', article.pk) # 댓글이 써지고나면 댓글이 있는 페이지로
```

## READ

```html
<!-- detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h2>{{ article.pk }}번째 글입니다.</h2>
  <hr>
  <p><b>작성자: {{ article.user }}</b></p>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
    {% endif %}
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
  <hr>
  <h4>댓글 목록</h4>
  {% if comments %}
    <p>{{ comments|length }}개의 댓글이 있습니다.</p>
  {% endif %}
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.user }} : {{ comment.content }}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="delete">  
          </form>
        </li>
      {% empty %}
        <li>댓글이 아직 없어요</li>
      {% endfor %}
    </ul>
  <hr>
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
{% endblock content %}
```

## DELETE

- 현재 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제할 수 있도록 함

```python
# articles/view.py

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)  
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
```

```html
<!-- detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h2>{{ article.pk }}번째 글입니다.</h2>
  <hr>
  <p><b>작성자: {{ article.user }}</b></p>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
    {% endif %}
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
  <hr>
  <h4>댓글 목록</h4>
  {% if comments %}
    <p>{{ commens|length }}개의 댓글이 있습니다.</p>
  {% endif %}
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.user }} : {{ comment.content }}
          
          {% if request.user == commnent.user %}
            <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
              {% csrf_token %}
              <input type="submit" value="delete">  
            </form>
          {% endif %}

        </li>
      {% empty %}
        <li>댓글이 아직 없어요</li>
      {% endfor %}
    </ul>
  <hr>
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
{% endblock content %}
```

## 인증된 사용자에 대한 접근 제한하기

`is_authenticated`  와 view decorator를 활용하여 코드 정리하기

### is_authenticated

- 인증된 사용자인 경우만 댓글 작성

```python
# articles/views.py

from django.views.decorators.http import require_http_methods, require_POST, require_safe

def comments_create(request, pk):
    if request.user.is_authenticated:                      # 인증된 사용자라면
        article = Article.objects.get(pk=pk)               # article의 pk(몇번째 글)를 사용하기 위해 조회
        comment_form = CommentForm(request.POST)           # data는 request.POST에 들어있다    
        if comment_form.is_valid():                        # 유효성 검사
            comment = comment_form.save(commit=False)      # 저장하면서 나올 객체를 미리 준다(저장X)
            comment.article = article                      # 몇 번째 게시글에 작성됐는지 
            comment.user = request.user                    # (생성) 요청객체에 유저정보를 넣고
            comment.save()                                 # 저장
            return redirect('articles:detail', article.pk) # 댓글이 써지고나면 댓글이 있는 페이지로
    return redirect('accounts:login')                      # 인증된 사용자가 아니라면 
```

- 추가

```html
<!-- detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h2>{{ article.pk }}번째 글입니다.</h2>
  <hr>
  <p><b>작성자: {{ article.user }}</b></p>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성 시각 : {{ article.created_at }}</p>
  <p>수정 시각 : {{ article.updated_at }}</p>
  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
    {% endif %}
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
  <hr>
  <h4>댓글 목록</h4>
  {% if comments %}
    <p>{{ comments|length }}개의 댓글이 있습니다.</p>
  {% endif %}
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.user }} : {{ comment.content }}
          {% if request.user == commnent.user %}
            <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
              {% csrf_token %}
              <input type="submit" value="delete">  
            </form>
          {% endif %}
        </li>
      {% empty %}
        <li>댓글이 아직 없어요</li>
      {% endfor %}
    </ul>
  <hr>

  {% if request.user.is_authenticated %}
  
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>

  {% else %}
    <a href="{% url 'accounts:login' %}">댓글을 작성하려면 로그인 하세요.</a>

  {% endif %}
  
{% endblock content %}
```

- 인증된 사용자인 경우만 댓글 작성

```python
# articles/views.py

from django.views.decorators.http import require_http_methods, require_POST, require_safe

def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk) 
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```

### View decorator

`@require_POST`

```python
# articles/views.py

from django.views.decorators.http import require_http_methods, require_POST, require_safe

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:                      # 인증된 사용자라면
        article = Article.objects.get(pk=pk)               # article의 pk(몇번째 글)를 사용하기 위해 조회
        comment_form = CommentForm(request.POST)           # data는 request.POST에 들어있다    
        if comment_form.is_valid():                        # 유효성 검사
            comment = comment_form.save(commit=False)      # 저장하면서 나올 객체를 미리 준다(저장X)
            comment.article = article                      # 몇 번째 게시글에 작성됐는지 
            comment.user = request.user                    # (생성) 요청객체에 유저정보를 넣고
            comment.save()                                 # 저장
            return redirect('articles:detail', article.pk) # 댓글이 써지고나면 댓글이 있는 페이지로
    return redirect('accounts:login')                      # 인증된 사용자가 아니라면
```

```python
# articles/views.py

from django.views.decorators.http import require_http_methods, require_POST, require_safe

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk) 
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```

# 마무리

- A many to one relationship
    - Foreign Key
    - Django Relationship fields
    - Related manager - 역참조
- N:1 모델 관계 설정
    1. Comment - Article
    2. Atricle - User
        - Referencing the User Model (유저 참조 방법)
    3. Comment - User

## [참고]

### import 문 정렬

`python -m pip install "isort >= 5.1.0"`

`isort accounts/views.py`

### 에러 메세지 출력

```python
# articles/views.py

from django.http import HttpResponse, HttpResponseForbidden

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:  # 인증
        # 현재 삭제를 요청하는 user가 article 작성자 user가 같다면
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
				return HttpResponseForbidden() 	# 인증은 됐지만 삭제할 권한이 없다
    return HttpResponse(status=401)     # 인증되지 않았을 때
		
```