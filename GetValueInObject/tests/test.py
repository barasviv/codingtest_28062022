import unittest
from GetValueInObject.src import search_dictionary as dictionary


class TestGetIn(unittest.TestCase):
    def test_1(self):
        data = {"a": {"b": {"c": "d"}}}
        self.assertEqual("d", dictionary.get_in(data, "a/b/c"))

    def test_2(self):
        data = {"x": {"y": {"z": "a"}}}
        self.assertEqual("a", dictionary.get_in(data, "x/y/z"))

    def test_3(self):
        data = {"a": {"b": {"c": "d"}}}
        self.assertEqual("No value found for the given key", dictionary.get_in(data, "a/b/x"))

    def test_4(self):
        data = {"a": {"b": {"c": "d"}}}
        self.assertEqual("No value found for the given key", dictionary.get_in(data, "a/b/c/d"))

    def test_5(self):
        data = {"a": {"b": {"c": "d"}}}
        self.assertEqual(dict({'c': 'd'}), dictionary.get_in(data, "a/b"))


if __name__ == '__main__':
    unittest.main()
