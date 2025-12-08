#!/usr/bin/env bash
# Run uv setup for the container

/usr/local/bin/uv venv --clear
/usr/local/bin/uv sync \
	--group dev \
	--group test
