import unittest

import os


class TestNativeSetup(unittest.TestCase):
    def test_list_subdirectories(self):
        from native import native_setup
        os.mkdir('./test1')
        os.mkdir('./test1/test2')
        native_setup.list_subdirectories('./')
    

if __name__ == "__main__":
    os.system('clear')
    unittest.main()