import pytest
import os
from src.reporter.json_export import export_to_json

def test_export_to_json(tmp_path):
    scores = {"A": 50}
    export_to_json(scores, 50, {"critical_gaps": 0}, str(tmp_path / "test.json"))
    assert os.path.exists(tmp_path / "test.json")