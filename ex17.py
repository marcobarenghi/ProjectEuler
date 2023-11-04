#If the numbers $1$ to $5$ are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.
#If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE:Do not count spaces or hyphens. For example, $342$ (three hundred and forty-two) contains $23$ letters and $115$ (one hundred and fifteen) contains $20$ letters. The use of "and" when writing out numbers is in compliance with British usage.

#set up array and then build up words
nums=["one","two", "three", "four", "five", "six", "seven","eight", "nine","ten","eleven","twelve","thirteen","fourteen","fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
decades=["twenty", "thirty","fourty","fifty","sixty", "seventy","eighty","ninety"]

#20-99
for d in decades:
	nums.append(d)
	for i in range(9):
		nums.append(str(d+nums[i]))

#100-999		
for i in range(9):
	nums.append(str(nums[i])+"hundred")
	#reuse first 99 numbers
	for j in range(99):
		nums.append(str(nums[i])+"hundredand"+str(nums[j]))

nums.append("onethousand")

count=0
for i in range(len(nums)):
	count+=len(nums[i])
print(count)