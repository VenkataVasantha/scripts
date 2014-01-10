#Write a command-line program to read one number from the keyboard, test to see
#if it's a prime, and print "yes" or "no" to the screen before exiting.
#You should handle errors gracefully (e.g. warn the user if a non-integer is entered, etc). The program needs to run quickly,
import sys

def main():
    n = ''
    try:
        n = sys.argv[1]
    except:
        help('Invalid input.')
        sys.exit(1)
    else:

        if n.isdigit():
           n = int(n)
           flag = True
           for num in range(2, n/2+1):
                if( n % num == 0 ):
                    flag = False;
                    break;

           if flag:
               print 'yes'
           else:
               print 'no'
        else:
            help('Invalid input. Only number is accepted' )
            sys.exit(1)

def help(msg):
    prgname = sys.argv[0]
    sys.stderr.write( msg + '\n' )
    sys.stderr.write( "Usage: " + prgname + " {number}\n" )

main()
