# HTML
Hyper Text Markup Language

### Hyper Text?
- 하이퍼링크(참조)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- 링크를 통해 문서를 이동한다

### Markup Language?
- 글에 역할을 부여하는 것
- 태그를 이용하여 문서나 데이터에 의미를 명시하는 단어
  - HTML, Markdown

### HTML?
- 웹페이지를 작성(구조화) 하기 위한 언어

## HTML 기본구조
- html : 문서의 최상위 요소
- head : 문서 메타데이터 요소
- body : 문서 본문 요소(실제 데이터, 내용)

### head
```html
<head> 
  <title>HTML 수업</title> <!--브라우저 상단 타이틀--> 
  <meta charset="UTF-8"> <!-- 문서 레벨 메타데이터 요소 -->
  <link href="style.css" rel="stylesheet"> <!-- /*외부 리소스 연결요소(CSS파일, favicon)*/ -->
  <script src="javascript.js"></script> <!-- 스크립트 요소(javascript 파일/코드) -->
  <style> /*CSS직접작성*/
    p {
      color: black;
    }
  </style>
</head>   
```

### 요소(element)
- 태그와 내용으로 구성되어 있다.
```html
<h1>contents</h1>
```
- <시작태그>내용<종료태그>
  - 요소는 태그로 내용을 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 내용이 없는 태그도 존재(닫는 태그가 없음)
    - br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화

### 속성(attribute)
```html
<a href="https://google.com"></a>
   속성명    속성값
```
- 태그의 부가적인 정보를 설정할 수 있음
- 경로나 크기와 같은 추가적인 정보 제공
- HTML Global Attribute
  ```html
  id 문서 전체에서 유일한 고유식별자 지정
  class 공백으로 구분된 해당 요소의 클래스 목록(CSS, JS에서 선택/접근)
  style 인라인 스타일
  title 요소에 대한 추가 정보 지정
  tabindex 요소의 탭순서
  data-* 페이지에 개인 사용자 정의 데이터를 지정하기 위해 사용
  ```

### 시맨틱 태그
- HTML태그가 특정 목적, 역할 및 의미적 가치(semantic value)를 가지는 것
- 접근성
  - h1 : 페이지의 최상위 제목
  ```html
  <header>문서 전체나 섹션의 헤더(머리말)</header>
  <nav>네비게이션</nav>
    <section> 문서의 일반적인 구분, 콘텐츠의 그룹
      <article> 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역</article>
    </section>
    <aside> 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠</aside>
  <footer> 문서 전체나 섹션의 푸터(마지막)  
  ```
  ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e9792568-e554-42b9-8ecc-c873ca346be9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220802T130616Z&X-Amz-Expires=86400&X-Amz-Signature=0b759ab0dc85239a52f1703cf1134cc7b3673f87859c50691369cf1e56e793a9&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

  - 사용해야 하는 이유
    - 개발자 및 사용자 뿐아니라 검색엔진 등에 의미있는 정보의 그룹을 태그로 표현
    - 단순히 구역을 나누는 것뿐아니라 '의미'를 가지는 태그들을 활용
    - 요소의 의미가 명확하기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
    - 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야함

### 렌더링
웹사이트 코드를 사용자가 보게되는 웹사이트로 바꾸는 과정
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ee72f98e-016f-4ddf-91d4-d7b445642b8e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220802T131220Z&X-Amz-Expires=86400&X-Amz-Signature=d0d5cf560acc052338acc37271f8cef269f444dd07947ba4c32ac1147487680a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### DON(Document Object Model) Tree
- 텍스트 파일인 HTML문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML은 글이고 실현은 브라우저가 한다
  - 자식과 부모 구조로 트리 형태로 이루어져 있다
- HTML 문서에 대한 모델을 구성함
- HTML 문서 내의 각 요소에 접근/수정에 필요한 property와 method를 제공
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cc1ff5f5-4286-4d2a-a319-f81f49058dbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220802T131438Z&X-Amz-Expires=86400&X-Amz-Signature=42e120872dfcd5f96324cfb024fdfa3e79cb6b5654d308dd46661286be51177d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

---

## HTML 문서 구조화
### 인라인/ 블록 요소
- 인라인 요소(텍스트 요소) : 글자처럼 취급
- 블록 요소(그룹 컨텐츠) :한 줄 모두 사용

### 텍스트 요소
```html
 <a></a>  href속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
 <b></b>, <strong></strong>  굵은 글씨 요소
 <i></i>, <em></em>  기울임 글씨 요소
 <br>  텍스트 내에 줄 바꿈 생성 
 <img>  src 속성을 활용하여 이미지 표현 
 <span></span>  의미 없는 인라인 컨테이너 
 ```

### 그룹 콘텐츠
```html
<p></p> 하나의 문단(paragraph)
<hr> 문단 레벨요소에서의 주제의 분리를 의미하며 수평선으로 표현
<ol></ol> 순서가 있는 리스트
<ul></ul> 순서가 없는 리스트
<pre></pre> HTML에 작성한 내용이 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백 문자를 유지
<blockquote></blockquote> 텍스트가 긴 인용문, 주로 들여쓰기를 한것으로 표현됨
<div></div> 의미 없는 블록 레벨 컨테이너
```

### form
- <form>은 사용자로부터 정보(데이터)를 입력받기 위해 쓰는 태그
- 사용자가 브라우저를 통해 서버(컴퓨터)에 데이터를 제출하기 위해 사용하는 태그
  - 로그인, 게시판

-  기본 속성
```html
<form action="메뉴" method="GET"> 
<!--action : 데이터를 보낼 서버의 URL-->
<!--method : 제출할 때 사용할 HTTP메서드(GRT, POST)-->
</form>
```

### input
- form 태그 안에서 실행
- 기본 속성
```html
type : form control에 적용되는 이름 (key)
value : form control에 적용되는 값 (value)
required, readonly, autofocus, autocomplete, disabled 등
```

### input label
- input 태그에 대한 설명
- 태그에 스페셜한 별명 붙임
- '아이디 : '의 아이디
- 시각적뿐아니라 화면 리더기에서도 쉽게 내용 확인할 수 있음
```html
<label for="agreement">개인정보 수집에 동의합니다.</label>
<input type="checkbox" name="agreement" id="agreement">

#<input>에는 id 속성을. <label>에는 for속성을 활용하여 상호 연관을 시킴
```

### input 유형
- 일반
```html
text 일반 텍스트 입력
password 입력 시 값이 보이지않고 문자를 특수기호(*)로 표현
email 이메일 형식이 아닌경우 제출불가
number min, max, step 속성을 이용하여 범위 설정 가능
file accept 속성을 활용하여 파일 타입 지정 가능
```

- 항목 중 선택
  - 일반적으로 label 태그와 함께 사용하여 선택 항목 작성
  - 동일 항목에 대해서는 name을 지정하고 선택된 항목에 대한 value를 지정해야함
    - checkbox : 다중 선택
    - radio : 단일 선택
  
```html
<p>checkbox</p>
<input id="html" type="checkbox" name="language" value="html">
<label for="html">HTML</label>
```

- 기타
```html
color 
date
hidden 사용자에게 보이지 않는 input
```



