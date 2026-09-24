# VoxBabel Backend — Main Entry Point
"""
VoxBabel: Real-Time AI-Powered Multilingual Voice Translation
FastAPI application entry point.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

app = FastAPI(
    title="VoxBabel",
    description="Real-time multilingual voice translation for video meetings",
    version="0.1.0",
)

# ── CORS ──
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "voxbabel"}
