# OOP

### 객체 지향 프로그래밍(사전적 정의)

> 객체 지향 프로그래밍은 (Object Oriented Programming, OOP)은 **컴퓨터 프로그래밍의 패러다임** 중 하나이다. 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 **여러 개의 독립된 단위, 즉 “객체”들의 모임**으로 파악하고자 하는 것이다. **각각의 객체는 메세지를 주고받고, 데이터를 처리**할 수 있다.
> 

 

### 객체 지향 프로그래밍이란?

- 프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
- 패러다임 = 방법론( 예시 : 라면 - 스프 패러다임, 면 패러다임)
- 콘서트
    - 가수 객체
    - 감독 객체
    - 관객 객체
- 객체는 **정보**와 **행동**을 묶어 놓은 것. = 변수 + 함수

### **절차 지향 프로그래밍(과거)**

- 변경하려면 연결된 모든 것을 변경해야한다.-

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a53d480d-e152-45e0-b5c3-938f85a474e4/Untitled.png)

### **객체 지향 프로그래밍(현재)**

= 객체라는 바구니 안에 특정 기준에 맞춰서 필요한 데이터를 놓고 함수를 묶는다

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/05a224d0-9311-4475-9d4c-7bc18a8c598a/Untitled.png)

### 객체 지향 프로그램이 필요한 이유

- 현실 세계를 프로그램 설계에 반영(추상화)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a9549005-2645-415b-a1fa-c49addb4d294/Untitled.png)

### 객체 지향의 장/단점

- 장점
    - 클래스 단위로 모듈화 시켜(영역을 명확하게 나눌 수 있음) 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
    - 필요한 부분만 수정하기 쉽기 때문에 프로그램이 유지 보수가 쉬움
- 단점
    - 설계 시 많은 노력과 시간이 필요함
        - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
    - 실행 속도가 상대적으로 느림(사람이 편하면 컴퓨터가 힘들다)
        - 절차 지향 프로그래밍이 컴퓨터의 처리 구조와 비슷해서 실행 속도가 빠름
        

# OOP 기초

### 객체(컴퓨터 과학)

물리적(유형)으로 존재하는 자동차, 컴퓨터, 사람과 추상적(무형)으로 존재하는 강의, 주문들이 모두 객체가 될 수 있다. 컴퓨터 과학에서 객체 또는 오브젝트(object)는 **클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것**으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 변수, 자료구조, 함수 또는 메서드가 될 수 있다.

> 클래스에 선언된 모양 그대로 생성된 실체. 속성과 행동으로 구성된 모든 것
> 
- 속성 = 변수
- 행동 = 메서드

### 클래스(Class)

객체를 생성하기 위한 설계도이다. 객체가 가지는 속성과 행동으로 이루어져있다. 객체를 추상화하기 위한 도구.

> 붕어빵(객체)를 만들기 위한 붕어빵틀(클래스)라고 생각하면 된다.
> 
- 필드 : 객체의 데이터가 저장되는 곳이다.
- 생성자 : 객체가 실제로 생성될 때 초기화 역할을 담당한다.
- 메서드 : 객체의 동작에 해당하는 실행 블록이다.

### 인스턴스(Instance)

클래스가 붕어빵 틀이라면 그 틀을 통해 생성된 객체(붕어빵) 하나하나를 해당 클래스의 인스턴스라고 부른다. 이렇게 생성된 인스턴스들은 각자 고유의 특성을 가지고 독립적으로 존재한다.

- 예시

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/33737eec-8e86-46c1-a088-a2a2838a55af/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dc34497c-dc68-449b-8ad0-f1097413c14f/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bbdf57a3-112d-4126-b7a7-c69296d5b893/Untitled.png)

                                     **추상적인 상징**   

### 객체와 인스턴스

- 클래스로 만든 객체를 **인스턴스** 라고도 함
    - 객체와 인스턴스의 차이점?
        - 인스턴스는 특정 클래스의 객체이고 객체는 객체
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2a396509-3856-437d-9bae-e185b2415010/Untitled.png)
    

### 클래스와 객체

**클래스(가수)**와 **객체(실제사례)**

      ⬇️

  **타입(list)**

클래스를 만든다 == 타입을 만든다

*⇒ 개별객체를 하나의 타입으로 보는것 자체가 **추상화**이다.*

(객체가 다 다른데 하나의 공통점으로 묶는것)

- 파이썬은 모든것이 객체(파이썬의 모든것엔 속성과 행동이 존재)

```python
[3,2,1].sort()
리스트.정렬()
객체.행동()
```

```python
“banana”.upper()
문자열.대문자로()
객체.행동()

정보 : iterable, immutable
```

### 타입과 실제 사례(값)

