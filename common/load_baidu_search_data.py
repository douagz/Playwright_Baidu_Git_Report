import yaml
from config.config import Config


def load_baidu_search_data():
    with open(Config.baidu_search_data_file, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data

