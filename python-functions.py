# number 1

def sum_to(n):
    sum = 0
    for num in range(1, n + 1):
        sum += num
    return sum

print(sum_to(6))

# number 2
    
def largest(nums):
  largest = 0
  for n in nums:
    if n > largest:
      largest = n
  return largest

print(largest([1, 2, 3, 4, 0]))

# number 3

def occurrences(s1, s2):
    return s1.count(s2)

print(occurrences('fleep floop', 'e'))

# number 4

def product(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

print(product(-1, 4))
        