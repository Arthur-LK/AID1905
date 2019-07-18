"""
编写接口函数，从终端输入端口名称获取端口运行状态中的
地址值

思路分析：
1. 根据输入的端口名称找到对应的段落
2. 在该段落中匹配address
"""

import re

def get_adderss(port):
    f = open('exc.txt')
    while True:
        # 获取一段内容
        data = ''
        for line in f:
            if line == '\n':
                break
            data += line

        # data为空说明到了文档结尾
        if not data:
            break

        obj = re.match(port,data) # 匹配开始位置
        # 如果obj不为None data就是目标段落
        if obj:
            # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"
            obj = re.search(pattern,data)
            return obj.group()
    return "没有该端口"


if __name__ == '__main__':
    port = input("端口:")
    print(get_adderss(port))






