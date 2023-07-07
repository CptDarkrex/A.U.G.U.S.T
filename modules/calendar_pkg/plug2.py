import datetime
import os
import re
import spacy
from dateutil import parser
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# OAuth 2.0 flow
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret_calendar.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Build the service
service = build('calendar', 'v3', credentials=creds)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Get user input
prompt = input("Enter your prompt: ")

# Process the text with spaCy
doc = nlp(prompt)

# Extract date and time
# Extract date and time
date = None
start_time = None
end_time = None
for ent in doc.ents:
    if ent.label_ == "DATE" and date is None:
        if ent.text.lower() == "tomorrow":
            date = datetime.datetime.now() + datetime.timedelta(days=1)
        else:
            try:
                date = parser.parse(ent.text)
            except:
                print("Could not parse date, please enter it manually.")
                date_str = input("Enter the date of the event: ")
                date = parser.parse(date_str)
    elif ent.label_ == "TIME":
        if start_time is None:
            start_time = parser.parse(f"{date.strftime('%Y-%m-%d')} {ent.text}")
        else:
            end_time = parser.parse(f"{date.strftime('%Y-%m-%d')} {ent.text}")


# Ask for date if not provided
if date is None:
    date_str = input("Enter the date of the event: ")
    date = parser.parse(date_str)

# Ask for start time if not provided
if start_time is None:
    start_time_str = input("Enter the start time of the event: ")
    start_time = parser.parse(f"{date.strftime('%Y-%m-%d')} {start_time_str}")

# Ask for end time if not provided
if end_time is None:
    end_time_str = input("Enter the end time of the event: ")
    end_time = parser.parse(f"{date.strftime('%Y-%m-%d')} {end_time_str}")

# Ask for title
title = input("Enter the title of the event: ")

# Ask for description
description = input("Enter the description of the event: ")

# Create event
event = {
    'summary': title,
    'description': description,
    'start': {
        'dateTime': start_time.isoformat(),
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': end_time.isoformat(),
        'timeZone': 'America/Los_Angeles',
    },
}

# Call the Calendar API
event = service.events().insert(calendarId='primary', body=event).execute()
print(f"Event created: {event.get('htmlLink')}")
