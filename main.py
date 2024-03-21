# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
import json
import math

np.random.seed(804)
fn = sys.argv[0].split('/')[-1].split('.')[0]
filename = 'log/' + sys.argv[0].split('/')[-1].split('.')[0] + '.log'

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=filename, level=logging.INFO, format=LOG_FORMAT)

def create_black_list():
    white_list = []
    with open("white_list/glossary_white_list.json", "w+", encoding='utf-8') as f:
        f.write(json.dumps(white_list, ensure_ascii=False))

    '''
    论文专题
    :return
    '''

if __name__ == '__main__':
    create_black_list()