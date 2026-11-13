# relevance-ranker (ART-4821)

Serving and training code for the `relevance-ranker` artifact in the Meridian
model-service registry.

## Repository Status

Released and in production use (tag `v2.3.1`). The repository contains the
complete serving loop, preprocessing pipeline and smoke tests.

## Layout

- `src/service.py` - request handling and model invocation
- `src/pipeline.py` - preprocessing/postprocessing helpers
- `tests/test_service.py` - smoke tests used by the release gate
