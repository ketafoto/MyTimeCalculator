#! /usr/bin/python3

#
# 23-Jul-2023
#
# Use "pip install -U pyinstaller" to install pyinstaller! What a wonderful tool!!!
# Use:
#   pyinstaller --clean --distpath . --onefile --windowed --icon "gui/novohours.ico" --add-data "gui;gui" novohours.py && rm -rf build novohours.spec
# to generate a self-contained novohours.exe out of novohours.py and it's
# dependencies. --add-data bundles the gui/ folder (the .ui and the .ico) into
# the exe, and --icon embeds the icon into the executable itself.
#

import os
import re
import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader

import gui.CustomWidgets

def resource_path(rel):
    # Resolve a bundled resource both when run from source and when frozen by
    # PyInstaller (which unpacks --add-data files into sys._MEIPASS).
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)

class NovoHours:
    def __init__(self):
        self.app     = QtWidgets.QApplication(sys.argv)
        self.app.setWindowIcon(QIcon(resource_path("gui/novohours.ico")))

        loader       = QUiLoader()
        loader.registerCustomWidget(gui.CustomWidgets.MyQTextEdit)
        self.window  = loader.load(resource_path("gui/MainWindow.ui"), None)
        self.window.setWindowIcon(QIcon(resource_path("gui/novohours.ico")))

        wnd = self.window
        wnd.btnPlus.clicked.connect(self.plus)
        wnd.btnReset.clicked.connect(self.reset)
        wnd.txtHrs.textChanged.connect(self.user_changed_hours)
        wnd.txtMns.textChanged.connect(self.user_changed_minutes)

        self.reset()

    def run(self):
        self.window.show()
        self.app.exec()

    def reset(self):
        self.last_hrs   = 0
        self.last_min   = 0
        self.last_sign  = None
        self.total_min  = 0
        self.window.lblResult.setText("")
        self.window.txtHrs.setText("")
        self.window.txtMns.setText("")
        self.window.txtHrs.setFocus()

    def user_changed_hours(self):
        new = self.window.txtHrs.toPlainText()
        new  = new.strip()
        if not new:
            return
        re_pattern = "^([-+]?)([0-9]*)$"
        m = re.match(re_pattern, new)
        if not m:
            QtWidgets.QMessageBox.critical(self.window, "Error", "invalid hours")
            return
        self.last_sign  = m.group(1) if m.group(1) else '+'
        self.last_hrs = int(m.group(2)) if m.group(2) else 0

    def user_changed_minutes(self):
        new = self.window.txtMns.toPlainText()
        enter_typed = True if "\n" in new else False
        new = new.strip()
        if not new:
            return
        re_pattern = "^([0-5]?[0-9]?)$"
        m = re.match(re_pattern, new)
        if not m:
            QtWidgets.QMessageBox.critical(self.window, "Error", "invalid minutes")
            return
        self.last_min = int(m.group(1)) if m.group(1) else 0

        if enter_typed:
            self.plus()

    def plus(self):
        if self.last_sign == '-':
            self.total_min -= (self.last_hrs * 60 + self.last_min)
        else:
            self.total_min += (self.last_hrs * 60 + self.last_min)

        # Show result
        #
        show_sign  = '+' if self.total_min > 0 else '-' if self.total_min < 0 else ''
        show_hours = int(abs(self.total_min) / 60)
        show_min   = int(abs(self.total_min) % 60)
        self.window.lblResult.setText(f"{show_sign}{show_hours:02}:{show_min:02}")
        self.window.txtHrs.setFocus()


if __name__ == '__main__':
    calc = NovoHours()
    calc.run()
