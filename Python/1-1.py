# 덧셈은 + 이용
print(1 + 1)

# 뺄셈은 - 이용
print(2 - 1)
print(3 - 1)

# 곱셈은 * 이용
print(5 * 3)

# 나눗셈은 / 이용
print(10 / 2)

# 프로그래밍 세계에서 소수점이 없는 수를 가리켜 정수라고 하고, 소수점이 있는 수를 가리켜 실수라고 한다.

# 프로그래밍 세계에서는 Primitive Types: 수(정수, 실수), 문자열

"Hello"
'World'

"3"

print("3 + 5")

# 변수, 수학 세계에서는 변하는 수라는 의미만을 내포하고 있음. 프로그래밍 세계에서는 변하는 수라는 의미 외에 
# 메모리 공간에 값을 담는다는 의미 또한 내포하고 있음.
# = (등호) 기호를 이용함.

a = 10

# a <- 10; a는 그냥 공간일 뿐임.

b = "Hello"

print(a)

# print(10)

print(b)

# print("Hello")


a = b

# a = "Hello"

print(a)


# Literal

10

"Hello"

print(10)
print("Hello")

# Literal: 일회용품, Variable: 재활용품

a = 9

# 파이썬에서 들여쓰기(Indentation)는 매우 중요 !!

if a > 10:      # if 10 > 10:   if 11 > 10:
    print("a가 10보다 크다.")
print("a가 10보다 크다.")       # 해당 문장은 a에 들어있는 값과 무관하게 항상 출력됨.


# 반복문: while, for

i = 0

# if문과 반복문, 그리고 앞으로 배울 함수에서도 끝에 :(콜론)을 붙여줘야 함.

# 변수에서 =(등호) 오른쪽의 최종 결과값이 왼쪽 변수에 들어간다는 개념으로 생각하면 됨.

while i < 5:
    print(i)

    i = i + 1

# 반복문을 사용해야 하는 이유

# "Hello"라는 문자열을 화면에 5번 출력한다고 가정.

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# 마치 move() 함수에서처럼,,


# "Hello"라는 문자열을 화면에 100번 출력한다고 해보면?

# 이러한 번거로움을 막기 위해 우리는 반복문의 개념을 활용한다.


i = 0

while i < 100:
    print("Hello")

    i = i + 1


# 자료구조가 있음. 대표적으로 List(리스트)

a = [10, 20, 30, "Hello"]

print(a)



















