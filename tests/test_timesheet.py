# -*- coding: utf-8 -*-

import unittest
from datetime import datetime

from timesheets.timesheet import Timesheet
from timesheets.timecard import Timecard

class TestTimesheet(unittest.TestCase):
    def setUp(self):
        self.timesheet = Timesheet()

    def testTimecardsDefaultValue(self):
        self.assertEqual(self.timesheet.timecards, {})

    def testGetTimecardReturnsATimecardObject(self):
        timecard = self.timesheet.get_timecard("2015-06-01")
        self.assertTrue(isinstance(timecard, Timecard))

    def testGetTimecardReturnsTimecardWithCorrectDate(self):
        timecard = self.timesheet.get_timecard("2015-06-01")
        self.assertEqual(timecard.date,
                datetime.strptime("2015-06-01", "%Y-%m-%d"))

    def testGetTimecardAddsTimecardToTimecardsDict(self):
        self.timesheet.get_timecard("2015-07-22")
        self.assertEqual(len(self.timesheet.timecards), 1)

    def testRepeatedCallsToGetTimecardReturnSameTimecard(self):
        tc1 = self.timesheet.get_timecard("2015-07-22")
        tc2 = self.timesheet.get_timecard("2015-07-22")

        self.assertEqual(tc1, tc2)

    def testDatesReturnsEmptyListWithoutTimecards(self):
        self.assertEqual(self.timesheet.dates(), [])

    def testDatesReturnsLengthTwoListWithTwoDifferentTimecards(self):
        self.timesheet.get_timecard("2015-06-01")
        self.timesheet.get_timecard("2015-06-02")

        self.assertEqual(len(self.timesheet.dates()), 2)

    def testDatesReturnsLengthOneListWithTwoSameTimecards(self):
        self.timesheet.get_timecard("2015-06-01")
        self.timesheet.get_timecard("2015-06-01")

        self.assertEqual(len(self.timesheet.dates()), 1)

    def testToCsvReturnsCsvFormattedDataForOneTimecard(self):
        item = {
                "time_spec": "10:00-18:30",
                "notes": "did stuff",
                }
        timecard = self.timesheet.get_timecard("2015-06-01")
        timecard.add(**item)

        timesheet_csv = self.timesheet.to_csv()
        expected = "Date work,Description,Tickets,Hours\r\n"
        expected += "2015-06-01,did stuff,,8.50\r\n"
        self.assertEqual(timesheet_csv, expected)

    def testToCsvReturnsCsvFormattedDataForTwoTimecards(self):
        first_item = {
                "time_spec": "10:00-18:30",
                "notes": "did stuff",
                }
        first_timecard = self.timesheet.get_timecard("2015-06-01")
        first_timecard.add(**first_item)

        second_item = {
                "time_spec": "19:00-20:00",
                "notes": "did more stuff",
                "tickets": "#123",
                }
        second_timecard = self.timesheet.get_timecard("2015-06-02")
        second_timecard.add(**second_item)

        timesheet_csv = self.timesheet.to_csv()
        expected = "Date work,Description,Tickets,Hours\r\n"
        expected += "2015-06-01,did stuff,,8.50\r\n"
        expected += "2015-06-02,did more stuff,#123,1.00\r\n"
        self.assertEqual(timesheet_csv, expected)

# vim: expandtab shiftwidth=4 softtabstop=4
