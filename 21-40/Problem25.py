"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time


def get_digits(number):
    return len(str(number))


def main():
    start_time = time.time()
    fib_1 = 1
    fib_2 = 1
    fib_3 = 2
    index = 3

    while get_digits(fib_3) < 1000:
        fib_1 = fib_2
        fib_2 = fib_3
        fib_3 = fib_1 + fib_2
        index += 1

    print(fib_3)
    end_time = time.time() - start_time
    print("found index value %s in %2f seconds." % (index, end_time))

    # answer = 107006626638275893676498058445739688508368389663215166501323520337531452060469404062188914758248979265780
    # 469488817759195748433646667256995951299603046126274809248218614406943305123477444275027378175308757939166619214925
    # 918675955396642283714894311307469950343954700198543260972306729019287052644724372611771582182554849112052501320147
    # 861296593138179223555965745203950613755146783754322911960212993404826070617539770684706820289548690266618543512452
    # 190036948064135744747091170761976694569107009802439343961747410373691250323136553216477369702316775505159517351846
    # 057995491941096777837322966579658164651390348815425631018422419025984608800011018625555024549393711365165703944762
    # 958471454852342595042858242530608354443542821261100899286379504800689433030977321783486454311320576565986845628861
    # 680871869383529735064398629764066000072356291790520705116407761481249188583094594056668833910935094445657635766615
    # 1619317753792891661581327159616877487983821820492520348473874384736771934512787029218636250627816

    return


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
