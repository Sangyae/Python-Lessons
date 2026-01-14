# always use generator for large number of datasets
def my_generator(x):
    for i in range(x):
        yield i

even = {num for num in my_generator(10) if num % 2 == 0}
print(even)

# fibonancci numbers

def fibonacci():
    a, b = 0,1
    while True:
        yield a
        a, b = b, a +b
    
fib = fibonacci()
for _ in range(10):
    print(next(fib))