import os


class Config:
    # 项目地址
    url = "https://baidu.com"

    # 项目目录
    root_dir = os.path.split(os.path.split(__file__)[0])[0]
    test_cases_dir = root_dir + os.path.sep + "tests"
    test_data_dir = root_dir + os.path.sep + "data"
    test_report_dir = root_dir + os.path.sep + "report" + os.path.sep + "AllureReport"
    test_result_dir = root_dir + os.path.sep + "report" + os.path.sep + "AllureResult"
    test_screenshot_dir = root_dir + os.path.sep + "report" + os.path.sep + "Screenshot"
    logs_dir = root_dir + os.path.sep + "Logs"

    # 权限认证目录
    auth_dir = root_dir + os.path.sep + "auth"

    # 测试文件
    baidu_search_data_file = root_dir + os.path.sep + "data/baidu_search.yml"


if __name__ == '__main__':
    print(Config.root_dir)
    print(Config.test_cases_dir)
