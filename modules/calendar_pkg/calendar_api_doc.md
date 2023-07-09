# GoogleCalendarEventCreator

The `GoogleCalendarEventCreator` is a Python class for creating events on Google Calendar. It uses the Google Calendar API v3 and authenticates with OAuth2.

## Prerequisites

Before using this class, please ensure that you've set up your OAuth2 credentials file (`credentials.json`) according to Google's guidelines.

This class requires the following Python packages, which you can install using pip:
- `google-auth`
- `google-auth-oauthlib`
- `google-auth-httplib2`
- `httplib2`
- `google-api-python-client`
- `pytz`

## Usage

First, import the class:

```python
from google_calendar import GoogleCalendarEventCreator  # assuming the class is in a file named google_calendar.py
```

Create an instance of the class:

```python
gcal = GoogleCalendarEventCreator()
```

You can specify a particular calendar ID when creating the instance. If not specified, it defaults to 'primary', indicating the primary calendar of the authenticated user.

To create an event, use the `create_event` method:

```python
gcal.create_event("09/07/2023", "10:00 AM", "12:00 PM", "Meeting with Team", "Discussing project updates and future plans.")
```

The `create_event` method requires the following parameters:
- `date`: The date of the event (in "dd/mm/yyyy" format)
- `start_time`: The start time of the event (in "hh:mm AM/PM" format)
- `end_time`: The end time of the event (in "hh:mm AM/PM" format)
- `title`: The title of the event
- `description`: The description of the event

After running this command, the event will be created on the specified Google Calendar.

## Timezone

By default, the class is configured to use the 'America/Los_Angeles' timezone. If you wish to use a different timezone, you must change it in the class definition:

```python
'start': {
    'dateTime': start_datetime.isoformat(),
    'timeZone': 'Your_Desired_Timezone',
},
'end': {
    'dateTime': end_datetime.isoformat(),
    'timeZone': 'Your_Desired_Timezone',
},
```

Python recognizes timezones such as 'America/New_York', 'Asia/Kolkata', 'Europe/London', and others.

## Troubleshooting

If the dates and times of your events are not as expected, check the timezone setting in your Google Calendar and the class definition. If they don't match, you might experience inconsistencies.

---