import os
import unittest
from unittest.mock import patch

from streamlit.testing.v1 import AppTest


class StudyChatAppTests(unittest.TestCase):
    def test_configured_key_is_not_presented_as_proof_of_live_access(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
            app = AppTest.from_file("app.py").run()
            app.text_area[0].set_value("Plants use sunlight to make food.")
            app.button[-1].click().run()

            self.assertEqual(len(app.exception), 0)
            self.assertTrue(
                any(
                    "Demo mode is active" in item.value
                    and "No AI request is sent" in item.value
                    and "counts frequent terms locally" in item.value
                    for item in app.info
                )
            )
            self.assertFalse(app.toggle[0].value)
            self.assertTrue(
                any(item.label.lower() == "plants" for item in app.metric)
            )
            self.assertTrue(
                any("No AI response was generated" in item.value for item in app.markdown)
            )

    def test_demo_mode_exposes_study_actions_without_claiming_analysis(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": ""}):
            app = AppTest.from_file("app.py").run()

            self.assertEqual(len(app.exception), 0)
            self.assertTrue(any(button.label == "Geometry" for button in app.button))
            self.assertTrue(any("Demo mode is active" in item.value for item in app.info))

            app.text_area[0].set_value("Plants use sunlight to make food.")
            app.button[-1].click().run()

            self.assertTrue(
                any(item.label.lower() == "plants" for item in app.metric)
            )
            labels = [button.label for button in app.button]
            self.assertIn("Explain more", labels)
            self.assertIn("Make flashcards", labels)
            self.assertIn("Start a short quiz", labels)
            self.assertTrue(
                any("No AI response was generated" in item.value for item in app.markdown)
            )

            app.button[2].click().run()

            self.assertEqual(len(app.exception), 0)
            self.assertTrue(
                any("No AI response was generated" in item.value for item in app.markdown)
            )

    def test_empty_submission_shows_reminder(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": ""}):
            app = AppTest.from_file("app.py").run()
            app.button[-1].click().run()

            self.assertTrue(
                any("Please paste some study text" in item.value for item in app.warning)
            )


if __name__ == "__main__":
    unittest.main()
