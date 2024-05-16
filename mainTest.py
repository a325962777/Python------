import math


# function
def find_primes(n):
    primes = []
    for num in range(3, n + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


print(find_primes(50))


def sort_list(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers


print(sort_list([5, 8, 9, 10, 2, 5, 7845, 10, 100, 5803]))


def calculate_expression(expression):
    result = eval(expression)
    return result


print(calculate_expression('2*5+1'))

# testing
def test_sort_list():
    assert sort_list({1,2,3,5,40,12,5}) == {1 ,2,3,5,5,12,40}

def test_sort_list_notGood():
    assert sort_list({1,2,3,5,40,12,5}) == {1 ,40,3,5,5,12,40}

def test_sort_list_uncorrectly():
    assert sort_list({1,2,3,5,40,12,5}) == {5,2,3,1,5,12,40}

def calculate_expression():
    assert calculate_expression("45+2==") == 47

def calculate_expression_uncorrectly():
    assert calculate_expression("45+2==") == 42

def test_find_prims():
    assert find_primes(1,10) == {1,3,7}

def test_find_prims_uncorrectly():
    assert find_primes(1, 50) =={1,3,7,11,13,17}

def test_find_prims_notGood():
    assert find_primes(12,100) == {1}