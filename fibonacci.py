import timeit
def fib_recur(n):
    if n <= 1:
        return n
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)

# fib_arr = []
# for i in range(11):
#     fib_arr.append(fib_recur(i))
    
# print(fib_arr)

def fib_loop(n):
    if n <= 1:
        return n
    array = list(range(n + 1))
    array[0] = 0
    array[1] = 1
    for i in array[2:]:
        array[i] = array[i - 1] + array[i - 2]
        
    return array[n]

# fib_arr = []
# for i in range(11):
#     fib_arr.append(fib_loop(i))
    
# print(fib_arr)
# print(fib_recur(100))
print(fib_loop(100))