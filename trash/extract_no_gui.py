#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Extract_No GUI
# GNU Radio version: v3.8.2.0-57-gd71cd177

from datetime import datetime
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time


class extract_no_gui(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Extract_No GUI")

        ##################################################
        # Variables
        ##################################################
        self.prefix = prefix = 'C:\\Users\\intern\\Documents\\GitHub\\Wifi-Cam\\signal_data\\filename'
        self.veclength = veclength = 1024
        self.time = time = prefix + datetime.now().strftime("%H.%M.%S")
        self.samp_rate = samp_rate = 1e6    
        self.duration = duration = 5

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_center_freq(2.4118e9, 0)
        self.uhd_usrp_source_0.set_gain(50, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0.set_bandwidth(samp_rate, 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec())
        self.fft_vxx_0 = fft.fft_vcc(veclength, True, window.blackmanharris(1024), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, veclength)
        self.blocks_integrate_xx_0 = blocks.integrate_ff(100, veclength)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, 10240000)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*veclength, time, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(veclength)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_integrate_xx_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_head_0, 0))


    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_time(self.prefix + datetime.now().strftime("%H.%M.%S"))

    def get_veclength(self):
        return self.veclength

    def set_veclength(self, veclength):
        self.veclength = veclength

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time
        self.blocks_file_sink_0.open(self.time)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_bandwidth(self.samp_rate, 0)

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration





def main(top_block_cls=extract_no_gui, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
