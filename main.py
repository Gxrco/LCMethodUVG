import math as l
from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class gui(QMainWindow):

	def __init__(self):
		super().__init__()
		uic.loadUi("Matrices.ui",self)
		self.btncalculate.clicked.connect(self.determinantOfMatrix)
		self.btnexit.clicked.connect(exit)

	def determinantOfMatrix(self):
		mat = [[self.txb11.toPlainText(),self.txb12.toPlainText(),self.txb13.toPlainText(),self.txb14.toPlainText(),self.txb15.toPlainText(),self.txb16.toPlainText(),self.txb17.toPlainText()],
			   [self.txb21.toPlainText(),self.txb22.toPlainText(),self.txb23.toPlainText(),self.txb24.toPlainText(),self.txb25.toPlainText(),self.txb26.toPlainText(),self.txb27.toPlainText()],
			   [self.txb31.toPlainText(),self.txb32.toPlainText(),self.txb33.toPlainText(),self.txb34.toPlainText(),self.txb35.toPlainText(),self.txb36.toPlainText(),self.txb37.toPlainText()],
			   [self.txb41.toPlainText(),self.txb42.toPlainText(),self.txb43.toPlainText(),self.txb44.toPlainText(),self.txb45.toPlainText(),self.txb46.toPlainText(),self.txb47.toPlainText()],
			   [self.txb51.toPlainText(),self.txb52.toPlainText(),self.txb53.toPlainText(),self.txb54.toPlainText(),self.txb55.toPlainText(),self.txb56.toPlainText(),self.txb57.toPlainText()],
			   [self.txb61.toPlainText(),self.txb62.toPlainText(),self.txb63.toPlainText(),self.txb64.toPlainText(),self.txb65.toPlainText(),self.txb66.toPlainText(),self.txb67.toPlainText()],
			   [self.txb71.toPlainText(),self.txb72.toPlainText(),self.txb73.toPlainText(),self.txb74.toPlainText(),self.txb75.toPlainText(),self.txb76.toPlainText(),self.txb77.toPlainText()]]
		
		mat = [[int(i) for i in inner_list] for inner_list in mat]

		N = len(mat)

		mul = 1

		while (N > 2):
			
			M = [[0 for i in range(N-1)] for j in range(N-1)]

			next_index = 1

			while (mat[0][0] == 0):
				if (mat[next_index][0] > 0):
					
					for k in range(N):
						temp = mat[0][k]
						mat[0][k] = mat[next_index][k]
						mat[next_index][k] = temp

					mul = mul * pow((-1),(next_index))

				elif (next_index == (N - 1)):
					return 0;
				next_index += 1

			p = mat[0][0]

			mul = mul * pow(1 / p, N - 2)

			for i in range(1,N):
				for j in range(1,N,1):
					
					M[i - 1][j - 1] = mat[0][0] * mat[i][j] - mat[i][0] * mat[0][j]

			for i in range(N - 1):
				for j in range(N - 1):
					mat[i][j] = M[i][j]

			N -= 1

		D = mul * (mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0])

		if D < 0 :
			self.lblresult.setText(str(float(l.floor(D))))
		else:
			self.lblresult.setText(str(float(l.ceil(D))))



if __name__ == '__main__':
	x = QApplication(sys.argv)
	y = gui()
	y.show()
	sys.exit(x.exec_())
	

#determinantOfMatrix(mat, len(mat))
	
