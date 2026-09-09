# PhrasePic API

PhrasePic API is a FastAPI backend for generating images from text prompts using Hugging Face inference models. The service is protected with Supabase bearer-token authentication and exposes a health endpoint for deployment checks.

## Features

- Text-to-image generation with Hugging Face InferenceClient
- FastAPI REST API
- Supabase access-token validation for protected routes
- CORS configuration for frontend origins
- Health check endpoint
- Docker support

## Project Structure

```text
phrasepics/
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── health.py
│   │       └── images.py
│   ├── clients/
│   │   └── huggingface.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── schemas/
│   │   └── image.py
│   ├── services/
│   │   └── image_service.py
│   └── main.py
├── .env
├── Dockerfile
├── README.md
├── requirements.txt
├── run.py
```

## Requirements

- Python 3.13+
- A Hugging Face token
- A Supabase project
- A frontend that obtains a Supabase session token

## Environment Variables

Create a `.env` file in the project root with the following values:

```env
API_KEY="<your_huggingface_token>"
HF_MODEL="<your_huggingface_model>"
SUPABASE_URL="https://<project-ref>.supabase.co"
SUPABASE_PUBLISHABLE_KEY="<your_supabase_publishable_key>"
ALLOWED_ORIGINS=["http://localhost:3000","https://your-frontend-domain.com"]
```

## Install Dependencies

```bash
python -m venv env
source env/bin/activate   # Linux/macOS
# or
.env\Scripts\activate    # Windows PowerShell
pip install -r requirements.txt
```

## Run Locally

```bash
python run.py
```

The app will run on:

```text
http://localhost:8000
```

## API Endpoints

### Health

```http
GET /api/health
```

### Generate Image

```http
POST /api/images/generate
Authorization: Bearer <supabase_access_token>
Content-Type: application/json
```

Request body:

```json
{
  "prompt": "A mountain lake at sunrise"
}
```

## Frontend Usage Example

```js
const { data: { session } } = await supabase.auth.getSession();

const response = await fetch("http://localhost:8000/api/images/generate", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${access_token}`,
  },
  body: JSON.stringify({ prompt: "A mountain lake at sunrise" }),
});
```

## Security Notes

- The `/api/images/generate` route requires a valid Supabase bearer token.
- The backend validates the token through Supabase Auth before processing requests.
- Keep secrets in deployment environment variables, not in source control.
- Use HTTPS in production and restrict `ALLOWED_ORIGINS` to trusted frontend domains.

## Docker

Build the image:

```bash
docker build -t phrasepics .
```

Run the container:

```bash
docker run -p 8000:8000 --env-file .env phrasepics
```

## Notes

- The app uses the Hugging Face InferenceClient with an `api_key` and `hf_model` from the environment.
- CORS is enabled for the configured origins in `ALLOWED_ORIGINS`.
