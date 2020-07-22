
import requests
import re
import pandas as pd


# 综合动态
def zhdt():
    html = requests.get('http://www.hangzhou.gov.cn/col/col812255/index.html?uid=4037001&pageNum=1')
    data = html.content.decode()
    pattern = re.compile(r"·<a.*?<br>")
    data_list = re.findall(pattern, data)
    result_list = []
    for i in data_list:
        title_parttern = re.compile(r"title='(.*?)'")
        url_parttern = re.compile(r"href='(.*?)'")
        time_pattern = re.compile(r"<span class='bt_time'>(.*?)</span>")
        title = re.findall(title_parttern, i)[0]
        url = 'http://www.hangzhou.gov.cn/' + re.findall(url_parttern, i)[0]
        time = re.findall(time_pattern,i)[0]
        print(url)
        print(title)
        print(time)
        result_dic = {'title': title, 'url': url,'time':time}
        result_list.append(result_dic)
    df = pd.DataFrame(result_list)
    df.to_excel('12.xlsx', index=False)


#市委动态
def swdt():
    html = requests.get('http://www.hangzhou.gov.cn/col/col812258/index.html')
    data = html.content.decode()
    print(data)
    pattern = re.compile(r"·<a.*?<br>")
    data_list = re.findall(pattern, data)

    result_list = []
    for i in data_list:
        title_parttern = re.compile(r"title='(.*?)'")
        url_parttern = re.compile(r"href='(.*?)'")
        time_pattern = re.compile(r"<span class='bt_time'>(.*?)</span>")
        title = re.findall(title_parttern, i)[0]
        url = 'http://www.hangzhou.gov.cn/' + re.findall(url_parttern, i)[0]
        time = re.findall(time_pattern, i)[0]
        print(url)
        print(title)
        print(time)
        result_dic = {'title': title, 'url': url,'time':time}
        result_list.append(result_dic)
    df = pd.DataFrame(result_list)
    df.to_excel('sw.xlsx', index=False)


#政府动态
def zfdt():
    html = requests.get('http://www.hangzhou.gov.cn/col/col812260/index.html')
    data = html.content.decode()
    pattern = re.compile(r"·<a.*?<br>")
    data_list = re.findall(pattern, data)

    result_list = []
    for i in data_list:
        title_parttern = re.compile(r"title='(.*?)'")
        url_parttern = re.compile(r"href='(.*?)'")
        time_pattern = re.compile(r"<span class='bt_time'>(.*?)</span>")
        title = re.findall(title_parttern, i)[0]
        url = 'http://www.hangzhou.gov.cn/' + re.findall(url_parttern, i)[0]
        time = re.findall(time_pattern, i)[0]
        print(url)
        print(title)
        print(time)
        result_dic = {'title': title, 'url': url,'time':time}
        result_list.append(result_dic)
    df = pd.DataFrame(result_list)
    df.to_excel('zf.xlsx', index=False)


#区县之窗
def qxzc():
    html = requests.get('http://www.hangzhou.gov.cn/col/col812264/index.html')
    data = html.content.decode()

    pattern = re.compile(r"·<a.*?<br>")
    data_list = re.findall(pattern, data)

    result_list = []
    for i in data_list:
        title_parttern = re.compile(r"title='(.*?)'")
        url_parttern = re.compile(r"href='(.*?)'")
        time_pattern = re.compile(r"<span class='bt_time'>(.*?)</span>")
        title = re.findall(title_parttern, i)[0]
        url = 'http://www.hangzhou.gov.cn/' + re.findall(url_parttern, i)[0]
        time = re.findall(time_pattern, i)[0]
        print(url)
        print(title)
        print(time)
        result_dic = {'title': title, 'url': url,'time':time}
        result_list.append(result_dic)
    df = pd.DataFrame(result_list)
    df.to_excel('qx.xlsx', index=False)


if __name__ == '__main__':
    zhdt()
    swdt()
    zfdt()
    qxzc()

# 因为网页数据的结构完全相同，所以可以只用一个函数传入不同的url和保存的文件名，提高代码的复用性，
# 但如果爬取的数据结构不同，建议还是使用一个函数或一个类爬取一类数据。