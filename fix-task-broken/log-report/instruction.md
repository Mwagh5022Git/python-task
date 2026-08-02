An Apache access log is available at /app/access.log.

Analyze the log and produce a JSON report at:

/app/report.json

The JSON object must contain exactly these fields:

- total_requests: Total number of log entries.
- unique_ips: Number of distinct client IP addresses.
- top_path: The requested URL path that appears most frequently.

Example format:

{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
