# python3

import sys
import threading

def compute_height(n, parents):

    h = [-1] * n
    max_height = 0

    def height(node):
        if h[node] != -1:
            return h[node]

        if parents[node] == -1:
            h[node] = 1
            return 1

        h1 = height(parents[node]) + 1
        h[node] = h1
        return h1

    for node in range(n):
        h1 = height(node)
        max_height = max(max_height, h1)

    return max_height


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    
    #print("input from keyboard or file (I or F)")
    while True:

        #print("input from keyboard or file (I or F)")
        try:
            inp = input()
        except EOFError:
            return

        if 'I' in inp:

            n = int(input())
            parents = list(map(int, input().split()))
            
            print(compute_height(n, parents))
            break

        if 'F' in inp:
            files = "test/" + input()

            if 'a' in files:
                #print("file can not contain letter a")
                return 

            try:
                with open(files) as F:

                    n = int(F.readline())
                    parents = list(map(int, F.readline().split()))
                    
                    print(compute_height(n, parents))
                    break

            except FileNotFoundError:
                print("file is not found")
                return 

    #print(compute_height(n, parents))



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
