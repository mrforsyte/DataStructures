from stack.stack import Stack
from linkedlist.linkedlist import LinkedList

import pytest

@pytest.fixture
def stack():
	return Stack()


def test_constructor():
	s = Stack()
	assert isinstance(s, Stack)
	assert len(s) == 0



def test_push(stack):
	stack.push(4)
	assert len(stack) == 1

def test_pop(stack):
	stack.push('hi')
	stack.push('error')
	assert stack.pop() == 'error'
	assert stack.pop() == 'hi'
	assert stack.pop() == None


def test_linkedlist():
	a = LinkedList()
	assert isinstance(a, LinkedList)