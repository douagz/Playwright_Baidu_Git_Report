import pytest,os,re
from config.config import Config
from typing import Union


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #python -m pytest tests --headed --slowmo 1000
    #python -m pytest tests --browser chromium --browser firefox --headed --slowmo 1000 --verbose
    #python -m pytest tests --browser-channel chrome
    #python -m pytest tests --browser-channel msedge
    #$ python -m pytest tests --device "iPad Mini"
    #$ python -m pytest tests --browser webkit --device "iPhone 11"
    #$ python -m pytest tests --browser chromium --device "Pixel 5"
    #pytest.main(['-vs', 'testtmp/test_tmp1.py', '--browser=webkit', '--browser=chromium', '--browser=firefox'])
    #pytest.main(['-vs', 'testtmp/test_tmp2.py', '--browser=chromium'])
    #pytest.main(['-vs', 'tests/test_search.py', '--browser=chromium'])
    #pytest.main(['-vs', 'tests', '--headed','--browser=webkit', '--device=iPhone 11'])
    #pytest.main(['-vs', 'tests', '--headed', '--browser=chromium', '--browser=firefox', '--slowmo=1000','--screenshot=only-on-failure'])
    #python3 -m pytest tests -n 5 --browser chromium --browser firefox --browser webkit
    #pytest.main(['-vs', 'tests', '--headed'])
    #pytest.main(['-vs', 'tests', '--headed', '--browser=chromium', '--browser=firefox', '--slowmo=1000','--video=retain-on-failure'])

    #x='abcakfasdlfkafkaa/jpress/user/registerb'
    #y='.jpress/user/register'
    #res,res_grp=find_str(x,y)
    #print(res,res_grp)

    AllureReport = Config.test_report_dir
    AllureResult = Config.test_result_dir
    Screenshot = Config.test_screenshot_dir
    #os.system(f"del {os.path.join(Screenshot, '*.png')}")
    #pytest.main(["-vs", 'tests', f'--alluredir={AllureResult}', "--clean-alluredir"])
    pytest.main(['-vs', 'tests'])
    #os.system(f'allure generate {AllureResult} -o {AllureReport} --clean')



