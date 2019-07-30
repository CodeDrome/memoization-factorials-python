import factorialmemoization


def main():

    """
    Demonstrate FactorialMemoization class.
    """

    print("-----------------------------")
    print("| codedrome.com             |")
    print("| Memoization of Factorials |")
    print("-----------------------------\n")

    fm = factorialmemoization.FactorialMemoization(8)

    try:

        # test beyond memoized range to demonstrate exception
        for n in range(0, 10):

            print("{:d}:  ".format(n), end="")

            print("{:d}".format(fm.get(n)))

    # If we call get outside memoized range it raises ValueError
    except ValueError as e:

        print(e)


main()
