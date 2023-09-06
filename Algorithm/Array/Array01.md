### 알고리즘

- 문제를 해결하기 위한 절차나 방법
- 컴퓨터가 어떤일을 수행하기 위한 단계적 방법

- 컴퓨터 분야에서 알고리즘을 표현하는 방법

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cd337875-0a44-4106-9b0c-c4f8ef75a6f4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220814T132946Z&X-Amz-Expires=86400&X-Amz-Signature=fd3d95dba720d614be0c2ad458f3000664052a6bfa14bbcba96a97562480e84c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- tip! A4용지에 필기하는 습관을 가져라!

### 무엇이 좋은 알고리즘인가?

1. 정확성
2. 작업량 : 적을수록
3. 메모리 사용량 : 적을수록
4. 단순성
5. 최적성 : 개선할 여지없이

### 시간 복잡도(Time Complexity)

- 알고리즘의 작업량을 표현할 때 사용
    - 실제 걸리는 시간 측정
    - 실행되는 명령문의 개수 계산

- 빅-오(O) 표기법
    - 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시
    - 계수 생략
    - 예시
      - n개의 데이터를 입력 받아 저장한 후 각 데이터에 1씩 증가시킨 후 각 데이터를 화면에 출력하는 알고리즘의 시간 복잡도는 어떻게 되나?
        - O(n)


---

## 배열

### 배열이란 무엇인가?

- 저장하는 형태(방식)
- 일정한 자료형의 변수들을 하나의 이름(연속적으로)으로 열거하여 사용하는 자료구조

```python
Num = [0,1,2,3,4,5]
```

### 배열의 필요성

- 프로그램 내에 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 비효율적
- 배열을 사용하면 하나의 선언을 통해 둘 이상의 변수를 선언할 수 있다
- 단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있다.

### 1차원 배열

- 1차원 배열의 선언
    - 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성
    - 이름 : 프로그램에서 사용할 배열의 이름
        - `Arr = [1, 2, 3]`

- 1차원 배열의 접근
    - `Arr[0] = 10` #배열 Arr의 0번 원소에 10을 저장하라
    - `Arr[idx] = 20` #배열 Arr의 idx번 원소에 20을 저장하라

---

## 정렬

### 정렬

- 2개 이상의 자료를 특정 기준에 의해 오름차순(ascending) 혹은 내림차순(descending)으로 재배열 하는 것

### 종류

- **버블 정렬**
- **카운팅 정렬**
- **선택 정렬**
- **퀵 정렬**
- 삽입 정렬
- 병합 정렬

### 버블 정렬

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
- 정렬 과정
    - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
    - 한 단계 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
- 시간 복잡도
    - O(n^2)

- 예시

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/eae649bf-7ac9-424c-86d2-59643f77a6b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220814T133241Z&X-Amz-Expires=86400&X-Amz-Signature=0ff5f31caaf1b6ab6b156007db78daa8ca4c4eb67330418cf61458cef716e829&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 구간의 시작 - 끝
- 0 - (n-1)
- 0 - (n-2)
- …
- 0 - 1

```python
for i : n-1 -> 1 #구간의 끝을 정하면
	for j : 0 -> i-1 #인접한 원소 중 왼쪽 인덱스
		if arr[i] > arr[j+1] #왼쪽이 크면
			arr[i] <-> arr[j+1] #자리 바꿈
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3268cd85-ead8-49b3-97ee-f0f540d948e9/Untitled.png)

- tip! 2중 for문 → n^2
- n + n-1 + n-2 +…+1 = n(n+1)/2 이기 때문

### 선택 정렬

### 카운팅 정렬

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몉ㅊ개씩 있는지 세는 작업을 하여, 선형 시간(O(n))에 정렬하는 효율적인 알고리즘
- 제한 사항
    - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
        - 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용
    - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.
- 시간 복잡도
    - O(n + k) : n은 리스트 길이, k는 정수의 최대값
    

범위가 주어진다

0으로 초기화된 배열을 만든다

count배열의 최대는 100만개

- 원소의 개수를 세는 작업

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5c5e5ac-adb1-4976-bd73-cd7fd368d668/Untitled.png)

```python
c = [0] * (k+1) #카운트 배열 k개 초기화

for i in range(0, len(A)): #카운트 하는 과정(n번)
	C[A[i]] += 1
```

- 0~n까지 전체 몇 개가 있니?

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/342f2c95-7960-448c-bb08-e8e02831666b/Untitled.png)

```python
for i in range(1, len(C)): #누적(k번)
	C[i] += C[i-1]
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8dd99e4a-ac44-41cb-936e-189770b10edf/Untitled.png)

