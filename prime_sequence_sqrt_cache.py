# program that checks a 16 bit number is prime or not
# Takes numbers as command line params and as well waits for the input
# until ctrl+c is pressed.
# If there is no issue with memory, this program caches the result
# of each number (prime or not or ignored) in a dict and uses the dict
# to lookup.

import sys
import math

def main():

    # This loop reads any input (numbers) passed as command line args
    # and checks whether the number is 16 bit or not. If 16 bit,
    # checks prime or not for each number
    for n in range( 1, len(sys.argv) ):

        num = sys.argv[n]
        result = check_prime( num )
        if result["status"] == "ignored":
            sys.stderr.write( num + "[ " + result["reason"] + " ]\n" )
        else:
            print num + " [ " + result["status"] + " ]"

    # This loop waits for the input until ctrl+c is pressed
    # The numbers are seperated by white space and it can take
    # any number of numbers
    try:
        while True: 

            sys.stderr.write( "Enter numbers, space separated. ctrl + c to exit\n" )

            line = sys.stdin.readline()
            nums = line.split()
            for n in nums:

                result = check_prime( n )
                if result["status"] == "ignored":
                    sys.stderr.write( n + "[ " + result["reason"] + " ]\n" )
                else:
                    print n + " [ " + result["status"] + " ]"

    except KeyboardInterrupt:
        print "Exited."
        sys.exit(1)

def check_prime(n):
    # Ignore this input, if not number
    if n.isalpha():
        return { "status":"ignored", "reason":"Not a number" }

    # Lookup in cache first
    if cache.has_key(n):
        return { "status":cache[n] }
    else:
        n = int(n)
        # Process only 16-bit numbers
        if is_16bit_number(n):

            result = is_prime( n )
            # update cache
            cache[ str(n) ] = result
            return { "status":result }
        else:
            return { "status":"ignored", "reason":"Not a 16-bit number" }

def is_16bit_number(num):
    max_limit = (2 ** 16) - 1
    if num > max_limit:
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

################
# MAIN EXECUTION
################
# Stores information about each number
# check the cache before for every input and if not in cache
# do the nornal prime check process
cache = {}
main()
