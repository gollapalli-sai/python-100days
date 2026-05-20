scores=[100,99,98,97,97,78,88,87,78,66,88]
total=sum(scores)
print(total)
print(max(scores))


total=0
for i in range(1,101):
    total=total+i
print(total)


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
