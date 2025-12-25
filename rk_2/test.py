import unittest
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "rk_1"))
from main import first_task, second_task, third_task, Directory, Document

class TestFileCatalogue(unittest.TestCase):
    def test_first_task(self):
        result = first_task(output=False)
        self.assertEqual(len(result["lab1"]), 2)
        self.assertEqual(result["lab0"][0].id, 1)

    def test_second_task(self):
        result = second_task(output=False)
        self.assertEqual(result[2][1], 2)
        self.assertEqual(result[3][1], 1)
        self.assertEqual(result[4][1], 0)

    def test_third_task(self):
        result = third_task(output=False)
        self.assertEqual(result["pcpl"][2].name, "lab1OOP.py")
        self.assertEqual(result["university docx"][0].size, 350)
        self.assertEqual(result["lab0"][0].id, 1)
        self.assertEqual(result["lab1"][0].size, 3)

if __name__ == "__main__":
    unittest.main()
