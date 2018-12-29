"""
    作者:付文军
    版本:v4.0
    日期:2018年12月12日
    功能:AQI计算
"""
import json
import csv
import os

def process_json_file(file_path):
    """
        JSON文件处理
    """
    # f = open(file_path, mode="r", encoding="utf-8")
    # city_list = json.load(f)
    # f.close()
    # return  city_list
    with open(file_path, mode="r", encoding="utf-8") as f:
        city_list = json.load(f)
        print(city_list)


def process_csv_file(file_path):
    """
        CSV文件处理
    """
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))


def main():
    """
        主函数
    """
    filepath = input("请输入json文件名称:")
    file_name, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        process_json_file(filepath)
    elif file_ext == '.csv':
        process_csv_file(filepath)
    else:
        print('不支持的文件类型')


if __name__ == '__main__':
    main()
