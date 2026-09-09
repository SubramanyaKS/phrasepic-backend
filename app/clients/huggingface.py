from huggingface_hub import InferenceClient

from app.core.config import settings


class HuggingFaceClient:

    def __init__(self):
        self.client = InferenceClient(
            api_key=settings.api_key,
            provider="auto",
            timeout=120,
        )

    def generate_image(self, prompt: str):
        return self.client.text_to_image(
            prompt=prompt,
            model=settings.hf_model,
        )


hf_client = HuggingFaceClient()