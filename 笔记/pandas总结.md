[TOC]

# pandas总结

## 基本操作

**详见[Pandas中文网](https://www.pypandas.cn/docs/getting_started/10min.html#%E7%94%9F%E6%88%90%E5%AF%B9%E8%B1%A1)**

###  导入库

```python
import numpy as np
import pandas as pd 
```

* 获取pandas的版本号

```python
In [1]: pd.__version__ 
Out[1]: '1.0.1'
```



###  读取文件

#### 读取excel文件

* hs300这列为字符串；其中除了可以指定具体Sheet的名字，还可以传入Sheet的顺序，从0开始计数，如果不指定sheet_name参数时，那么默认导入的都是第一个Sheet的文件。

```python
In [1]: 
df = pd.read_excel('上证指数与沪深300.xlsx', 
                   sheet_name = "Sheet1",
                   dtype = {'hs300':str})  
In [2]:df
Out[2]: 
            日期      hs300         sz
0   2019-11-22  3849.9948  2885.2884
1   2019-11-21   3889.598  2903.6379
2   2019-11-20  3907.8641  2911.0534
3   2019-11-19  3947.0392  2933.9908
4   2019-11-18  3907.9291  2909.2002
..         ...        ...        ...
455 2018-01-08  4160.1595  3409.4795
456 2018-01-05  4138.7505  3391.7501
457 2018-01-04  4128.8119  3385.7102
458 2018-01-03  4111.3925  3369.1084
459 2018-01-02  4087.4012  3348.3259

[460 rows x 3 columns]
```

* 将第一列作为日期，index_col = 0表示第一列作为行索引；header=0表示第一行作为列索引；usecols参数来指定要导入的列。

```python
In [1]: 
df = pd.read_excel('上证指数与沪深300.xlsx', 
                  parse_dates = True, 
                  index_col = 0,
                  header = 0,
                  usecols = [0,1,2] )
In [2]: df
Out[10]: 
                hs300         sz
日期                              
2019-11-22  3849.9948  2885.2884
2019-11-21  3889.5980  2903.6379
2019-11-20  3907.8641  2911.0534
2019-11-19  3947.0392  2933.9908
2019-11-18  3907.9291  2909.2002
              ...        ...
2018-01-08  4160.1595  3409.4795
2018-01-05  4138.7505  3391.7501
2018-01-04  4128.8119  3385.7102
2018-01-03  4111.3925  3369.1084
2018-01-02  4087.4012  3348.3259

[460 rows x 2 columns]
```

#### 读取csv文件

分割符号为空格，编码方式为gbk，启动器为python（防止路径存在中文时报错）

```python
df = read_csv('文件名', sep = ' ', encoding = "gbk", engine = "python")
```

#### 读取txt文件

```python
df = read_table('文件名', sep = ',')
```

#### 读取数据库sql文件

```python
import pymysql

# 创建连接
eng = pymysql.connect(host = 'localhost' , user = 'user',
                      password = 'passwd'，db = 'db', charset = 'utf8'）
# user：用户名
# password：密码
# host：数据库地址/本机使用localhost
# db：数据库名
# charset：数据库编码，一般为UTE-8
                      
df = pd.read_sql(sql,eng)    # sql为需要执行的sql语句
```



### 保存文件

#### 保存为excel文件

索引去掉，sheet名为测试文档,导出hs300与sz这列数据；设置columns参数来指定要导出的列；na_rep=0表示缺失值填充为0；inf_rap = 0 表示 inf 值填充为0；float_format保留三位小数

```python
df.to_excel(excel_writer = r'测试.xlsx',  
            sheet_name = '测试文档',       
            columns = ['hs300','sz'],
            index = False,
           	encoding = 'utf-8',
           	na_rep = 0,
           	inf_rap = 0,
            float_format='%.3f')                  
```

#### 保存为csv文件

设置.csv 文件的导出路径时，与设置.xlsx 文件的导出路径一样，但是参数不一样，.csv文件的导出路径需通过path_or_buf参数来设置；sep表示分隔符

```python
df.to_csv(path_or_buf = '路径名', sep = ' ')
```



##  清洗数据

### 按选定列去重

还可以自定义删除重复项时保留哪个，默认保留第一个，也可以设置保留最后一个，或者全部不保留。通过传入参数keep进行设置，参数keep默认值是first，即保留第一个值；也可以是last，保留最后一个值；还可以是False，即把重复值全部删除。

```python
df = df.drop_duplicates(['name','year','stkcd'], keep = 'first')
```



### 更改索引

```python
df = df.reset_index(drop=True)    # 重置索引
df.set_index('a')                 # 设置a列为索引
```



### 把字符串数据传换成日期数据

```python
df['date'] = pd.to_datetime(df['指标名称']) 
```



###  缺失值处理

#### 查找缺失值

```python
df.isnull()     
df[df['age'].isnull()]          # 获取age值缺失的行
```

* 查找缺失值的位置，并返回缺失值行号以及列号

```python
In [1]:
import pandas as pd
data = [[None, None, 90, 80],[57, 43, 89, 65],[78, 50, 67, 78],[None, 78, 90, 73],[67, 45, 78, 76],[77, 88, None, 45],[52, 110, 120, 99],[131, 13, 32, 12]]
index = ['语文', '英语', '数学', '政治', '物理', '化学', '生物', '地理']
column = ['张三', '李四', '王五', '周六']
data = pd.DataFrame(data,index=index,columns=column)
print(data)
print("=========================================================\n")

for columname in data.columns:
    if data[columname].count() != len(data):
         loc = data[columname][data[columname].isnull().values==True].index.tolist()
         print('列名："{}", 第{}行位置有缺失值'.format(columname,loc))
        
Out[1]: 
       张三     李四     王五  周六
语文    NaN    NaN   90.0  80
英语   57.0   43.0   89.0  65
数学   78.0   50.0   67.0  78
政治    NaN   78.0   90.0  73
物理   67.0   45.0   78.0  76
化学   77.0   88.0    NaN  45
生物   52.0  110.0  120.0  99
地理  131.0   13.0   32.0  12
=========================================================

列名："张三", 第['语文', '政治']行位置有缺失值
列名："李四", 第['语文']行位置有缺失值
列名："王五", 第['化学']行位置有缺失值
```

#### 修改缺失值

```python
df = df.dropna()                  # 删除含有缺失值的行
df = df.dropna(how = 'all')       # 删除空白行，只删除那些全为空值的行
df.dropna(how = 'any')            # 删除所有含缺失值的行
df = df.fillna(value = 0)         # 补齐法(赋值0)
df = df.fillna(method = 'ffill')  # 补齐法(向前填充)
df = df.fillna(method = 'bfill')  # 补齐法(向后填充)
df = df.fillna({'性别':'男'})      # 对某列填充，只对性别列缺失值补充为男
```



## 查看并获取数据

### 查看数据

```python
df.describe()          # 描述性统计
df.head()              # 查看表头
df.head(4)             # 查看前4行
df.tail()              # 查看表尾
df.info()              # 输出整个表中所有列的数据类型。
```

* 显示索引与列名

```python
In [1]: df.index
Out[1]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

In [2]: df.columns
Out[2]: Index(['A', 'B', 'C', 'D'], dtype='object')
```



### 获取数据

```python
df['A'] ;df[['f1','f2']]        # 获取单列,多列
df.values                       # 获取序列值
df.shape                        # 获取行列数
df.loc[0:5, ['f1', 'f2']]       # 通过标签同时在两个轴上切片
df['age'].sum()                 # 计算age列的总和
df['stkcd'].value_counts()      # 计算stkcd的每个股票代码的数量
```

* 获取某列/某几列

```python
In [8]: df = pd.DataFrame(np.random.randn(5,5))

In [9]: df
Out[9]: 
          0         1         2         3         4
0 -0.696858  0.333139 -0.573525  0.014137 -0.238860
1 -1.891888  0.200042 -0.119071  0.606198  0.836731
2  0.247054 -0.617390 -0.499058  0.286085 -0.733036
3 -0.561588 -0.237216 -0.059110 -0.442450 -1.923475
4  1.933672  0.380029 -0.041450 -1.292448  1.416120

In [10]: df.iloc[:,[0,1]]
Out[10]: 
          0         1
0 -0.696858  0.333139
1 -1.891888  0.200042
2  0.247054 -0.617390
3 -0.561588 -0.237216
4  1.933672  0.380029

In [11]: df.iloc[1:4,1:3]
Out[11]: 
          1         2
1  0.200042 -0.119071
2 -0.617390 -0.499058
3 -0.237216 -0.059110
```



### 筛选数据

```python
df[(df['开盘价']>4100)&(df['收盘价']<=4200)]     # 条件性截取
df[df['列名'].isin(['相应的值'])]                # 获取某值所在的行
df[df['列名'].isin(['相应的值'])].index          # 获取某值所在的行号
df['name'].unique()                            # 获取某列唯一值
```

* 列表达式：df.query('a<b')，可以用&表示与；|表示逻辑或

  ```python
  In [1]: 
  import pandas as pd
  import numpy as np
  df = pd.DataFrame(np.random.randn(10,2),columns=list('ab'))
  
  In [2]: df
  Out[2]: 
            a         b
  0 -0.482305 -1.708220
  1 -0.736760  0.820898
  2 -0.875194 -0.086371
  3  0.572075  0.791663
  4 -0.918758  1.286178
  5  0.983193 -0.252690
  6  0.377285  0.624212
  7  0.611985 -1.793063
  8 -0.289774 -1.262484
  9 -1.300345 -0.418877
  
  In [3]: df.query('a < b')
  Out[3]: 
            a         b
  1 -0.736760  0.820898
  2 -0.875194 -0.086371
  3  0.572075  0.791663
  4 -0.918758  1.286178
  6  0.377285  0.624212
  9 -1.300345 -0.418877
  ```

  

##  操作数据

### 转置数据

```python
df = df.T
```



### 追加数据

```python
In [87]: df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])

In [88]: df
Out[88]: 
          A         B         C         D
0  1.346061  1.511763  1.627081 -0.990582
1 -0.441652  1.211526  0.268520  0.024580
2 -1.577585  0.396823 -0.105381 -0.532532
3  1.453749  1.208843 -0.080952 -0.264610
4 -0.727965 -0.589346  0.339969 -0.693205
5 -0.339355  0.593616  0.884345  1.591431
6  0.141809  0.220390  0.435589  0.192451
7 -0.096701  0.803351  1.715071 -0.708758

In [89]: s = df.iloc[3]

In [90]: df.append(s, ignore_index=True)
Out[90]: 
          A         B         C         D
0  1.346061  1.511763  1.627081 -0.990582
1 -0.441652  1.211526  0.268520  0.024580
2 -1.577585  0.396823 -0.105381 -0.532532
3  1.453749  1.208843 -0.080952 -0.264610
4 -0.727965 -0.589346  0.339969 -0.693205
5 -0.339355  0.593616  0.884345  1.591431
6  0.141809  0.220390  0.435589  0.192451
7 -0.096701  0.803351  1.715071 -0.708758
8  1.453749  1.208843 -0.080952 -0.264610
```



###  数据格式

* 查看数据类型

```python
df.dtypes         # 对所有列数据进行查看
df['日期'].dtype   # 对某列进行查看
```

* 更改数据类型

```python
df['Chinese'].astype('str')
df['Chinese'].astype(np.int64)
```



###  删除数据

```python
df = df.drop('行名或列名', axis = 0)    # 删除第0行,当axis=1表示删除某列,默认axis=0
df = df.drop(columns=['Chinese'])     # 删除某列
df = df.drop(index=['80'])            # 删除某行
```



### apply()与applymap()函数

apply()对某一行或列中的元素执行相同的函数操作，applymap()对每一个元素执行相同的函数操作。

```python
df['C1'].apply(lambda x:x+1)          # 对C1列元素加1
df.applymap(lambda x:x+1)             # 对df里的每个元素都加1
df.apply(lambda x:x.sum(), axis=1)    # 生成加总列
df.apply(lambda x:x.sum(), axis=0)    # 生成加总行
```



###  重命名行列名

```python
df.rename({1: 2, 2: 4}, axis='index')               # 重命名行名
df.rename(index=str, columns={"A": "a", "B": "c"})  # 重命名列名
```



###  替换数据

* 将priority列中的yes, no替换为布尔值True, False

  ```python
  df['priority'] = df['priority'].map({'yes': True, 'no': False})
  ```

* 将animal列中的snake替换为python

  ```python
  df['animal'] = df['animal'].replace('snake', 'python')
  ```



### 排序

* 按轴排序，axis=1表示列指标，0表示行标；ascending为True表示正序

  ```python
  df.sort_index(axis=1, ascending=True)
  ```

* 按某列值排序

  ```python
  df.sort_values(by='B', ascending=True)
  ```

* 先按age降序排列，后按visit升序排列

  ```python
  df.sort_values(by=['age','visit'],ascending[False,True])
  ```

  

### 分组

```python
In [91]: df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
   ....:                          'foo', 'bar', 'foo', 'foo'],
   ....:                    'B': ['one', 'one', 'two', 'three',
   ....:                          'two', 'two', 'one', 'three'],
   ....:                    'C': np.random.randn(8),
   ....:                    'D': np.random.randn(8)})
   ....: 

In [92]: df
Out[92]: 
     A      B         C         D
0  foo    one -1.202872 -0.055224
1  bar    one -1.814470  2.395985
2  foo    two  1.018601  1.552825
3  bar  three -0.595447  0.166599
4  foo    two  1.395433  0.047609
5  bar    two -0.392670 -0.136473
6  foo    one  0.007207 -0.561757
7  foo  three  1.928123 -1.623033
```

先分组，再用 [`sum()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html#pandas.DataFrame.sum)函数计算每组的汇总数据：

```python
In [93]: df.groupby('A').sum()
Out[93]: 
            C        D
A                     
bar -2.802588  2.42611
foo  3.146492 -0.63958
```

多列分组后，生成多层索引，也可以应用 `sum` 函数：

```python
In [94]: df.groupby(['A', 'B']).sum()
Out[94]: 
                  C         D
A   B                        
bar one   -1.814470  2.395985
    three -0.595447  0.166599
    two   -0.392670 -0.136473
foo one   -1.195665 -0.616981
    three  1.928123 -1.623033
    two    2.414034  1.600434
```



### 其他操作

```python
df.iterrows()                                           # 对行遍历
df.insect(2,'name',['liming','xiaoming')                # 插入一个新的列
df['Chinese'] = df['Chinese'].map(str.strip)            # 删除数据两边空格
df.loc[i,'appoint2'] = 0                                # 按行列号赋值
df.rolling(window=窗口数,axis=0或1).统计量函数(axis=0或1)   # 移动窗口函数
df.cut(df['年龄'],3,bins = [0,3,6,10])                   # 区间切分
```



##  创建序列

```python
time = pd.Series([1,2],index = ['1994','1995'])  # 创建时间序列{'a':1, 'b':2})
time = pd.Series({'a':1, 'b':2})
data = pd.DataFrame(data,index,columns)          # 创建数据框
```

* 用索引自动对齐新增列的数据：

  ```python
  In [45]: s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
  
  In [46]: s1
  Out[46]: 
  2013-01-02    1
  2013-01-03    2
  2013-01-04    3
  2013-01-05    4
  2013-01-06    5
  2013-01-07    6
  Freq: D, dtype: int64
  
  In [47]: df['F'] = s1
  ```

  

## 拼接数据框

### merge:用于列拼接

#### merge函数用法

```python
merge(left            ,right,
      how='inner'     ,on=None,
      left_on=None    ,right_on=None,
      leftindex=False ,right_index=False, 
      sort=False      ,suffixes=('x','_y'), 
      copy=True       ,indicator=False,
      validate=None)
```

####  各参数意义

|     参数     |                             含义                             |
| :----------: | :----------------------------------------------------------: |
|     left     |                   参与合并的左侧DataFrame                    |
|    right     |                   参与合并的右侧DataFrame                    |
|     how      |   连接方式：'inner'（默认）；还有'outer'、'left'、'right'    |
|      on      | 用于连接的列名，必须同时存在于左右两个DataFrame对象中，如果位指定，则以left和right列名的交集作为连接键 |
|   left\_on   |                左侧DataFarme中用作连接键的列                 |
|  right\_on   |                右侧DataFarme中用作连接键的列                 |
| left\_index  |                  将左侧的行索引用作其连接键                  |
| right\_index |                  将右侧的行索引用作其连接键                  |
|     sort     | 根据连接键对合并后的数据进行排序，默认为True。有时在处理大数据集时，禁用该选项可获得更好的性能 |
|   suffixes   | 字符串值元组，用于追加到重叠列名的未尾，默认为（'\_x','\_y'）\.例如，左右两个DataFrame对象都有'data'，则结果中就会出现'data\_x'，'data\_y' |
|     copy     | 设置为False，可以在某些特殊情况下避免将数据复制到结果数据结构中。默认总是赋值 |

其中how的连接方式：

| 连接方式 |              作用               |
| :------: | :-----------------------------: |
|  inner   |          内连接,取交集          |
|  outer   |       取并集，并用nan填充       |
|   left   | 左连接， 左侧取全部，右侧取部分 |
|  right   | 右连接，左侧取部分，右侧取全部  |

#### 举例

```py
df = pd.merge(df1,df2,on=['stkcd','year','name'],how='left') # 按左合并
```



### concat函数:行列都可拼接

#### 函数用法

其中axis = 0为按行拼接，1位按列拼接；参数ignore_index等于True，这样就会生成一组新的索引，而不保留原表的索引；drop_duplicates用于删除重复值

```python
concat([df1,df2], axis = 0, ignore_index = True)
concat([df1,df2]).drop_duplicates()
```



## 绘图

```python
ax = df.plot(figsize=(10,5))
fig = ax.get_figure()
fig.savefig('plot.png')
```

```python
df.plot(x='A',y='B',kind='line') # 制定x，y坐标
```

![image-20200408233153296](https://raw.githubusercontent.com/lei940324/picture/master/typora202004/08/233156-881574.png)

## 进阶操作

转自知乎:[50道题玩转pandas](https://zhuanlan.zhihu.com/p/94096219?utm_source=qq&utm_medium=social&utm_oi=565317664290025472)

* 一个全数值DatraFrame，每个数字减去该行的平均数

```python
df = pd.DataFrame(np.random.random(size=(5, 3)))
print(df)
df1 = df.sub(df.mean(axis=1), axis=0)
print(df1)
```

* 一个有5列的DataFrame，求哪一列的和最小

```python
df = pd.DataFrame(np.random.random(size=(5, 5)), columns=list('abcde'))
print(df)
df.sum().idxmin()
```

* 给定DataFrame，求A列每个值的前3大的B的值的和

```python
df = pd.DataFrame({'A': list('aaabbcaabcccbbc'), 
                   'B': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
print(df)
df1 = df.groupby('A')['B'].nlargest(3).sum(level=0)
print(df1)
```

* 给定DataFrame，有列A, B，A的值在1-100（含），对A列每10步长，求对应的B的和

```python
df = pd.DataFrame({'A': [1,2,11,11,33,34,35,40,79,99], 
                   'B': [1,2,11,11,33,34,35,40,79,99]})
print(df)
df1 = df.groupby(pd.cut(df['A'], np.arange(0, 101, 10)))['B'].sum()
print(df1)
```

* 给定DataFrame，将负值代替为同组的平均值

```python
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 
                   'vals': [-12,345,3,1,45,14,4,-52,54,23,-235,21,57,3,87]})
print(df)

def replace(group):
    mask = group<0
    group[mask] = group[~mask].mean()
    return group

df['vals'] = df.groupby(['grps'])['vals'].transform(replace)
print(df)
```
