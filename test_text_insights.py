import unittest

from text_insights import extract_frequent_terms


class FrequentTermsTests(unittest.TestCase):
    def test_returns_three_most_frequent_non_common_words(self):
        text = (
            "Photosynthesis supports plants. Plants use photosynthesis. "
            "Photosynthesis stores energy in plants."
        )

        self.assertEqual(
            extract_frequent_terms(text),
            [("photosynthesis", 3), ("plants", 3), ("supports", 1)],
        )

    def test_ignores_common_words_and_counts_case_insensitively(self):
        self.assertEqual(
            extract_frequent_terms("The CELL cell, and CELL!"),
            [("cell", 3)],
        )

    def test_returns_no_terms_for_empty_or_common_word_only_text(self):
        self.assertEqual(extract_frequent_terms(""), [])
        self.assertEqual(extract_frequent_terms("the and for"), [])


if __name__ == "__main__":
    unittest.main()
