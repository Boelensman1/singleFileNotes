#!/usr/bin/env python3
import os
import sys
from datetime import date
from icalendar import Calendar, Event
from urllib.request import urlopen


def get_events():
    url = os.environ['TODO_CALENDER_URL']
    g = urlopen(url)
    gcal = Calendar.from_ical(g.read())

    today = date.today()

    events = []
    for component in gcal.walk():
        if component.name == "VEVENT":
            startDateTime = component.get('dtstart').dt
            if startDateTime.year == today.year and startDateTime.month == today.month and startDateTime.day == today.day:
                events.append({"summary": component.get('summary'), "startDateTime": startDateTime})
    g.close()

    sortedEvents = sorted(events, key = lambda i: i['startDateTime'])

    return_value = []
    for event in sortedEvents:
        return_value.append("- " + event['summary'].capitalize())
    return return_value

if 'TODO_CALENDER_URL' in os.environ:
    if __name__ == '__main__':
        events = get_events()
        for event in events:
            print(event)
