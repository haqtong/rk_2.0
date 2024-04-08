# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
import json

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='short_term.log', level=logging.INFO, format=LOG_FORMAT)


def get_these_item_white_list():
    aim_list = []
    with open("thesis_structuring_white_list.json", "w+", encoding='utf-8') as f:
        f.write(json.dumps(aim_list, ensure_ascii=False))

def get_these_record_white_list():
    aim_list = []
    with open("thesis_record_white_list.json", "w+", encoding='utf-8') as f:
        f.write(json.dumps(aim_list, ensure_ascii=False))


if __name__ == '__main__':
    # get_these_item_white_list()
    get_these_record_white_list()