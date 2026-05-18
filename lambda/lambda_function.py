import json
import logging
import os
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

logger = logging.getLogger()
logger.setLevel(logging.INFO)

CALENDARS = json.loads(os.environ.get("CALENDARS_JSON", "[]"))
TIMEZONE = os.environ.get("TIMEZONE", "Europe/Rome")


def get_ics(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode("utf-8")
    except Exception as error:
        logger.error(f"Error downloading ICS: {error}")
        return ""


def parse_dt(dt_raw):
    try:
        if len(dt_raw) == 8:
            return datetime.strptime(dt_raw, "%Y%m%d")
        elif len(dt_raw) == 15:
            return datetime.strptime(dt_raw, "%Y%m%dT%H%M%S")
        elif len(dt_raw) == 13:
            return datetime.strptime(dt_raw, "%Y%m%dT%H%M")
    except Exception:
        return None


def parse_events(ics_text, calendar_name, start_date, end_date):
    events = []

    raw_events = re.findall(
        r"BEGIN:VEVENT(.*?)END:VEVENT",
        ics_text,
        re.DOTALL
    )

    for event in raw_events:
        summary_match = re.search(r"SUMMARY:(.*)", event)
        dtstart_match = re.search(r"DTSTART[^:]*:(\d{8}T?\d{0,6})", event)

        if not summary_match or not dtstart_match:
            continue

        summary = summary_match.group(1).strip()
        dtstart = parse_dt(dtstart_match.group(1))

        if not dtstart:
            continue

        if start_date <= dtstart.date() <= end_date:
            events.append({
                "title": summary,
                "datetime": dtstart,
                "calendar": calendar_name
            })

    return events


def format_events(events):
    return [
        {
            "title": event["title"],
            "date": event["datetime"].strftime("%Y-%m-%d"),
            "time": event["datetime"].strftime("%H:%M") if event["datetime"].hour != 0 else "All Day",
            "calendar": event["calendar"]
        }
        for event in events
    ]


def lambda_handler(event, context):
    logger.info("Calendar Reader Lambda started")
    logger.info(json.dumps(event))

    params = event.get("queryStringParameters") or {}

    try:
        days_offset = int(params.get("days_offset", 0))
    except Exception:
        days_offset = 0

    try:
        range_days = int(params.get("range_days", 1))
    except Exception:
        range_days = 1

    tz = ZoneInfo(TIMEZONE)
    today = datetime.now(tz).date()

    start_date = today + timedelta(days=days_offset)
    end_date = start_date + timedelta(days=range_days - 1)

    all_events = []

    for calendar in CALENDARS:
        ics_text = get_ics(calendar["url"])

        if not ics_text:
            continue

        parsed_events = parse_events(
            ics_text,
            calendar["name"],
            start_date,
            end_date
        )

        all_events.extend(parsed_events)

    formatted_events = format_events(all_events)
    formatted_events.sort(key=lambda x: (x["date"], x["time"]))

    logger.info(f"Total events found: {len(formatted_events)}")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "start_date": str(start_date),
            "end_date": str(end_date),
            "total_events": len(formatted_events),
            "events": formatted_events
        })
    }
