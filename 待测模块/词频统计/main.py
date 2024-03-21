from collections import Counter
import re
import pandas as pd

def get_item_dict(path):
    black_list = ['词频','①','②','③']
    list_ = []
    switch = 0
    with open(path) as f:
        for line in f:
            mes = line.strip().split('；')
            if mes[0] =='词频':
                switch = 1
            if mes[0] =='log':
                switch = 0
            if switch == 1:
                for item in mes:
                    pattern = r'[^a-zA-Z\u4e00-\u9fa5]'  # 定义要匹配的非文字字符范围
                    new_item = re.sub(pattern, '', item)
                    if new_item not in black_list:
                        list_.append(new_item)
    return list_

import os
tokens = []
freq_dict_ = dict()
path_  = '../../data'
for root in os.listdir(path_):
    if root.find('项目')>0:
        path_hier2 = path_+'/'+root
        list_ = get_item_dict(path_hier2)
        tokens.extend(list_)

freq_dict = Counter(tokens)

df = pd.DataFrame(list(freq_dict.items()),
                   columns=['word', 'freq'])

df.to_excel('output.xlsx',index = 0)