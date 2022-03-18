#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Extract
# GNU Radio version: v3.8.2.0-57-gd71cd177

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from datetime import datetime
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class extract(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Extract")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Extract")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "extract")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.prefix = prefix = 'C:\\Users\\intern\\Documents\\GitHub\\Wifi-Cam\\signal_data\\filename'
        self.tuning = tuning = 2.422e9
        self.time = time = prefix + datetime.now().strftime("%H.%M.%S")
        self.samp_rate = samp_rate = 1e6
        self.duration = duration = 1
        self.Switch = Switch = 0

        ##################################################
        # Blocks
        ##################################################
        self._tuning_range = Range(70e6, 3e9, 2e6, 2.422e9, 200)
        self._tuning_win = RangeWidget(self._tuning_range, self.set_tuning, 'tuning', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tuning_win)
        # Create the options list
        self._Switch_options = (0, 1, )
        # Create the labels list
        self._Switch_labels = ('Off', 'On', )
        # Create the combo box
        self._Switch_tool_bar = Qt.QToolBar(self)
        self._Switch_tool_bar.addWidget(Qt.QLabel('Switch' + ": "))
        self._Switch_combo_box = Qt.QComboBox()
        self._Switch_tool_bar.addWidget(self._Switch_combo_box)
        for _label in self._Switch_labels: self._Switch_combo_box.addItem(_label)
        self._Switch_callback = lambda i: Qt.QMetaObject.invokeMethod(self._Switch_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._Switch_options.index(i)))
        self._Switch_callback(self.Switch)
        self._Switch_combo_box.currentIndexChanged.connect(
            lambda i: self.set_Switch(self._Switch_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._Switch_tool_bar)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_center_freq(tuning, 0)
        self.uhd_usrp_source_0.set_gain(50, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0.set_bandwidth(samp_rate, 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec())
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            tuning, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(True)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(Switch)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, time, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-140, 1e-4, 0, True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.analog_pwr_squelch_xx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "extract")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_time(self.prefix + datetime.now().strftime("%H.%M.%S"))

    def get_tuning(self):
        return self.tuning

    def set_tuning(self, tuning):
        self.tuning = tuning
        self.qtgui_sink_x_0.set_frequency_range(self.tuning, self.samp_rate)
        self.uhd_usrp_source_0.set_center_freq(self.tuning, 0)

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time
        self.blocks_file_sink_0.open(self.time)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(self.tuning, self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_bandwidth(self.samp_rate, 0)

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_Switch(self):
        return self.Switch

    def set_Switch(self, Switch):
        self.Switch = Switch
        self._Switch_callback(self.Switch)
        self.blocks_multiply_const_vxx_0.set_k(self.Switch)





def main(top_block_cls=extract, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
