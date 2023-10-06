import unittest
from Clock import Clock


class ClockCreationTest(unittest.TestCase):

    def test_can_print_time_on_the_hours(self):
        """
        Test can print time on the hour
        """
        clock = Clock(8, 0)
        self.assertEqual("08:00", print(clock))

    def test_can_print_time_with_minutes(self):
        """
        Test can print time with minutes
        """
        clock = Clock(11, 9)
        self.assertEqual("11:09", print(clock))

    def test_midnight_prints_as_zero(self):
        """
        Test midnight prints as zero
        """
        clock = Clock(24, 0)
        self.assertEqual("00:00", print(clock))

    def test_hour_roll_over(self):
        """
        Test hour rollover
        """
        clock = Clock(25, 0)
        self.assertEqual("01:00", print(clock))

    def test_hour_rolls_over_continuously(self):
        """
        Test hour rolls over continuously
        """
        clock = Clock(1, 60)
        self.assertEqual("02:00", print(clock))

    def test_sixty_minutes_is_next_hour(self):
        """
        Test sixty minutes is next hour
        """
        clock = Clock(1, 60)
        self.assertEqual("02:00", print(clock))

    def test_minutes_roll_over(self):
        """
        Test minutes roll over
        """
        clock = Clock(0, 160)
        self.assertEqual("02:40", print(clock))

    def test_minutes_roll_over_continuously(self):
        """
        Test minutes roll over continuously
        """
        clock = Clock(0, 1723)
        self.assertEqual("04:43", print(clock))

    def test_hour_and_minutes_roll_over(self):
        """
        Test hour and minutes roll over
        """
        clock = Clock(25, 160)
        self.assertEqual("03:40", print(clock))

    def test_hour_and_minutes_roll_over_continuously(self):
        """
        Test hour and minutes roll over continuously
        """
        clock = Clock(201, 3001)
        self.assertEqual("11:01", print(clock))

    def test_hour_and_minutes_roll_over_to_exactly_midnight(self):
        """
        Test hour and minutes roll over to exactly midnight
        """
        clock = Clock(72, 8640)
        self.assertEqual("00:00", print(clock))

    def test_negative_hour(self):
        """
        Test negative hour
        """
        clock = Clock(-25, 0)
        self.assertEqual("23:00", print(clock))

    def test_negative_hour_rolls_over_continuously(self):
        """
        Test negative hour rolls over continuously
        """
        clock = Clock(-91, 0)
        self.assertEqual("05:00", print(clock))

    def test_negative_minutes(self):
        """
        Test negative minutes
        """
        clock = Clock(1, -40)
        self.assertEqual("00:20", print(clock))

    def test_negative_minutes_roll_over(self):
        """
        Test negative minutes roll over
        """
        clock = Clock(1, -160)
        self.assertEqual("22:20", print(clock))

    def test_negative_minutes_roll_over_continuously(self):
        """
        Test negative minutes roll over continuously
        """
        clock = Clock(1, -4820)
        self.assertEqual("16:40", print(clock))

    def test_negative_sixty_minutes_is_previous_hour(self):
        """
        Test negative 60 minutes is previous hour
        """
        clock = Clock(2, -60)
        self.assertEqual("01:00", print(clock))

    def test_negative_hour_and_minutes_both_roll_over(self):
        """
        Test negative hour and minutes both roll over
        """
        clock = Clock(-25, -160)
        self.assertEqual("20:20", print(clock))

    def test_negative_hour_and_minutes_both_roll_over_continuously(self):
        """
        Test negative hour and minutes both roll over continuously
        """
        clock = Clock(-121, -5810)
        self.assertEqual("22:10", print(clock))


if __name__ == '__main__':
    unittest.main()
