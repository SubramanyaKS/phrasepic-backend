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
        try:
            result = self.client.text_to_image(
                prompt=prompt,
                model=settings.hf_model,
            )
            print("Image generated successfully")
            return result
        except Exception as e:
            print("Hugging Face error:", repr(e))
            raise
        
hf_client=HuggingFaceClient