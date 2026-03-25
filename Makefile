.PHONY: test

test:
	cd scripts && uv run --with pytest pytest -v
