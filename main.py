from core import Chatbot
from modules import Memory
from modules import GoogleCalendar


def main():
    # initialize modules
    bot = Chatbot("TheBloke/vicuna-13B-1.1-HF")
    memory = Memory("10.20.10.30:27017", "August")
    calendar = GoogleCalendar("client_secret_748103692463-gfksfg8t7c0incv6qslvffhnto0678qd.apps.googleusercontent.com.json", "token.pickle")
    #client id: 748103692463-gfksfg8t7c0incv6qslvffhnto0678qd.apps.googleusercontent.com

    # loop to handle user interactions
    while True:
        prompt = input("You: ")

        # check if user asked for calendar events
        if "calendar" in prompt.lower():
            events = calendar.get_events()
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(f"{start}: {event['summary']}")

        # check if user asked for memory data
        elif "remember" in prompt.lower():
            memory_data = memory.get_data({"input": prompt})
            print(f"I remember: {memory_data}")

        else:
            output = bot.generate_response(prompt)
            print(f"Bot: {output}")
            memory.save_interaction(prompt, output)


if __name__ == "__main__":
    main()
