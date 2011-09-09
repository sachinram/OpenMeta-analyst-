# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnostic_metrics.ui'
#
# Created: Thu Aug 18 15:12:50 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_diag_metric(object):
    def setupUi(self, diag_metric):
        diag_metric.setObjectName(_fromUtf8("diag_metric"))
        diag_metric.setWindowModality(QtCore.Qt.ApplicationModal)
        diag_metric.resize(300, 147)
        diag_metric.setMinimumSize(QtCore.QSize(250, 140))
        diag_metric.setMaximumSize(QtCore.QSize(300, 147))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        diag_metric.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/meta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        diag_metric.setWindowIcon(icon)
        self.formLayout_2 = QtGui.QFormLayout(diag_metric)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.metrics_grp_box = QtGui.QGroupBox(diag_metric)
        self.metrics_grp_box.setObjectName(_fromUtf8("metrics_grp_box"))
        self.verticalLayout = QtGui.QVBoxLayout(self.metrics_grp_box)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chk_box_sens = QtGui.QCheckBox(self.metrics_grp_box)
        self.chk_box_sens.setChecked(True)
        self.chk_box_sens.setObjectName(_fromUtf8("chk_box_sens"))
        self.gridLayout.addWidget(self.chk_box_sens, 0, 0, 1, 1)
        self.chk_box_spec = QtGui.QCheckBox(self.metrics_grp_box)
        self.chk_box_spec.setChecked(True)
        self.chk_box_spec.setObjectName(_fromUtf8("chk_box_spec"))
        self.gridLayout.addWidget(self.chk_box_spec, 0, 1, 1, 1)
        self.chk_box_lr = QtGui.QCheckBox(self.metrics_grp_box)
        self.chk_box_lr.setChecked(True)
        self.chk_box_lr.setObjectName(_fromUtf8("chk_box_lr"))
        self.gridLayout.addWidget(self.chk_box_lr, 2, 0, 1, 1)
        self.chk_box_dor = QtGui.QCheckBox(self.metrics_grp_box)
        self.chk_box_dor.setChecked(True)
        self.chk_box_dor.setObjectName(_fromUtf8("chk_box_dor"))
        self.gridLayout.addWidget(self.chk_box_dor, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.metrics_grp_box)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_ok = QtGui.QPushButton(diag_metric)
        self.btn_ok.setMaximumSize(QtCore.QSize(75, 23))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.horizontalLayout.addWidget(self.btn_ok)
        self.formLayout_2.setLayout(1, QtGui.QFormLayout.LabelRole, self.horizontalLayout)

        self.retranslateUi(diag_metric)
        QtCore.QMetaObject.connectSlotsByName(diag_metric)

    def retranslateUi(self, diag_metric):
        diag_metric.setWindowTitle(QtGui.QApplication.translate("diag_metric", "Diagnostic Metrics", None, QtGui.QApplication.UnicodeUTF8))
        self.metrics_grp_box.setTitle(QtGui.QApplication.translate("diag_metric", "select metrics for analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_box_sens.setText(QtGui.QApplication.translate("diag_metric", "sensitivity", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_box_spec.setText(QtGui.QApplication.translate("diag_metric", "specificity", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_box_lr.setText(QtGui.QApplication.translate("diag_metric", "likelihood ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_box_dor.setText(QtGui.QApplication.translate("diag_metric", "diagnostic odds ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ok.setText(QtGui.QApplication.translate("diag_metric", "next >", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc