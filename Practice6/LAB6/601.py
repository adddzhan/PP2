n = int(input())
arr = list(map(int, input().split()))

result = map(lambda x:  x ** 2 ,arr) # контейнердің каждый элементіне бірдей амал қолданамыз
print(sum(list(result)))
# print(sum(result))

# sum = 0
# for x in arr:
#    sum += x ** 2
#print(sum)