# -*- coding: utf-8 -*-

import csv
import StringIO
import codecs

from timesheets.timecard import Timecard

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = StringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

class Timesheet(object):
    def __init__(self):
        self.timecards = {}

    def get_timecard(self, date_string):
        if date_string in self.timecards:
            timecard = self.timecards[date_string]
        else:
            timecard = Timecard(date_string)
            self.timecards[date_string] = timecard

        return timecard

    def dates(self):
        return sorted(self.timecards.keys())

    def to_csv(self):
        csv_fh = StringIO.StringIO()
        writer = UnicodeWriter(csv_fh, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = ["Date work", "Description", "Tickets", "Hours"]
        writer.writerow(header)
        for date in self.dates():
            timecard = self.timecards[date]
            writer.writerow([
                str(date),
                timecard.notes,
                timecard.tickets,
                "{0:.2f}".format(timecard.hours_worked),
                ])
        csv_out = csv_fh.getvalue()
        csv_fh.close()

        return csv_out

    def total_hours_worked(self):
        total_hours = 0.0
        for date in self.dates():
            timecard = self.timecards[date]
            total_hours += timecard.hours_worked

        return total_hours

# vim: expandtab shiftwidth=4 softtabstop=4