```python
# list = 설계도(타입, 클래스) 이름 
[1,2,3][1][]['hi'] #리스트 타입(클래스)의 객체
'','hi','파이썬' #문자열 타입(클래스)의 객체
```

*객체는 **특정 타입의 인스턴스**이다.*

```python
123,900,5 #int의 인스턴스
'hello','a' #string의 인스턴스 -> 행동 .upper() 
[123,456,7][] #list의 인스턴스
```

### 객체

- 객체의 특징
    - 타입 : 어떤 연산자와 조작이 가능한가?
    - 속성 : 어떤 상태(데이터)를 가지는가?
    - 조작법 : 어떤 행위(함수)를 할 수 있는가?

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bb8ce099-0960-4fbe-ac0c-9f0e75b62505/Untitled.png)

                                                                    (상태, 정보)

### 기본 문법

- 클래스 정의         **class** **M**yClass:                             ⇒ 설명(정보와 행동)
    
                                         속성, 행위
    
- 인스턴스 생성     my_instance = **MyClass()**            ⇒ 인스턴스를 만든다
    
                                 인스턴스 =     type의 객체를 생성
    
- 메서드 호출         my_instance.**my_method()** ⇒ 메서드 호출
- 인스턴스의 역할.책임
- 속성                     my_instance.**my_attribute** ⇒ 변수 호출

                           인스턴스의 역할.속성

### 클래스와 인스턴스

- 클래스 : 객체들의 분류 / 설계도
- 인스턴스 : 하나하나의 실체 / 예
    - 파이썬은 모든 것이 **객체**, 모든 객체는 특정 타입의 **인스턴스**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90527984-1022-4f8c-836f-80443a44033f/Untitled.png)

### 객체 비교하는 방법

- **==**
    - **동등한**
    - 변수가 참조하는 객체가 내용이 같은 경우(생긴것이) True ⇒ 쌍둥이
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해준것은 아님
- **is**
    - **동일한**(identical)
    - 두 변수가 동일한 객체를 가리키는 경우 True ⇒ 분신(주소가 같으면)

```python
a = [1,2,3]
b = [1,2,3]
print(a==b, a is b) #True(값이 같음), False(서로 다른 객체)

a = [1,2,3]
b = a
print(a==b, a is b) #True(값이 같음), True(주소도 같음)
```

# OOP 속성

### 속성

- 속성(데이터, 정보, 상태) ⇒ 변수
- 특정 데이터 **타입/클래스의 객체들이 가지게 될 상태/데이터**를 의미
- **클래스 변수 / 인스턴스 변수**가 존재

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e7affe21-a0fd-4601-83c4-a07b81223bbc/Untitled.png)

객체 =  **정보** + 행동

정보에는 **클래스** 변수 / **인스턴스** 변수 2가지가 있다.

### 인스턴스 변수

- 인스턴스 변수란?
    - 인스턴스가 **개인적**으로 가지고 있는 속성
    - 각 인스턴스들의 고유한 변수
- 생성자 메서드(__**in it**__)안에서 **self.<name>**으로 정의(설계도로 사람을 만들 때 쓰는 것이 생성자메서드)
    - **self.name**
    - person1,2,3,… 가 다 다르다
- 인스턴스가 생성된 이후**<instance>.<name>**으로 접근 할당
- **나만 쓰는 변수**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/eb619159-4758-4e8f-94d2-d7c480d6dd9d/Untitled.png)

### 클래스 변수

- class안에 self없이
- 한 클래스의 **모든 인스턴스가 공유**하는 값을 의미(공용)
    - Person
- 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
- 예) 특정 사이트의 User 수 등은 클래스 변수를 사용해야함
- 클래스 선언 매부에서 정의
- **<classname>.<name>**으로 접근 및 할당

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e623196d-51ea-470e-b19c-46859650b8dc/Untitled.png)

- 인스턴스로도 클래스변수 조회가 가능하다 ⇒ **인스턴스.클래스변수**
- 클래스 변수를 변경할 때는 항상 **클래스.클래스변수** 형식으로 변경
- 인스턴스 변수는 **인스턴스.인스턴스 변수**
- 인스턴스 변수를 찾는데 없으면 클래스 변수를 찾아옴

# OOP 메서드

### 메서드

- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
- 메서드는 **클래스 안에 있는 함수**다
    - **인스턴트 메서드**
    - **클래스 메서드**
    - **정적 메서드**

## 인스턴스 메서드

- 인스턴스 변수 처리
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫 번째 인자로 인스턴스 자기자신(**self**)이 전달됨(자동)
- **클래스 변수, 인스턴스 변수** 둘 다 사용이 가능(웬만하면 인스턴스로 하고 꼭 만들어야할 때 클래스)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4d8a90fc-302f-44ee-b9db-c28f92242466/Untitled.png)

