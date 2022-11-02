## Django Form

사용자가 입력한 데이터가 우리가 원하는 데이터 형식이 맞는지에 대한 유효성 검증이 반드시 필요

유효성 검사를 단순화하고 자동화할 수 있다

### 처리

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성 (form, input)
3. 클라이언트로부터 받은 데이터 수신 및 처리

## The Django Form Class

### Form Class 선언

Model Class를 선언하는 것처럼 상속을 통해 선언한다

forms 라이브러리의 Form 클래스를 상속받음

### 실습

1. application 폴더 내에 [`forms.py`](http://forms.py) 라고하는 파일 생성
2. `from django import forms`
3. Form class 선언
    
    ```python
    # articles/forms.py
    
    from django import forms
    
    class ArticlsForm(forms.Form):
    # forms라는 모듈안데 Form이라는 클래스의 상속받음 
    
    		# 사용자로부터 받는 것 (input)
        title = forms.CharField(max_length=10)   # max_length가 필수는 아님
        content = forms.CharFeild                # TextFeild가 존재하지 않음
    ```
    
4. new.html 의 input부분 교체
    
    ```html
    # articles/new.html
    
    {% csrf_token %}
    <label for="title">Title : </label>
    <input type="text" name="title" id="title"></br>
    <label for="content">Content : </label>
    <textarea name="content" id="content"></textarea><br>
    ```
    
5. views.py에 new 함수 수정
    
    ```python
    # articles/views.py
    
    from .forms import ArticleForm
    
    def new(request):
    		# 인스턴스	생성	
    		form = ArticleForm()
    		context = {
    				'form': form,
    		}
    		return render(request, 'articles/new.html', context)
    ```
    
6. new.html 수정
    
    ```html
    {% csrf_token %}
    {{ form }}
    # 줄바꿈이 안된다
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/01a72a92-bbf4-4275-b436-2eef7ec3aebf/Untitled.png)
    
    ```html
    {% csrf_token %}
    {{ form.as_p }}
    # 줄바꿈이 된다
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3745680a-3358-4aa9-91c5-c4a22df1bd0c/Untitled.png)
    
7. contetnt input태그의 표현을 textarea로 바꾸기 → widgets
    
    ```python
    # articles/forms.py
    
    from django import forms
    
    class ArticlsForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharFeild(widget=forms.Textarea)             
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5debf8e8-e01b-4f48-a4e3-312c4faa1306/Untitled.png)
    

### widget

Django의 HTML input element의 표현 담당

단순히 HTML의 렌더링을 처리하는 것이며 유효성 검증과 아무런 관계가 없음

### 응용

```python
# articles/forms.py

from django import forms

class ArticlsForm(forms.Form):
		# django의 권장 style guide
		NATION_A = 'kr'
		NATION_B = 'ch'
		NATION_C = 'jp'
		NATION_CHOICES = [
				(NATION_A, '한국'),
				(NATION_B, '중국'),
				(NATION_C, '일본'),
		]

    title = forms.CharField(max_length=10)
    content = forms.CharFeild(widget=forms.Textarea)
		nation = forms.ChoicsFeild(choices=NATIONS_CHOICES)
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d2dbe993-8cff-4012-8a92-7e8ab3e66019/Untitled.png)

## Django ModelForm

### ModelForm Class

Model을 통해 Form Class를 만들 수 있는 helper class

> 회원가입 기능을 만들 때 Form을 이용한다면 클라이언트로부터 전달받은 ID나 닉네임 등을 이미 사용하고있는 계정이 있는지 없는지 따로 코드를 작성하여 체크를 해야하지만, ModelForm은 기본적으로 Model과 연동이 되어있기때문에 아래와 같이 ModelField에 unique=True 속성만 추가해준다면 장고가 알아서 중복된 ID가 있는지 없는지를 체크해준다.
> 

### 실습

