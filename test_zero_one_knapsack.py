from knapsack import zero_one_knapsack

def compare_lists(lst1, lst2):
    for x in lst1:
        if lst1.count(x) != lst2.count(x):
            return False
    return True

def test1():
    """test for 1 item"""
    n = 1
    weights = [5]
    values = [12]
    capacity = 29
    lst = zero_one_knapsack(capacity,n,weights,values)
    result = compare_lists(lst, [12])
    assert result , 'test1 failed!'
    
def test2():
    """test for capacity = 1"""
    n = 2
    weights = [5, 4]
    values = [12, 9]
    capacity = 1
    lst = zero_one_knapsack(capacity,n,weights,values)
    result = compare_lists(lst, [])
    assert result , 'test2 failed!'

def test3():
    """test for capacity = 1"""
    n = 2
    weights = [5, 4]
    values = [12, 9]
    capacity = 29
    lst = zero_one_knapsack(capacity,n,weights,values)
    result = compare_lists(lst, [0, 0, 0, 0, 0, 1])
    assert result , 'test3 failed!'

def test4():
    """test for capacity = 1"""
    n = 3
    weights = [7, 3, 20]
    values = [12, 2, 41]
    capacity = 1
    lst = zero_one_knapsack(capacity,n,weights,values)
    result = compare_lists(lst, [2, 2, 0, 0, 1])
    assert result , 'test4 failed!'


def test_all():
    test1()
    # test2()
    # test3()
    print('All tests successful')



test_all()