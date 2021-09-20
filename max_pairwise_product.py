def max_func(arr):
    n = len(arr)
    max_digit_idx = 0
    for idx in range(0, n):
        if arr[idx] > arr[max_digit_idx]:
            max_digit_idx = idx
            
    second_max_digit_idx = 0
    for idx in range(0, n):
        if arr[idx] < arr[max_digit_idx] and arr[idx] > arr[second_max_digit_idx]:
            second_max_digit_idx = idx

            
    return arr[max_digit_idx], arr[second_max_digit_idx]

def max_pairwise_product(arr):
    max_digit, second_max_digit = max_func(arr)
    return max_digit * second_max_digit
    