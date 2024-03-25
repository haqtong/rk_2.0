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


with open(r'../../white_list/thesis_structuring_white_list.json', encoding='utf-8') as f:
    thesis_structuring_white_list = json.load(f)

with open(r'../../data/structure_data/thesis_structuring_data.json', encoding='utf-8') as f:
    thesis_structuring_data = json.load(f)

aim_dict = {}
def main():
    aim_list = ['项目整体管理', '项目范围管理', '项目风险管理', '项目成本管理', '项目进度管理',
            '项目质量管理', '项目采购管理', '项目沟通管理', '项目人力资源管理', '项目干系人管理']
    item ='a'

    while item == 'a':
        key = 1
        while key:
            _ = np.random.choice(aim_list, 1)[0]
            if _ not in thesis_structuring_white_list:
                print(_)
                key = 0
                print('请输入当前管理的过程组清单：')
                process_group_str = input()
                process_group_list = process_group_str.split('#')
                thesis_structuring_data[_] = {}
                for process in process_group_list:
                    print('请输入{}的输入'.format(process))
                    input_str = input()
                    input_list = input_str.split('#')
                    print('请输入{}的工具'.format(process))
                    tool_str = input()
                    tool_list = tool_str.split('#')
                    print('请输入{}的输出'.format(process))
                    output_str = input()
                    output_list = output_str.split('#')
                    print(_)
                    thesis_structuring_data[_][process] = {}
                    thesis_structuring_data[_][process]['输入'] = input_list
                    thesis_structuring_data[_][process]['工具'] = tool_list
                    thesis_structuring_data[_][process]['输出'] = output_list


        print('是否继续：换行，结束 其他任意键')
        item = input()
        thesis_structuring_white_list.append(_)
    with open("../../white_list/thesis_structuring_data.json", "w+", encoding='utf-8') as f:
        f.write(json.dumps(thesis_structuring_white_list, ensure_ascii=False))

    with open("../../data/structure_data/thesis_structuring_data.json", "w+", encoding='utf-8') as f:
        f.write(json.dumps(thesis_structuring_data, ensure_ascii=False))

if __name__ == '__main__':
    main()