n = int(input())
arr = list(map(int, input().split()))

result = sorted(
    set(arr)
)

print(*result)