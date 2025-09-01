#import
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QVBoxLayout,QWidget,QLabel,QPushButton,QGridLayout,QLineEdit
#main window
app=QApplication([])
main_window=QWidget()
main_window.setWindowTitle("calculator")
main_window.resize(500,500)
#create
text_box=QLineEdit()
grid=QGridLayout()
buttons=["7","8","9","/",
         "4","5","6","*",
         "1","2","3","-",
         "0",".","=","+"]
c=QPushButton("clear")
d=QPushButton("delete")
#function creation
def button_func():
    button=app.sender() #konsa button click hova
    text=button.text() #button to text creation
    if text=="=":
        symbol=text_box.text()
        try:
            res=eval(symbol)
            text_box.setText(str(res))
        except:
            text_box.setText("ERROR")
    elif text=="clear":
        text_box.clear()
    elif text=="delete":
        new=text_box.text()
        text_box.setText(new[:-1])
    else:
        new1=text_box.text()
        text_box.setText(new1+text)
#widgets set up
row=0
col=0
for text in buttons:
    button=QPushButton(text)
    button.clicked.connect(button_func)
    grid.addWidget(button,row,col)
    col+=1
    if col>3:
        col=0
        row+=1
        
main_=QVBoxLayout()
button_=QHBoxLayout()
main_.addWidget(text_box)
main_.addLayout(grid)
button_.addWidget(c)
button_.addWidget(d)
main_.addLayout(button_)
main_window.setLayout(main_)

c.clicked.connect(button_func)
d.clicked.connect(button_func)


#show objects
main_window.show()
app.exec()