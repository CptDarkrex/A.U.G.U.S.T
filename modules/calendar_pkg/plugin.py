import os.path
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from transformers import pipeline


class GoogleCalendarManager:
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    def __init__(self, credentials_file='client_secret_calendar.json', token_file='token.pickle'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.creds = self.authenticate()
        self.service = build('calendar', 'v3', credentials=self.creds)

    def authenticate(self):
        creds = None
        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(self.token_file, 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def create_event(self, event):
        return self.service.events().insert(calendarId='primary', body=event).execute()

    def view_events(self, max_results=10):
        events_result = self.service.events().list(calendarId='primary', maxResults=max_results, singleEvents=True,
                                                   orderBy='startTime').execute()
        return events_result.get('items', [])

    def delete_event(self, event_id):
        self.service.events().delete(calendarId='primary', eventId=event_id).execute()


def main():
    # Initialize the GoogleCalendarManager
    calendar_manager = GoogleCalendarManager()

    # Initialize the language model
    nlp = pipeline("question-answering")

    # Interact with the user
    while True:
        user_input = input("How can I assist you with your calendar? (type 'exit' to quit)\n")

        if user_input.lower() == 'exit':
            break

        # Using the language model to understand user's request
        answer = nlp(question=user_input, context="view events, create event, delete event")

        # Handling a request to view events
        if "view" in answer["answer"].lower() and "events" in answer["answer"].lower():
            events = calendar_manager.view_events()
            if not events:
                print("No upcoming events found.")
            for event in events:
                print(event['summary'], event['start'], event['end'])

        # Handling a request to create an event
        elif "create" in answer["answer"].lower() and "event" in answer["answer"].lower():
            # For simplicity, let's create a fixed event. In practice, you should ask the user for details.
            event = {
                'summary': 'Test Event',
                'start': {'dateTime': '2023-07-10T09:00:00-07:00'},
                'end': {'dateTime': '2023-07-10T10:00:00-07:00'},
            }
            created_event = calendar_manager.create_event(event)
            print(f'Event created: {created_event["htmlLink"]}')

        # Handling a request to delete an event
        elif "delete" in answer["answer"].lower() and "event" in answer["answer"].lower():
            # For simplicity, let's ask the user for the event ID. In practice, you might want to provide a better interface.
            event_id = input("Please enter the event ID you want to delete: ")
            calendar_manager.delete_event(event_id)
            print('Event deleted')

        else:
            print("I'm sorry, I didn't understand your request.")


if __name__ == '__main__':
    main()
