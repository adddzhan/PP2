n = int(input())
text = input().split()
result = tuple(enumerate(text))    # әр элементке 0 ден бастап индекс қояды

for index, value in result:
    print(f"{index}:{value}", end=" ")

# (index, value)