# VoxBabel — Provider Base Classes
"""
Abstract base classes for all AI providers (STT, LID, MT, TTS).
Implement these interfaces to add new providers.
Swap providers via config.py settings.
"""

from abc import ABC, abstractmethod


class BaseSTTProvider(ABC):
    """Speech-to-Text provider interface."""

    @abstractmethod
    async def transcribe(self, audio: bytes) -> str:
        """Convert audio bytes to text transcript."""
        ...


class BaseLIDProvider(ABC):
    """Language Identification provider interface."""

    @abstractmethod
    async def detect(self, text: str) -> str:
        """Detect language of text, return ISO 639-1 code (e.g., 'en', 'ur')."""
        ...


class BaseMTProvider(ABC):
    """Machine Translation provider interface."""

    @abstractmethod
    async def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """Translate text from source to target language."""
        ...


class BaseTTSProvider(ABC):
    """Text-to-Speech provider interface."""

    @abstractmethod
    async def synthesize(self, text: str, lang: str) -> bytes:
        """Convert text to audio bytes in the specified language."""
        ...
