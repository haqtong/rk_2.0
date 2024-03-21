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


def get_structure_data_initialize():
    aim_dict = {}
    with open("thesis_structuring_data.json", "w+", encoding='utf-8') as f:
        f.write(json.dumps(aim_dict, ensure_ascii=False))


if __name__ == '__main__':
    get_structure_data_initialize()