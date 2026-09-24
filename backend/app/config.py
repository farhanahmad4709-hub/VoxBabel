# VoxBabel Backend — Configuration
"""
Application settings loaded from environment variables.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """VoxBabel configuration — reads from .env file."""

    # ── App ──
    APP_NAME: str = "VoxBabel"
    DEBUG: bool = True

    # ── CORS ──
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]  # Vite dev server

    # ── Database ──
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/voxbabel"

    # ── Provider toggles (local vs cloud) ──
    STT_PROVIDER: str = "whisper"        # "whisper" | "google"
    MT_PROVIDER: str = "opus"            # "opus" | "google"
    TTS_PROVIDER: str = "piper"          # "piper" | "google"

    # ── API Keys (only needed if using cloud providers) ──
    GOOGLE_CLOUD_API_KEY: str = ""
    GOOGLE_APPLICATION_CREDENTIALS: str = ""

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
