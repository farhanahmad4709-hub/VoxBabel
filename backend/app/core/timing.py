# VoxBabel Backend — Latency Instrumentation
"""
Timestamps each pipeline boundary for RQ1 evaluation.
Measures end-to-end latency and per-component breakdown.
"""

import time
from dataclasses import dataclass, field


@dataclass
class PipelineTimings:
    """Records timestamps at each stage of the translation pipeline."""

    start: float = 0.0
    stt_done: float = 0.0
    lid_done: float = 0.0
    mt_done: float = 0.0
    tts_done: float = 0.0
    delivered: float = 0.0

    def mark_start(self):
        self.start = time.perf_counter()

    def mark_stt(self):
        self.stt_done = time.perf_counter()

    def mark_lid(self):
        self.lid_done = time.perf_counter()

    def mark_mt(self):
        self.mt_done = time.perf_counter()

    def mark_tts(self):
        self.tts_done = time.perf_counter()

    def mark_delivered(self):
        self.delivered = time.perf_counter()

    @property
    def total_ms(self) -> float:
        return (self.delivered - self.start) * 1000

    def breakdown(self) -> dict[str, float]:
        """Returns per-component latency in milliseconds."""
        return {
            "stt_ms": (self.stt_done - self.start) * 1000,
            "lid_ms": (self.lid_done - self.stt_done) * 1000,
            "mt_ms": (self.mt_done - self.lid_done) * 1000,
            "tts_ms": (self.tts_done - self.mt_done) * 1000,
            "delivery_ms": (self.delivered - self.tts_done) * 1000,
            "total_ms": self.total_ms,
        }
