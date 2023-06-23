import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *


# class 클래스_이름(상속할_클래스_이름)
class MyApp(QMainWindow):

    # 생성자
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))  # currentDate() 메서드를 통해 현재 날짜를 얻고 showMessage() 메서드로 상태표시줄에 현재 날짜를 표시했습니다.
        self.setWindowTitle('My First Application')  # setWindowTitle() 메서드는 타이틀바에 나타나는 창의 제목을 설정합니다.
        self.move(300, 300)  # move() 메서드는 위젯을 스크린의 x=300px, y=300px의 위치로 이동시킵니다.
        self.resize(500, 500)   # resize() 메서드는 위젯의 크기를 너비 500px, 높이 500px로 조절합니다.
        self.center()           # center() 메서드를 통해서 창이 화면의 가운데에 위치하게 됩니다.
        self.show()             # show() 메서드는 위젯을 스크린에 보여줍니다.

    # 메인 UI
    # 여기서 self는 MyApp 객체를 말합니다.
    def initUI(self):

        # 종료 Button
        btnButton = QPushButton("종료", self)
        btnButton.move(350, 450)
        btnButton.clicked.connect(self.btn_click)

        # ComboBox.
        cb = QComboBox(self)
        cb.addItem('한국')
        cb.addItem('미국')
        cb.move(10, 300)
        cb.activated[str].connect(self.onActivated)

        # Tab Widget
        tabs = QTabWidget(self)
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        tabs.addTab(tab1, "tab1")
        tabs.addTab(tab2, "tab3")
        tabs.addTab(tab3, "tab3")

        label1 = QLabel("tab1 widget", tab1)
        label2 = QLabel("tab2 widget", tab2)
        label3 = QLabel("tab3 widget", tab3)

        label1.move(10, 10)
        label2.move(10, 10)
        label3.move(10, 10)



# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

    # 종료 버튼
    def btn_click(self):
        QApplication.instance().quit()

    # 라벨 크기
    # 선택한 항목의 텍스트가 라벨에 나타나도록 하고, adjustSize() 메서드를 이용해서 라벨의 크기를 자동으로 조절하도록 합니다.
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    # UI 크기 및 정렬
    def center(self):
        qr = self.frameGeometry()  # frameGeometry() 메서드를 이용해서 창의 위치와 크기 정보를 가져옵니다.
        cp = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치를 파악합니다.
        qr.moveCenter(cp)  # 창의 직사각형 위치를 화면의 중심의 위치로 이동합니다.
        self.move(qr.topLeft())  # 현재 창을, 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킵니다.


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
