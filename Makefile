install:
	pip install -r requirements.txt

format:
	black .
	isort .
	
local_run:
	streamlit run src/app.py
