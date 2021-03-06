"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However,
their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which
their sum and difference are pentagonal and D = |Pk − Pj|
is minimised; what is the value of D?
"""
import time
from Misc.useful import is_pentagonal


# driver function for our program
def main():
    """
    With m = 7042750 and n = 1560090 it calculated
    D = 5482660 in 672 seconds.
    """
    start_time = time.time()

    distance = 0
    not_found = True
    i = 2
    num_m = 0
    num_n = 0

    while not_found:
        m = i * (3*i - 1) / 2
        j = i - 1

        while j > 0:
            n = j * (3*j - 1) / 2
            if is_pentagonal(m+n) and is_pentagonal(abs(m-n)):
                distance = abs(m-n)
                not_found = False
                num_m = m
                num_n = n
                break

            j -= 1

        i += 1

    # calculate end time and print results
    end_time = time.time() - start_time
    print("Found %s in %2f seconds." % (distance, end_time))
    print(num_m, num_n)


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
