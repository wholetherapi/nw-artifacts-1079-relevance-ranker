"""Pre/post-processing helpers shared by the relevance-ranker service."""

from __future__ import annotations

import re
import unicodedata

TOKEN_RE = re.compile(r"[a-z0-9_]+")
MAX_TOKENS = 512


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return " ".join(text.split())


def transform(text: str) -> list[str]:
    tokens = TOKEN_RE.findall(normalize(text))
    if len(tokens) > MAX_TOKENS:
        tokens = tokens[:MAX_TOKENS]
    return tokens


def postprocess(scores: list[float], labels: dict[int, str]) -> dict[str, float]:
    total = sum(scores) or 1.0
    return {labels.get(i, str(i)): s / total for i, s in enumerate(scores)}
