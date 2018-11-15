#!/usr/bin/python3
"""review unittest module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.review import Review


class TestReview(unittest.TestCase):
    """test cases for review class"""

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(Review.__doc__)

    def test_review(self):
        """ checks review out. whatta hottie """
        r = Review()
        self.assertEqual(type(r), Review)
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")
        r.place_id = "a"
        r.user_id = "b"
        r.text = "c"
        self.assertEqual(r.place_id, "a")
        self.assertEqual(r.user_id, "b")
        self.assertEqual(r.text, "c")

if __name__ == "__main__":
    unittest.main()
