from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Mini Space Shooter backend is running!"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/level-info")
def level_info():
    return {
        "max_level": 8,
        "has_boss_levels": [4, 8],
        "message": "Level information API is working!"
    }
