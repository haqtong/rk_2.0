# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
import json
import math

fn = sys.argv[0].split('/')[-1].split('.')[0]
filename = 'log/' + sys.argv[0].split('/')[-1].split('.')[0] + '.log'

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename=filename, level=logging.INFO, format=LOG_FORMAT)


def thesis():
    '''
    论文
    :return:
    '''
    list = ['项目整体管理', '项目范围管理', '项目风险管理', '项目成本管理', '项目进度管理',
            '项目质量管理', '项目采购管理', '项目沟通管理', '项目人力资源管理', '项目干系人管理','合同管理','八大绩效域']
    _ = np.random.choice(list, 1)

    print(_)

def glossory():
    '''
    英文
    :return:
    '''
    infnf = r'data\英文'
    with open('white_list/glossary_white_list.json', encoding='utf-8') as f:
        glossary_white_list = json.load(f)
    df = pd.read_csv(infnf,encoding='gbk')
    aim_dict = df.set_index('英文名')['中文名'].to_dict()
    # print(aim_dict)
    item ='a'

    while item == 'a':
        key = 1
        while key:
            _ = np.random.choice(list(aim_dict.keys()), 1)
            if _ not in glossary_white_list:
                print(_)
                key = 0
        print('请输入中文名：')
        cn = input()
        if aim_dict[_[0]] == cn:
            print('pass')
            glossary_white_list.append(_[0])
        else:
            print(aim_dict[_[0]])

        print('是否继续：换行，结束 其他任意键')
        item = input()

    with open("white_list/glossary_white_list.json", "w+", encoding='utf-8') as f:
        f.write(json.dumps(glossary_white_list, ensure_ascii=False))



    print('当前学习进度{}/353'.format(len(glossary_white_list)))

if __name__ == '__main__':
    thesis()
    # glossory()
