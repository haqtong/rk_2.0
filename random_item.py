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
            '项目质量管理', '项目采购管理', '项目沟通管理', '项目人力资源管理', '项目干系人管理', '合同管理', '八大绩效域']
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
    df = pd.read_csv(infnf, encoding='gbk')
    aim_dict = df.set_index('英文名')['中文名'].to_dict()
    # print(aim_dict)
    item = 'a'

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


def thesis_upgrade():
    '''
    当前训练为thesis 三层训练
    :return:
    '''
    infn = r'D:\program\data\a_rk_2\data\structure_data\thesis_structuring_data_bak.json'
    config_path = r'D:\program\data\a_rk_2\white_list\thesis_record_white_list.json'
    with open(config_path, 'r', encoding='utf_8') as f:
        thesis_record_white_list = json.load(f)
    with open(infn, 'r', encoding='utf_8') as f:
        thesis_dict = json.load(f)
    password = 'Y'
    while password == 'Y':
        thesis_hir1 = list(thesis_dict.keys())
        random_hir1_ = np.random.choice(thesis_hir1, 1)[0]
        thesis_hir2 = list(thesis_dict[random_hir1_].keys())
        random_hir2_ = np.random.choice(thesis_hir2, 1)[0]
        thesis_hir3 = ['输入', '工具', '输出']
        random_hir3_ = np.random.choice(thesis_hir3, 1)[0]
        if '-'.join([random_hir1_,random_hir2_,random_hir3_]) not in thesis_record_white_list:
            print('请输入{}-{}的{}'.format(random_hir1_, random_hir2_, random_hir3_))
            print('元素分隔符用#号')
            _ = input()
            if sorted(_.split('#')) == sorted(thesis_dict[random_hir1_][random_hir2_][random_hir3_]):
                print('通过')
                thesis_record_white_list.append('-'.join([random_hir1_,random_hir2_,random_hir3_]))
            else:
                print('回答错误')
                print('正确组件为：{}'.format(thesis_dict[random_hir1_][random_hir2_][random_hir3_]))
            print('是否继续判定，是：Y；否：~Y')
            password = input()

    with open(config_path, "w+", encoding='utf-8') as f:
        f.write(json.dumps(thesis_record_white_list, ensure_ascii=False))

if __name__ == '__main__':
    thesis_upgrade()
    # thesis()
    # glossory()
