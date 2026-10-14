import unittest
from unittest.mock import Mock, patch

import httpx
from openai import APIConnectionError, RateLimitError

import ai_client


class AIClientTests(unittest.TestCase):
    @patch("ai_client.get_api_key", return_value=None)
    def test_live_mode_is_disabled_without_key(self, _get_api_key):
        self.assertFalse(ai_client.is_live_configured())
        with self.assertRaisesRegex(RuntimeError, "OPENAI_API_KEY"):
            ai_client.generate_summary("A study passage.")

    @patch("ai_client.get_api_key", return_value="test-key")
    @patch("ai_client.OpenAI")
    def test_summary_uses_configured_model_and_material(
        self, openai_constructor, _get_api_key
    ):
        client = Mock()
        client.responses.create.return_value.output_text = "A concise summary."
        openai_constructor.return_value = client

        result = ai_client.generate_summary("Photosynthesis uses sunlight.")

        self.assertEqual(result, "A concise summary.")
        openai_constructor.assert_called_once_with(api_key="test-key")
        client.responses.create.assert_called_once()
        request = client.responses.create.call_args.kwargs
        self.assertEqual(request["model"], ai_client.MODEL)
        self.assertEqual(request["input"], "Photosynthesis uses sunlight.")

    @patch("ai_client.get_api_key", return_value="test-key")
    @patch("ai_client.OpenAI")
    def test_follow_up_includes_study_material_and_prior_chat(
        self, openai_constructor, _get_api_key
    ):
        client = Mock()
        client.responses.create.return_value.output_text = "It captures light."
        openai_constructor.return_value = client
        conversation = [
            {"role": "user", "content": "Summarize this."},
            {"role": "assistant", "content": "Plants use sunlight."},
        ]

        result = ai_client.answer_follow_up(
            "Photosynthesis uses light energy.",
            conversation,
            "What does it capture?",
        )

        self.assertEqual(result, "It captures light.")
        input_messages = client.responses.create.call_args.kwargs["input"]
        self.assertIn("Photosynthesis uses light energy.", input_messages[0]["content"])
        self.assertEqual(input_messages[1:3], conversation)
        self.assertEqual(input_messages[-1]["content"], "What does it capture?")

    @patch("ai_client.get_api_key", return_value="test-key")
    @patch("ai_client.OpenAI")
    def test_provider_connection_errors_are_not_hidden(
        self, openai_constructor, _get_api_key
    ):
        client = Mock()
        client.responses.create.side_effect = APIConnectionError(
            request=httpx.Request("POST", "https://api.openai.com/v1/responses")
        )
        openai_constructor.return_value = client

        with self.assertRaises(APIConnectionError):
            ai_client.generate_summary("A study passage.")

    def test_exhausted_quota_explains_billing_action(self):
        request = httpx.Request("POST", "https://api.openai.com/v1/responses")
        error = RateLimitError(
            "Quota unavailable",
            response=httpx.Response(429, request=request),
            body={"error": {"message": "Quota unavailable"}},
        )
        error.code = "credit_balance_exhausted"

        message = ai_client.explain_api_error(error)

        self.assertIn("no available credits or quota", message)
        self.assertIn("Check API billing and project limits", message)
        self.assertNotIn("API key:", message)


if __name__ == "__main__":
    unittest.main()
