# Playwright_Baidu
This is a Python+Pytest+Playwright automation test framework practice.

In this practice, a web page will be launched to access Baidu.com, then it will search the phrases in the test data file. Some assertions will be made to verify the test result. Browser type can be specified in the pytest.ini file. If 2 browser types are specified, for example: chromium and firefox, the testcases will run twice, one for chromium, another for firefox.

# Structure

**common**: directory for general tools.

**config**: directory for configuration file.

**data**: directory for test data files.

**pages**: directory for page files.

**tests**: directory for testcase files.

**main.py**: run automation test.

**pytest.ini**: pytest configuration file.

**requirements.txt**: packages that should be installed for this practice.

# How to run
Run main.py



