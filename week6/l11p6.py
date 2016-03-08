import unittest

class Queue(object):
    
    def __init__(self):
        self.vals = []
        
    def insert(self, e):
        self.vals.append(e)
    
    def remove(self):
        try:
            return self.vals.pop(0)
        except:
            raise ValueError
            





"""
class TestLesson11Problem6(unittest.TestCase):
        
    def test_remove_method_works(self):
        self.queue = Queue()
        self.queue.insert(5)
        self.queue.insert(6)
        self.assertEqual(queue.remove(), 5)
        queue.insert(7)
        self.assertEqual(queue.remove(), 6)
        self.assertEqual(queue.remove(), 7)
        self.assertRaises(ValueError, queue.remove())

if __name__ == '__main__':
    unittest.main()
"""