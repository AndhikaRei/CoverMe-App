# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Klien_PesanRS.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from autentikasi import get_username
from PyQt5 import QtCore, QtGui, QtWidgets
from pesanan import *
from rumah_sakit import *
import mysql.connector
from ui_login import *


class Ui_PesanRSWindow(object):
	def setupUi(self, PesanRSWindow, ID_Pengguna=3):
		# Inisialisasi GUI
		self.PesanRSWindow = PesanRSWindow
		self.PesanRSWindow.setObjectName("PesanRSWindow")
		self.PesanRSWindow.resize(900, 591)
		self.centralwidget = QtWidgets.QWidget(PesanRSWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.Sidebar = QtWidgets.QFrame(self.centralwidget)
		self.Sidebar.setGeometry(QtCore.QRect(0, 0, 211, 591))
		self.Sidebar.setStyleSheet("QFrame{\n"
		"    background-color: rgb(72, 67, 67);\n"
		"}")
		self.Sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.Sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
		self.Sidebar.setObjectName("Sidebar")
		self.SuhuHarian = QtWidgets.QPushButton(self.Sidebar)
		self.SuhuHarian.setGeometry(QtCore.QRect(20, 180, 171, 51))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.SuhuHarian.setFont(font)
		self.SuhuHarian.setStyleSheet("QPushButton{\n"
		"    background-color: rgb(72, 67, 67);\n"
		"    color: rgb(255, 255, 255);\n"
		"}")
		self.SuhuHarian.setObjectName("SuhuHarian")
		self.label = QtWidgets.QLabel(self.Sidebar)
		self.label.setGeometry(QtCore.QRect(20, 20, 171, 71))
		font = QtGui.QFont()
		font.setPointSize(28)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setStyleSheet("QLabel{\n"
		"    color: rgb(255, 255, 255);\n"
		"}")
		self.label.setObjectName("label")
		self.PesanRS = QtWidgets.QPushButton(self.Sidebar)
		self.PesanRS.setGeometry(QtCore.QRect(20, 250, 171, 51))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.PesanRS.setFont(font)
		self.PesanRS.setStyleSheet("QPushButton{\n"
		"    background-color: rgb(72, 67, 67);\n"
		"    color: rgb(255, 255, 255);\n"
		"}")
		self.PesanRS.setObjectName("PesanRS")
		self.Pesanan = QtWidgets.QPushButton(self.Sidebar)
		self.Pesanan.setGeometry(QtCore.QRect(20, 320, 171, 51))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.Pesanan.setFont(font)
		self.Pesanan.setStyleSheet("QPushButton{\n"
		"    background-color: rgb(72, 67, 67);\n"
		"    color: rgb(255, 255, 255);\n"
		"}")
		self.Pesanan.setObjectName("Pesanan")
		self.Home = QtWidgets.QPushButton(self.Sidebar)
		self.Home.setGeometry(QtCore.QRect(20, 110, 171, 51))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.Home.setFont(font)
		self.Home.setStyleSheet("QPushButton{\n"
		"    background-color: rgb(72, 67, 67);\n"
		"    color: rgb(255, 255, 255);\n"
		"}")
		self.Home.setObjectName("Home")
		self.Logout = QtWidgets.QPushButton(self.Sidebar)
		self.Logout.setGeometry(QtCore.QRect(20, 520, 171, 51))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.Logout.setFont(font)
		self.Logout.setStyleSheet("QPushButton{\n"
		"    background-color: rgb(72, 67, 67);\n"
		"    color: rgb(255, 255, 255);\n"
		"}")
		self.Logout.setObjectName("Logout")
		self.Nama_Klien = QtWidgets.QLabel(self.centralwidget)
		self.Nama_Klien.setGeometry(QtCore.QRect(640, 10, 251, 61))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(16)
		self.Nama_Klien.setFont(font)
		self.Nama_Klien.setObjectName("Nama_Klien")
		self.header_pesan = QtWidgets.QLabel(self.centralwidget)
		self.header_pesan.setGeometry(QtCore.QRect(250, 60, 301, 41))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.header_pesan.setFont(font)
		self.header_pesan.setStyleSheet("QLabel{\n"
		"    color: rgb(0, 0, 0);\n"
		"}")
		self.header_pesan.setObjectName("header_pesan")
		self.tabel_pesan = QtWidgets.QTableWidget(self.centralwidget)
		self.tabel_pesan.setGeometry(QtCore.QRect(250, 110, 588, 361))
		self.tabel_pesan.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.tabel_pesan.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tabel_pesan.setColumnCount(4)
		self.tabel_pesan.setObjectName("tabel_pesan")
		self.tabel_pesan.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.tabel_pesan.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabel_pesan.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabel_pesan.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tabel_pesan.setHorizontalHeaderItem(3, item)
		self.tabel_pesan.verticalHeader().setVisible(False)
		self.tabel_pesan.verticalHeader().setDefaultSectionSize(30)
		self.button_pesan = QtWidgets.QPushButton(self.centralwidget)
		self.button_pesan.setGeometry(QtCore.QRect(630, 500, 211, 31))
		font = QtGui.QFont()
		font.setFamily("Roboto")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.button_pesan.setFont(font)
		self.button_pesan.setStyleSheet("QPushButton{\n"
		"    background-color: rgb(92, 184, 92);\n"
		"}")
		self.button_pesan.setObjectName("button_pesan")
		PesanRSWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(PesanRSWindow)
		self.statusbar.setObjectName("statusbar")
		PesanRSWindow.setStatusBar(self.statusbar)

		# Fungsionalitas tambahan
		# Set ID_Pengguna
		self.ID_Pengguna = ID_Pengguna
		
		# Setup koneksi ke database SQL
		self.setupSQL()
		
		# Apabila tombol pesan RS diklik
		self.button_pesan.clicked.connect(self.showConfirmBox)

		# Apabila tombol Logout di klik
		self.Logout.clicked.connect(self.logout)

		self.loadTable()
		
		self.retranslateUi(PesanRSWindow)
		QtCore.QMetaObject.connectSlotsByName(PesanRSWindow)

	
	def setupSQL(self):
		# Melakukan setup koneksi ke database
		config = {
			"user": "root",
			"password": "root",
			"host": "localhost",
			"port" : "3307"
		}
		self.DB_NAME = 'Cover_Me'
		self.db = mysql.connector.connect(**config)
		self.cursor = self.db.cursor()

	def pesanRS(self, i):
		# Melakukan pemesanan rumah sakit oleh klien
		# Apabila pesanan tidak valid (sudah pernah pesan atau masih ada pemesanan berlangsung) akan dimunculkan pesan kesalahan
		if (i.text()=="&Yes"):
			Nama_RS = str(self.tabel_pesan.selectedItems()[0].text())
			ID_RS = get_idRS(self.db,self.cursor,self.DB_NAME,Nama_RS)[1]
			res= add_new_pesanan(self.db,self.cursor,self.DB_NAME,ID_RS,self.ID_Pengguna)
			if (res[0]==1):
				tambah_pasien(self.db,self.cursor,self.DB_NAME,Nama_RS)
				self.loadTable()
				self.showSucc("Pesanan berhasil dibuat")
			else:
				self.showAlert(res[1])
		else :
			print("Gjadi Pesen")

	def showAlert(self,err):
		# Menampilkan pesan kesalahan
		msg = QtWidgets.QMessageBox()
		msg.setIcon(QtWidgets.QMessageBox.Critical)
		msg.setText(err)
		x = msg.exec_()

	def showSucc(self,succ):
		msg = QtWidgets.QMessageBox()
		msg.setIcon(QtWidgets.QMessageBox.Information)
		msg.setText(succ)
		x = msg.exec_()

	def showConfirmBox(self):
		# Menampilkan confirmation box apabila tombol pemesanan diklik
		# Apabila Klien belum memilih rumah sakit akan ditampilkan pesan kesalahan
		try:
			print(self.tabel_pesan.selectedItems()[0].text())
			msg = QtWidgets.QMessageBox()
			msg.setWindowTitle("Konfirmasi Pemesanan")
			msg.setText("Apakah anda yakin ingin memesan :")
			msg.setInformativeText("Nama: "+self.tabel_pesan.selectedItems()[0].text() +"\nHarga :"+self.tabel_pesan.selectedItems()[1].text())
			msg.setIcon(QtWidgets.QMessageBox.Question)
			msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
			msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
			msg.buttonClicked.connect(self.pesanRS)
			x = msg.exec_()
		except:
			self.showAlert("Anda belum memilih rumah sakit")

	def loadTable(self):
		# Melakukan konfigurasi ukuran tabel dan load dari database
		self.tabel_pesan.setColumnWidth(0,225)
		self.tabel_pesan.setColumnWidth(1,150)
		self.tabel_pesan.setColumnWidth(2,105)
		self.tabel_pesan.setColumnWidth(3,105)
		res = get_rs_klien(self.cursor,self.DB_NAME)
		if (res[0]==1):
			data = res[1]
			self.tabel_pesan.setRowCount(len(data))
			idx = 0
			for row in data:
				print(row)
				self.tabel_pesan.setItem(idx, 0, QtWidgets.QTableWidgetItem(row[0]))
				self.tabel_pesan.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(row[1])))
				self.tabel_pesan.setItem(idx, 2, QtWidgets.QTableWidgetItem(str(row[2])))
				self.tabel_pesan.setItem(idx, 3, QtWidgets.QTableWidgetItem(str(row[3])))
				idx = idx + 1
		else: 
			self.showAlert(res[1])
	
	def logout(self):
		# Melakukan fungsionalitas logout
		from ui_login import Ui_LoginWindow
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_LoginWindow()
		self.ui.setupUi(self.window)
		self.window.show()
		self.PesanRSWindow.close()
		print("Logout")
		return

	
	def retranslateUi(self, PesanRSWindow):
		# Menulis ulang text di GUI
		_translate = QtCore.QCoreApplication.translate
		PesanRSWindow.setWindowTitle(_translate("PesanRSWindow", "PesanRSWindow"))
		self.SuhuHarian.setText(_translate("PesanRSWindow", "Suhu Harian"))
		self.label.setText(_translate("PesanRSWindow", "CoverMe"))
		self.PesanRS.setText(_translate("PesanRSWindow", "Pesan RS"))
		self.Pesanan.setText(_translate("PesanRSWindow", "Pesanan"))
		self.Home.setText(_translate("PesanRSWindow", "Home"))
		self.Nama_Klien.setText(_translate("PesanRSWindow", "Welcome  <KlienName>"))
		self.Logout.setText(_translate("PesanRSWindow", "Logout"))
		username_Pengguna = get_username(self.cursor,self.DB_NAME,self.ID_Pengguna)[1]
		self.Nama_Klien.setText(_translate("PesanRSWindow", "Welcome  "+username_Pengguna))
		self.header_pesan.setText(_translate("PesanRSWindow", "Rumah Sakit Tersedia"))
		item = self.tabel_pesan.horizontalHeaderItem(0)
		item.setText(_translate("PesanRSWindow", "Nama_Rs"))
		item = self.tabel_pesan.horizontalHeaderItem(1)
		item.setText(_translate("PesanRSWindow", "Harga Rumah Sakit"))
		item = self.tabel_pesan.horizontalHeaderItem(2)
		item.setText(_translate("PesanRSWindow", "Kapasitas"))
		item = self.tabel_pesan.horizontalHeaderItem(3)
		item.setText(_translate("PesanRSWindow", "Jumlah Pasien"))
		self.button_pesan.setText(_translate("PesanRSWindow", "+ Pesan Rumah Sakit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    print("mainAkses")
    PesanRSWindow = QtWidgets.QMainWindow()
    ui = Ui_PesanRSWindow()
    ui.setupUi(PesanRSWindow)
    PesanRSWindow.show()
    sys.exit(app.exec_())
