from datetime import datetime, date

class Timecard(object):
    def __init__(self, date_string):
        if isinstance(date_string, date):
            self.date = date_string
        else:
            self.date = datetime.strptime(date_string, "%Y-%m-%d")
        self.time_spec = None
        self.hours_worked = 0
        self.notes = ""
        self.tickets = ""

    def add(self, time_spec, notes, tickets=""):
        if time_spec == self.time_spec:
            error_message = "Repeated time spec found; please check input data"
            raise ValueError(error_message)
        self.time_spec = time_spec
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

        # incoming "tickets" values could already contain commas, so get the
        # initial data into a form we can always work with
        new_tickets = ",".join(filter(None, [self.tickets, tickets]))
        all_tickets = new_tickets.split(',')

        self.tickets = ",".join(sorted(list(set(all_tickets))))

# vim: expandtab shiftwidth=4 softtabstop=4
