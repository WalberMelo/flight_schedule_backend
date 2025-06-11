# Flight Schedule Backend

This is a **serverless backend API** for an aviation log/flight schedule platform, built with [FastAPI](https://fastapi.tiangolo.com/) and deployed to AWS Lambda using [AWS SAM (Serverless Application Model)](https://docs.aws.amazon.com/serverless-application-model/).

The backend exposes endpoints for:

- Fetching live flight data (AviationStack API)
- Analyzing aviation maintenance logs using the OpenAI API

It is designed for scalability, pay-per-use billing, and secure key management via AWS Secrets Manager.

---

## Technologies Used

- **FastAPI** – Modern Python web framework for building APIs, async-ready.
- **Mangum** – ASGI adapter to run FastAPI on AWS Lambda.
- **AWS Lambda** – Serverless compute for backend logic.
- **AWS API Gateway** – HTTP REST endpoint in front of Lambda.
- **AWS SAM** – Infrastructure-as-code tool to define and deploy serverless stacks.
- **AWS Secrets Manager** – Securely store and retrieve API keys/secrets at runtime.
- **AviationStack API** – External service for live flight data.
- **OpenAI API** – For analyzing and summarizing aircraft maintenance logs.
- **httpx** – Async HTTP client for making external API calls.
- **pydantic** – Data validation and serialization (FastAPI models).
- **boto3** – AWS SDK for Python, used to access Secrets Manager.

---

## Data Sources

**Aviation Data**  
Live and sample aircraft maintenance log data used in this platform is based on real-world datasets from [MaintNet](https://people.rit.edu/fa3019/technical/aircraft.html) (the Collaborative Open-Source Library for Predictive Maintenance Language Resources in Aviation). MaintNet includes curated maintenance records, event logs, and related metadata from actual aviation operations, supporting research and robust AI-powered log analysis.

## Environment & Secrets

- **Sensitive API keys** (e.g., OpenAI, AviationStack) are **not hardcoded** or stored in environment variables.
- All secrets are stored in **AWS Secrets Manager** under the secret name (e.g., `prod/iag`).
- Keys are retrieved at runtime using **boto3** inside the Lambda function.

---

## API Endpoints

| Method | Path           | Description                                              |
| ------ | -------------- | -------------------------------------------------------- |
| GET    | `/api/flights` | Query live flight data                                   |
| POST   | `/api/analyze` | Analyze aircraft maintenance logs (AI-generated summary) |
| GET    | `/api/logs`    | Maintenance log dataset                                  |

- **CORS** is configured to allow your deployed frontend domain.

---

## Local Development

- Run locally with:
  ```sh
  uvicorn app.main:app --reload
  ```

---

## Deployment

Deployment uses **AWS SAM** and assumes you have configured AWS CLI credentials.

**Quick Start:**

```sh
# Install dependencies
pip install -r requirements.txt

# Build with SAM
sam build --use-container

# Deploy interactively
sam deploy --guided
```
