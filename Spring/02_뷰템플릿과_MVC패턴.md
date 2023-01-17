## View Templates

- 화면을 담당

## Controller - logic

- 처리 과정

## Model - data

- 데이터 관리

### view templates의 위치

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8ef79b55-b029-43c0-9d24-6ea5a28513f7/Untitled.png)

- 사전 작업 = mustache 설치
- `resources/templates/greetings.mustache`파일 생성

### Controller 만들기

- ``````````````java/기본패키지/controller 패키지 생성`
- [ㄴFirstController.java](http://ㄴController.java) 파일 생성
    
    ```java
    package com.example.firstproject.controller;
    
    @Controller // 컨트롤러 선언
    public class FirstController {
    	
    		@GetMapping("/hi")
    		public String niceToMeetYou() {
    				return "greeting";  // templates/greetings.mustache -> 브라우저로 전송!
    		}
    }
    ```
    
- greetings.mustache

```html
...
<h1>{{ username }}님, 반갑습니다.</h1>
...
```

### Model 사용하기

```java
package com.example.firstproject.controller;

@Controller // 컨트롤러 선언
public class FirstController {
	
		@GetMapping("/hi")
		public String niceToMeetYou(Model model) {
				// 모델이라는 객체를 통해서 addAttribute라는 메서드를 실행시키는데
				// username이라는 변수를 등록시키고, 홍팍이라는 값을 등록
				model.addAttribute(attirbuteName: "username", attributeValue: "홍팍")   
				return "greeting";    // templates/greetings.mustache -> 브라우저로 전송!
		}
}
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c2bc706c-3fc9-420d-8255-05a474a93df4/Untitled.png)

```java
package com.example.firstproject.controller;

@Controller // 컨트롤러 선언
public class FirstController {
	
		@GetMapping("/hi")
		public String niceToMeetYou(Model model) {
				model.addAttribute(attirbuteName: "username", attributeValue: "홍팍")   
				return "greeting";
		}

		@GetMapping("/bye")
		public String seeYouNext(Model model) {
				model.addAttribute(attirbuteName: "nickname", attributeValue: "홍길동")
				return "goodbye";     // 보여줄 뷰 템플릿 페이지
		}
}
```