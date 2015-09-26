# pTimesheets

A program to manage timesheets by using simple text files.

## Setup

    git clone git@github.com:paultcochrane/ptimesheets.git

## Timesheet format

Timesheets are YAML files with the following format:

    date: 2015-09-24
    time_spec: 12:50-15:30
    tickets: "#181"
    notes:
	- |
	    - notes about work I've done in this time period
    ---
    date: 2015-09-24
    time_spec: 22:00-23:30
    tickets: "#23"
    notes:
	- |
	    - notes about work I did later in the same day
            - more info about work done in this time period

Each entry is separated by a line containing only three hyphens `---`; the
entries are referred to as "timecards" as they are much the same idea as
checking in and checking out at a workplace with an automated employee time
management system.  An entire file is thus a "timesheet", and generally will
encompass the work of an entire month.

## Usage

    python show_timesheet.py --timesheet job-timesheet-2015-09.yml > job-timesheet-2015-09.csv

The CSV file can then be used to summarise data when writing invoices, or
when descriptions of daily work are required by a client or customer.

## Notes

Yes, the 'p' is silent.
