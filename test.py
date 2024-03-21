# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
import json
import math
import re
from collections import Counter

np.random.seed(804)
fn = sys.argv[0].split('/')[-1].split('.')[0]
filename = 'log/' + sys.argv[0].split('/')[-1].split('.')[0] + '.log'

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=filename, level=logging.INFO, format=LOG_FORMAT)


def exec():
    # declare
    infn = r'D:\program\data\软考\data\3_项目进度管理.txt'
    key_words = []
    major_item = ['项目整体管理','项目进度管理','项目范围管理']
    # major
    with open(infn, 'r') as f:
        for line in f:
            # print(line)
            mes = line.strip().split('；')
            for item in mes:
                new_item = re.sub("[^\u4e00-\u9fff]+", "", item)
                if new_item not in major_item:
                    key_words.append(new_item)
    result = Counter(key_words)
    print(result)





if __name__ == '__main__':
    exec()