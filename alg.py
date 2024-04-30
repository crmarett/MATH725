import math
#Prints the Hasselbarth (0,1)-matrix
def print_hass(a: list[int]):
    n = len(a)
    mat = [[1 if j<i else 0 for j in range(n)] for i in a]
    for i in mat:
        for j in i:
            print(j, end = ' ')
        print("")

#Prints the fxn submatrix given by a'
def print_a_prime(a_prime: list[int], n):
    mat = [[1 if j<val+index else 0 for j in range(n)] for index,val in enumerate(a_prime)]
    for i in mat:
        for j in i:
            print(j, end = ' ')
        print("")

#Takes in graphic integer sequence, runs algorithm
def alg(seq: list[int]):
    n = len(seq)
    #Calculate f
    f = 0
    for index, val in enumerate(seq):
        if val >= index+1:
            f = index + 1
        else:
            break
    
    #Calculate d* to later calculate b
    seq_2 = seq.copy()
    seq_star = [0 for _ in range(f)]
    for i in range(f):
        seq_star[i] = sum([1 if i>0 else 0 for i in seq_2])
        seq_2 = [i-1 for i in seq_2]


    #Make a_i and b_i sequences
    a = [0 for _ in range(f)]
    b = [0 for _ in range(f)]
    for i in range(f):
        a[i] = seq[i] - i
        b[i] = seq_star[i]-i-1

    #Make a_i' and b_i' sequences. Don't have to be copies of a and b, but helps for b
    a_prime = a.copy()
    b_prime = b.copy()

    #Run algorithm
    k = f-1
    while k>0:
        #Prints fxn submatrix
        print("")
        print_a_prime(a, n)
        if a[k] == b[k]:
            a_prime[k] = a[k]
        elif a[k]< b[k]:
            a_prime[k] = int(a[k] + math.floor(0.5*(b[k]-a[k])))
            if (b[k]-a[k])%2 == 1:
                a[k-1] += 1
        elif a[k]>b[k]:
            a_prime[k] = b[k]
            a[k-1] += a[k]-b[k]
        k -= 1
            
    a_prime[0] = int(a[0] + 1/2*(b[1]-a[1]))
    
    for i in range(f):
        b_prime[i] = a_prime[i]

    print(f"\na' is {a_prime} at end of algorithm")

    return a_prime


