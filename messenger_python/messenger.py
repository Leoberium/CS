import requests
import clientui
from datetime import datetime
from PyQt5 import QtWidgets, QtCore


class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):

    def __init__(self, url="http://127.0.0.1:5000/"):
        super().__init__()
        self.url = url
        self.setupUi(self)

        self.pushButton.pressed.connect(self.send_message)

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def get_messages(self):
        try:
            response = requests.get(
                self.url + "get_messages",
                params={"after": self.after}
            )
        except:
            return

        if response.status_code == 200:
            messages = response.json()["messages"]

            for message in messages:
                self.after = message["time"]
                ftime = datetime.fromtimestamp(message["time"]).strftime("%Y-%m-%d %H:%M:%S")
                self.textBrowser.append(ftime + " " + message["author"])
                self.textBrowser.append(message["text"])
                self.textBrowser.append("")

    def send_message(self):
        print("123123")

        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()

        try:
            response = requests.post(
                self.url + "send_message",
                json={"text": text, "author": name}
            )
        except requests.exceptions.ConnectionError:
            self.textBrowser.append("Server is not accessible")
            self.textBrowser.append("")
            self.textEdit.repaint()
            return

        if response.status_code != 200:
            self.textBrowser.append("Validation error")
            self.textBrowser.append("")
            self.textEdit.repaint()
            return

        self.textEdit.clear()
        self.textEdit.repaint()


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec_()
