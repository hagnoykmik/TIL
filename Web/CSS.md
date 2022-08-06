# CSS
Cascading Style Sheets
계단식(상속)

## CSS란?
태그를 선택하고 스타일을 지정하기 위한 언어


![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/28e2003b-9ced-4e1b-8d94-d65d9ab0d5be/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220805T144047Z&X-Amz-Expires=86400&X-Amz-Signature=dd5475766d58b2045a25507b5ffdd89e6882edb3aaa2c7fac7a42ee88bc43289&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 선택자(selector) : 스타일을 지정할 HTML 요소 선택
- 중괄호 안
  - 속성(property) : 값(value)
  - 어떤 스타일 기능을 변경할지 : 어떻게 스타일 기능을 변경할지

## CSS 정의 방법
- 인라인
- 내부 참조
- 외부 참조

### 인라인 (inline)
- 태그에 직접 style 속성을 활용
```html
<body>
  <h1 style="color: blue; font-size: 100px;">Hello</h1>
</body>
```
- 단점 : 실수가 잦아짐(중복, 찾기가 어려움)

### 내부 참조(embedding)
- <head> 태그 내에 지정
```html
<head>
  <style>
    h1 {
      color: blue;
      font-size: 100px;
    }
  </style>
</head>
```
- 단점 : 코드가 너무 길어질 수 있음

### 외부 참조(link file)
- 외부의 CSS 파일을 <link>를 통해 불러오기
```CSS
h1 {
    color: blue;
    font-size: 100px;
}
```
```html
<head>
  <link rel-"stylesheet" href="mystyle.css">
</head>
```

## CSS 선택자(selector)
- 기본 선택자
- 결합자(combinators)

### 기본 선택자
- <기본>
  - 전체 선택자(*)
  - 요소 선택자(html 태그)
```html
  <style>
  /*전체 선택자*/
  * {
    color: red;
  }
  /*요소 선택자*/
  h1 {
    color: orange;
  }
  </style>
 ```
- <내가 원하는 거>
  - 클래스 선택자(.)
  - 아이디 선택자(#)
```html
  <style>
  /*class 선택자*/
  .green {
    color: green;
  }
  /*id 선택자*/
  #purple {
    color: purple;
  }
  </style>
```

### 결합자(combinators)
- 자손 결합자( )
- 자식 결합자(>)
```html
<style>
  /*자손 결합자*/
  .box p {
    color: blue;
  }
  /*자식 결합자*/
  .box p {
    color: yellow;
  }
</style>
```
- 일반 형제 결합자(~)
- 인접 형제 결합자(+)
```html
<style>
  /*일반 형제 결합자*/
  p ~ span {
    color: red;
  }
  /*인접 형제 결합자*/
  p + span {
    color: red;
  }
```

### *Selectors 심화
- 자손 결합자( )
  - selectiorA의 하위 모든 요소
```html
<style>
  div span {
    color: red;
  }
</style>
```
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b5d48154-11ec-4bad-9e31-0aa2eae2a67f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220806T084107Z&X-Amz-Expires=86400&X-Amz-Signature=b5f097b1d2618b4c110fc18e0401b2cef9cee4baca2282b743e621e92f8290bf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 자식 결합자(>)
  - selectorA 바로 뒤 위치하는(아래) 하위요소
```html
<style>
  div > span {
    color: red;
  }
</style>
```
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0279fe26-f1c1-4e39-872d-632275dee638/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220806T084251Z&X-Amz-Expires=86400&X-Amz-Signature=33fd5fe40d2ec67f64e18f8b4ee14122c83495a3763a6bd6739559c4cc16de3e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
- 일반 형제 결합자(~)
  - selectorA의 형제 요소 중 뒤에 위치하는 모든 요소
```html
<style>
  p ~ span {
    color: red;
  }
</style>  
```
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/624dbb90-7976-4ed4-8cf6-eed0742572de/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220806T084614Z&X-Amz-Expires=86400&X-Amz-Signature=455eaa965662ab524cce809b254be033a99e86dd7e3efe398add68ce632a9dc6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
- 인접 형제 결합자(+)
  - selectorA의 형제 요소 준 바로 뒤에 위치하는(아래) 요소
```html
<style>
  p + span {
    color: red;
  }
</style>
```
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/34e2ca0d-6f2e-445e-a217-51ab3039dbe0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220806T085103Z&X-Amz-Expires=86400&X-Amz-Signature=e71998ea1d9b1b2e33d062c1e6b795323a1e2d23306957baf72346627d2b6be8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### 선택자의 우선순위
범위가 좁을수록 강하다!

1. 중요도
  - !important
2. 우선순위
  - 인라인 > id > class > <div> 태그 이름 > 상속
  - 주의 : 상속은 항상 마지막 순위!
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/19e76baa-bb93-44ea-a0b2-2b3bff3c92a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220806T093217Z&X-Amz-Expires=86400&X-Amz-Signature=617eab8ab52b0cecad3a1f002b9eb1ed53c21ac3eef69534a1fc246f90a2019a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### CSS 상속
- 상속 되는 것
  - text관련 요소(color, font, text-align)
  - opacity
  - visibility
- 상속 안되는 것
  - box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
  - position 관련 요소(position, top/right/bottom/left, z-index)

## CSS 기본 스타일
### 크기 단위
- px
  - 고정적인 단위
- %
  - 가변적인 단위
- em
  - 부모요소에 대한 (바로 위) 상속의 영향을 받음
  - 지정된 사이즈에 상대적인 사이즈
- rem
  - root em
  - 부모 요소에 대한 상속의 영향을 받지않음
  - 최상위 요소(html)의 사이즈(기본 글자)를 기준으로 배수 단위를 가짐
  - html tag의 font-size를 base로 함
- viewport
  - 디바이스 화면에 따라 상대적인 사이즈가 결정됨

### CSS 문서 표현
- 텍스트
  - 서체(font-family)
  - 서체 스타일(font-style, font-weight)
  - 자간(letter-spacing)
  - 단어 간격(word-spacing)
  - 행간(line-height)
- color, background-image, background-color
- 기타
  - 목록(li)
  - 표(table)

### CSS Box model
CSS 원칙 1
- CSS의 모든것은 "Box"다.
- 위에서 아래로, 왼쪽에서 오른쪽으로

- box model 구성
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7319285c-1b7c-4cf1-8a3d-fc2ef141c0a8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220806T105107Z&X-Amz-Expires=86400&X-Amz-Signature=82993463e3d0201708ebee32c79b7bafe3ca5020e29483a823b816a7bae412a5&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 사이즈를 정할 때 content box와 border box 주의!

## CSS Display
CSS 원칙 2
- display에 따라 크기와 배치가 달라진다.

- 종류
  - block
  - inline
  - inline-block
  - none

### block
div, li(ol,ul), p, hr, form
- 한 줄을 다 차지(나머지 부분은 margin으로)
- 위에서 아래로
- 줄 바꿈이 일어나는 요소
- 블록 레벨 요소안에 인라인 레벨 요소가 들어갈 수 있음


### inline
span, a ,img, input, label, b, em, i, strong
- content 너비 만큼 가로폭 차지
- 왼쪽에서 오른쪽으로(글자처럼 취급)
- 상하 여백은 line-height로 지정
- width, height, margin-top, margin-bottom 지정할 수 없음

### inline-block
- 원래는 block인데 inline처럼 보인다
- block이므로 width, height, margin-top, margin-bottom속성을 모두 지정할 수 있음

### None
- 화면에 표시하지 않고 공간도 부여하지 않음
- None vs Hidden
  - 숨겼다가 나중에 보여줄 일이 없다/있다
  - 공간이 부여되지 않음/ 됨

## CSS position
- 레이아웃을 결정할 떄
- 문서상에서 요소의 위치를 지정

- 종류
  - static
  - relative
  - absolute
  - fixed
  - sticky
  
### static
- 모든 태그의 기본 값(기준 위치)
- 일반적인 요소의 배치순서에 따름(좌측 상단)

### relative
- 자기자신의 **static 위치**를 기준으로 이동
- 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음

### absolute(공중부양)
- 가장 가까이 있는 **static이 아닌** 부모요소를 기준으로 이동(없으면 브라우저 기준)
- 공간을 차지하지 않음

### fixed
- 부모요소와 상관없이 viewport 기준으로 이동
- 스크롤 시에도 항상 같은 곳 위치

### sticky
- 평소에는 static과 같이 일반적인 흐름에 따르지만
- 스크롤 위치가 임계점에 이르면 fixed로 고정

## CSS Layout
- float
- flex
- grid

### float

#### float이 나온 배경
- normal flow로는 우리가 원하는 레이아웃을 만들지 못한다
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ac53f2a7-298c-49bb-9bdb-15ab396233ed/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220806T113231Z&X-Amz-Expires=86400&X-Amz-Signature=d925b6d6e94b5164a8ec40dac0c25db5df8e08b1c9f107668ab26706595ef9c2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
- 어떤 요소를 감싸는 형태로 배치는?
- 좌/우측에 배치는?

#### float
- 박스를 왼쪽/오른쪽으로 이동시켜 텍스트를 포함한 인라인 요소들이 주변을 wrapping하도록 함
- 요소가 Normal flow를 벗어나도록 함
  
#### float 속성
- `float: none`  기본값
- `float: left` 요소를 왼쪽으로 띄움
- `float: right` 요소를 오른쪽으로 띄움
- `float: clear` 해제 
  
### flexbox

#### flexbox가 나온 배경
- absolute, float에는 한계가 있음
- 수직, 수평축을 이용해서 정렬하고 싶음

#### flexbox
- 행과 열의 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 수동 값 부여없이 수직 정렬
- 아이템의 너비와 높이 혹은 간격을 동일하게 배치
  
#### flexbox를 어디에 적용할까?
- 부모 컨테이너
  - `display: flex`
  - `flex direction: `
  - `flex wrap: `
  - `flex flow: `
  - `justify-content- `
  - `align-items- ` and `align-content- `
- 자식 아이템
  - `style="flex grow "`
  - `style="align-self: "`
  - `style="order: "`

#### flex 속성
- flex direction
  - main axis 방향을 설정
    - row
    - row-reverse
    - column
    - column-reverse
- flex wrap
  - wrap
  - nowrap(기본값)
- flex-flow
  - flex direction-flex wrap
- justify-content(main axis)
  - flex-start
  - flex-end
  - center
  - space-between
  - space-around
  - space-evenly
- align-content(cross axis가 여러개)
  - flex-start
  - flex-end
  - center
  - space-between
  - space-around
  - space-evenly
- align-items(crow axis가 한 개)
  - stretch
  - flex-start
  - flex-end
  - center
  - baseline
- align-self(cross axis 개별 아이템 한 개)
  - stretch
  - flex-start
  - flex-end
  - center
- 기타 속성
  - flex-grow 남은 영역을 아이템에 분배
  - order 배치 순서
  ```html
  <div class="flex_item grow-1 order-3>
  
  ```