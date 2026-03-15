n = int(input())
arr = list(map(int, input().split()))

result = map(bool, arr) # 0 = false, otherwise true
print(sum(result))  # true = 1

# result = filter(
#    lambda x: x != 0, arr
# )
# print(len(list(result)))