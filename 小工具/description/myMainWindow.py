# -*- coding: utf-8 -*-

import sys
import os
from func import description, deal_int
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from ui_MainWindow import Ui_MainWindow


class QmyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)   # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)      # 构造UI界面

        # 初始化各参数
        self.ui.lineEdit.setText('使用说明: 按顺序选择统计量')
        self.ui.spinBox.setValue(3)   # 设置默认保留三位小数
        self.ui.checkBox.setChecked(True)
        self.line_list = [self.ui.lineEdit_1, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4, 
                          self.ui.lineEdit_5, self.ui.lineEdit_6, self.ui.lineEdit_7, self.ui.lineEdit_8, 
                          self.ui.lineEdit_9, self.ui.lineEdit_10, self.ui.lineEdit_11, self.ui.lineEdit_12, 
                          self.ui.lineEdit_13, self.ui.lineEdit_14, self.ui.lineEdit_15]
        self.values = ['1', '', '', '3', '4', '', '2',
                       '5', '6', '7', '8', '', '', '', '']
        for widget, value in zip(self.line_list, self.values):
            widget.setText(value)

            # ==========由connectSlotsByName()自动连接的槽函数============
    @pyqtSlot()
    def on_action_triggered(self):  # 导入数据按钮
        download_path = QFileDialog.getOpenFileName(None, "浏览", None,
                                                    "Text Files (*.xlsx);;Text Files (*.xls)")
        try:
            self.df = pd.read_excel(download_path[0])
            self.ui.lineEdit.setText("恭喜,数据读取成功!")
        except:
            self.ui.lineEdit.setText("数据读取失败,请重新导入数据!")
        if self.ui.checkBox.isChecked():
            # 判断date是否勾选，如果勾选，删除第一列日期数据
            self.df = self.df.drop(self.df.columns[0], axis=1)

    @pyqtSlot()
    def on_action_2_triggered(self):   # 开始运行按钮
        parameter = []
        for widget in self.line_list:
            parameter.append(widget.text())
        opt = deal_int(parameter)
        stat = description(opt, self.ui.spinBox.value())
        stat.run(self.df)
        self.ui.lineEdit.setText(f'结果已保存在{os.getcwd()}\\output.xlsx!')

    @pyqtSlot()
    def on_action_3_triggered(self):   # 清空按钮
        for widget in self.line_list:
            widget.setText('')
            self.ui.lineEdit.setText('已清空全部顺序量！')

    @pyqtSlot()
    def on_action_4_triggered(self):   # 初始化按钮
        for widget, value in zip(self.line_list, self.values):
            widget.setText(value)
        self.ui.lineEdit.setText('使用说明: 按顺序选择统计量')


# ============窗体测试程序 ================================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWindow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
