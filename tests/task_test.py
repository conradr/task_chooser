import unittest
from src.task import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("wash dishes", ["cook dinner", "wash clothes"])
        self.task2 = Task("cook dinner", ["clean windows", "ironing"])
        self.task3 = Task("clean windows", ["wash dishes", "ironing"])
        self.task4 = Task("ironing", ["wash dishes", "wash clothes"])
        self.task5 = Task("wash clothes", ["cook dinner", "clean windows"])

    def test_task_has_description(self):
        self.assertEqual("cook dinner", self.task2.description)
    
    def test_task_has_preferred_list(self):
        self.assertEqual(["cook dinner", "wash clothes"], self.task1.preferred_list)
    
    def test_task_not_duplicate(self):
        result = self.tasks_not_duplicate(self.task1, self.task1)
        self.assertEqual("tasks are the same", result)
