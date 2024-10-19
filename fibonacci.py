def fibonacci(n):
    # Initialize the first two terms of the series
    a, b = 0, 1
    fib_series = []

    # Generate the Fibonacci sequence
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b  # Update the values for next iteration

    return fib_series


# Input: number of terms
num_terms = int(input("Enter the number of terms: "))

# Output: Fibonacci series
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:", fibonacci(num_terms))
