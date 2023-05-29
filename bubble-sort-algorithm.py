
# buble sort
def bubbleSort(x):
    # getting number of elements
    n = len(x)
    # go through all elements
    for i in range(n-1):
        # and compare with all other elements
        for j in range(0, n-i-1):
            # swap elements if they are in the incorrect order
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

  
# example array
numbers = [1, 99, 38, 5, 88, 23, 42, 16, 15, 8]

# printing unsorted numbers
print("unsorted:", numbers)

# sorting here
bubbleSort(numbers)

# printing sorted numbers
print("sorted:", numbers)
