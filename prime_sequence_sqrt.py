import sys
import math

def main():

    # This loop reads any input (numbers) passed as command line args
    # and checks whether the number is 16 bit or not. If 16 bit,
    # checks prime or not for each number
    for n in range( 1, len(sys.argv) ):

        num = sys.argv[n]
        # Ignore this input, if not number
        if num.isalpha():
            print num + " [ ignored ]"
            continue

        # Process only 16-bit numbers
        if is_16bit_number(num):
            print  num + " [ " + is_prime( int(num) ) + " ]"

    # This loop waits for the input until ctrl+c is pressed
    # The numbers are seperated by white space and it can take
    # any number of numbers
    try:
        while True:

            sys.stderr.write( "ctrl + c to exit\n" )

            line = sys.stdin.readline()
            nums = line.split()
            for n in nums:

                # Ignore this input, if not number
                if n.isalpha():
                    print n + " [ ignored ]"
                    continue

                # Process only 16-bit numbers
                if is_16bit_number(n):
                    print  n + " [ " + is_prime( int(n) ) + " ]"

    except KeyboardInterrupt:
        print "Exited."
        sys.exit(1)

def is_16bit_number(num):
    max_limit = (2 ** 16) - 1
    if int(num) > max_limit:
        return 0
    else:
        return 1

def is_prime(n):
    prime = 1
    for num in range(2, int(math.sqrt(n))+1):  # Changed to sqrt here, which reduces number of iterations when compared to n/2
        if( n % num == 0 ):
            prime = 0
            break;

    if prime:
        return 'yes'
    else:
        return 'no'

main()
