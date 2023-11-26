#<p>Consider the fraction, $\dfrac n d$, where $n$ and $d$ are positive integers. If $n \lt d$ and $\operatorname{HCF}(n,d)=1$, it is called a reduced proper fraction.</p>
#<p>If we list the set of reduced proper fractions for $d \le 8$ in ascending order of size, we get:
#$$\frac 1 8, \frac 1 7, \frac 1 6, \frac 1 5, \frac 1 4, \frac 2 7, \frac 1 3, \frac 3 8, \frac 2 5, \frac 3 7, \frac 1 2, \frac 4 7, \frac 3 5, \frac 5 8, \frac 2 3, \frac 5 7, \frac 3 4, \frac 4 5, \frac 5 6, \frac 6 7, \frac 7 8$$</p>
#<p>It can be seen that there are $21$ elements in this set.</p>
#<p>How many elements would be contained in the set of reduced proper fractions for $d \le 1\,000\,000$?</p>

#for each denominator we can use the totient function to calculate n of properly reduced function
def sol(nMax):
    phi=list(range(nMax+1))
    for n in range(2, nMax+1):
        #n was not evaluated, proceed
        if(phi[n]==n):
            #reduce all values (see for loop), because fraction is not reduced
            for k in range(n, nMax+1, n):
                phi[k]-=phi[k]//n
    #do not count 1/1
    return sum(phi)-1

nMax=1000000
print(sol(nMax))