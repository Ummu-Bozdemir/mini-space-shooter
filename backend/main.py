
import os
import json
from typing import Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")


@app.get("/")
def home():
    return {"message": "Mini Space Shooter backend is running!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/level-info")
def level_info():
    """Basit seviye metadata endpoint'i (ödev için)."""
    return {
        "max_level": 8,
        "has_boss_levels": [4, 8],
        "message": "Level information API is working!"
    }


@app.post("/ask")
async def ask_llm(payload: dict[str, Any]):
    """
    Example payload:
    { "prompt": "Explain the rules of the game in one sentence." }
    """
    prompt = payload.get("prompt")
    if not prompt:
        raise HTTPException(status_code=400, detail="Missing 'prompt' field")

    if not OPENAI_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Server missing OPENAI_API_KEY environment variable"
        )

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    body = {
        "model": OPENAI_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 400,
        "temperature": 0.7,
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            resp = await client.post(OPENAI_API_URL, headers=headers, json=body)
        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"OpenAI request failed: {e}")

    if resp.status_code != 200:
        text = resp.text
        raise HTTPException(status_code=502, detail=f"OpenAI API error: {resp.status_code} - {text}")

    data = resp.json()
    try:
        answer = data["choices"][0]["message"]["content"]
    except Exception:
        raise HTTPException(status_code=502, detail=f"Unexpected response from OpenAI: {data}")

    return {"prompt": prompt, "answer": answer}
