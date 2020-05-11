# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'All pins config.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import re
import os



from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
MFIC_text = []
DIO_text= []
class Ui_Form(object):
  
    def setupUi(self, Form):

        
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(869, 620)
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.addItem(str())
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 40, 241, 22))
        self.Config_groupbox = QGroupBox(Form)
        self.Config_groupbox.setObjectName(u"Config_groupbox")
        self.Config_groupbox.setGeometry(QRect(90, 100, 741, 321))
        self.output_radioBox = QRadioButton(self.Config_groupbox)
        self.output_radioBox.setObjectName(u"output_radioBox")
        self.output_radioBox.setEnabled(True)
        self.output_radioBox.setGeometry(QRect(50, 50, 93, 20))
        self.output_radioBox.setChecked(True)
        self.Input_radioBox = QRadioButton(self.Config_groupbox)
        self.Input_radioBox.setObjectName(u"Input_radioBox")
        self.Input_radioBox.setGeometry(QRect(50, 110, 93, 20))
        self.PinName_label = QLabel(self.Config_groupbox)
        self.PinName_label.setObjectName(u"PinName_label")
        self.PinName_label.setGeometry(QRect(60, 180, 47, 14))
        self.PinName_lineedit = QLineEdit(self.Config_groupbox)
        self.PinName_lineedit.setObjectName(u"PinName_lineedit")
        self.PinName_lineedit.setGeometry(QRect(50, 220, 113, 20))
        self.UseDefault_combobox = QCheckBox(self.Config_groupbox)
        self.UseDefault_combobox.setObjectName(u"UseDefault_combobox")
        self.UseDefault_combobox.setGeometry(QRect(50, 260, 80, 20))
        self.UseDefault_combobox.setChecked(True)

        self.Outpu_groupBox = QGroupBox(self.Config_groupbox)
        self.Outpu_groupBox.setObjectName(u"Outpu_groupBox")
        self.Outpu_groupBox.setGeometry(QRect(380, 30, 331, 131))
        self.High_radioBox = QRadioButton(self.Outpu_groupBox)
        self.High_radioBox.setObjectName(u"High_radioBox")
        self.High_radioBox.setGeometry(QRect(30, 30, 93, 20))
        self.High_radioBox.setChecked(True)
        self.Low_radioBox = QRadioButton(self.Outpu_groupBox)
        self.Low_radioBox.setObjectName(u"Low_radioBox")
        self.Low_radioBox.setGeometry(QRect(30, 90, 93, 20))
        self.Input_GroupBox = QGroupBox(self.Config_groupbox)
        self.Input_GroupBox.setObjectName(u"Input_GroupBox")
        self.Input_GroupBox.setEnabled(False)
        self.Input_GroupBox.setGeometry(QRect(370, 180, 341, 111))
        self.PullUp_radioBox = QRadioButton(self.Input_GroupBox)
        self.PullUp_radioBox.setObjectName(u"PullUp_radioBox")
        self.PullUp_radioBox.setGeometry(QRect(40, 20, 93, 20))
        self.HighImpedance_radioBox = QRadioButton(self.Input_GroupBox)
        self.HighImpedance_radioBox.setObjectName(u"HighImpedance_radioBox")
        self.HighImpedance_radioBox.setGeometry(QRect(40, 80, 93, 20))
        self.HighImpedance_radioBox.setChecked(True)
        self.Path_lineEdit = QLineEdit(Form)
        self.Path_lineEdit.setObjectName(u"Path_lineEdit")
        self.Path_lineEdit.setGeometry(QRect(100, 450, 721, 20))
        self.send_pushButton = QPushButton(Form)
        self.send_pushButton.setObjectName(u"send_pushButton")
        self.send_pushButton.setGeometry(QRect(100, 500, 112, 34))
        self.load_pushButton = QPushButton(Form)
        self.load_pushButton.setObjectName(u"load_pushButton")
        self.load_pushButton.setGeometry(QRect(270, 500, 112, 34))
        

        self.retranslateUi(Form)
        QObject.connect(self.output_radioBox, SIGNAL("clicked(bool)"), self.Input_GroupBox.setDisabled)
        QObject.connect(self.Input_radioBox, SIGNAL("clicked(bool)"), self.Outpu_groupBox.setDisabled)
        QObject.connect(self.Input_radioBox, SIGNAL("clicked(bool)"), self.Input_GroupBox.setEnabled)
        QObject.connect(self.output_radioBox, SIGNAL("clicked(bool)"), self.Outpu_groupBox.setEnabled)
        QObject.connect(self.UseDefault_combobox, SIGNAL("clicked(bool)"), self.PinName_lineedit.setDisabled)
        
        

        
      

        self.send_pushButton.clicked.connect(self.GenerateFunction)
        self.load_pushButton.clicked.connect(self.loadFunction)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def loadFunction(self):
      global MFIC_text
      global DIO_text
      MFIC_handler = open(self.Path_lineEdit.text()+ '\MFIC.h','r+')
      DIO_handler = open(self.Path_lineEdit.text()+ '\DIO.h','r+')
      if len(MFIC_text) == 0:
        MFIC_text= MFIC_handler.readlines()
        DIO_text= DIO_handler.readlines()
      status= False
      for line in DIO_text:
        match = re.search (str(self.comboBox.currentText()+"MODE     DIO_u8(\w\w\w)"),line)
        if match:
          status= True

          if match.group(1) == "Hig":
            self.output_radioBox.setChecked(True)
            self.High_radioBox.setChecked(True)
            
            
            self.Input_GroupBox.setDisabled(True)
            self.Outpu_groupBox.setEnabled(True)
            
          elif match.group(1) == "Low":
            self.output_radioBox.setChecked(True)
            self.Low_radioBox.setChecked(True)
            
            self.Input_GroupBox.setDisabled(True)
            self.Outpu_groupBox.setEnabled(True)
            
          elif match.group(1) == "PUL":
            self.Input_radioBox.setChecked(True)
            self.PullUp_radioBox.setChecked(True)
            
            self.Input_GroupBox.setEnabled(True)
            self.Outpu_groupBox.setDisabled(True)


            
          elif match.group(1) == "Imp":
            self.Input_radioBox.setChecked(True)
            self.HighImpedance_radioBox.setChecked(True)
            
            self.Input_GroupBox.setEnabled(True)
            self.Outpu_groupBox.setDisabled(True)
      MFIC_handler.close()
      DIO_handler.close()
    


    def GenerateFunction(self):
    
      status = 0
      global MFIC_text
      global DIO_text
      MFIC_handler = open(self.Path_lineEdit.text()+ '\MFIC.h','r+')
      DIO_handler = open(self.Path_lineEdit.text()+ '\DIO.h','r+')
      if len(MFIC_text) == 0:
        MFIC_text= MFIC_handler.readlines()
        DIO_text= DIO_handler.readlines()
        
      MFIC_handler.close()
      DIO_handler.close()
      MFIC_handler = open(self.Path_lineEdit.text()+ '\MFIC.h','w+')
      DIO_handler = open(self.Path_lineEdit.text()+ '\DIO.h','w+')
      currentLocation = 0
      
      for line in DIO_text:
         
        match = re.search (self.comboBox.currentText(),line)
        
        if match:
          status = 1
          if self.output_radioBox.isChecked():
            if self.High_radioBox.isChecked():
              DIO_text[currentLocation]="#define DIO_u8"+self.comboBox.currentText()+"MODE     DIO_u8High\n"
            else:
              DIO_text[currentLocation]="#define DIO_u8"+self.comboBox.currentText()+"MODE     DIO_u8Low\n"          
          else:
            if self.PullUp_radioBox.isChecked():
              DIO_text[currentLocation]="#define DIO_u8"+self.comboBox.currentText()+"MODE     DIO_u8PULLUP\n"
            else:
              DIO_text[currentLocation]="#define DIO_u8"+self.comboBox.currentText()+"MODE     DIO_u8Impedance\n"
              
          if self.UseDefault_combobox.isChecked():
            MFIC_text[currentLocation]="#define MFIC_u8"+self.comboBox.currentText()+"  DIO_u8"+self.comboBox.currentText()+"MODE"
          else:
            MFIC_text[currentLocation]="#define " + self.PinNameLineEdit.text() + "   DIO_u8"+self.comboBox.currentText()+"MODE"
              
        currentLocation +=1
      if status == 0:
        if self.output_radioBox.isChecked():
            if self.High_radioBox.isChecked():
              DIO_text.append("#define DIO_u8"+self.comboBox.currentText()+"MODE     DIO_u8High\n")
            else:
              DIO_text.append("#define DIO_u8"+self.comboBox.currentText()+"MODE     DIO_u8Low\n")          
        else:
          if self.PullUp_radioBox.isChecked():
            DIO_text.append("#define DIO_u8"+self.comboBox.currentText()+"MODE     DIO_u8PULLUP\n")
          else:
            DIO_text.append("#define DIO_u8"+self.comboBox.currentText()+"MODE     DIO_u8Impedance\n")
              
        if self.UseDefault_combobox.isChecked():
          MFIC_text.append("#define MFIC_u8"+self.comboBox.currentText()+"  DIO_u8"+self.comboBox.currentText()+"MODE\n")
        else:
          MFIC_text.append("#define " + self.PinNameLineEdit.text() + "   DIO_u8"+self.comboBox.currentText()+"MODE\n")
          
      #MFIC_handler.write('\n')
      #DIO_handler.write('\n')
      MFIC_handler.writelines(MFIC_text)
      DIO_handler.writelines(DIO_text)
      MFIC_handler.close()
      DIO_handler.close()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"PA0", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"PA1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"PA2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"PA3", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"PA4", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"PA5", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"PA6", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Form", u"PA7", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Form", u"PB0", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Form", u"PB1", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Form", u"PB2", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Form", u"PB3", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("Form", u"PB4", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("Form", u"PB5", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("Form", u"PB6", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("Form", u"PB7", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("Form", u"PC0", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("Form", u"PC1", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("Form", u"PC2", None))
        self.comboBox.setItemText(19, QCoreApplication.translate("Form", u"PC3", None))
        self.comboBox.setItemText(20, QCoreApplication.translate("Form", u"PC4", None))
        self.comboBox.setItemText(21, QCoreApplication.translate("Form", u"PC5", None))
        self.comboBox.setItemText(22, QCoreApplication.translate("Form", u"PC6", None))
        self.comboBox.setItemText(23, QCoreApplication.translate("Form", u"PC7", None))
        self.comboBox.setItemText(24, QCoreApplication.translate("Form", u"PD0", None))
        self.comboBox.setItemText(25, QCoreApplication.translate("Form", u"PD1", None))
        self.comboBox.setItemText(26, QCoreApplication.translate("Form", u"PD2", None))
        self.comboBox.setItemText(27, QCoreApplication.translate("Form", u"PD3", None))
        self.comboBox.setItemText(28, QCoreApplication.translate("Form", u"PD4", None))
        self.comboBox.setItemText(29, QCoreApplication.translate("Form", u"PD5", None))
        self.comboBox.setItemText(30, QCoreApplication.translate("Form", u"PD6", None))
        self.comboBox.setItemText(31, QCoreApplication.translate("Form", u"PD7", None))

        self.Config_groupbox.setTitle(QCoreApplication.translate("Form", u"Configurations", None))
        self.output_radioBox.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_radioBox.setText(QCoreApplication.translate("Form", u"Input", None))
        self.PinName_label.setText(QCoreApplication.translate("Form", u"Pin Name", None))
        self.PinName_lineedit.setText(QCoreApplication.translate("Form", u"Enter Pin Name", None))
        self.UseDefault_combobox.setText(QCoreApplication.translate("Form", u"Use Default", None))
        self.Outpu_groupBox.setTitle(QCoreApplication.translate("Form", u"Output level", None))
        self.High_radioBox.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_radioBox.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_GroupBox.setTitle(QCoreApplication.translate("Form", u"Input level", None))
        self.PullUp_radioBox.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.HighImpedance_radioBox.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.Path_lineEdit.setText(QCoreApplication.translate("Form", os.getcwd(), None))
        self.send_pushButton.setText(QCoreApplication.translate("Form", u"Send", None))
        self.load_pushButton.setText(QCoreApplication.translate("Form", u"Load", None))
    # retranslateUi



app = QApplication(sys.argv)                  #create and application to be runned. You must include the sys.argv
widget = QWidget()                            #create a widget in this application
form = Ui_Form()                              #create a form to be inside the widget

form.setupUi(widget)                          #setup your buttons, text, etc... in the form and link it to the widget
widget.show()
x = app.exec_()                               #app.exec_() will be stuck until i close my app, and then it will exit
#if this last line is not included the gui will appear for a split second and close because the last line is finished with no loop to make it stay open     

#sys.exit(x)                                   #for error level


