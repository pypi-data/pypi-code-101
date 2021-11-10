import timeit
from random import randint
from rand import randlist

# define a function that receives an array and two indexes,
# and returns the array with the elements in those two indexes swapped
def eswap(arr, a, b):
    c = arr[a]
    arr[a] = arr[b]
    arr[b] = c
    return arr

# define a function that receives an array and an optional starting point
# and returns the index of the lowest value from that starting point
# to the end
def leastof(arr, start=0):
    least = start
    i = start
    while i < len(arr):
        if arr[i] < arr[least]:
            least = i
        i += 1
    return least

def greatestof(arr, start=0):
    greatest = start
    i = start
    while i < len(arr):
        if arr[i] > arr[greatest]:
            greatest = i
        i += 1
    return greatest

# define a function that recieves an array, an optional setting
# and returns the array sorted using selection sort
def selection_sort(arr, l2g=True):
    if l2g:
        i = 0
        while i < len(arr):
            arr = sort.eswap(arr, i, sort.leastof(arr, i))
            i += 1
    elif not l2g:
        i = 0
        while i < len(arr):
            arr = sort.eswap(arr, i, sort.greatestof(arr, i))
            i += 1
    return arr
def bubbler(arr, a, b):
    pass
def bubble(arr, l2g=True):
    if l2g:
        cpass = 1
        sorted = False
        z = 0
        while (z < len(arr) - 1) and not sorted:
            swap = False
            for u in range( len(arr) - cpass):
                v = u + 1
                if arr[u] > arr[v]:
                    swap = True
                    arr = sort.eswap(arr, u, v)
            if not swap:
                sorted = True
            cpass += 1
            z += 1
    elif not l2g:
        cpass = 1
        sorted = False
        z = 0
        while (z < len(arr) - 1) and not sorted:
            swap = False
            for u in range( len(arr) - cpass):
                v = u + 1
                if arr[u] < arr[v]:
                    swap = True
                    arr = sort.eswap(arr, u, v)
            if not swap:
                sorted = True
            cpass += 1
            z += 1
    return arr

                

test = randlist(20, 1, 100)
print("SELECTION SORT")
print("unsorted: ", test)
print("sorted: ", sort.selection_sort(test))
t = timeit.timeit(lambda: "sort.selection_sort(test)")
print(t)
print()
print("BUBBLE SORT")
anothertest = randlist(20, 1, 100)
print("unsorted: ", anothertest)
print("sorted: ", sort.bubble(anothertest))
print(timeit.timeit(lambda: "sort.bubble(anothertest)"))