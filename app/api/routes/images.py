from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse

from app.core.security import get_current_user
from app.schemas.image import PromptRequest
from app.services.image_service import (
    generate_image,
    ImageGenerationError,
    ImageGenerationTimeoutError,
)


router = APIRouter(
    prefix="/api/images",
    tags=["Images"],
)


@router.post("/generate")
async def generate_image_endpoint(
    prompt_request: PromptRequest,
    user: dict[str, Any] = Depends(get_current_user),
):

    prompt = prompt_request.prompt.strip()

    if not prompt:
        raise HTTPException(
            status_code=400,
            detail="Prompt cannot be empty.",
        )

    # This comes from the validated Supabase user.
    user_id = user["id"]

    try:
        image_bytes = generate_image(prompt)

        return StreamingResponse(
            image_bytes,
            media_type="image/png",
        )

    except ImageGenerationTimeoutError:
        raise HTTPException(
            status_code=504,
            detail="Image generation timed out.",
        )

    except ImageGenerationError as e:
        print("ImageGenerationError:", repr(e))
        raise HTTPException(
            status_code=502,
            detail="Failed to generate image using Hugging Face.",
        )