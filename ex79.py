#<p>A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.</p>
#<p>The text file, <a href="resources/documents/0079_keylog.txt">keylog.txt</a>, contains fifty successful login attempts.</p>
#<p>Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.</p>

#find which digits are before the investigate one
def findDigitsBefore(digit, loginCodes):
    beforeDigit=set()
    for code in loginCodes:
        if digit in code:
            for testDigit in code:
                if(testDigit==digit):
                    break
                else:
                    beforeDigit.add(testDigit)
    return beforeDigit

def sol(codeDigits, loginCodes):
    fullCode=[]
    #append or insert digits accordingly
    for digit in codeDigits:
        beforeDigit=findDigitsBefore(digit, loginCodes)
        if not beforeDigit:
            fullCode.append(digit)
        else:
            for d in fullCode:
                if d in beforeDigit:
                    fullCode.insert(fullCode.index(d), digit)
                    break
            else:
                fullCode.append(digit)
    return "".join(reversed(fullCode))
    
with open('ex79_input.txt', 'r') as file:
	#use set to remove duplicates
	loginCodes=list(set(file.read().split()))

firstDigits=set()
secondDigits=set()
thirdDigits=set()
for code in loginCodes:
    firstDigits.add(code[0])
    secondDigits.add(code[1])
    thirdDigits.add(code[2])
codeDigits=(firstDigits|secondDigits|thirdDigits)
print("first digits:", firstDigits)
print("second digits:", secondDigits)
print("third digits:", thirdDigits)
print("Digits present in the passcode:", codeDigits)
print("Complete passcode:", sol(codeDigits, loginCodes))