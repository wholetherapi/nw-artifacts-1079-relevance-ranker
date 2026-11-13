from src.service import Request, handle


class FakeModel:
    version = "test"

    def predict(self, features):
        return [0.2, 0.8]


class FakePreprocessor:
    def transform(self, payload):
        return payload.split()


def test_handle_returns_scores():
    out = handle(Request("r-1", "hello world"), FakeModel(), FakePreprocessor())
    assert out["request_id"] == "r-1"
    assert out["scores"] == [0.2, 0.8]
