a = [10, 20, 30, "Hello", "World"]

# print(a[0])
# print(a[1])

i = 0

while i < 5:
    print(a[i])

    i = i + 1

# for 반복문을 이용하면, 리스트에 들어가 있는 모든 수들을 순차적으로 하나씩 꺼내는 연산이 수월함.
# 아래 for 반복문은 리스트에 들어가 있는 값만큼 반복을 진행함.

for j in a:
    print(j)

# 이 경우 for 반복문을 이용하는 것이 더 효율적이고 유연함.
# 프로그래밍에서는 문제를 푸는 여러가지 방식들이 존재를 하기 때문에 무엇 하나 꼬집어서 그것이 정답이라고 말하기는 어려움.

print("Hello")

# 우리가 print라는 함수를 정의한 적이 있었는가?
# 필요에 따라서 우리는 함수를 정의할 필요가 있다.

def add(a, b):
    return a + b

# return: 되돌아 가다, 반환하다

add(3, 4)

# 7

print(add(3, 4))
print(add(6, 6))

c = add(3, 4)

print(c)

# print(12)

# Hangman Game

# Literal (리터럴)

# s (x), e (o), c (x), a (o), t (o), s (x), x (x), l (o), i (x), r (o)
