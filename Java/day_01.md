# 변수

## 변수

- 자료를 저장하기 위한 **메모리공간**으로 타입에 따라 크기가 달라짐
- 메모리 공간에 값(value)을 할당(assign) 후 사용

## 타입

- 기본형
    - 미리 정해진 크기의 메모리 사이즈로 표현
    - 변수 자체에 값 저장
    - `int 나이 = 10`
- 참조형
    - 크기가 미리 정해질 수 없는 데이터의 표현
    - 변수에는 실제 갑슬 참조할 수 있는 주소만 저장
    - `집 우리집 = 서울시 성북구 ~`

### 기본형

- 논리형
    - boolean
- 정수형
    - byte
    - short
    - **int**
    - long
- 실수형
    - float
        - `float f1 = 10.0f`
        - 실수는 정확하지 않다 (유효 자리수를 이용한 반올림 처리)
    - **double**
- 문자형
    - char

## 형변환

- 형 변환 연산자(괄호) 사용

```java
double d = 100.5;
int result = (int)d;

// result = 100
// d = 100.5
```

- boolean은 다른 기본 타입과 호환되지 않음
- 기본 타입과 참조형의 형 변환을 위해서 Wrapper 클래스 사용

### 묵시적 형변환

- 바이트 크기가 작은 자료형에서 큰 자료형으로 대입하는 경우

### 명시적 형 변환

- 바이트 크기가 큰 자료형에서 작은 자료형으로 대입하는 경우

![작은 자료형 → 큰 자료형](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de4c67ec-36c1-4e29-9a2c-b0ddb81f1517/Untitled.png)
이미지

작은 자료형 → 큰 자료형

# 연산자

## 연산자 우선 순위

- 최우선 순위는 괄호 `()`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bf9d1da-03c6-494f-8193-a53089eea0d3/Untitled.png)

- `| (or)` : 하나라도 true라면 true
- `|| (or)` : 앞의 것이 true라면 무조건 true

```java
int a = 10;
int b = 20;

// 1
System.out.println((a += 10) < 15 | (b -= 10) > 15);    // true
System.out.println("a " + a + ", b = " + b);            // a = 20, b = 10    

// 2
System.out.println((a += 10) < 15 || ~~(b -= 10) > 15)~~;   // true
System.out.println("a " + a + ", b = " + b);            // a = 20, b = 20    
```

