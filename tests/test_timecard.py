# -*- coding: utf-8 -*-

import unittest
from datetime import date

from timesheets.timecard import Timecard

def minimum_item(**kwargs):
    kwargs.setdefault("notes", "")
    kwargs.setdefault("tickets", "")

    return kwargs

class TestTimecard(unittest.TestCase):
    def setUp(self):
        self.timecard = Timecard("2015-06-01")

    def testRaisesValueErrorOnInvalidDateString(self):
        with self.assertRaises(ValueError):
            Timecard("201-07-22")

    def testRaisesTypeErrorOnInvalidDateData(self):
        with self.assertRaises(TypeError):
            Timecard(20)

    def testHoursWorkedDefaultValue(self):
        self.assertEqual(Timecard("2015-07-22").hours_worked, 0)

    def testNotesDefaultValue(self):
        self.assertEqual(Timecard("2015-06-01").notes, "")

    def testTicketsDefaultValue(self):
        self.assertEqual(Timecard("2015-06-01").tickets, "")

    def testAddOneHourTimecardEntryThenHoursWorkedIsOne(self):
        item = minimum_item(time_spec="10:00-11:00")
        self.timecard.add(**item)
        self.assertEqual(self.timecard.hours_worked, 1)

    def testAddThirtyMinutesTimecardEntryThenHoursWorkedIsOneHalf(self):
        item = minimum_item(time_spec="10:00-10:30")
        self.timecard.add(**item)
        self.assertEqual(self.timecard.hours_worked, 0.5)

    def testAddRaisesValueErrorOnInvalidTimeString(self):
        with self.assertRaises(ValueError):
            item = minimum_item(time_spec="10:00")
            self.timecard.add(**item)

    def testAddSwappedTimeSpecRaisesValueError(self):
        with self.assertRaises(ValueError):
            item = minimum_item(time_spec="10:00-09:00")
            self.timecard.add(**item)

    def testAddEqualStartEndTimesRaisesValueError(self):
        with self.assertRaises(ValueError):
            item = minimum_item(time_spec="10:00-10:00")
            self.timecard.add(**item)

    def testAddAcceptsEmptyNotes(self):
        item = minimum_item(time_spec="10:00-11:00", notes="")
        self.timecard.add(**item)
        self.assertEqual(self.timecard.notes, "")

    def testAddSetsNotes(self):
        item = minimum_item(time_spec="10:00-11:00", notes="stuff")
        self.timecard.add(**item)
        self.assertEqual(self.timecard.notes, "stuff")

    def testAddAcceptsNotesAsList(self):
        item = minimum_item(time_spec="10:00-11:00", notes=["stuff"])
        self.timecard.add(**item)
        self.assertEqual(self.timecard.notes, "stuff")

    def testAddAcceptsEmptyTickets(self):
        item = minimum_item(time_spec="10:00-11:00", tickets="")
        self.timecard.add(**item)
        self.assertEqual(self.timecard.tickets, "")

    def testAddWithTwoItemsFromSameDaySumsTheHoursWorked(self):
        first_item = minimum_item(time_spec="09:00-11:00")
        second_item = minimum_item(time_spec="12:00-14:00")
        self.timecard.add(**first_item)
        self.timecard.add(**second_item)
        self.assertEqual(self.timecard.hours_worked, 4)

    def testTimecardsWithDifferentDatesHaveIndependentData(self):
        tc1 = Timecard("2015-06-01")
        item1 = minimum_item(
                time_spec="10:00-11:00",
                notes="blah blah",
                )
        tc1.add(**item1)

        tc2 = Timecard("2015-06-02")
        item2 = minimum_item(
                time_spec="16:00-20:00",
                notes="moo moo",
                )
        tc2.add(**item2)

        self.assertNotEqual(tc1, tc2)

    def testTimecardAcceptsDatetimeObjectAsDate(self):
        item_date = date(2015, 6, 1)
        timecard = Timecard(item_date)
        self.assertEqual(timecard.date, item_date)

# vim: expandtab shiftwidth=4 softtabstop=4
