def main():
    x = int(input("What is X? "))
    print("X squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()