1. `forms[.py](http://views.py)`
    
    ```python
    # articles/forms.py
    
    from django import forms
    from .models import Article  # model에서 만든 그대로 사용
    
    class ArticleForm(forms.ModelForm):
    		
    		class Meta:
    				# 어떤 모델을 기반으로 할지 (호출(Article())하지 않는다 just 등록)
    				model = Article
    				# 어떤 모델필드 중 어떤 것을 출력할지
    			#	fields = ('title', 'content')  # 튜플이나 리스트 형식
    				fields = '__all__'  # Article 모델에서 사용자로부터 입력받는 모든 필드
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/461749fb-8551-4943-8b85-e87c0ee04c04/Untitled.png)
    
    알아서 textarea반영됨
    

### Meta Class

- ModleForm의 정보를 작성하는 곳
- ModelForm을 사용할 경우 참조할 모델이 있어야 하는데, Meta class의 model 속성이 이를 구성함
- 참조하는 모델에 정의된 field 정보를 Form에 적용함
- Meta data : ‘데이터를 표현하기 위한 데이터’

fields 속성에 `'__all__'` 을 사용하여 모델의 입력 받아야 하는 모든 필드를 포함할 수 있음

[참고] `exclude = ('title',)` 를 이용해 제외할 수도 있음

### [참고] 참조 값과 반환 값

```python
def greeting():
		return '안녕하세요'

# 1. 함수의 참조값
print(greeting)    # <fundtion greeting at 0x10761caf0>
# 2. 함수의 반환값 
print(greeting())  # 안녕하세요
```

### 참조 값

함수를 호출하지 않고 함수 자체를 그대로 전달하여, 다른 함수에서 필요한 시점에 호출하는 경우 

```python
# urls.py

urlpatterns = [
		path('', views.index, name='index'
]

# view 함수의 참조값을 그대로 넘김으로써, path 함수가 내부적으로 해당 view함수를 필요한 시점에 사용
```

## ModelForm with View functions

## Create

```python
# articles/views.py

from .forms import ArticleForm

def create(request):
		form = ArticleForm(request.POST)  # 이미 완성된 model을 기반으로 만들어진 폼에서 받은 데이터
											# data=request.POST 
		# 검증 과정
		if form.is_valid():  # True
				article = form.save()
				return redirect('articles:index')
		return redirect('articles:new')  # False
```

### errors 속성

False일 경우 form 인스턴스의 errors 속성에 값이 작성되는데, 유효성 검증을 실패한 원인이 딕셔너리 형태로 저장됨

```python
# articles/views.py

def create(request):
		form = ArticleForm(request.POST)
		if form.is_valid():
				article = form.save()
				return redirect('articled:detail', article.pk)
		print(f'에러: {form.errors}')
		return redirect('articles:new')

# <ul class="errorlist"><li>title<ul class="errorlist"><li>필수 항목입니다.</li></ul></ul>
```

```python
		# print(f'에러: {form.errors}')
		context = {
				'form': form,                       # 실패한 form
		}
		return render(request, 'articles/new.html', context)
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f02c2882-1d31-4464-a46c-f63eb6b8c3a6/Untitled.png)

### **save()**

form 인스턴스에 바인딩(데이터가 들어가다)된 데이터를 통해 데이터베이스 객체를 만들고 저장

ModelForm의 하위 클래스는 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정함

제공되지 않은 경우 save()는 지정된 모델의 새 인스턴스를 만듦(CREATE)

```python
# CREATE
form = ArticleForm(request.POST)
form.save()
```

제공되면 save()는 해당 인스턴스를 수정(UPDATE)

```python
# UPDATE
form.ArticleForm(request.POST, instance=article)
form.save()
```

## UPDATE

```python
# views.py

def edit(request, pk):
		article = Article.objects.get(pk=pk)
		form = ArticleForm(instance=article)  # 기본 데이터를 보여준다
		context = {
				'article': article,
				'form': form,
		}
		return render(request, 'articles/edit.html', context) 
```

