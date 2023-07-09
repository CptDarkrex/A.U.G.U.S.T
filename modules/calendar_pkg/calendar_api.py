from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import datetime
# import pytz


class GoogleCalendarEventCreator:
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    def __init__(self, calendar_id='primary'):
        self.service = self.get_service()
        self.calendar_id = calendar_id

    def get_service(self):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json')
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret_calendar.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        try:
            service = build('calendar', 'v3', credentials=creds)
            return service
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def create_event(self, date, start_time, end_time, title, description):
        start_datetime = datetime.datetime.strptime(f"{date} {start_time}", "%d/%m/%Y %I:%M %p")
        end_datetime = datetime.datetime.strptime(f"{date} {end_time}", "%d/%m/%Y %I:%M %p")

        event_body = {
            'summary': title,
            'description': description,
            'start': {
                'dateTime': start_datetime.isoformat(),
                'timeZone': 'Australia/Sydney',  # Change this to your desired timezone
            },
            'end': {
                'dateTime': end_datetime.isoformat(),
                'timeZone': 'Australia/Sydney',  # Change this to your desired timezone
            },
        }

        try:
            event = self.service.events().insert(calendarId=self.calendar_id, body=event_body).execute()
            print(f"Event created: {event['htmlLink']}")
        except Exception as e:
            print(f"An error occurred: {e}")


# Example Usage
gcal = GoogleCalendarEventCreator()
gcal.create_event("09/07/2023", "10:00 AM", "12:00 PM", "Meeting with Team", "Discussing project updates and future plans.")
