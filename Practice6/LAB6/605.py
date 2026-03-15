text = input()

vowels = 'aeiouAEIOU'

if any( x in vowels for x in text ):
    print("Yes")
else:
    print("No")

# result = []
# for x in text:
#    if x in vowels:
#        result.append(1) # true
#    else:
#        result.append(0) # false