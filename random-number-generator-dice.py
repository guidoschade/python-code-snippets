import random

# main function
def main():
    random.seed()
    while True:
        input("Press enter to roll, Control-C to exit:")
        print("Rolled a ", end="")
        print(random.choice(range(6))+1)

# only start when called directly
if __name__ == "__main__":
    main()