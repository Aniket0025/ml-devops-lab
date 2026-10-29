
from pathlib import Path
import csv
import random
import html

output_dir = Path("monitoring/reports")
output_dir.mkdir(parents=True, exist_ok=True)

random.seed(42)

# Reference data: normal measurements
reference = [random.gauss(5.8, 0.8) for _ in range(150)]

# Current data: shifted measurements to simulate drift
current = [random.gauss(6.5, 0.8) for _ in range(150)]

ref_mean = sum(reference) / len(reference)
cur_mean = sum(current) / len(current)
difference = cur_mean - ref_mean

status = "Drift detected" if abs(difference) > 0.3 else "No significant drift"

report_path = output_dir / "data_drift_report.html"

report_path.write_text(f"""
<html>
<head><title>Data Drift Monitoring Report</title></head>
<body style="font-family:Arial;margin:40px">
<h1>Data Drift Monitoring Report</h1>
<p><b>Reference records:</b> {len(reference)}</p>
<p><b>Current records:</b> {len(current)}</p>
<p><b>Reference mean:</b> {ref_mean:.3f}</p>
<p><b>Current mean:</b> {cur_mean:.3f}</p>
<p><b>Mean difference:</b> {difference:.3f}</p>
<h2>{html.escape(status)}</h2>
<p>This is a simple demonstration using synthetic data and a threshold.</p>
</body>
</html>
""", encoding="utf-8")

print("Monitoring completed.")
print(f"Reference mean: {ref_mean:.3f}")
print(f"Current mean: {cur_mean:.3f}")
print(f"Status: {status}")
print(f"Report: {report_path.resolve()}")
