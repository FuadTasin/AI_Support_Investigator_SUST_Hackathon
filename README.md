# AI_Support_Investigator_SUST_Hackathon

AI-powered complaint investigation system built for the SUST Hackathon.

## Features

- FastAPI REST API
- Gemini 2.5 Flash integration
- Complaint analysis
- Transaction matching
- Rule-based investigation
- AI-generated customer response
- Safe response guardrails

## Tech Stack

- Python
- FastAPI
- Google Gemini API
- Pydantic
- Uvicorn

## Run Locally

```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

## API

```
GET /health
POST /analyze-ticket
```

## Swagger

```
http://127.0.0.1:8000/docs
```
