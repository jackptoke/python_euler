# Python program for implementation of heap Sort 
  
def printArray(arr):
    n = len(arr) 
    for i in range(n): 
        print ("%d " %arr[i], end = ''), 
    print()

# To heapify subtree rooted at index i. 
# n is size of heap 

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 

    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
    
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
    
    # Step 1: Build a maxheap.
    # To reduce unnecessary round we are starting at n/2 
    for i in range(int(n/2)-1, -1, -1): 
        heapify(arr, n, i) 
  
    # Step 2: One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 

        # printArray(arr)

        heapify(arr, i, 0) 
  

# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7, 8, 2, 4, 10, 15, 1] 
n = len(arr) 
heapSort(arr) 
# This code is contributed by Mohit Kumra