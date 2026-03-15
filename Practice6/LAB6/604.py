n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = map(
    lambda x:   x[0] * x[1] , zip(arr1, arr2)  # zip returns tuple(in our case binary relation)
)

print(sum(
    list(result)
))