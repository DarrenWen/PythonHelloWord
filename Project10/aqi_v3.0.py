"""
    作者:付文军
    版本:v3.0
    日期:2018年12月12日
    功能:AQI计算
"""
import json
import csv

def process_json_file(file_path):
    """
        JSON文件处理
    """
    f = open(file_path, mode="r", encoding="utf-8")
    city_list = json.load(f)
    f.close()
    return  city_list


def main():
    """
        主函数
    """
    filepath = input("请输入json文件名称:")
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city["aqi"], reverse=True)
    lines = []
    lines.append(city_list[0].keys())
    for city in city_list:
        lines.append(list(city.values()))
    f = open('aqi.csv','w',encoding='utf-8',newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
