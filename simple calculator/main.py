from simple_calculator import Ui_Dialog
from qtpy.QtWidgets import QDialog, QApplication
from qtpy.QtCore import Qt
import sys


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_button_signals()
        self.typing_high = True  # keeps in mind which lcd to display to
        self._up = 0
        self._down = 0
        self.symbol=''
        self.reset_cal()

    def reset_cal(self):

        self.factor_before_float = 10
        self.factor_after_float = 1

    def display_2_lcd(self, num, digit, lcd):
        # todo: check for max possible digit, currently is 20
        precision = len(str(self.factor_after_float)) - 1
        f = f"{{:.{precision}f}}"
        if digit is None:
            #   means equal sign is pressed so reset the cal for new stuff
            pass
        else:
            num = (num * self.factor_before_float) + (digit / self.factor_after_float)
        str_to_display = f.format(num)
        lcd.display(str_to_display)
        if self.factor_after_float != 1:
            self.factor_after_float = self.factor_after_float * 10
        return num

    def number_clicked(self, digit):
        if self.typing_high:
            self._up = self.display_2_lcd(self._up, digit, self.lcd_high_num)
        else:
            self._down = self.display_2_lcd(self._down, digit, self.lcd_low_num)

    def symbol_clicked(self, symbol):
        if symbol == '=':
            ans = 0
            if not self.typing_high:
                self.reset_cal()
                self.typing_high = True
                if self.symbol == '+':
                    ans = self._up + self._down
                elif self.symbol == '-':
                    ans = self._up - self._down
                elif self.symbol == '*':
                    ans = self._up * self._down
                elif self.symbol == r'/':
                    ans = self._up / self._down
                else:
                    raise Exception(f'Wrong symbol: {symbol}')
            self.symbol = ''
            self.display_2_lcd(ans, None, self.lcd_result)
            return None
        elif symbol == '.':
            if self.typing_high:
                self._up = float(self._up)
            else:
                self._down = float(self._down)
            self.factor_before_float = 1
            self.factor_after_float = 10
            return None
        self.reset_cal()
        self.label_sign.setText(symbol)
        self.symbol = symbol
        self.typing_high = False

    def KeyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            print("here")
            if not self.typing_high:
                print('Pressed enter and are about to get served some good dick')
                self.typing_high = True
                ans = 0
                if self.symbol == '+':
                    ans = self._up + self._down
                elif self.symbol == '-':
                    ans = self._up - self._down
                elif self.symbol == '*':
                    ans = self._up * self._down
                elif self.symbol == r'/':
                    ans = self._up / self._down
                self.display_2_lcd(ans, None, self.lcd_result)

    def connect_button_signals(self):
        self.butt_0.clicked.connect(lambda: self.number_clicked(0))
        self.butt_1.clicked.connect(lambda: self.number_clicked(1))
        self.butt_2.clicked.connect(lambda: self.number_clicked(2))
        self.butt_3.clicked.connect(lambda: self.number_clicked(3))
        self.butt_4.clicked.connect(lambda: self.number_clicked(4))
        self.butt_5.clicked.connect(lambda: self.number_clicked(5))
        self.butt_6.clicked.connect(lambda: self.number_clicked(6))
        self.butt_7.clicked.connect(lambda: self.number_clicked(7))
        self.butt_8.clicked.connect(lambda: self.number_clicked(8))
        self.butt_9.clicked.connect(lambda: self.number_clicked(9))

        self.butt_plus.clicked.connect(lambda: self.symbol_clicked('+'))
        self.butt_minus.clicked.connect(lambda: self.symbol_clicked('-'))
        self.butt_multiple.clicked.connect(lambda: self.symbol_clicked('*'))
        self.butt_division.clicked.connect(lambda: self.symbol_clicked('/'))
        self.butt_equal.clicked.connect(lambda: self.symbol_clicked('='))
        self.butt_point.clicked.connect(lambda: self.symbol_clicked('.'))


if __name__ == '__main__':
    app = QApplication([])
    d = MainDialog()
    d.show()
    sys.exit(app.exec_())
