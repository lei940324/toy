# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:49:10 2020
实现pdf去水印

@author: lei
"""

from pdf2image import convert_from_path
import tempfile
from PIL import Image
import numpy as np
import fitz
import glob
import re


def main(filename, value = 108):
    # 1.将pdf转化为图片
    with tempfile.TemporaryDirectory() :
        images = convert_from_path(filename)
        for index, img in enumerate(images):
            name = r'.\处理结果\pdf转图片' + r'\page_%s.png' % (index)
            img.save(name)
            # 2.图片处理
            img = Image.open(name)
            #第一个值越大越清晰，一般为108到130，越小越能去水印，但越不清晰
            img = levelsDeal(img,value,164)
            img_res = Image.fromarray(img.astype('uint8'))
            print(f'转化图片中：页码{index}处理完毕')
            img_res.save(r'.\处理结果\去水印图片' + r'\page_%s.png' % (index))
    
#图像矩阵处理
def levelsDeal(img, black,white):
    if white > 255:
        white = 255
    if black < 0:
        black = 0
    if black >= white:
        black = white - 2
    img_array = np.array(img, dtype = int)
    cRate = -(white - black) /255.0 * 0.05
    rgb_diff = img_array - black
    rgb_diff = np.maximum(rgb_diff, 0)
    img_array = rgb_diff * cRate
    img_array = np.around(img_array, 0)
    img_array = img_array.astype(int)
    return img_array

def pic2pdf():
    doc = fitz.open()
    a = glob.glob(r".\处理结果\去水印图片\*")
    a.sort(key= lambda x:int(re.compile(r'page_(\d*).png').findall(x)[0]))
    for img in a:  # 读取图片，确保按文件名排序
        print('图片转为pdf:',img)
        imgdoc = fitz.open(img)                 # 打开图片
        pdfbytes = imgdoc.convertToPDF()        # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)                   # 将当前页插入文档
    doc.save(r".\处理结果\去水印结果.pdf")                   # 保存pdf文件
    doc.close()

if __name__ == "__main__":
 
    main('测试.pdf', 120)
    pic2pdf()