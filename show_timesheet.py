# -*- coding: utf-8 -*-

import yaml

from timesheets.timesheet import Timesheet

yml_fh = open("aaw.yml")
timesheet_items = yaml.load_all(yml_fh)

timesheet = Timesheet()
for item in timesheet_items:
    timecard = timesheet.get_timecard(item.pop('date'))
    timecard.add(**item)

timesheet_csv = timesheet.to_csv()
print timesheet_csv

# vim: expandtab shiftwidth=4 softtabstop=4
