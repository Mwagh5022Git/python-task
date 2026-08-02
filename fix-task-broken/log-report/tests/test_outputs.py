import json
from pathlib import Path

REPORT = Path("/app/report.json")

def test_report_exists():
    assert REPORT.exists(), "report.json not found"

def test_report_contents():
    data = json.loads(REPORT.read_text())

    assert data["total_requests"] == 6
    assert data["unique_ips"] == 3
    assert data["top_path"] == "/index.html"