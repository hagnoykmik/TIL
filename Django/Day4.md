# Django Form
사용자가 입력한 데이터가 우리가 원하는 데이터 형식이 맞는지에 대해 유효성 검증이 반드시 필요함
-> 유효성 검사를 **단순화**하고 **자동화**할 수 있다

### 처리
1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

# Django Form Class
## Form Class 선언
Model Class를 선언하는 것처럼 상속을 통해 선언한다 (forms 라이브러리의 Form 클래스를 상속)

## 실습
1. application 폴더 내 `forms.py` 파일 생성
2. Form class 선언
    ```python
    # articles/forms.py
    # 장고의 forms 모듈 사용
    from django import forms
    # forms의 Form 클래스 상속
    class ArticleForm(forms.Form):
        # 사용자로부터 받는 데이터(input)
        title = forms.CharField(max_length=10)
        content = forms.CharFeild
    ```
3. views.py의 new 함수 수정
    ```python
    # articles/views.py
    from .forms import ArticleForm

    def new(request):
        # 인스턴스 생성
        form = ArticleForm()  # 호출
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', comtext)
    ```
4. new.html 변경
    ```html
    # articles/new.html

    {% csrf_token %}
    <!-- <label for="title">Title : </label>
    <input type="text name="title" id="title"></br>
    <label for="content">Content : </label>
    <textarea name="content" id="content"></textarea><br> -->
    {{ form }}  <!-- 줄 바꿈이 안됨 -->
    ```
    ![](https://user-images.githubusercontent.com/109258144/188677939-e3f10b71-5389-45f3-ab10-5198aa270037.png)
    ```html
    {{ form.as_p }}  
    ```
    ![](https://user-images.githubusercontent.com/109258144/188678752-863a8a76-8d33-46ae-91cc-325d0f6ba7a0.png)
5. content의 input태그 표현을 textarea로 바꾸기 -> widget
    ```python
    # articles/forms.py
    from django import forms

    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharField(widget=forms.Textarea)
    ```
    ![](https://user-images.githubusercontent.com/109258144/188679412-168e4abe-90e6-432f-8965-fcbd71703e1b.png)

### widget
- Django의 HTML input element의 표현 담당
- 단순히 HTML의 렌더링을 처리하는 것이며 유효성 검증과 아무런 관계가 없음

# Django ModelForm
## ModelForm Class
Model을 통해 Form Class를 만들 수 있는 helper class

### 실습
1. forms.py
```python
# articles/forms.py
from django import forms
from .models import Article  # model에서 만든 그대로 사용하겠다

class ArticleForm(forms.ModelForm):
    
    class Meta:  # 데이터의 데이터
        model = Article    # Article 참조
        fields = '__all__' # Article 모델에서 사용자로부터 입력받는 모든 필드
        
      # fields = ('title', 'content') 처럼 튜플이나 리스트 형식으로도 가능
      # exclude = ('제외할 필드',) 를 이용해 제외할 수도 있음
```
![](https://user-images.githubusercontent.com/109258144/188787059-768e4c55-1ef8-4305-a6be-429180caf945.png)
model을 상속받기 때문에 알아서 textarea가 반영됨

### Meta Class
- ModelForm의 정보를 작성하는 곳
- ModelForm을 사용할 경우 참조할 모델이 있어야하는데, Meta class의 model 속성이 이를 구성함
- 참조하는 모델에 정의된 field를 Form에 적용함

### 참조 값과 반환 값
```python
def greeting():
    return '안녕하세요'

# 1. 함수의 참조값
print(greeting)    # <function greeting at 0x10761caf0>
# 2. 함수의 반환값
print(greetinf())  # 안녕하세요
```

### 참조 값
함수를 호출하지 않고 함수 자체를 그대로 전달하여, 다른 함수에서 필요한 시점에 호출하는 경우
- views.index
```python
# urls.py
urlpattern = [
    path('', views.index, name='index')
]
# view 함수의 참조값을 그대로 넘김으로써, path 함수가 내부적으로 해당 view 함수를 필요한 시점에 사용
```

# ModelForm with View functions
## Create
```python
# articles/views.py
from .forms import ArticleForm

def create(request):
  # form = ArticleForm(사용자로부터 입력받는 데이터)
    form = ArticleForm(request.POST)

    # 유효성 검사 도구(form)
    # form 인스턴스를 저장하기 전에 검증 진행
    if form.is_valid():
        # True 
      # form.save()  # 새 글을 작성했으니까 반환값을 주지 않을까?
        article = form.save()  # 생성된 객체가 리턴됨
        return redirect('articles:detail', article.pk)
    # False 면 현재 작성페이지로
    return redirect('articles:new')
    

```
### errors 속성
False일 경우 form 인스턴스의 errors 속성에 값이 작성되는데, 유효성 검증을 실패한 원인이 딕셔너리 형태로 저장됨
```python
# articles/views.py
def create(request):
    form = ArticleForm(request.POST)

    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    # False
    print(f'에러: {form.errors}')  # False가 되면 속성 값이 채워짐
    return redirect('articles:new')
```

## Update
```python

```

## Delete