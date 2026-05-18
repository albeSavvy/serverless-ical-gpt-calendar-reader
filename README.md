# AWS Serverless iCal GPT Calendar Reader

## Overview

This project implements a serverless AWS API that reads multiple iCal calendar feeds, parses upcoming events, and exposes structured calendar data to a GPT-based assistant through Amazon API Gateway and AWS Lambda.

The project was designed as a hands-on AWS serverless integration and AI automation exercise, with a focus on API design, calendar parsing, external service integration, cost optimization, monitoring, and security best practices.

## Business Scenario

Users often manage multiple calendars across personal, work, study, sport, and recurring activity categories. Manually checking each calendar can be inefficient, especially when trying to ask natural-language questions such as:

- What do I have today?
- What events are scheduled tomorrow?
- What is planned for the next week?
- Which calendar does this event belong to?

This project exposes calendar data through a simple API so that a Custom GPT or AI assistant can retrieve structured calendar events and generate user-friendly answers.

## Architecture

```text
User asks calendar question
        |
        v
Custom GPT Action
        |
        v
Amazon API Gateway
        |
        v
AWS Lambda
Calendar Reader / Parser
        |
        v
External iCal Feeds
        |
        v
JSON Response
        |
        v
GPT-generated answer
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
- JSON response optimized for GPT Actions
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

## Repository Structure

```text
serverless-ical-gpt-calendar-reader/
│
├── README.md
├── .gitignore
├── lambda/
│   └── lambda_function.py
├── api/
│   ├── openapi.yaml
│   └── README.md
├── config/
│   ├── calendars.example.json
│   └── README.md
├── architecture/
│   ├── README.md
│   ├── data-flow.md
│   └── design-decisions.md
├── docs/
│   ├── project-overview.md
│   ├── setup-guide.md
│   ├── custom-gpt-action.md
│   ├── security.md
│   ├── cost-optimization.md
│   ├── monitoring.md
│   └── cleanup.md
└── tests/
    └── sample_event.json
```

## Certification Alignment

This project supports practical learning for AWS and cloud architecture topics such as:

- Serverless API design
- Lambda-based integration
- API Gateway configuration
- IAM execution roles
- External API/feed integration
- CloudWatch monitoring
- Cost optimization
- Secure configuration management
- AI assistant API integration

## Future Improvements

- Add DynamoDB caching layer
- Add EventBridge scheduled refresh
- Add authentication for API Gateway
- Add structured JSON logging
- Add unit tests for iCal parsing
- Add CI/CD deployment with GitHub Actions
- Add Infrastructure as Code with AWS SAM, CDK, or Terraform

## Author

Created by Alberto Savino as part of a practical AWS learning path focused on serverless architecture, automation, AI integrations, and cloud-based productivity workflows.
