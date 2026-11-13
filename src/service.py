"""Serving entry point for the relevance-ranker artifact."""

from __future__ import annotations

import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Request:
    request_id: str
    payload: str
    timeout_ms: int = 2500


class ServingError(RuntimeError):
    pass


def handle(request: Request, model, preprocessor) -> dict:
    """Run one inference request through the published model pipeline."""
    if not request.payload:
        raise ServingError("empty payload")
    try:
        features = preprocessor.transform(request.payload)
        scores = model.predict(features)
    except Exception as exc:  # pragma: no cover - defensive
        logger.exception("inference failed for %s", request.request_id)
        raise ServingError(str(exc)) from exc
    return {
        "request_id": request.request_id,
        "scores": [float(s) for s in scores],
        "model_version": getattr(model, "version", "unknown"),
    }
