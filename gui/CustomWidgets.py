#! /usr/bin/python3

#
# 31-Jul-2023 - based on https://www.pythonguis.com/pyqt6-tutorial/
#

from PySide6 import QtWidgets

class MyQTextEdit(QtWidgets.QTextEdit):

    def focusInEvent(self, event):
        self.selectAll()
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        cursor = self.textCursor()
        cursor.clearSelection()
        self.setTextCursor(cursor)
        super().focusOutEvent(event)
