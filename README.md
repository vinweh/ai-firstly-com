# ai-firstly-com is the repo for aifirstly.com


## Local Dev
python -m venv .venv && source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload
# open http://127.0.0.1:8000
