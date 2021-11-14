__author__ = "Abenezer Walelign."

class AwSort:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap)-1) 

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return None 
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1,len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            return None
        return max
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return None 
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        largest = index 
        left = index *2 
        right = index *2 +1 
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left 
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest) 

    def __repr__(self):
        return '<The MaxHeap algo implementation>'



class SortingAlgo:

    def selectionSort(self,input_list):
        '''	
        Selection sort works by selecting the smallest element from an unsorted array and moving it to the front
        Now, the first item is sorted, and the rest of the array is unsorted so We'll look through all the unsorted items, 
        find the smallest one, and swap it with the first unsorted item. We will repeat this step untill the array is fully sorted. Holla know your array is sorted
        
        ##### Time Complexity: 
                Best : Ω(n^2)
                Avrage : Θ(n^2)
                worst : o(n^2)
            
        ##### Space Complexity:
            worst : Ω(1)

        '''
        for i in range(len(input_list)):
            i_min = i
            for j in range(i+1,len(input_list)):
                if input_list[j] < input_list[i_min]:
                    i_min = j

            tmp = i
            input_list[tmp],input_list[i_min] = input_list[i_min],input_list[tmp]
        return input_list   


    def insertionSort(self,input_list):
        '''
        #### Insertion sort works by inserting elements from an unsorted list into a sorted subsection of the list, one item at a time.

        ##### Time Complexity: 
                Best : Ω(n)
                Avrage : Θ(n^2)
                worst : o(n^2)
            
        ##### Space Complexity:
            worst : Ω(1)
        '''
        for i in range(1,len(input_list)):
            value = input_list[i]
            hole = i 
            while hole > 0 and input_list[hole -1] > value:
                input_list[hole] = input_list[hole-1]
                hole = hole -1

            input_list[hole] = value

        return input_list
        
    def __merge(self,array1, array2):
        combined = []
        i = 0
        j = 0
        while i < len(array1) and j < len(array2):
            if array1[i] < array2[j]:
                combined.append(array1[i])
                i += 1
            else:
                combined.append(array2[j])
                j += 1
                
        while i < len(array1):
            combined.append(array1[i])
            i += 1

        while j < len(array2):
            combined.append(array2[j])
            j += 1

        return combined


    
    def mergeSort(self,input_list):
        '''
        Merge sort is a recursive algorithm that works like this:-
            1) split the input in half\n
            2) sort each half by recursively using this same process\n
            3) merge the sorted halves back together\n

        #### Note: Like all recursive algorithms, merge sort needs a base case. Here, the base case is an input list with one item Cause we all know that a one-element list is already sorted.
        	
        ##### Time Complexity: 
                Best : Ω(n log(n))
                Avrage : Θ(n log(n))
                worst : o(n log(n))
            
        ##### Space Complexity:
            worst : Ω(n)
        '''

        if len(input_list) == 1:
            return input_list
        mid = int(len(input_list)/2)
        left = input_list[:mid]
        right = input_list[mid:]
        return self.__merge(self.mergeSort(left), self.mergeSort(right))

    
    def bubbleSort(self,input_list):
        '''
        A bubble sort algorithm goes through a list of data a number of times, comparing two items that are side by side to see which is out of order. 
        It will keep going through the list of data until all the data is sorted into order. 
        Each time the algorithm goes through the list it is called a ‘pass’
        '''
        for i in range(len(input_list)):
            for j in range(len(input_list)-i-1):
                if input_list[j] > input_list[j+1]:
                    input_list[j],input_list[j+1] = input_list[j+1],input_list[j]

        return input_list

    def swap(self,my_list, index1, index2):
        temp = my_list[index1]
        my_list[index1] = my_list[index2]
        my_list[index2] = temp


    def pivot(self,my_list, pivot_index, end_index):
        swap_index = pivot_index

        for i in range(pivot_index+1, end_index+1):
            if my_list[i] < my_list[pivot_index]:
                swap_index += 1
                self.swap(my_list, swap_index, i)
        self.swap(my_list, pivot_index, swap_index)
        return swap_index


    def quick_sort_helper(self,my_list, left, right):
        if left < right:
            pivot_index = self.pivot(my_list, left, right)
            self.quick_sort_helper(my_list, left, pivot_index-1)  
            self.quick_sort_helper(my_list, pivot_index+1, right)       
        return my_list

    def quickSort(self,my_list):
        '''
        #### Quick Sort works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, 
        according to whether they are less than or greater than the pivot

        ##### Time Complexity: 
                Best : Ω(n log(n))
                Avrage : Θ(n log(n))
                worst : o(n^2)
            
        ##### Space Complexity:
            worst : Ω(log(n))
        '''
        return self.quick_sort_helper(my_list, 0, len(my_list)-1)


    def __is_sorted(self,arr): 
        n = len(arr) 
        for i in range(0, n-1): 
            if (arr[i] > arr[i+1] ): 
                return False
        return True

    def __shuffle(self,arr): 
        import random
        n = len(arr) 
        for i in range (0,n): 
            r = random.randint(0,n-1) 
            arr[i], arr[r] = arr[r], arr[i]
    
    def bogoSort(self,input_list): 
        '''
        The Bogosort is considered one of the worst sorting algorithms. 
        It works by creating random arrangements of given values and randomly moving them until they are sorted. 
        It is not effective for any form of sorting.

        ##### Time Complexity: 
                Best : Ω(n)
                Avrage : Θ((N+1)!)
                worst : o((N+1)!)

            
        ##### Space Complexity:
            worst : Ω(1)

        Cheak out this link for indepth info on bogoSort--> https://www.youtube.com/watch?v=RGuJga2Gl_k 
        '''

        n = len(input_list) 
        while (self.__is_sorted(input_list)== False): 
            self.__shuffle(input_list) 
        return input_list

    def awSort(self,inputList, reverse=False):
        '''
        awSort is a sorting algorithm that is written by me.

        Tha algorithms sorts an array by appending the largest value that it gets from the Max heap to the queue.

        Ex: lets say we have this --> [1,3,4,5] kind of array

        1) Passing this list to max heap will give us 5 as our first element

        so we will peak 5 and append it to our queue like this --> queue.append_left(5) so know our list is 
        
        [1,3,4] and our queue == [5] if we repeat this step again

        max_value will be equal to 4  so queue.append_left(4) will give us a queue with value of [4,5] and  list with a value of [1,3] so if we repeat this step once again

        max_value will be 3 so  queue.append_left(3) will give us a queue with value of [3,4,5] and a list with a value of [1]. Repeating this step for once will give us a sorted list that looks like this [1,3,4,5]

        ###### So by using ( MaxHeap and Queue ) and  doing this steps repeatedly the algorithm will sort the unsorted array. 

        '''
        from collections import deque
        heap = AwSort(inputList)
        queue = deque()
        if reverse:
            for i in range(len(heap.heap)-1):
                item = heap.pop()
                queue.append(item)
                
        else:
            for i in range(len(heap.heap)-1):
                item = heap.pop()
                queue.appendleft(item)
        return list(queue)


    def __binary_search(self,arr, val, start, end):
        if start == end:
            if arr[start] > val:
                return start
            else:
                return start+1

        if start > end:
            return start
    
        mid = (start+end)//2
        if arr[mid] < val:
            return self.__binary_search(arr, val, mid+1, end)
        elif arr[mid] > val:
            return self.__binary_search(arr, val, start, mid-1)
        else:
            return mid
  
    def binaryInsertionSort(self,arr):
        '''
        Steps of Binary Insertion Sort are similar to Insertion Sort. 
        But to insert a new element into a sorted subarray, 
        we use binary search algorithm to find the suitable position for it, 
        instead of iterating all elements backward from i to 0 position

        ##### Time Complexity: 
                worst : o(n^2)

            
        ##### Space Complexity:
            worst : 0(1)
        '''
        
        for i in range(1, len(arr)):
            val = arr[i]
            j = self.__binary_search(arr, val, 0, i-1)
            arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
        return arr
