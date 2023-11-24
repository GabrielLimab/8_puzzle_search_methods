import unittest
import main as TP1

class TestNode(unittest.TestCase):

    def test_init(self):
        node = Node(0, None, None)
        self.assertEqual(node.state, 0)
        self.assertEqual(node.parent, None)
        self.assertEqual(node.move, None)

    def test_eq(self):
        node1 = Node(0, None, None)
        node2 = Node(0, 2, 3)
        self.assertEqual(node1, node2)

class TestQueue(unittest.TestCase):

    def test_init(self):
        queue = Queue()
        self.assertEqual(queue.items, [])

    def test_put(self):
        queue = Queue()
        node = Node(1, 2, 3)
        queue.put(node)
        self.assertEqual(queue.items, [node])

    def test_get(self):
        queue = Queue()
        node = Node(1, 2, 3)
        queue.put(node)
        self.assertEqual(queue.get(), node)
        self.assertEqual(queue.items, [])

    def test_empty(self):
        queue = Queue()
        self.assertEqual(queue.empty(), True)

    def test_not_empty(self):
        queue = Queue()
        node = Node(1, 2, 3)
        queue.put(node)
        self.assertEqual(queue.empty(), False)

class TestHeap(unittest.TestCase):

    def test_init(self):
        heap = Heap('U')
        self.assertEqual(heap.items, [])
        self.assertEqual(heap.algorithm, 'U')

    def test_heappush(self):
        heap = Heap('U')
        node = Node(1, 2, 3)
        heap.heappush(node)
        self.assertEqual(heap.items, [node])

    def test_heappop(self):
        heap = Heap('U')
        node = Node(1, 2, 3)
        heap.heappush(node)
        self.assertEqual(heap.heappop(), node)
        self.assertEqual(heap.items, [])

    def test_empty(self):
        heap = Heap('U')
        self.assertEqual(heap.empty(), True)

    def test_not_empty(self):
        heap = Heap('U')
        node = Node(1, 2, 3)
        heap.heappush(node)
        self.assertEqual(heap.empty(), False)

if __name__ == '__main__':
    unittest.main()