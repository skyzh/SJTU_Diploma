from requests import session
import json
from io import BytesIO
# 在此填入i.sjtu.edu.cn的cookies
cookies = {
    'JSESSIONID': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'kc@i.sjtu.edu.cn': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
}

# 在此填入学年和学期(1:秋季学期，2:春季学期，3:夏季小学期)
xuenian = '2020-2021'
xueqi = 1
filename = 'lessionData_{}_{}.json'.format(xuenian, xueqi)

# 功能模块：按条件查询上课情况
requestUrl = 'https://i.sjtu.edu.cn/design/funcData_cxFuncDataList.html?func_widget_guid=DA1B5BB30E1F4CB99D1F6F526537777B&gnmkdm=N219904'


def getData(xueqi, xuenian, maxDataCount):
    xueqi_map = {1: '3', 2: '12', 3: '16'}
    requestData = {
        'xnm': xuenian[:4],
        'xqm': xueqi_map[xueqi],
        'queryModel.showCount': str(maxDataCount),  # 最大获取数
        'queryModel.currentPage': '1',
        'queryModel.sortName': '',
        'queryModel.sortOrder': 'asc'
    }

    s = session()
    s.cookies.update(cookies)
    r = s.post(requestUrl, data=requestData, stream=True)
    dataIO = BytesIO()
    for chunk in r.iter_content(chunk_size=2048):
        if chunk:
            dataIO.write(chunk)
    r.close()
    dataIO.seek(0)
    dataBinary = dataIO.read()
    return dataBinary


print('当前任务：{}学年第{}学期'.format(xuenian, xueqi))
print('正在获取测试数据，大约需要10秒，请等待')
dataBinary = getData(xueqi, xuenian, 15)
lessionData = json.loads(dataBinary.decode('utf8'))['items']
if len(lessionData) == 15:
    print('测试成功，数据长度符合预期')
else:
    raise Exception('测试失败，数据长度不匹配，期望15，实际%d' % len(lessionData))

print('正在请求数据，大约需要3分钟，请耐心等待')
dataBinary = getData(xueqi, xuenian, 10000)
lessionData = json.loads(dataBinary.decode('utf8'))['items']
print('数据请求完成，大小：%d字节' % len(dataBinary))


with open(filename, "w", encoding='utf8') as f:
    json.dump(lessionData, f, ensure_ascii=False)
print('《{}学年第{}学期课程信息》已经成功保存至文件"{}"，共包含课程{}门'.format(
    xuenian, xueqi, filename, len(lessionData)))
