# Bootstrap

- 추상화
- [bootstrap으로 이동하기]([https://getbootstrap.com/](https://getbootstrap.com/))

## 사용방법

```html
<title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" r
el="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBv
ApHHNl/vI1Bx" crossorigin="anonymous">

<body>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.
js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa"
 crossorigin="anonymous"></script>
</body>
```

## 기본원리

### Spacing (margin and padding)

`{property}{side}-{size}`

- {property}
    - m- margin
    - p - padding
- {sides}
    - t - top
    - b - bottom
    - s - start(left)
    - e - end(right)
    - x - both(left, right)
    - y - both(top, bottom)
    - blank - all 4 sides
- {size}
    - 0 - 0
    - 1 - * .25(rem)
    - 2 - * .5
    - 3 - * 1
    - 4 - * 1.5
    - 5 - * 3
    - auto - auto
        - 1rem == 16px

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5bc7df82-61db-471b-b72e-e4a31c2aeb86/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220804T103309Z&X-Amz-Expires=86400&X-Amz-Signature=d7070dd13438098d3461bd10bfd5f8c19742680c73ef8c80586996c35a956c72&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

```html
<body>
  <h2>Spacing</h2>
	<!--div.mt-3.ms-5.box-->
	<div class="mt-3 ms-5 box">margin-top3</div>
	<div class="m-4 box">margin 4</div>
	<div class="mx-auto box">가운데정렬</div> <!--정중앙 정렬-->
	<div class="ms-auto box">오른쪽정렬</div> <!--오른쪽 정렬-->
</body>
```

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/44083d05-8594-4974-9347-3d248e78f2f1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220804T103330Z&X-Amz-Expires=86400&X-Amz-Signature=5695fec614a6938e4d49da24a1b84d5e37481a2a0939d7ff253d509d5e8a7c12&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### Color

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e0944b53-7705-42ed-8067-14a854949f24/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220804T103349Z&X-Amz-Expires=86400&X-Amz-Signature=b792bf4662b9a60eff2ac6a5fb71bb08a40cf9a3dc554e3e83f7081f987ed03b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

```html
<body>
  <h2>Color</h2>
  <!--div.bg-primary--> 
	<div class="bg-primary">이건 파랑</div>
	<div class="bg-secondary">이건 회색</div>
	<div class="bg-danger">이건 빨강</div>
  <!--p.text-success-->
	<p class="text-success">이건 초록색 글씨</p>
</body>
```

### Text

```html
<body>
	<h2>Text</h2>
   <!--p.text-start-->
	<p class="text-start">text-start</p> 
	<p class="text-center">text-center</p>
	<p class="text-end">text-end</p>
</body>
```

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/742accb9-986b-4df1-9467-51ed1562a800/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220804T103549Z&X-Amz-Expires=86400&X-Amz-Signature=dc3d4573ee1c5edb97fdf4050b4ad57694fd8431816dd50212fc26c7a05ce89c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

```html
<body>
	<h2>Text</h2>
   <!--a.text-decoration-none.text-dark-->
	<a href="#" class="text-decoration-none text-dark">none-underline-link</a>
		        (빈칸)       
	<p class="fw-bold">bold text</p>
	<p class="fw-normal">normal text</p>
	<p class="fst-italic">italic text</p>
</body>
```

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/65912892-5e25-4d5a-9aee-e54e35cd7dab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220804T103606Z&X-Amz-Expires=86400&X-Amz-Signature=a4b1f7b943808af0461380404c5ca9045347b8a3608478d438b6cbcd32ce825b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### Position

```html
<body>
  <h2>position</h2>
  <!--div.box.fixed-top-->
	<div class="box fixed-top">fixed top</div>
	<div class="box fixed-bottom">fixed bottom</div>
</body>
```

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/65dd3a01-520c-4e26-93b0-863529b19782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220804T103411Z&X-Amz-Expires=86400&X-Amz-Signature=9cd349df32b72caf97f2ac5eaa37cdbc80a8484f4789a790bea6d3f634dcd8b9&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

```html
<body>
	<h2>position</h2>
	<div class="bigbox position-relative">
	  <div class="box position-absolute top-0 start-0">top-0/start-0</div>
	  <div class="box position-absolute top-0 end-0">top-0/end-0</div>
	  <div class="box position-absolute bottom-0 start-0">bottom-0/start-0</div>
	  <div class="box position-absolute bottom-0 end-0">bottom-0/end-0</div>
	</div>
</body>
```

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9171e14a-c6aa-4285-9d42-25d126e403ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220804T103639Z&X-Amz-Expires=86400&X-Amz-Signature=54f504dae1aa4072551acb7c7d8e741eb8615cac3002ec2e915b008458314e89&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### Display

```html
<body>
	<h2>Display</h2>
	<div class="d-inline p-2 text-bg-primary">d-inline</div>
	<div class="d-inline p-2 text-bg-dark">d-inline</div>
	<div class="d-none p-2 text-bg-dark">d-inline</div>
</body>
```

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2bff16ca-14d2-4c21-ace3-2a75d516d9c9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220804T103658Z&X-Amz-Expires=86400&X-Amz-Signature=90f443adb919b89f751cfb114849ffd72edad824c7fac0f968925170a3c3aec7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### 기타

- button
- dropbox
- navbar
- form
- carousel
- modal
    - ! 중첩되서 들어가면 안됨
- flex-box
    - `d-flex`
- card
    - grid-card(반응형)
        
        

### Grid system(web design)

- breakpoint
    - `col-{breakpoint}`

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9d17fc11-90e6-46e7-b59a-62c3dad5bb8a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220804T103715Z&X-Amz-Expires=86400&X-Amz-Signature=2c12d05d83e11adae2d7dfda43efa2fe834f0e883d6d1b92675514fa14a7e515&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 기본 요소
    - column :실제 컨텐츠를 포함하는 부분
    - gutter : 칼럼과 칼럼 사이의 공간(사이 간격)
    - container : column들을 담고 있는 공간

- 반드시 기억해야 할 2가지!
    1. 12개의 column
    2. 6개의 grid breakpoints

### Grid breakpoint

- 크기에 따라서 비율이 변경되도록 설정

```html
<h2 class="text-center">Grid breakpoints</h2>
    <div class="row">
      <div class="box col-2 col-sm-8 col-md-4 col-lg-5">1</div>
      <div class="box col-8 col-sm-2 col-md-4 col-lg-2">2</div>
      <div class="box col-2 col-sm-2 col-md-4 col-lg-5">3</div>
    </div>
```

### Nesting

- ?

```html
<h2 class="text-center">nesting</h2>
    <div class="row">
      <div class="box col-6">
        <div class="row">
          <div class="box col-3">1</div>
          <div class="box col-3">2</div>
          <div class="box col-3">3</div>
          <div class="box col-3">4</div>
        </div>
      </div>
      <div class="box col-6">1</div>
      <div class="box col-6">2</div>
      <div class="box col-6">3</div>
    </div>
```

### Offset

- 비우고 싶을 때 사용