install:
	pip install -r requirements.txt

format:
	black .
	isort .
	
local_run:
	@echo "Starting streamlit on docker, (localhost:8501)"
	streamlit run src/app.py

local_docker_build:
	@echo "Starting docker-compose build"
	docker-compose build

local_docker_run:
	@echo "Starting streamlit on docker, port 8501"
	docker-compose up
