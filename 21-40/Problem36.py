"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import time


# driver function for our program
def main():
    """
    Driver function for our program.  This program is designed to sum the numbers
    between 1 and 1,000,000 that have the property that both the number and the
    binary representation of said number are palindroms.
    """
    start_time = time.time()

    sum = 0

    # loop from 2 to 1,000,000 because 1 is not prime!
    for num in range(1, 1000001):
        if is_palindrome(num) and is_bin_palindrome(num):
            sum += num

    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (sum, end_time))


def is_palindrome(n):
    """ Tests if the given number n is a palindrome """
    return n == reverse_int(n)


def is_bin_palindrome(n):
    """ Tests if the given binary number n is a palindrome """
    bin_n = dec_to_bin(n)
    return bin_n == reverse_int(bin_n)


def dec_to_bin(n):
    """ Converts decimal to binary """
    return int(bin(n)[2:])


def reverse_int(n):
    """ Reverses the values in an integer. 1234 = 4321 """
    reverse = 0
    while n > 0:
        remainder = n % 10
        reverse = (reverse * 10) + remainder
        n = n // 10
    return reverse


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
