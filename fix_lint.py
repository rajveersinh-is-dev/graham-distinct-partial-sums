import re

with open('src/graham_backtrack.py', 'r') as f:
    content = f.read()

# Fix mypy error by checking start_time is not None
content = content.replace(
    'if timeout is not None and time.time() - start_time > timeout:',
    'if timeout is not None and start_time is not None and time.time() - start_time > timeout:'
)
with open('src/graham_backtrack.py', 'w') as f:
    f.write(content)
