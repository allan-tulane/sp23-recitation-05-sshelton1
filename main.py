import random, time
import tabulate


def qsort(a, pivot_fn):
  ## TO DO
  if len(a) < 2:
    return a
  else:
    pivot = pivot_fn(a)

    left = []
    right = []
    middle = [pivot]
    mid = 0

    for i in a:
      if i < pivot:
        left.append(i)
      if i == pivot:
        mid += 1
        if mid == 1:
          continue
        else:
          left.append(i)
      if i > pivot:
        right.append(i)
    if not left:
      return middle + qsort(right, pivot_fn)
    elif not right:
      return qsort(left, pivot_fn) + middle
    else:
      return qsort(left, pivot_fn) + middle + qsort(right,pivot_fn)
    
def time_search(sort_fn, mylist):
  """
  Return the number of milliseconds to run this
  sort function on this list.

  Note 1: `sort_fn` parameter is a function.
  Note 2: time.time() returns the current time in seconds. 
  You'll have to multiple by 1000 to get milliseconds.

  Params:
    sort_fn.....the search function
    mylist......the list to search
    key.........the search key 

  Returns:
    the number of milliseconds it takes to run this
    search function on this input.
  """
  start = time.time()
  sort_fn(mylist)
  return (time.time() - start) * 1000
  ###

def ssort(L):
    for i in range(len(L)):
        #print(L)
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
  """
  Compare the running time of different sorting algorithms.

  Returns:
    A list of tuples of the form
    (n, linear_search_time, binary_search_time)
    indicating the number of milliseconds it takes
    for each method to run on each value of n
  """
  ### TODO - sorting algorithms for comparison
  qsort_fixed_pivot = lambda a: qsort(a, lambda p: p[0])
  qsort_random_pivot = lambda a: qsort(a, lambda p: random.choice(p))
  tim_sort = 0
  result = []
  for size in sizes:
      # create list in ascending order
      mylist = list(range(size))
      # shuffles list if needed
      random.shuffle(mylist)
      result.append([
          len(mylist),
          time_search(qsort_fixed_pivot, mylist),
          time_search(qsort_random_pivot, mylist),
      ])
  return result
  
def compare_qsort(sizes=[100, 200, 500, 1000, 2000, 3000, 5000, 7500, 9000, 10000]):
  qsort_random_pivot = lambda a: qsort(a, lambda p: random.choice(p))
  tim_sort = 0
  result = []
  for size in sizes:
      # create list in ascending order
      mylist = list(range(size))
      # shuffles list if needed
      random.shuffle(mylist)
      result.append([
          len(mylist),
          time_search(ssort, mylist),
          time_search(qsort_random_pivot, mylist),
      ])
  return result

def compare_tsort(sizes=[100, 200, 500, 1000, 2000, 3000, 5000, 7500, 9000, 10000]):
  qsort_random_pivot = lambda a: qsort(a, lambda p: random.choice(p))
  tim_sort = 0
  result = []
  for size in sizes:
      # create list in ascending order
      mylist = list(range(size))
      # shuffles list if needed
      random.shuffle(mylist)
      result.append([
          len(mylist),
          time_search(sorted, mylist),
          time_search(qsort_random_pivot, mylist),
      ])
  return result
  
def print_results(results):
  """ change as needed for comparisons """
  print(tabulate.tabulate(results,
                          headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                          floatfmt=".3f",
                          tablefmt="github"))
def print_qresults(results):
  """ change as needed for comparisons """
  print(tabulate.tabulate(results,
                          headers=['n', 'ssort', 'qsort-random-pivot'],
                          floatfmt=".3f",
                          tablefmt="github"))
def print_tresults(results):
  """ change as needed for comparisons """
  print(tabulate.tabulate(results,
                          headers=['n', 'timsort', 'qsort-random-pivot'],
                          floatfmt=".3f",
                          tablefmt="github"))

def test_print():
  print_results(compare_sort())

def test_qprint():
  print_qresults(compare_qsort())

def test_tprint():
  print_tresults(compare_tsort())

#random.seed()
#test_print()
#test_qprint()
test_tprint()
#print(compare_sort())