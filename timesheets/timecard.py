from datetime import datetime, date

class Timecard(object):
    def __init__(self, date_string):
        if isinstance(date_string, date):
            self.date = date_string
        else:
            self.date = datetime.strptime(date_string, "%Y-%m-%d")
        self.hours_worked = 0
        self.notes = ""
        self.tickets = ""

    def add(self, time_spec, notes, tickets=""):
        start_time, end_time = time_spec.split('-')
        start = datetime.strptime(start_time, "%H:%M")
        end = datetime.strptime(end_time, "%H:%M")
        if end <= start:
            raise ValueError("Start time after end time")
        hours_worked = (end-start).total_seconds()/3600.
        self.hours_worked += hours_worked

        if type(notes) is list:
            notes = notes[0]

        self.notes = "".join([self.notes, notes])
        self.tickets = tickets

# "{:02d}:{:02d}".format(int(t.seconds/3600), int((t.seconds%3600/60)))

# vim: expandtab shiftwidth=4 softtabstop=4
