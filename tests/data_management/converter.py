import unittest
from head.data_management import DataConverter
from head.messages.messages import Messages as Msg


class DataConverterTest(DataConverter, unittest.TestCase):
    def test_to_float(self):
        func = self.to_float
        err_msg = Msg.must_be_number
        cases = (
            ([1, 2, 3], ([1.0, 2.0, 3.0], False)),
            ((i for i in range(0, 4)), ([0.0, 1.0, 2.0, 3.0], False)),
            ((i for i in "wee"), ([None]*3, [err_msg]*3)),
            ([1, -2, 3], ([1.0, -2.0, 3.0], False)),
            ([1, 2, 3.2], ([1.0, 2.0, 3.2], False)),
            (2, (2.0, False)),
            ("\n", (None, err_msg)),
            ([1, "2f", 3.2], ([1.0, None, 3.2], [0, err_msg, 0])),
            ([1, None, 3], ([1.0, None, 3.0], [0, err_msg, 0])),
            ([-2, "sas", 3], ([-2.0, None, 3.0], [0, err_msg, 0])),
        )

        for case, expected_result in cases:
            with self.subTest(case=case):
                self.assertEqual(func(case), expected_result)


if __name__ == "__main__":
    unittest.main()
