# report.py
from hello import greet

html = f"""
<html>
<head><title>CI/CD Report</title></head>
<body>
    <h1>{greet("CI/CD")}</h1>
    <p>Pipeline ran successfully!</p>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html)

print("Report generated: index.html")