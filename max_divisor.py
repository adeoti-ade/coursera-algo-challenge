def max_divisor_loop(a, b):
    """
    """
    if a == 0 or b == 0:
        return 0
    best = 0
    for i in range(1, a + b):
        if (a % i) == 0 and  (b % i) == 0:
            best = i
    return best

print(max_divisor_loop(4, 8))

def max_divisor_recur(a, b):
    if b == 0:
        return a
    remainder = 0
    if a % b > 0:
        remainder = a % b
        
    return max_divisor_recur(b, remainder)
print(max_divisor_recur(1653264, 3918848))