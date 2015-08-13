#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import argparse

from timesheets.timesheet import Timesheet

parser = argparse.ArgumentParser(description='Convert timesheets to CSV')
parser.add_argument('--timesheet', type=str, required=True,
                        help='timesheet file name')
args = parser.parse_args()
timesheet_yml_fname = args.timesheet

yml_fh = open(timesheet_yml_fname)
timesheet_items = yaml.load_all(yml_fh)

timesheet = Timesheet()
for item in timesheet_items:
    timecard = timesheet.get_timecard(item.pop('date'))
    timecard.add(**item)

timesheet_csv = timesheet.to_csv()
print timesheet_csv

# vim: expandtab shiftwidth=4 softtabstop=4