⇒ my_instance가 self에 들어감

- **self**
    - 인스턴트 자기자신
    - 파이썬에서 인스턴트 메서드는 호출시 **첫번째 인자**로 인스턴스 자기자신이 전달되게 설계
        - person1 = self
        - 매개변수 이름으로 self를 첫 번째 인자로 정의
        - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙
        
- **생성자(constructor) 메서드**
    - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
        - 인스턴스(person1) 생성
        - 내가 클래스 만들 때(Class+()할 때) **__init__**메서드 자동호출
        - 지민(argument) → name(2번째 parameter)
        
- **매직 메서드 (↪인스턴스 메서드)**
    - 특정 상황에서 특수한 동작을 위해 만들어진 메서드
    - __를 이용
    - __**str**__ 그대로 출력하고 싶을 때
    - print는 기본적으로 인자를  str()을 씌워서 출력 무엇을 str씌울지 알려주는 메서드가 __**str**__

```python
class Person:
	def __init__(self,name)
		self.name = name

	def __str__(self):
		return self.name

person1 = Person("김경아")
print(person1) #김경아
```

- **소멸자 메서드**
    - 없어질 때 생성되는 메서드
    - __del__
    - 왜 del

```python
class Person:
	def __init__(self,name)
		self.name = name

	def __str__(self):
		return self.name

	def __del__(self)"
		return("삭제되었습니다")

person1 = Person("김경아")
person2 = person1 
del person1 #포스트잇을 뗀것
print(person1) #김경아
               #삭제되었습니다 

#del은 객체를 지우는 것이아니라 변수가 객체를 가리키는 참조값을 없애는 것
#del이 마지막에 나온건 그냥 프로그램이 끝나서
```

## 클래스 메서드

- 클래스에 있는 속성을 활용할 때 사용(**cls.속성)**
- **@classmethod 데코레이터**를 사용하여 정의
- 호출시, 첫번째 인자로 **cls**가 전달됨
- **클래스 변수**만 사용 가능

```python
class Person: 
	count = 0 #클래스 변수
	def __init__(self,name): #인스턴스 변수 설정
		self.name = name
		Person.count += 1
	@classmethod
	def number_of_population(cls):
		print(f'인구수는 **{cls.count}**입니다.')
```

- **데코레이터**
    - 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
    - 데코레이터 형태로 함수 위에 작성
    - 순서대로 적용되므로 작성순서가 중요
    - 한꺼번에 수정가능해서 편리

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2346cd20-caef-4974-9733-cecab851fc38/Untitled.png)

## 정적(static) 메서드

- 나머지
- **속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때 사용**
- No cls, self
- @staticmethod 데코레이터를 사용하여 정의

```python
class Person:
	def __init__(self,name)
		self.name = name
		self.age = age

	def call_name(self) #이름을 가져오려면 self 필요함
		return f'대전 2반 {self.name}입니다!'

	@staticmethod
	def hello(): #self필요없음
		return '안녕하세요!' 

person1 = Person("김경아")
print(person1.call_name())
print(person1.hello())
```

### 인스턴스와 클래스 간의 이름 공간

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8d0dbf8c-d3b8-4a86-8758-2214f2ff0a81/Untitled.png)

결과가 무엇일까요?

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/637b2dd3-5d3e-4983-9f1d-54ccdab16e8a/Untitled.png)

p1 = 클래스 변수(인스턴스에 없으면)

p2 = 인스턴스 변수

## 메서드 정리

- 인스턴스 메서드
    - 호출한 인스턴트를 의미하는 **self 매개 변수**를 통해 인스턴스를 조작
- 클래스 메서드
    - 클래스를 의미하는 **cls 매개 변수**를 통해 클래스를 조작
    - @classmethod
- 스태틱 메서드
    - 클래스 변수나 인스턴스 변수를 사용하지 않는 경우에 사용
    - @staticmethod
        - 객체상태나 클래스 상태를 수정할 수 없음

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c3d864ba-fd51-49e4-ad3f-b5bca30e90c9/Untitled.png)

## 객체 지향의 핵심 4가지

- 추상화
- 상속
- 다형성
- 캡슐화

### 추상화(Abstraction)

- 현실 세계를 프로그램 설계에 반영
    - 복잡한 것은 숨기고, 필요한 것만 들어내기(interface)
    - 수정해야 할 내용이 있더라도 인터페이스는 그대로 유지(변경할 필요X)

ex) log-in, log-out의 작동 원리는 모르지만 실행 가능

### 상속(Inheritance)

