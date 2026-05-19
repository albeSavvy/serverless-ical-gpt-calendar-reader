# AWS Serverless iCal GPT Calendar Reader

## Project in One Sentence

I built a serverless AWS API that reads iCal calendar feeds and exposes structured upcoming events to a GPT-based assistant through API Gateway and Lambda.

## What I Built

This project is a lightweight cloud-based calendar assistant backend designed to retrieve events from multiple iCal feeds and expose them through a simple API.

It includes:

- iCal feed ingestion
- recurring event parsing
- API Gateway integration
- Lambda-based event processing
- GPT-friendly JSON responses
- configurable calendar sources
- CloudWatch logging

## Why I Built It

I built this project to practice AWS serverless APIs and AI integration workflows in a realistic personal productivity and automation scenario.

The goal was to move beyond theoretical study and experiment with how GPT assistants can interact with external services through APIs.

## Architecture at a Glance

```text
Published iCal Feeds
        |
        v
AWS Lambda
Calendar Parsing
        |
        v
Amazon API Gateway
REST API Endpoint
        |
        v
Custom GPT Action
Calendar Requests
        |
        v
Structured JSON Response
```

## AWS Services Used

| Service | Purpose |
|---|---|
| Amazon API Gateway | Exposes the calendar reader endpoint |
| AWS Lambda | Downloads and parses iCal calendar feeds |
| Amazon CloudWatch | Provides logging and debugging |
| AWS IAM | Manages Lambda execution permissions |
| Environment Variables | Stores calendar configuration safely |

## Key Features

- Serverless API architecture
- Multiple iCal calendar feed support
- Query parameters for date ranges
- Support for recurring events through RRULE parsing
- Support for EXDATE exclusions
- Europe/Rome timezone handling
- GPT-friendly JSON response format
- No hardcoded personal calendar URLs
- CloudWatch logging
- Cost-conscious AWS design

## API Usage

Endpoint example:

```text
GET /events?days_offset=0&range_days=1
```

| Parameter | Description | Example |
|---|---|---|
| days_offset | Number of days from today | 0 = today, 1 = tomorrow |
| range_days | Number of days to include | 1 = one day, 7 = one week |

## Example Response

```json
{
  "start_date": "2026-05-18",
  "end_date": "2026-05-18",
  "total_events": 2,
  "events": [
    {
      "title": "AWS Study Session",
      "date": "2026-05-18",
      "time": "18:30",
      "calendar": "Study"
    }
  ]
}
```

## What I Learned

- How API Gateway and Lambda can expose serverless APIs
- How to parse and process iCal feeds programmatically
- How recurring events and RRULE logic work
- How GPT Actions can integrate with external APIs
- How to structure JSON responses for AI assistants
- How to think about security, monitoring, cleanup, and cost optimization

## Future Improvements

- Add DynamoDB caching layer
- Add EventBridge scheduled refresh
- Add authentication for API Gateway
- Add structured JSON logging
- Add unit tests for iCal parsing
- Add CI/CD deployment with GitHub Actions
- Add Infrastructure as Code with AWS SAM, CDK, or Terraform

## Technical Documentation

- [Architecture Diagram](architecture/README.md)
- [Custom GPT Action](docs/custom-gpt-action.md)
- [Setup Guide](docs/setup-guide.md)
- [Security](docs/security.md)
- [Cost Optimization](docs/cost-optimization.md)
- [Monitoring](docs/monitoring.md)
- [Cleanup](docs/cleanup.md)
- [OpenAPI Specification](api/openapi.yaml)

## Certification Alignment

This project supports practical learning for AWS and cloud architecture topics such as serverless API design, Lambda integration, API Gateway configuration, IAM execution roles, CloudWatch monitoring, cost optimization, and AI assistant API integrations.

## Repository Structure

```text
serverless-ical-gpt-calendar-reader/
│
├── README.md
├── .gitignore
├── lambda/
├── api/
├── config/
├── architecture/
├── docs/
└── tests/
```

## Author

Created by Alberto Savino as part of a practical AWS learning path focused on serverless architecture, automation, AI integrations, and cloud-based productivity workflows.
