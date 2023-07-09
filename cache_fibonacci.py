
# Part 1

## Basic Fibonnaci Function for Single Integer Input
def fibonacci_output(n):
    if n < 2:
        return n
    n = fibonacci_output(n - 1) + fibonacci_output(n - 2)
    return n

    # This approach has no memory
    # Recursively uses the function call twice

## Create a Caching Function to Give Fibonacci Memory with Recursion
def cache(fibonacci_output):
    cache = dict()
    def cache_fib(*args):
        num = args[0]
        if num in cache: 
            return cache[num]
        solution = fibonacci_output(*num)
        cache[num] = solution
        return solution
    return cache_fib

    # This approach creates a dictionary of tuples (immutable lists) called *args
    # Each arg stores one value for fibonacci sequence
    # If num (first element of the cache) is within the cache, return that value
    # Feed that number into our fibonacci_output function, save that solution
    # Replace the cache at that index with the solution, then return the whole cache


#-----#



# Part 2

## Create a Fibonacci Sequence in an Empty List, Populate List
def fibonacci_list(fib_len):
    if fib_len <= 0:
        return[0]
    fib_seq = [0, 1]
    while (len(fib_seq) <= fib_len):
        next_end_of_seq = fib_seq[len(fib_seq) - 1] + fib_seq[len(fib_seq) - 2]
        fib_seq.append(next_end_of_seq)
    return fib_seq

    # This approach uses the List as a method for memory storage 
    # Since this data structure can store values, we don't need recursion



#-----#



# Part 3

## Main Function to Run Python File (e.g. Python3 cache_fibonacci.py in Term.)
def main():
    print(fibonacci_output(5))
    print(cache(5))
    print(fibonacci_list(5))

if __name__ == "__main__":
    main()