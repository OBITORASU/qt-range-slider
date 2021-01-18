import sys
import unittest

from PyQt5.QtCore import QRect
from PyQt5.QtTest import QTest
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from qt_range_slider import QtRangeSlider

class QtRangeSliderTest(unittest.TestCase):
	"""Tests for qt_range_slider
	"""
	@classmethod
	def setUpClass(cls):
		cls._app = QApplication(sys.argv)
		cls._form = QMainWindow()
		cls._form.setFixedWidth(500)
		cls._form.setFixedHeight(100)

	def test_init(self):
		slider = QtRangeSlider(QtRangeSliderTest._form, 0, 10, 3, 5)
		self.assertIsNotNone(slider)
		with self.assertRaises(ValueError):
			QtRangeSlider(QtRangeSliderTest._form, 0, 10, 5, 3)

	def test_paint_event(self):
		slider = QtRangeSlider(QtRangeSliderTest._form, 0, 10, 3, 5)
		unused_event = QPaintEvent(QRect(0, 0, 1, 1))
		slider.paintEvent(unused_event)
