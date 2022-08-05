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
  - 요소 선택자(html 태그)
  - 클래스 선택자(.)
  - 아이디 선택자(#)
- 