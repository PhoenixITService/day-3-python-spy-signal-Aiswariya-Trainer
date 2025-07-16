nums = map(int, input().split())
numbers = list(nums)
chars = list(map(chr, numbers)) 
threes = chars[1::3]
reverse = threes[::-1] 
print(''.join(reverse))
