watch:
	iwatch -c "./venv/bin/pytest -v -ra --tb=short" -e close_write -t '.*.py' .
