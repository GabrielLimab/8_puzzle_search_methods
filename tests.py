import unittest
import main as TP1

class TestNode(unittest.TestCase):

    def test_init(self):
        node = TP1.Node(0, None, None)
        self.assertEqual(node.state, 0)
        self.assertEqual(node.parent, None)
        self.assertEqual(node.move, None)

    def test_eq(self):
        node1 = TP1.Node(0, None, None)
        node2 = TP1.Node(0, 2, 3)
        self.assertEqual(node1, node2)

class TestQueue(unittest.TestCase):

    def test_init(self):
        queue = TP1.Queue()
        self.assertEqual(queue.items, [])

    def test_put(self):
        queue = TP1.Queue()
        node = TP1.Node(1, 2, 3)
        queue.put(node)
        self.assertEqual(queue.items, [node])

    def test_get(self):
        queue = TP1.Queue()
        node = TP1.Node(1, 2, 3)
        queue.put(node)
        self.assertEqual(queue.get(), node)
        self.assertEqual(queue.items, [])

    def test_empty(self):
        queue = TP1.Queue()
        self.assertEqual(queue.empty(), True)

    def test_not_empty(self):
        queue = TP1.Queue()
        node = TP1.Node(1, 2, 3)
        queue.put(node)
        self.assertEqual(queue.empty(), False)

class TestHeap(unittest.TestCase):

    def test_init(self):
        heap = TP1.Heap('U')
        self.assertEqual(heap.items, [])
        self.assertEqual(heap.algorithm, 'U')

    def test_heappush(self):
        heap = TP1.Heap('U')
        node = TP1.Node(1, 2, 3)
        heap.heappush(node)
        self.assertEqual(heap.items, [node])

    def test_heappop(self):
        heap = TP1.Heap('U')
        node = TP1.Node(1, 2, 3)
        heap.heappush(node)
        self.assertEqual(heap.heappop(), node)
        self.assertEqual(heap.items, [])

    def test_empty(self):
        heap = TP1.Heap('U')
        self.assertEqual(heap.empty(), True)

    def test_not_empty(self):
        heap = TP1.Heap('U')
        node = TP1.Node(1, 2, 3)
        heap.heappush(node)
        self.assertEqual(heap.empty(), False)

if __name__ == '__main__':
    unittest.main()