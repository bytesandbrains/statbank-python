import statbank

import unittest


class TestService(unittest.TestCase):

    def test_tables(self):
        self.assertEqual(statbank.tableinfo('aup03').id, 'aup03')

if __name__ == '__main__':
    unittest.main()
