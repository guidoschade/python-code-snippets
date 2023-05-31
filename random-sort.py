import random
import time

"""
This is an implementation of the quite useless random sort function, which shuffles the array and stops when the array is sorted by chance
"""

# main
def main():
    # create list with 10 random numbers up to 100
    arr = [random.randint(1,100) for _ in range(10)]
    startTime = time.time()
    sorted = randomSort(arr)
    endTime = time.time()
    executionTime = (endTime - startTime) * 1000  # Converting to milliseconds
    print("Execution time:", executionTime, "ms")
    print(sorted)

# random sort function (do not use in production)
def randomSort(arr):
    while True:
        random.shuffle(arr)
        if sorted(arr) == arr:
            return(arr)

# start
if __name__ == "__main__":
    main()
 
