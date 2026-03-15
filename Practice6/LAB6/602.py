n = int(input())
arr = list(map(int, input().split()))

result = filter(lambda x:  x % 2 == 0 ,arr) # filter() егер шарт арқылы жүгіру керек болса
print(
    len(list(result))
)

# counter = 0
# for x in arr:
#    if x % 2 == 0:
#        counter += 1
# print(counter)