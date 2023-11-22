#<p>The $5$-digit number, $16807=7^5$, is also a fifth power. Similarly, the $9$-digit number, $134217728=8^9$, is a ninth power.</p>
#<p>How many $n$-digit positive integers exist which are also an $n$th power?</p>

#exp is not limited! we should increase it until condition fails
count=0
for b in range(1, 10):
    exp=1
    while(True):
        if(exp==len(str(b**exp))):
            count+=1
            print(b,exp,b**exp)
        else:
            break
        exp+=1
print(count)