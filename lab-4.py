from itertools import islice


def lazy_evaluation(generator_func):
    def wrapper(*args, **kwargs):
        return lambda: generator_func(*args, **kwargs)
    return wrapper


@lazy_evaluation
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci_lazy = fibonacci()
for num in islice(fibonacci_lazy(), 10):
    print(num)
