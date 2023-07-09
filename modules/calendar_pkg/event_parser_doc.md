## Event Data Parser Algorithm Documentation

### Introduction
The Event Data Parser Algorithm is designed to extract relevant information such as date, starting and ending time, title, and description from an input string. The input string is typically formatted to represent event details in a Google Calendar-like format.

### Input
The algorithm expects an input string containing event information. The input string should follow a specific format with labeled sections for each attribute such as date, start time, end time, title, and description.

### Output
The algorithm outputs the extracted event information as separate variables:
- `event_date`: A string representing the date of the event.
- `start_time`: A string representing the starting time of the event.
- `end_time`: A string representing the ending time of the event.
- `event_title`: A string representing the title of the event.
- `event_description`: A string representing the description of the event.

### Algorithm Steps
1. Define variables to store the extracted information: `event_date`, `start_time`, `end_time`, `event_title`, and `event_description`.
2. Accept the input string from the user.
3. Use regular expressions or string manipulation techniques to extract the relevant information from the input string.
4. Extract the date from the input string and assign it to the `event_date` variable.
5. Extract the starting time from the input string and assign it to the `start_time` variable.
6. Extract the ending time from the input string and assign it to the `end_time` variable.
7. Extract the event title from the input string and assign it to the `event_title` variable.
8. Extract the event description from the input string and assign it to the `event_description` variable.
9. The extracted information is now stored in the respective variables.

### Error Handling
In case the regular expressions fail to find a match for any attribute in the input string, the corresponding variable will be set to `None`. This allows for error handling and prevents the algorithm from raising an exception.

### Example Usage
```python
import re

input_string = "<Your input string>"

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
```

Replace `<Your input string>` with the actual input string containing the event details. The algorithm will extract the information and display it as separate variables.

### Conclusion
The Event Data Parser Algorithm simplifies the process of extracting event information from a string and storing it in separate variables. It provides a convenient way to parse event data related to a Google Calendar-like format, enabling further manipulation and utilization of the extracted information.