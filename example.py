from paper_alg import print_a_prime, print_hass, alg


#Shows examples or gives 
def main():
    while True:
        example_seq = [[3,3,3,3], [4,3,3,2,2,2], [6,5,5,4,4,4,3,3]]
        user_input = input("Would you like to 1) look at some examples from the paper or 2) input your own sequence or 3) Quit: ")
        if user_input == "1":
            for i in range(len(example_seq)):
                print(f'\n\nFor example {i} the sequence is {example_seq[i]}\nBelow is the Hasselbarth (0,1)-matrix for the sequence')
                print_hass(example_seq[i])
                a_prime = alg(example_seq[i])
                print("\nFinal fxn matrix is")
                print_a_prime(a_prime, len(example_seq[i]))
        elif user_input == "2":
            d = input("Enter sequence of numbers with a comma separator (e.g. 1,2,3,4): ")
        
            #Cleaning of input sequence while also assuming good input (please)
            seq = d.split(",")
            seq = [int(i.strip()) for i in seq]

            a_prime = alg(seq)
            print_a_prime(a_prime, len(seq))

        elif user_input == "3":
            break
        else:
            print("Bad input, please retry")

main()
