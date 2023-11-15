#<p>The series, $1^1 + 2^2 + 3^3 + \cdots + 10^{10} = 10405071317$.</p>
#<p>Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \cdots + 1000^{1000}$.</p>

nMax=1000
n=0
for i in range(1, nMax+1):
    n+=i**i

print(str(n)[-10:])