from io import BytesIO

from huggingface_hub import InferenceTimeoutError

from app.clients.huggingface import hf_client


class ImageGenerationError(Exception):
    pass


class ImageGenerationTimeoutError(Exception):
    pass


def generate_image(prompt: str) -> BytesIO:

    try:
        image = hf_client.generate_image(prompt)

        image_bytes = BytesIO()

        image.save(
            image_bytes,
            format="PNG"
        )

        image_bytes.seek(0)

        return image_bytes

    except InferenceTimeoutError as e:
        raise ImageGenerationTimeoutError(
            "Image generation timed out."
        ) from e

    except Exception as e:
        raise ImageGenerationError(
            "Failed to generate image."
        ) from e