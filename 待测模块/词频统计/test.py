import re


def remove_nontext(input):
    pattern = r'[^a-zA-Z\u4e00-\u9fa5]'  # 定义要匹配的非文字字符范围
    result = re.sub(pattern, '', input)  # 使用re.sub函数将非文字字符替换为空字符串
    return result


# 测试样例
input1 = "①组织过程资产"
output1 = remove_nontext(input1)
print("原始输入：", input1)
print("处理后结果：", output1)

input2 = "这是一个测试！"
output2 = remove_nontext(input2)
print("\n原始输入：", input2)
print("处理后结果：", output2)