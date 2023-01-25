import os
import sys
import unittest
import pandas as pd

class TestCombiner(unittest.TestCase):
    def test_no_input(self):
        self.assertNotEqual(os.path.getsize("combined.csv"), 0, "No input files")

    def test_missing_filename_column(self):
        data = pd.read_csv("./fixtures/accessories.csv", index_col=False)
        output = pd.read_csv("combined.csv", index_col=False)
        self.assertNotEqual(len(data.columns.values), len(output.columns.values))


if __name__ == '__main__':
    unittest.main()