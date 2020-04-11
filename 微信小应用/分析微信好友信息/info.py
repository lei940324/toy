import itchat
import pandas as pd
from pyecharts.charts import Pie, Map, Page, Bar
from pyecharts import options as opts


# 根据key值得到对应的信息
def get_key_info(friends_info, key):
    return list(map(lambda friend_info: friend_info.get(key), friends_info))


# 获得所需的微信好友信息
def get_friends_info():
    friends = itchat.get_friends()
    friends_info = dict(
        # 省份
        province = get_key_info(friends, "Province"),
        # 城市
        city = get_key_info(friends, "City"),
        # 昵称
        nickname = get_key_info(friends, "NickName"),
        # 性别
        sex = get_key_info(friends, "Sex"),
        # 签名
        signature = get_key_info(friends, "Signature"),
        # 备注
        remarkname = get_key_info(friends, "RemarkName"),
        # 用户名拼音全拼
        pyquanpin = get_key_info(friends, "PYQuanPin")
    )
    df = pd.DataFrame(friends_info)
    return df


# 性别分析
def analysisSex():
    friends_info = get_friends_info()
    df = pd.DataFrame(friends_info)
    sex_count = df.groupby(['sex'], as_index=True)['sex'].count()
    temp = dict(zip(list(sex_count.index), list(sex_count)))
    data = {}
    data['保密'] = temp.pop(0)
    data['男'] = temp.pop(1)
    data['女'] = temp.pop(2)

    # 画图
    c = (
    Pie()
    .add("", [list(z) for z in zip(data.keys(), data.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="微信好友性别比"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("微信好友性别比.html")
)


# 省份分析
def analysisProvince():
    province_count = df.groupby('province', as_index=True)['province'].count().sort_values()
    data = list(map(lambda x: x if x != '' else '未知', list(province_count.index)))
    # 画图
    page = Page()
    chart1 = (
    Map()
    .add("人数", [list(z) for z in zip(data, list(province_count))], "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="好友分布(中国地图)"),
                     visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=False))
    )
    page.add(chart1)
    
    chart2 = (
     Bar()
    .add_xaxis(data)
    .add_yaxis('人数', list(province_count))
    .set_global_opts(title_opts=opts.TitleOpts(title="好友分布柱状图"))
    )
    page.add(chart2)
    page.render('好友分布分析.html')
    
    
    
# 具体省份分析
def analysisCity(province):
    temp1 = df.query('province == "%s"' % province)
    city_count = temp1.groupby('city', as_index=True)['city'].count().sort_values()
    attr = list(map(lambda x: '%s市' % x if x != '' else '未知', list(city_count.index)))
    value = list(city_count)
    # 画图
    page = Page()
    chart1 = (
    Map()
    .add("人数", [list(z) for z in zip(attr, value)], province)
    .set_global_opts(title_opts=opts.TitleOpts(title="好友分布(中国地图)"),
                     visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=False))
    )
    page.add(chart1)
    
    chart2 = (
     Bar()
    .add_xaxis(attr)
    .add_yaxis('人数', value)
    .set_global_opts(title_opts=opts.TitleOpts(title="好友分布柱状图"))
    )
    page.add(chart2)
    page.render(f'{province}省分布分析.html')
    



if __name__ == '__main__':
    itchat.auto_login()
    df = get_friends_info()
    
    analysisSex()
    analysisProvince()
    analysisCity("山东")

