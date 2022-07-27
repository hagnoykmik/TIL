### 기본

- **스타일 가이드**

[PEP8](https://peps.python.org/pep-0008/)

(= 맞춤법을 지키는 것)

- **들여쓰기**

공백(space 4칸) 사용을 권장(Tab과 혼용 X)

- **주석**

코드에 대한 설명

사람과 사람의 소통을 위함(only for 개발자)

주석을 다는 습관을 들이는 것이 좋은(협업!!)

---

# 저장

### 변수(variable)

데이터를 담는 상자(1개)

***프로그래밍의 핵심***

⇒ 데이터를 어떻게 **저장**하고 어떻게 **처리**할까?

                               (변수)

***추상화**

(변수를 사용해야 하는 이유)

원리는 모르지만 대충 어떤 느낌인지 안다. (ex/ 전화, 카페 파이썬)

![KakaoTalk_20220718_213040205.jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f4e8fb8c-a996-4305-86c9-116b43b36f14/KakaoTalk_20220718_213040205.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T143839Z&X-Amz-Expires=86400&X-Amz-Signature=038f32dd4a9f93ca306ced9111d4ecdfe533e88180cafaa8d8066151ea185908&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22KakaoTalk_20220718_213040205.jpg%22&x-id=GetObject)

```python
a = 1  # a라는 상자에 1을 저장한다.
a == 1 # a는 1이다.
```

### 식별자

변수 이름 규칙

※ 다음의 키워드는 예약어로 사용할 수 없음

함수, 명령어 등등

![KakaoTalk_20220718_213303800.jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b881c501-823f-4c91-ad74-c4b8ad4ec91e/KakaoTalk_20220718_213303800.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T143854Z&X-Amz-Expires=86400&X-Amz-Signature=75ed3f6e7cf0c76022188c5c8bcabdf85344016ff8a84ef1c0d5c946ae5bf0e8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22KakaoTalk_20220718_213303800.jpg%22&x-id=GetObject)

## 자료형(Datatype)

**상자**의 종류마다 넣을 수 있는게 다르다

![KakaoTalk_20220718_162138980.jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4c4a8ac1-42e1-42ec-bf27-7a63a5ae3c8a/KakaoTalk_20220718_162138980.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T143908Z&X-Amz-Expires=86400&X-Amz-Signature=617dea0a05d19dcaab1fa6f40366057500847c5ff57383c5c4fc751101ffc208&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22KakaoTalk_20220718_162138980.jpg%22&x-id=GetObject)

- 참/거짓(Boolean)
- 숫자(Numeric)
    - int(정수, integer)
    - float(실수)
- 문자열(string)
- none

### float

*부동소수점

파도의 높이가 뭐야?

실수 연산할 때 오류날 수 있음.

해결방법 ⇒ `print(abs(a - b) ≤ 1e-10)`

### string

모든 문자는 str타입

‘,”를 활용하여 표기(하나의 문장부호를 유지)

`print(’hello’)`

```python
print("문자열 안에 ‘작은따옴표’를 사용하려면 큰따옴표로 묶는다.")
print('문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.')
```

\문법

| \n  | 줄바꿈                        |
| --- | ----------------------------- |
| \t  | tab                           |
| \\  | \                             |
| \r  | 캐리지 리턴(커서를 맨 앞으로) |
| \0  | Null                          |
| \’  | '                             |
| \”  | "                             |

String Interpolation (문자열 안에 변수쓰는 법)

- % - formatting
    - %d : 정수
    - %f : 실수
    - %s : 문자열

```jsx
print('hello %s' % name)
print('내 성적은 %d' % score) #정수
print('hello %f' % score) #실수
```

- str.format()

```jsx
print('Hello, {}'.format(name))
```

- #f-strings

```python
#f-strings
name='Kim'
score=4.5

print(f'Hello, {name}! 성적은 {score}')

# Hello, Kim! 성적은 4.5
```

### None

값이 없음(반환 값이 없는 함수에서 사용)

### Boolean

논리 자료형으로 참/거짓을 표현

`펜은 검은색이다 = True/False`

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ea8f9839-8c96-41c5-9960-ed34b3564e2c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T143934Z&X-Amz-Expires=86400&X-Amz-Signature=914e36d479525cced7c95ac9311e6892e399d197e4b6d1d9d27c89266f5ece15&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

산술연산자

| +   | 덧셈     |
| --- | -------- |
| -   | 뺄셈     |
| *   | 곱셈     |
| /   | 나눗셈   |
| //  | 몫       |
| **  | 거듭제곱 |
| %   | 나머지   |

비교연산자

| <=     | 이하                        |
| ------ | --------------------------- |
| >=     | 이상                        |
| !=     | 같지않음                    |
| is     | 객체 아이덴티티             |
| is not | 객체 아이덴티티가 아닌 경우 |

논리연산자

| A and B        #모두 | A,B 모두 True시에만 True   |
| -------------------- | -------------------------- |
| A or B    #하나라도  | A,B 모두 False시에만 False |
| Not                  | True ↔ False               |
|                      |                            |

Falsy (False는 아니지만 False로 취급됨)

- 0, 0.0, (), [], {}, None, “”(빈 문자열)

처리우선순위 

- not → and → or

and에서 첫번째 값이 False인 경우 무조건 False ⇒ 첫번째 값 반환

or에서 첫번째 값이 True 인 경우 무조건 True ⇒ 첫번째 값 반환

---

## 컨테이너(자료구조)

**여러 개의 값**(데이터)을 담을 수 있는 것(객체)

서로 다른 자료형을 저장할 수 있음

- **Ordered** (순서가 있는(≠정렬되어 있다) 데이터) **시퀀스**
    
    ex) 1 2 3
    