```python
def update(request, pk):
		article = Article.objects.get(pk=pk)
		# 데이터 만들어서 instance 만듬
		form = ArticleForm(request.POST, instance=article)  # 있으면 저장될 때 수정
		
		# 검증
		if forms.is_valid():
				# True
				form.save()
				return redirect('articles:detial', article.pk)
		# False (with error 메세지)
		context = {
				'form': form,
		}
		# 에러메세지를 출력하려면 새로운 페이지 요청을 보내면안되고 현재 페이지를 렌더링해야함 
		return render(request, 'articles/edit.html', context) 
		
```

## Widgets 활용하기

```python
# form.py

from django import forms

class ArticlsForm(forms.Form):
    # 위젯을 쓰려면 반드시 form필드 안에서 작성
    title = forms.CharField(
        label='제목',
        # renders as <input type="text">
        widget=forms.TextInput(
           attrs={
                # 속성값
                'class': 'my-title',              
                'placeholder': 'Enter the title',
                'maxlength': 10,
            } 
        )  
    )

    content = forms.CharField(
        label='내용'
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',              
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
        error_messages={
            'required': 'Please enter your content'
        }
    )

```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a296ff09-3f65-456d-b211-b46a75196b6d/Untitled.png)

## Handling HTTP requests

- 생성 : new + create
- 수정 : edit + update
- new, edit → GET 요청에 대한 처리 (페이지 렌더링)
- create, update → POST 요청에 대한 처리 (DB 조작)

### CREATE

```python
# view.py
from .forms import ArticleForm

def create(request):

		if request.method == 'POST'
				# create
				form = ArticleForm(request.POST)
		    if form.is_valid():
						# 통과하면
		        article = form.save()
		        return redirect('articles:detail', article.pk)

		else:
				# new 
				form = ArticleForm()  # 빈 폼
		
		# 통과하지 못하면 에러 메세지를 보여준다
		context = {
		    'form': form,  # 에러 메세지 포함 or 빈 인스턴스 폼
		}
		return render(request, 'articles/new.html', context)
```

url의 path 삭제 and new → create 로 바꾼다

```python
# urls.py

~~path('new/', views.new, name='new'),~~
```

### UPDATE

```python
def update(request):
		article = Article.objects.get(pk=pk)  # 공통 부분
		
		if request.method == 'POST'
				# update (DB 수정)
		    form = ArticleForm(request.POST, instance=article)
		    # form = ArticleForm(data=request.POST, instance=article)
		    
				if form.is_valid():
		        form.save()
		        return redirect('articles:detail', article.pk)
		
		# POST가 아니라면
		else:
				# edit (수정 페이지)
		    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

url의 path 삭제 and edit → update 로 바꾼다

```python
# urls.py

~~path('<int:pk>/edit/', views.edit, name='edit'),~~
```

### DELETE

```python
def delete(request, pk):
		# POST일 때만 삭제
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')
```

## view methods

### require_safe()

```python
from django.views.decorators.http import reqire_safe

@require_safe
def index(request):
		
# GET인 요청에 대해서만 view함수 실행
# 아니라면 405 Method Not Allowed
```

### require_http_methods()

```python
from django.views.decorators.http import require.http.methods

@require_http_methods(['GET', 'POST'])
def create(request):
```

### require_POST()

- GET으로 받은 거는 안됨

```python
from django.views.decorators.http import require_http_methods, require_POST

@require_POST
def delete(request, pk):
		~~if request.method == 'POST':~~
		article = Article.objects.get(pk=pk)
		article.delete()

		return redirect('articles:index')
```

## 마무리

### Django Form Class

- django 프로젝트의 주요 유효성 검사 도구
- 공격 및 데이터 손상에 대한 중요한 방어 수단
- 유효성 검사에 대해 개발자에게 강력한 편의를 제공
- ex) 로그인

### ModelForm

- DB로 저장된 데이터를 받을 때
- ex) 게시글 작성, 회원 가입

### View 함수 구조 변화

- new + create, edit + update 함수
- HTTP requests 처리에 따른 구조 변화