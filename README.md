# Amazon Affiliate URL Converter - Backend

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

The server starts on `http://localhost:5000`.

## API Endpoints

### POST /api/convert
Converts an Amazon URL to an affiliate URL.

**Request:**
```json
{
  "url": "https://www.amazon.in/dp/B0EXAMPLE"
}
```

**Response:**
```json
{
  "original_url": "https://www.amazon.in/dp/B0EXAMPLE",
  "affiliate_url": "https://www.amazon.in/dp/B0EXAMPLE?tag=bestprod01228-21",
  "tag": "bestprod01228-21"
}
```

### GET /api/health
Health check endpoint.
