# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnostic_data_form.ui'
#
# Created: Tue Dec 27 13:43:58 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DiagnosticDataForm(object):
    def setupUi(self, DiagnosticDataForm):
        DiagnosticDataForm.setObjectName(_fromUtf8("DiagnosticDataForm"))
        DiagnosticDataForm.resize(318, 250)
        DiagnosticDataForm.setWindowTitle(QtGui.QApplication.translate("DiagnosticDataForm", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/meta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DiagnosticDataForm.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(DiagnosticDataForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.two_by_two_table = QtGui.QTableWidget(DiagnosticDataForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two_by_two_table.sizePolicy().hasHeightForWidth())
        self.two_by_two_table.setSizePolicy(sizePolicy)
        self.two_by_two_table.setMinimumSize(QtCore.QSize(260, 80))
        self.two_by_two_table.setMaximumSize(QtCore.QSize(260, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.two_by_two_table.setFont(font)
        self.two_by_two_table.setFrameShape(QtGui.QFrame.NoFrame)
        self.two_by_two_table.setFrameShadow(QtGui.QFrame.Plain)
        self.two_by_two_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.two_by_two_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.two_by_two_table.setAlternatingRowColors(True)
        self.two_by_two_table.setGridStyle(QtCore.Qt.DashLine)
        self.two_by_two_table.setRowCount(2)
        self.two_by_two_table.setColumnCount(2)
        self.two_by_two_table.setObjectName(_fromUtf8("two_by_two_table"))
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DiagnosticDataForm", "(test) +", None, QtGui.QApplication.UnicodeUTF8))
        self.two_by_two_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DiagnosticDataForm", "(test) -", None, QtGui.QApplication.UnicodeUTF8))
        self.two_by_two_table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DiagnosticDataForm", "(disease) +", None, QtGui.QApplication.UnicodeUTF8))
        self.two_by_two_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DiagnosticDataForm", "(disease) -", None, QtGui.QApplication.UnicodeUTF8))
        self.two_by_two_table.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.two_by_two_table)
        spacerItem = QtGui.QSpacerItem(20, 25, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_13 = QtGui.QLabel(DiagnosticDataForm)
        self.label_13.setMinimumSize(QtCore.QSize(50, 0))
        self.label_13.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_13.setFont(font)
        self.label_13.setText(QtGui.QApplication.translate("DiagnosticDataForm", "metric", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_2.addWidget(self.label_13)
        self.effect_cbo_box = QtGui.QComboBox(DiagnosticDataForm)
        self.effect_cbo_box.setMinimumSize(QtCore.QSize(100, 20))
        self.effect_cbo_box.setMaximumSize(QtCore.QSize(76, 20))
        self.effect_cbo_box.setObjectName(_fromUtf8("effect_cbo_box"))
        self.horizontalLayout_2.addWidget(self.effect_cbo_box)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_14 = QtGui.QLabel(DiagnosticDataForm)
        self.label_14.setMinimumSize(QtCore.QSize(0, 20))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_14.setFont(font)
        self.label_14.setText(QtGui.QApplication.translate("DiagnosticDataForm", "est.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_15 = QtGui.QLabel(DiagnosticDataForm)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_15.setFont(font)
        self.label_15.setText(QtGui.QApplication.translate("DiagnosticDataForm", "low", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 0, 2, 1, 1)
        self.label_16 = QtGui.QLabel(DiagnosticDataForm)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_16.setFont(font)
        self.label_16.setText(QtGui.QApplication.translate("DiagnosticDataForm", "high", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 0, 4, 1, 1)
        self.effect_txt_box = QtGui.QLineEdit(DiagnosticDataForm)
        self.effect_txt_box.setMinimumSize(QtCore.QSize(50, 22))
        self.effect_txt_box.setMaximumSize(QtCore.QSize(50, 22))
        self.effect_txt_box.setObjectName(_fromUtf8("effect_txt_box"))
        self.gridLayout_3.addWidget(self.effect_txt_box, 0, 1, 1, 1)
        self.low_txt_box = QtGui.QLineEdit(DiagnosticDataForm)
        self.low_txt_box.setMinimumSize(QtCore.QSize(50, 22))
        self.low_txt_box.setMaximumSize(QtCore.QSize(50, 22))
        self.low_txt_box.setObjectName(_fromUtf8("low_txt_box"))
        self.gridLayout_3.addWidget(self.low_txt_box, 0, 3, 1, 1)
        self.high_txt_box = QtGui.QLineEdit(DiagnosticDataForm)
        self.high_txt_box.setMinimumSize(QtCore.QSize(50, 22))
        self.high_txt_box.setMaximumSize(QtCore.QSize(50, 22))
        self.high_txt_box.setObjectName(_fromUtf8("high_txt_box"))
        self.gridLayout_3.addWidget(self.high_txt_box, 0, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(DiagnosticDataForm)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("DiagnosticDataForm", "α:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.alpha_edit = QtGui.QLineEdit(DiagnosticDataForm)
        self.alpha_edit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.alpha_edit.setText(QtGui.QApplication.translate("DiagnosticDataForm", ".05", None, QtGui.QApplication.UnicodeUTF8))
        self.alpha_edit.setObjectName(_fromUtf8("alpha_edit"))
        self.horizontalLayout.addWidget(self.alpha_edit)
        self.ci_label = QtGui.QLabel(DiagnosticDataForm)
        self.ci_label.setText(QtGui.QApplication.translate("DiagnosticDataForm", "(95% confidence interval)", None, QtGui.QApplication.UnicodeUTF8))
        self.ci_label.setObjectName(_fromUtf8("ci_label"))
        self.horizontalLayout.addWidget(self.ci_label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(DiagnosticDataForm)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DiagnosticDataForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DiagnosticDataForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DiagnosticDataForm.reject)
        QtCore.QMetaObject.connectSlotsByName(DiagnosticDataForm)

    def retranslateUi(self, DiagnosticDataForm):
        item = self.two_by_two_table.verticalHeaderItem(0)
        item = self.two_by_two_table.verticalHeaderItem(1)
        item = self.two_by_two_table.horizontalHeaderItem(0)
        item = self.two_by_two_table.horizontalHeaderItem(1)

import icons_rc