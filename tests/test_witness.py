# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Steven Minh Phat Duong
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("checker", ROOT / "check_witness.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

class WitnessTests(unittest.TestCase):
    def test_published(self):
        self.assertEqual(checker.verify(ROOT / "q8_k40.txt")["edges_separated"], 1024)

    def reject(self, words):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "witness.txt"
            path.write_text("\n".join(words) + "\n")
            with self.assertRaises(ValueError):
                checker.verify(path)

    def test_missing(self):
        self.reject((ROOT / "q8_k40.txt").read_text().split()[:-1])

    def test_duplicate(self):
        words = (ROOT / "q8_k40.txt").read_text().split()
        self.reject(words[:-1] + words[:1])

    def test_nonbinary(self):
        words = (ROOT / "q8_k40.txt").read_text().split()
        self.reject(["0000000x"] + words[1:])

    def test_wrong_length(self):
        words = (ROOT / "q8_k40.txt").read_text().split()
        self.reject(["000000000"] + words[1:])

    def test_wrong_valid_size_code(self):
        self.reject([format(i, "08b") for i in range(40)])

if __name__ == "__main__":
    unittest.main()
