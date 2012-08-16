#!/usr/bin/python
# -*- coding: utf-8 -*-
# www.halitalptekin.com - Halit Alptekin

from PyQt4 import QtCore
from PyQt4 import QtGui
from araci import Ui_MainWindow
import sys, os, threading

class AsyncArama(threading.Thread):
	def __init__(self, yer, kelime, uzanti):
		threading.Thread.__init__(self)
		self.yer = yer
		self.kelime = kelime
		self.uzanti = uzanti
		self.bulunan = []

	def run(self):
		
		def dosyalama(yer, uzanti):
			dosyalist = []

			for kok, altdizinler, dosyalar in os.walk(yer):
				for dosya in dosyalar:
					if dosya.endswith(uzanti):
						dosyalist.append(os.path.join(kok,dosya))	
			return dosyalist

		def aramayap(yer, kelime, uzanti):
			dosyalar = dosyalama(yer, uzanti)
			for dosya in dosyalar:
				try:
					satirlar = open(dosya)
					for satir in satirlar:
						if satir.find(kelime) > 0:
							if self.bulunan.count(dosya) == 0:
								self.bulunan.append(dosya)	
				except:
					pass				
		aramayap(self.yer, self.kelime, self.uzanti)						
		return self.bulunan		

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.statusBar().showMessage(unicode("Arama icin hazir\n"))
		self.aramayeri = "kayit"
		self.uzanti    = "uzanti"
		self.kelime	   = "kelime"
		self.bulunan   = []

	@QtCore.pyqtSignature("bool")
        def on_pushButton_clicked(self):
        	self.aramayeri = "%s" %QtGui.QFileDialog.getExistingDirectory(self, "Dizin Sec")
        	self.statusBar().showMessage(unicode("Arama yeri: %s\n"%self.aramayeri))

	@QtCore.pyqtSignature("bool")
        def on_pushButton_2_clicked(self):
        	self.uzanti, tamam=QtGui.QInputDialog.getItem(self, u"Uzanti Secimi", u"Bir uzanti seciniz:", [".py", ".txt"], 0, False)      		
        	self.statusBar().showMessage(unicode("Arama yeri: %s/*%s\n"%(self.aramayeri, self.uzanti)))

	@QtCore.pyqtSignature("bool")
        def on_pushButton_3_clicked(self): 

        	self.kelime = self.lineEdit.text()
        	self.listWidget.clear()

        	def dosyalama(yer, uzanti):
				dosyalist = []

				for kok, altdizinler, dosyalar in os.walk(yer):
					for dosya in dosyalar:
						if dosya.endswith(uzanti):
							dosyalist.append(os.path.join(kok,dosya))	
				return dosyalist

	        def aramayap(yer, kelime, uzanti):
	        	yer = str(yer)
	        	kelime = str(kelime)
	        	uzanti = str(uzanti)

			dosyalar = dosyalama(yer, uzanti)
			for dosya in dosyalar:
				satirlar = open(dosya)
				for satir in satirlar:
					if satir.find(kelime) > 0:
						if self.bulunan.count(dosya) == 0:
							self.bulunan.append(dosya)
						return 1

						  

        	if self.aramayeri == "kayit":
        		a = QtGui.QMessageBox()
	        	a.setWindowTitle("Arama Yeri Bos!")		
	        	a.setText("Lutfen arama yerini secip tekrar deneyiniz.")
	        	a.setIcon(a.Information)
	        	a.exec_()

        	if self.uzanti == "uzanti":
        		a = QtGui.QMessageBox()
	        	a.setWindowTitle("Uzanti Bos!")		
	        	a.setText("Lutfen uzanti secip tekrar deneyiniz.")
	        	a.setIcon(a.Information)
	        	a.exec_()	

	        if self.kelime == "kelime":
        		a = QtGui.QMessageBox()
	        	a.setWindowTitle("Kelime Bos!")		
	        	a.setText("Lutfen arama kelimesi secip tekrar deneyiniz.")
	        	a.setIcon(a.Information)
	        	a.exec_()

	        aramath = AsyncArama(self.aramayeri, self.kelime, self.uzanti)
	        aramath.start()

	        if aramath.run():	        	
		        for sonuc in aramath.run():
		        	self.listWidget.addItem(sonuc)
	        else:
	        	self.listWidget.addItem("Bulunamadi!")	

app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())		
