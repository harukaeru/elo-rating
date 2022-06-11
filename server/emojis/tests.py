from django.test import TestCase
from .logics import calculate_elo

# Create your tests here.
class EloTestCase(TestCase):
    def test_is_mirror1(self):
        left_ans = calculate_elo(-200, 200, True)
        right_ans = calculate_elo(200, -200, False)

        self.assertEqual(left_ans[0], right_ans[1])
        self.assertEqual(left_ans[1], right_ans[0])

    def test_is_mirror2(self):
        left_ans = calculate_elo(-300, 104, True)
        right_ans = calculate_elo(104, -300, False)

        self.assertEqual(left_ans[0], right_ans[1])
        self.assertEqual(left_ans[1], right_ans[0])

