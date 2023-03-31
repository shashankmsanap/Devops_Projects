import unittest
from todo import ToDo

class TestToDo(unittest.TestCase):
    def test_add_task(self):
        todo = ToDo()
        todo.add_task('Task 1')
        self.assertEqual(todo.get_tasks(), ['Task 1'])

    def test_remove_task(self):
        todo = ToDo()
        todo.add_task('Task 1')
        todo.add_task('Task 2')
        todo.remove_task('Task 1')
        self.assertEqual(todo.get_tasks(), ['Task 2'])

if __name__ == '__main__':
    unittest.main()