- 두 클래스 사이 부모-자식 관계를 정립하는 것
- 클래스는 상속이 가능함
    - 모든 파이썬 클래스는 object를 상속받음
- 정보, 행동 모두 물려받음(재사용)

- **상속 관련 함수와 메서드**
    - **instance(*object, classinfo*)**
        - object가 classinfo로부터 만들어졌습니까?
        - classinfo의 instance거나 subclass인 경우 True
    - **issubclass(class, classinfo)**
        - class가 classinfo의 subclass(자식)이면 True
    - **super()**
        - 자식 클래스에서 부모 클래스를 사용하고 싶은 경우
    - mro 메서드(Method Resolution Order)
        - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
        - 인스턴스 → 자식 클래스 → 부모 클래스

- **상속 정리**
    - 파이썬의 모든 클래스는 object로 부터 상속됨
    - 부모클래스의 모든 요소(속성, 메서드)가 상속됨
    - sper()을 통해 부모 클래스의 요소를 호출할 수 있음
    - 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능
    - 이름공간은 인스턴스→자식→부모 클래스 순으로 탐색

- **다중 상속**
    - 클래스 두개 이상으로 부터 상속받는 경우
    - 중복 된다면 상속 순서에 따라 결정됨(앞에 있는 것)
    

### 다형성(Polymorphism)

- 여러(multple) 모양(Forms)을 뜻하는 그리스어
- 클래스의 핵심은 그대로 있고, 구현방식의 모양과 모습은 달라진다
- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
- 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메세지에 대해 다른 방식으로 응답할 수 있음
    - ex) say Hi 를 다른 방식으로 하고 싶을 때(same name, different 구현방식)

- **메서드 오버라이딩**
    - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
        - **ex) say Hi는 무조건 문자열이어야함(이것만 지켜줘)**
    - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
    - 부모 클래스의 메서드를 실행시키고 싶은 경우 super를 활용(우선순위:가까운것)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8708a8c1-530e-4e3f-b267-fd37e917abb0/Untitled.png)
    
- **오버로딩**
    - 
- 파이썬에서는 *args로 해결가능!

### 캡슐화(Encapsulation)

- 데이터나 함수를 캡슐 안에 두는 것
- 노출할 자료와 숨길 자료를 선택할 수 있음!
- capsule = class
- 객체 일부 구현내용에 대해 외부로터의 직접적인 액세스를 차단
    - 예시 : 주민등록번호

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bdfcbba-5ee7-466f-932e-41ca9f62f32a/Untitled.png)

- 접근제어자 종류
    - Public Access Modifier
    - Protected Access Modifier
    - Private Access Modifier

- **Public Access Modifier**
    - **언더바 없이** 시작하는 메서드나 속성
    - 어디서나 호출이 가능, 하위 클래스 override 허용

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7c6d452e-b56f-4afa-bcbc-0498ca04c269/Untitled.png)

- **Protected Access Modifie**
    - **언더바 1개**로 시작하는 메서드나 속성
    - 부모 클래스 내부와 자식 클래스에서만 호출가능
    - 하위클래스 override 허용

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5b6f8426-5c46-4d25-8370-3b9d85b7a877/Untitled.png)

- **Private Access Modifie**
    - 외부 사용자는 해당 필드에 엑세스하거나 수정할 수 없음
    - **언더바 2개**
    - 본 클래스 내부에서만 사용 가능(자기자신)
    - 하위클래스 상속 및 호출 불가능(오류)
    - 외부 호출 불가능(오류)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4a228839-e13a-4477-bad9-15f1c623ff48/Untitled.png)

- **getter 메서드와 setter 메서드로 해결**
- 직접 접근하면 안되니까←객체의 자율성
    - getter 메서드 : 변수의 값을 읽는 메서드→*get_age*
        - @property 데코레이터 사용 → *p1.age*로 사용하기 위해서 (편리성)
    - setter 메서드 : 변수의 값을 설정하는 성격의 메서드→*set_age*
        - @변수.setter 사용 → *age.setter*

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0b5026fd-afa1-4fdf-839f-6d750cde6a03/Untitled.png)

# 정리

- **객체**
    - **정보(변수)**
        - 클래스
        - 인스턴트
    - **행동(메서드)**
        - 클래스
        - 인스턴트
        - 스태틱(정적)

- **추상화 →** 복잡한거 숨기고 필요한거 나타냄
- **다형성 →** 이름은 같은데 동작은 다른 것 → 오버라이딩 → 부모자식이 그대로(x) → 자식이 변경
- **상속 →** 부모클래스에서 자식클래스 관계 → 물려받기 → for 재사용
- **캡슐화 →** 민감한 정보를 숨기는 것, 못 고치게 하는 것 → getter, setter로 변경