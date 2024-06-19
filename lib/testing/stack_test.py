import pytest
from lib.Stack import Stack

class TestStack:
    def test_init(self):
        '''Initialize Stack with list'''
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        for index in range(len(expected)):
            assert stk.items[index] == expected[index]

    def test_push(self):
        '''Push 0 to stack'''
        stk = Stack([1, 2, 3, 4, 5])
        stk.push(0)
        expected = [1, 2, 3, 4, 5, 0]
        for index in range(len(expected)):
            assert stk.items[index] == expected[index]

    def test_pop(self):
        '''Pop 1 off the stack'''
        stk = Stack([1, 2, 3, 4, 5])
        stk.pop()
        expected = [1, 2, 3, 4]
        for index in range(len(expected)):
            assert stk.items[index] == expected[index]

    def test_size(self):
        '''Test Stack size() method'''
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        assert stk.size() == len(expected)

    def test_empty(self):
        '''Test Stack empty() method'''
        stk = Stack()
        assert stk.isEmpty()
        assert stk.size() == 0
        assert stk.pop() is None
        stk.push(1)
        assert not stk.isEmpty()
        assert stk.size() == 1
        assert stk.pop() == 1

    def test_full(self):
        '''Test Stack full() method'''
        stk = Stack([1], 1)
        
        # Check initial state
        assert stk.full()
        assert stk.size() == 1
        assert stk.pop() == 1
        
        # Push an element to fill the stack
        stk.push(1)
        assert stk.size() == 1
        
        # Attempt to push another element, which should raise an Exception
        with pytest.raises(Exception) as excinfo:
            stk.push(2)
        
        # Check the exception message if needed
        assert str(excinfo.value) == "Stack is full"
    def test_search(self):
        '''Test Stack search() method. How far is the element in the stack?'''
        stk = Stack([5, 6, 7, 8, 9, 10])
        assert stk.search(5) == 5
        assert stk.search(6) == 4
        assert stk.search(7) == 3
        assert stk.search(8) == 2
        assert stk.search(9) == 1
        assert stk.search(10) == 0

        # Case with target not in Stack
        assert stk.search(15) == -1

    # Bonus methods tests (uncomment to test)
    # def test_limit_init(self):
    #     '''Test Stack __init__() method with limit'''
    #     stk = Stack(limit=3)
    #     assert stk.limit == 3

    # def test_push_limit(self):
    #     '''Test Stack push() method with limit'''
    #     stk = Stack([1, 2], 2)
    #     assert stk.push(3) is True
    #     assert stk.push(4) is False
    #     assert stk.size() == 2
    #     assert stk.pop() == 3
    #     assert stk.size() == 1

    # def test_size_limit(self):
    #     '''Test Stack size() method with limit'''
    #     stk = Stack([1, 2], 2)
    #     assert stk.size() == 2
    #     assert stk.push(3) is True
    #     assert stk.size() == 3

    # def test_empty_limit(self):
    #     '''Test Stack empty() method with limit'''
    #     stk = Stack(limit=2)
    #     assert stk.isEmpty()
    #     assert stk.push(1) is True
    #     assert not stk.isEmpty()

    # def test_full_limit(self):
    #     '''Test Stack full() method with limit'''
    #     stk = Stack([1], 1)
    #     assert stk.full()
    #     assert stk.pop() == 1
    #     assert stk.push(1) is True
    #     assert stk.push(2) is False
    #     assert stk.full()

    # def test_search_limit(self):
    #     '''Test Stack search() method with limit'''
    #     stk = Stack([5, 6, 7], 3)
    #     assert stk.search(5) == 2
    #     assert stk.search(6) == 1
    #     assert stk.search(7) == 0
    #     assert stk.search(8) == -1

