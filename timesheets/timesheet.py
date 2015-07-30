# -*- coding: utf-8 -*-

import csv
import StringIO

from timesheets.timecard import Timecard

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
        writer = csv.writer(csv_fh, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for date in self.dates():
            timecard = self.timecards[date]
            writer.writerow([
                date,
                timecard.notes,
                timecard.tickets,
                "{0:.2f}".format(timecard.hours_worked),
                ])
        csv_out = csv_fh.getvalue()
        csv_fh.close()

        return csv_out

# vim: expandtab shiftwidth=4 softtabstop=4
