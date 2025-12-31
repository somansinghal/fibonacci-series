def fibonacci_series(n):
    """
    This function generates and prints the Fibonacci series up to n terms.
    The Fibonacci sequence is a series of numbers where each number is the
    sum of the two preceding ones, usually starting with 0 and 1.
    
    Args:
        n (int): The number of terms to print in the series.
    """
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive integer to generate the series.")
    elif n == 1:
        print("Fibonacci series up to 1 term:")
        print(a)
    else:
        print(f"--- Generating series for n = {n} ---")
        count = 0
        while count < n:
            print(a, end=" ")
            a, b = b, a + b
            count += 1
        print("\n" + "-"*35) 
