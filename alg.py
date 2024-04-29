import math

def main():
    d = input("Enter sequence of numbers with a comma separator (e.g. 1,2,3,4): ")
    
    #Cleaning of input sequence
    seq = d.split(",")
    seq = [int(i.strip()) for i in seq]
    
    #Calculate f
    f = 0
    for index, val in enumerate(seq):
        if val >= index:
            f = index
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
        a[i] = seq[i] - i + 1
        b[i] = seq_star[i]-i

    #Make a_i' and b_i' sequences. Don't have to be copies of a and b, but helps for b
    a_prime = a.copy()
    b_prime = b.copy()

    #Run algorithm
    k = f
    while k>0:
        if a[k] == b[k]:
            a_prime[k] = a[k]
        elif a[k]< b[k]:
            a_prime[k] = int(a[k] + math.floor(0.5(b[k]-a[k])))
            if (b[k]-a[k])%2 == 1:
                a[k-1] += 1
        elif a[k]>b[k]:
            a_prime[k] = b[k]
            a[k-1] += a[k]-b[k]
        k -= 1

    a_prime[1] = a[1] + 1/2*(b[1]-a[1])

    for i in range(f):
        b_prime[i] = a_prime[i]



if __name__ == "__main()__":
    main()
