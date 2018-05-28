# yxmc="船舶海洋与建筑工程学院"
# xm="许劲松"
# zcmc="副教授  "
# kcmc="海洋结构物动力学  "
# kcbm="001-(2018-2019-1)NA317(教学班)  "
# xqxs="32"
# xqxf="2.0"
# sjms="行课安排为第1-8周,其中:&#xD;&#xA;星期一  第3节--第4节&#xD;&#xA;东下院111(1-8周) 许劲松(1-8周)&#xD;&#xA;星期三  第3节--第4节&#xD;&#xA;东下院111(1-8周) 许劲松(1-8周)&#xD;&#xA;"
# bz="限船舶专业  "
# nj="2015"
# xn="2018-2019"
# xq="1"
# yqdrs="0"

from bs4 import BeautifulSoup
import json
from model import attr


def parseNode(node):
    info = {}
    for key in attr.keys():
        o_O = node.get(key)
        info[key] = o_O.replace('\r', '').strip() if o_O else o_O
    return info


def main():
    with open('Store.xml', encoding='utf-8') as f:
        data = f.read()

    nodelst = BeautifulSoup(data, 'lxml').find_all('detail')
    lessonlst = []
    for node in nodelst:
        lessonlst.append(parseNode(node))

    with open('LessonArrangeForOthers.js', 'w', encoding="utf-8") as f:
        f.write('var data = '+json.dumps(lessonlst, ensure_ascii=False))
        print(len(lessonlst))
    # with open('LessonArrangeForOthers.json', 'w', encoding="utf-8") as f:
    #     f.write(json.dumps(lessonlst, ensure_ascii=False))
    #     print(len(lessonlst))


if __name__ == '__main__':
    main()
