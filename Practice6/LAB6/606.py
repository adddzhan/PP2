n = int(input())
arr = list(map(int, input().split()))

if all( x >= 0 for x in arr ):
    print("Yes")
else:
    print("No")

# result = []
# for x in arr:
#    if x >= 0:
#        result.append(1) # true
#    else:
#        result.append(0) # false