```python
for i in range(len(B)-1,-1,-1) #마지막 원소 n번
	C[A[i]] -= 1
	B[C[A[i]]] = A[i]
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f6e5d6d-d5d7-4fdb-9c63-b9df98076bfb/Untitled.png)

## 예제)Baby-gin Game

### 완전 검색(Brute-force, generate-and-test)

- 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
- 모든 경우의 수를 테스트한 후, 최종 해법을 도출한다
- 속도가 느리지만 해답을 찾아내지 못할 확률이 작다.
- 자격검정평가 등에서 주어진 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직하다.

### 완전 검색의 동작 과정

1. 고려할 수 있는 나열의 모든 경우의 수 생성하기(순열)
2. 해답 테스트하기
 `A[0] + 1 = A[1] and A[1] + 1 = A[2]`  `#run`

### 순열(Permutation)

- nPr = n * (n-1) * (n-2) * … * (n-(r-1))
- nPn = n!

- 예시
    - {1, 2, 3}을 포함하는 모든 순열

![Untitled]()

### 탐욕(Greedy) 알고리즘

- 최적해를 구하는데 사용되는 근시안적인 방법
- 머릿속에 떠오르는 생각을 검증없이 바로 구현하면 Greedy 접근이 된다.

### 탐욕 알고리즘의 동작 과정

1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해집합(Solution Set)에 추가한다.
2. 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지 확인한다. 곧 문제의 제약 조건을 위반하지 않는지 검사한다.
3. 해 검사 : 새로운 부분해 집합이 문제의 해가 되는지 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 1부터 다시 시작한다.

### 예제) 거스름돈 줄이기(개수)

1. 500원 선택(액수가 클수록 좋음)
2. 거스름돈을 초과하지 않는지 확인(300원이면 500원탈락 그 다음 100원)
3. 남은 돈이 없으면 끝!

### 탐욕 알고리즘으로 Baby gin 을 푼다면?

- run → 연속된 숫자 3개가 1씩 있을 때(1,1,1)
- triplet → 한 개의 숫자가 3이면

- 카운트 배열을 채워보자!

![Untitled])

- 12자리를 만든 이유
    - 9번부터 연속된 세 개를 검사할 경우를 대비
- 자릿수가 정해져 있지 않을 때는?

```python
while num > 0:
	c[num % 10] += 1
  num //= 10
```

- triplet

```python
while i < 10:
	if c[i] >= 3: #triplet조사 후 	
		c[i] -= 3 #데이터 삭제
		tri += 1
		continue; #그 자리에서 다시 조사
```

- run

```python
	if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >=1:
		c[i] -= 1
		c[i+1] -= 1
		c[i+2] -= 1
		run += 1
		continue
	i += 1
```

- 결론

```python
if run + tri == 2:
	print("Baby gin")
else:
	print("Lose")
```

---

### 코드 예시

- 최대값의 위치, 같은 값이 있을 때는 맨 오른쪽

```python
9
7 4 2 0 0 6 0 7 0 

N = int(input())
arr = list(map(intm input().split())

maxIdx = 0 #맨 앞이 가장 큰수라고 가정

for i in range(1, N):
	if arr[maxIdx] <= arr[i]: #'등호'가 / 비교하는 값이 같을 때 '오른쪽'을 선택하는 기능을 함
		maxIdx = i
```

- 버블 정렬(오름차순)

```python
9
7 4 2 0 0 6 0 7 0 

N = int(input())
arr = list(map(intm input().split())

for i in range(n-1, 0, -1): #구간의 끝에서 1까지 줄여나감
	for j in range(i): #인접원소 중 왼쪽 원소 인덱스(i-1까지)
		if arr[j] > arr[j+1]: #오름차순, 더 큰수를 오른쪽으로
			arr[j], arr[j+1] = arr[j+1], arr[j] #자리바꿈
print(arr)		
```

- 카운트 정렬

```python
9
7 4 2 0 0 6 0 7 0 

N = int(input())
arr = list(map(intm input().split())

tmp = [0] * N

c = [0] * 101 #0부터 100까지 숫자 개수, 인덱스가 100까지 있어야함
for i in range(N):
	c[arr[i]] += 1

for j in range (1,101) #개수 누적(0번은 왼쪽이 없으므로 1부터)
	c[j] += c[j-1]

for i in range(N-1, -1, -1): #원본을 뒤에서부터 읽으면서 정렬 결과를 tmp에 저장
	c[arr[i]] -= 1 #인덱스로 바꿔준다
	tmp[c[arr[i]]] = arr[i]

print(tmp)	
```