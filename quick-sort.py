import random
import time

# main
def main():
    # create list with 1000 random numbers up to 1 million
    arr = [random.randint(1,1_000_000) for _ in range(1_000)]
    startTime = time.time()
    sorted = quickSort(arr)
    endTime = time.time()
    executionTime = (endTime - startTime) * 1000  # Converting to milliseconds
    print("Execution time:", executionTime, "ms")
    print(sorted)

# quicksort function (recursive)
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
    
# start
if __name__ == "__main__":
    main()
 
