# This will run fine, but it won't print the entire word. Can you make the output correct?


def main():
    x = "Python"
    # Here are two ways to perform a slice:
    print(x[0:3])
    s = slice(3)
    print(x[s])
    print("\n\n\n")
    # The bug is in this for loop.
    for z in range(0,len(x)):
        print(z)
        s = slice(z)
        print(x[s])


if __name__ == "__main__":
    main()
