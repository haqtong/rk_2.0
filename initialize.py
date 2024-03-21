# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
import json

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='initialize.log', level=logging.INFO, format=LOG_FORMAT)


def exec():
    list_1 = [ 'data', 'tag', 'log']
    list = list_1
    for path_item in list:
        if os.path.exists(path_item):
            pass
        else:
            os.makedirs(path_item)


if __name__ == '__main__':
    exec()

#data_check 模块
