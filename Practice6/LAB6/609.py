n = int(input())
arr1 = input().split()
arr2 = input().split()
target = input()

result = dict(zip(arr1, arr2))

print(result.get(target, "Not found"))