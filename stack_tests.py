import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
# from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push(0)
        stack.push('string')
        self.assertEqual(stack.peek(), 'string')
        self.assertEqual(stack.size(), 2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        stack.push(5)
        stack.push(10.0)
        self.assertTrue(stack.is_full())
        with self.assertRaises(IndexError):
            stack.push(14)
        self.assertFalse(stack.is_empty())
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertFalse(stack.is_full())
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.pop()
        stack.push(None)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.size(),1)


if __name__ == '__main__':
    unittest.main()
