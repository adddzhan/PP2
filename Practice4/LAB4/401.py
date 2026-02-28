def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2
        
n = int(input())

for x in square_generator(n):
    print(x)