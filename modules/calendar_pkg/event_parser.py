import re

user_input = "Date: 09/07/2023 Start Time: 10:00 AM End Time: 12:00 PM " \
             "Title: Meeting with Team Description: Discussing project updates and future plans."


class EventParse:
    def get_event(self, input_string):
        event_date_match = re.search(r"Date: (\d{2}/\d{2}/\d{4})", input_string)
        start_time_match = re.search(r"Start Time: (\d{2}:\d{2} [APM]{2})", input_string)
        end_time_match = re.search(r"End Time: (\d{2}:\d{2} [APM]{2})", input_string)
        event_title_match = re.search(r"Title: (.+)", input_string)
        event_description_match = re.search(r"Description: (.+)", input_string)

        event_date = event_date_match.group(1) if event_date_match else None
        start_time = start_time_match.group(1) if start_time_match else None
        end_time = end_time_match.group(1) if end_time_match else None
        event_title = event_title_match.group(1) if event_title_match else None
        event_description = event_description_match.group(1) if event_description_match else None

        print("Event Date:", event_date)
        print("Start Time:", start_time)
        print("End Time:", end_time)
        print("Event Title:", event_title)
        print("Event Description:", event_description)

        event_details = {"event_date": event_date, "start_time": start_time, "end_time": end_time,
                         "event_title": event_title, "event_Description": event_description}

        return event_details
