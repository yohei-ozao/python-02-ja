from event_scheduler import Event, schedule_events, print_schedule

def test_event_scheduler():
    events = [Event("Python Workshop", 14), Event("Data Science Meetup", 18), Event("Web Dev Seminar", 18)]
    schedule = schedule_events(events)
    assert schedule == {14: ["Python Workshop"], 18: ["Data Science Meetup", "Web Dev Seminar"]}
    print("All tests passed!")

test_event_scheduler()
