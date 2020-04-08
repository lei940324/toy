# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:49:12 2020

@author: lei
"""

import pandas as pd
import docx
from docx.shared import RGBColor   # 设置颜色
from docx.shared import Pt         # 设置字体
from docx.oxml.ns import qn        # 设置中文字体


class word():
    def __init__(self, doc, data):
        self.doc = doc
        self.data = data

    def location(self, color=RGBColor(0xff, 0x00, 0x00)):
        """
        查找特定颜色所在位置

        Parameters
        ----------
        color : 颜色，默认红色

        Returns
        -------
        modify : 待修改对象

        """
        modify = [
            j for i in self.doc.paragraphs for j in i.runs if j.font.color.rgb == color]
        return modify

    def main(self, modify, save_name):
        """
        更改内容,改变样式,并进行存储

        Parameters
        ----------
        modify : 待修改对象
        save_name : 存储名

        """
        for i, row in self.data.iterrows():  # 遍历每行数据
            for index, run in enumerate(modify):
                run.text = str(row[index])
                self.change_style(run)
            self.doc.save(f'./输出结果/{save_name[i]}.docx')

    def change_style(self, run, color=RGBColor(0, 0, 0), size=9, bold=False, name='宋体', number='Times New Roman'):
        """
        修改样式

        Parameters
        ----------
        run : 待修改对象,为列表
        color : 字体颜色
        size : 字体字号
        bold : 是否加粗
        name : 字体名
        number : 特定修改字母与数字格式

        """
        run.font.size = Pt(size)
        run.bold = bold
        run.font.color.rgb = color
        run.font.name = name
        # 设置字体必须要下面2步
        s = run._element
        s.rPr.rFonts.set(qn('w:eastAsia'), name)
        if run.text.encode('utf-8').isalnum() and number:
            run.font.name = number
            s = run._element
            s.rPr.rFonts.set(qn('w:eastAsia'), number)


if __name__ == "__main__":
    doc = docx.Document('个人情况表.docx')
    data = pd.read_excel('信息.xlsx')

    exc = word(doc, data)
    modify = exc.location()   # 确定待修改位置
    exc.main(modify, save_name=data.iloc[:, 0])   # 修改内容并存储
