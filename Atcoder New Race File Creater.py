"""
AtCoder 比赛文件生成器
作者: Albert
版本: v1.1C (中文版)
更新日期: 2025-2-9
修改：
    - 使用了更新版本的 PyQt6 以取代 PyQt5
"""
from PyQt6 import QtGui
from PyQt6.QtWidgets import *
import sys, os

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        # 窗口设置
        self.setWindowTitle("Atcoder New Race Files Creater v1.1C")
        self.font = QtGui.QFont("等线", 14)
        self.main_vbox = QVBoxLayout(self)

        # 比赛类型
        race_type_label = QLabel()
        race_type_label.setText("比赛类型:")
        race_type_label.setFont(self.font)
        self.race_type_box = QComboBox()
        self.race_type_box.addItems(["ATBC", "ATRC", "ATGC", "ATHC"])
        self.race_type_box.move(20, 10)
        self.race_type_box.setFont(self.font)
        race_type_hbox = QHBoxLayout()
        race_type_hbox.addWidget(race_type_label)
        race_type_hbox.addWidget(self.race_type_box)
        self.main_vbox.addLayout(race_type_hbox)

        # 比赛编号
        race_number_label = QLabel()
        race_number_label.setText("比赛编号:")
        race_number_label.setFont(self.font)
        self.race_number_lne = QLineEdit()
        self.race_number_lne.setFont(self.font)
        self.main_vbox.addWidget(self.race_number_lne)
        race_number_hbox = QHBoxLayout()
        race_number_hbox.addWidget(race_number_label)
        race_number_hbox.addWidget(self.race_number_lne)
        self.main_vbox.addLayout(race_number_hbox)

        # 模式选择
        sellect_mode_label = QLabel()
        sellect_mode_label.setText("模式选择:")
        sellect_mode_label.setFont(self.font)
        self.mode_btn1 = QRadioButton("To")
        self.mode_btn1.setFont(self.font)
        self.mode_btn2 = QRadioButton("Select")
        self.mode_btn2.setFont(self.font)
        self.mode_btn1.setChecked(True)
        mode_hbox = QHBoxLayout()
        mode_hbox.addWidget(sellect_mode_label)
        mode_hbox.addWidget(self.mode_btn1)
        mode_hbox.addWidget(self.mode_btn2)
        self.main_vbox.addLayout(mode_hbox)
        self.to_box()
        self.main_vbox.addWidget(self.mode_to_gbox)
        self.main_vbox.addWidget(self.mode_to_done_btn)
        self.select_box()
        self.mode_btn1.toggled.connect(self.mode_to)
        self.mode_btn2.toggled.connect(self.mode_select)

    def to_box(self):
        # 题目选择
        self.mode_to_gbox = QGroupBox("题目")
        self.mode_to_gbox.setFont(self.font)
        self.btnA = QRadioButton("A")
        self.btnB = QRadioButton("B")
        self.btnC = QRadioButton("C")
        self.btnD = QRadioButton("D")
        self.btnE = QRadioButton("E")
        self.btnF = QRadioButton("F")
        self.btnG = QRadioButton("G")
        self.btnA.setFont(self.font)
        self.btnB.setFont(self.font)
        self.btnC.setFont(self.font)
        self.btnD.setFont(self.font)
        self.btnE.setFont(self.font)
        self.btnF.setFont(self.font)
        self.btnG.setFont(self.font)
        hbox = QHBoxLayout()
        hbox.addWidget(self.btnA)
        hbox.addWidget(self.btnB)
        hbox.addWidget(self.btnC)
        hbox.addWidget(self.btnD)
        hbox.addWidget(self.btnE)
        hbox.addWidget(self.btnF)
        hbox.addWidget(self.btnG)
        self.btnA.setChecked(True)
        self.mode_to_gbox.setLayout(hbox)

        # 创建按钮
        self.mode_to_done_btn = QPushButton("创建")
        self.mode_to_done_btn.setFont(self.font)
        self.mode_to_done_btn.clicked.connect(self.mode_to_done)


    def select_box(self):
        # 题目选择
        self.mode_select_gbox = QGroupBox("题目")
        self.mode_select_gbox.setFont(self.font)
        self.cboxA = QCheckBox("A")
        self.cboxB = QCheckBox("B")
        self.cboxC = QCheckBox("C")
        self.cboxD = QCheckBox("D")
        self.cboxE = QCheckBox("E")
        self.cboxF = QCheckBox("F")
        self.cboxG = QCheckBox("G")
        self.cboxA.setFont(self.font)
        self.cboxB.setFont(self.font)
        self.cboxC.setFont(self.font)
        self.cboxD.setFont(self.font)
        self.cboxE.setFont(self.font)
        self.cboxF.setFont(self.font)
        self.cboxG.setFont(self.font)
        hbox = QHBoxLayout()
        hbox.addWidget(self.cboxA)
        hbox.addWidget(self.cboxB)
        hbox.addWidget(self.cboxC)
        hbox.addWidget(self.cboxD)
        hbox.addWidget(self.cboxE)
        hbox.addWidget(self.cboxF)
        hbox.addWidget(self.cboxG)
        self.mode_select_gbox.setLayout(hbox)

        # 创建按钮
        self.mode_select_done_btn = QPushButton("创建")
        self.mode_select_done_btn.setFont(self.font)
        self.mode_select_done_btn.clicked.connect(self.mode_select_done)

    def mode_to(self):
        # 交换
        self.main_vbox.replaceWidget(self.mode_select_gbox, self.mode_to_gbox)
        self.main_vbox.replaceWidget(self.mode_select_done_btn, self.mode_to_done_btn)
        self.mode_select_gbox.hide()
        self.mode_select_done_btn.hide()
        self.mode_to_gbox.show()
        self.mode_to_done_btn.show()

    def mode_select(self):
        # 交换
        self.main_vbox.replaceWidget(self.mode_to_gbox, self.mode_select_gbox)
        self.main_vbox.replaceWidget(self.mode_to_done_btn, self.mode_select_done_btn)
        self.mode_to_gbox.hide()
        self.mode_to_done_btn.hide()
        self.mode_select_gbox.show()
        self.mode_select_done_btn.show()
    
    def mode_to_done(self):
        if(self.race_number_lne.text() == ""):
            QMessageBox.question(self, "错误", "请键入比赛编号", QMessageBox.Ok, QMessageBox.Ok)
            return
        if(self.btnA.isChecked()):
            lst = 65
        elif(self.btnB.isChecked()):
            lst = 66
        elif(self.btnC.isChecked()):
            lst = 67
        elif(self.btnD.isChecked()):
            lst = 68
        elif(self.btnE.isChecked()):
            lst = 69
        elif(self.btnF.isChecked()):
            lst = 70
        elif(self.btnG.isChecked()):
            lst = 71
        for i in range(65, lst + 1):
            self.create_file(chr(i))
        self.clear_main_vbox()

    def mode_select_done(self):
        if(self.race_number_lne.text() == ""):
            QMessageBox.question(self, "错误", "请键入比赛编号", QMessageBox.Ok, QMessageBox.Ok)
            return
        if(self.cboxA.isChecked()):
            self.create_file('A')
        if(self.cboxB.isChecked()):
            self.create_file('B')
        if(self.cboxC.isChecked()):
            self.create_file('C')
        if(self.cboxD.isChecked()):
            self.create_file('D')
        if(self.cboxE.isChecked()):
            self.create_file('E')
        if(self.cboxF.isChecked()):
            self.create_file('F')
        if(self.cboxG.isChecked()):
            self.create_file('G')
        self.clear_main_vbox()
    
    def create_file(self, problem):
        s = self.race_type_box.currentText() + self.race_number_lne.text() + problem + '.cpp'
        if os.path.exists(s):
            self.check_overwrite_or_not(s)
        else:
            file = open(s, 'w')
            file.close()
    
    def check_overwrite_or_not(self, s):
        rep = QMessageBox.question(self, "文件已存在", "文件 \"" + s + "\" 已存在，您希望覆盖它吗?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if rep == QMessageBox.Yes:
            os.remove(s)
            file = open(s, 'w')
            file.close()
        else:
            pass

    def clear_main_vbox(self):
        item_list = list(range(self.main_vbox.count()))
        item_list.reverse()
        for i in item_list:
            item = self.main_vbox.itemAt(i)
            self.main_vbox.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
        done_label = QLabel()
        done_label.setText("创建成功！")
        done_label.setFont(self.font)
        self.main_vbox.addWidget(done_label)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