- **Unordered** (순서가 없는 데이터) **비시퀀스**
    
    ex) 빨간색 파란색 노란색
    

![KakaoTalk_20220718_162138980_01.jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ee7108a0-61d8-48dd-9685-a7ab0ba2b683/KakaoTalk_20220718_162138980_01.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T144000Z&X-Amz-Expires=86400&X-Amz-Signature=dae14c76c38c2897c1a1a90ff1ae7d50c83456daa2b1e27873f0acab1b7c7755&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22KakaoTalk_20220718_162138980_01.jpg%22&x-id=GetObject)

## 시퀀스형

- 특징
    - 순서가 있다.( ≠ sorted 정렬되어있다)
    - **특정 위치의 데이터를 가리킬 수 있다.**
- 종류
    - 리스트(list)
    - 튜플(tuple)
    - 레인지(range)
    - 문자형(string)
    

### 1. 리스트

여러 개의 값을 **순서가 있는** 구조로 저장하고 싶을 때 사용

0번째부터 시작

생성된 이후 내용 변경이 가능(mutable)(유연성)

`list()` 혹은 `[]`

- 값 추출 : list[i]

```python
# 리스트명 = [요소1, 요소2, 요소3, ... ]
list_a = []
list_b = [1, 2, 3]
list_c = ['Life','is','too','short'] 
list_d = [1,2,3,'Python',['리스트','안에','리스트']]
```

### 2. 튜플

리스트와 같지만 생성 후, 담고있는 값 **변경 불가**(불변 자료형)

`() 혹은 tuple()`

- 단일 항목의 경우
    
    하나의 항목으로 구성된 튜플은 생성 시 값 뒤에 **쉼표**를 붙여야함
    
    - 값 추출 : tuple[i]
    
    ```python
    tuple_a = (1,)
    tuple_b = (1,2,3,) # 습관을 위해 그냥 쉼표를 붙여라
    ```
    

- 튜플 대입
    - 우변의 값을 좌변의 변수에 한번에 할당

```python
x, y = (1, 2) # x=1, y=2
```

### 3. Range

숫자의 시퀀스를 나타내기 위해 사용

주로 **반복문**과 함께 사용

```python
range(0, 4) # 0부터 4칸
[0,1,2,3]

range(n) # 0부터 n-1까지
range(n,m) # n부터 m칸
range(n,m,s) # n(시작)부터 m(끝)까지 s(간격)만큼 증가 
	ex) range(6,1,1) => []
			range(6,1,-2) => [6,4,2] 
```

**슬라이싱**

인덱스와 콜론을 사용하여 문자열의 특정 부분만 잘라낼 수 있음

콜론 기준 앞 인덱스는 포함, 뒤 인덱스는 미포함

```python
print([1,2,3,5][1:4]) => [2,3,5]
print('abcd'[2:4]) => cd

print([1,2,3,5][0,4,2]) => [1,3]
print('abcdefg'[1:3:2]) => b

[::] == 전체(처음부터 끝까지 순서대로)
[::-1] == 처음부터 끝까지 거꾸로간다
```

## 비시퀀스형

### SET =집합

- 중복되는 요소가 없이 **순서에 상관없는** 데이터들의 묶음
- 인덱스를 이용한 접근 불가능(방번호부여x)(순서가 없어 값추출 불가)
- 가변자료형(mutable)

`{} 혹은 set()`

```python
blank = {} #dictionary
blank_set = set() #빈 set을 만들려면set()을 반드시 사용
```

다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음

set연산자

| +   | 합집합            |     |
| --- | ----------------- | --- |
| &   | 교집합            |     |
| -   | 차집합            |     |
| ^   | 대칭차집합(합-차) |     |

### 딕셔너리

키-값(key-value) 쌍으로 이뤄진 자료형

- key
    
    **변경 불가능**한 데이터만 활용 가능(immutable)
    
    string, integer, float, boolean, tuple, range
    
- value
    
    어떤 형태든 관계없음
    

 `{} 혹은 dict()`

**key를 통해 value에 접근**

```python
dict_a = {'a':'apple','b':'banana','list':[1,2,3]}
dict_b = dict(a='apple',b='banana',list=[1,2,3])

# 추출방법
dict_a.keys()
dict_b.values()
dict_a.items()

print(air_info[0]['air_status']['O2'], air_info[1]['air_status']['O2'])
```

# 형변환(Typecasting)

파이썬에서 데이터 형태는 서로 변환할 수 있음

ex) 숫자 ↔ 문자

- **암시적(Implicit)**
    
    사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환
    
    - bool
    - numeric type(int, float,complex)
    
    ```python
    print(True + 3) => 4
    print(3 + 5.0) = 8.0
    ```
    
- **명시적(Explicit)**
    
    위의 상황을 제외하고 모두 다 명시적으로 형변환 필요
    
    사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환
    
    - string, float → int
        
        (형식에 맞는 문자열만 정수로 변환 가능)
        
    - str, int → float
    - int, float, list, tuple, dict → str
    
    ```python
    print(int('3') + 4) => 7  # 명시적 타입 변환이 필요함
    print(float('3') => 3.0   
    ```
    

input()은 숫자로 입력받아도 문자열로 저장됨

그래서 다시 숫자로 변환해야함

![KakaoTalk_20220718_220611954.jpg](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/50d211f5-d96c-410a-9b96-4966be125bd0/KakaoTalk_20220718_220611954.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T144018Z&X-Amz-Expires=86400&X-Amz-Signature=ffa9d16f7fd109cc613baa0487edbe3ecb7055930be79b0e09282711606cce02&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22KakaoTalk_20220718_220611954.jpg%22&x-id=GetObject)