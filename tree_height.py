# python3

import sys
import threading

def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here

    for node in range (n):
        h = 0
        
        while node != -1:
            h += 1
            node = parents[node]
        max_height = max(max_height, h) 
    return max_height


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    
    while True:

        #print("input from keyboard or file (I or F)")
        inp = input()

        if inp == 'I':

            n = int(input())
            parents = list(map(int, input().split()))
            break

        elif inp == 'F':
            files = "test/" + input()

            if 'a' in files:
                #print("file can not contain letter a")
                return 

            try:
                with open(files) as F:

                    n = int(F.readline())
                    parents = list(map(int, F.readline().split()))
                    break

            except FileNotFoundError:
                #print("file is not found")
                return 

    h = compute_height(n, parents)

    print(h)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
