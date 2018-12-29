"""
    作者:付文军
    版本:v2.0
    日期:2018年12月12日
    功能:AQI计算
"""
import json


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
    top5_list = city_list[:5]

    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()
