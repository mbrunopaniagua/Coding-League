import unittest
from Clock import Clock


class ClockAddTest(unittest.TestCase):

    def test_add_minutes(self):
        """
        Test add minutes
        """
        clock = Clock(10, 0)
        clock.add(3)
        self.assertEqual("10:03", print(clock))

    def test_add_no_minutes(self):
        """
        Test add no minutes
        """
        clock = Clock(6, 41)
        clock.add(0)
        self.assertEqual("06:41", print(clock))

    def test_add_to_next_hour(self):
        """
        Test add to next hour
        """
        clock = Clock(0, 45)
        clock.add(40)
        self.assertEqual("01:25", print(clock))

    def test_add_more_than_hour(self):
        """
        Test add more than hour
        """
        clock = Clock(10, 0)
        clock.add(61)
        self.assertEqual("11:01", print(clock))

    def test_add_more_than_two_hours_with_carry(self):
        """
        Test add more than two hours with carry
        """
        clock = Clock(0, 45)
        clock.add(160)
        self.assertEqual("03:02", print(clock))

    def test_add_across_midnight(self):
        """
        Test add across midnight
        """
        clock = Clock(23, 59)
        clock.add(2)
        self.assertEqual("00:01", print(clock))

    def test_add_more_than_one_day(self):
        """
        Test add more than one day
        """
        clock = Clock(5, 32)
        clock.add(1500)
        self.assertEqual("06:32", print(clock))

    def test_add_more_than_two_days(self):
        """
        Test add more than two days
        """
        clock = Clock(1, 1)
        clock.add(3500)
        self.assertEqual("11:21", print(clock))

    def test_subtract_minutes(self):
        """
        Test subtract minutes
        """
        clock = Clock(10, 3)
        clock.add(-3)
        self.assertEqual("10:00", print(clock))

    def test_subtract_to_previous_hour(self):
        """
        Test subtract to previous hour
        """
        clock = Clock(10, 3)
        clock.add(-30)
        self.assertEqual("09:33", print(clock))

    def test_subtract_more_than_an_hour(self):
        """
        Test subtract mote than an hour
        """
        clock = Clock(10, 3)
        clock.add(-70)
        self.assertEqual("08:53", print(clock))

    def test_subtract_across_midnight(self):
        """
        Test subtract across midnight
        """
        clock = Clock(0, 3)
        clock.add(-4)
        self.assertEqual("23:59", print(clock))

    def test_subtract_more_than_two_hours(self):
        """
        Test subtract more than two hours
        """
        clock = Clock(0, 0)
        clock.add(-160)
        self.assertEqual("03:55", print(clock))

    def test_subtract_more_than_one_day(self):
        """
        Test subtract more than one day
        """
        clock = Clock(5, 32)
        clock.add(-1500)
        self.assertEqual("04:32", print(clock))

    def test_subtract_more_than_two_days(self):
        """
        Test subtract more than two days
        """
        clock = Clock(2, 20)
        clock.add(-3000)
        self.assertEqual("00:20", print(clock))


if __name__ == '__main__':
    unittest.main()
