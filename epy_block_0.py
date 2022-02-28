"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt, time, threading


class txrx(gr.basic_block):
    """
    docstring for block txrx
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="txrx",
            in_sig=None,
            out_sig=None)
        self.time_count = 5 #initial timestamp to allow for setup time
        self.current_freq = 100000000
        self.message_port_register_out(pmt.intern("rx_cmd"))
        threading.Thread(target=self.send_rx_cmd).start()
        
    def send_rx_cmd(self):
    	time.sleep(1)
    	count = 0 
    	while (count < 10000):
    	    self.time = pmt.cons(
    	    pmt.from_uint64(int(self.time_count)),
    	    pmt.from_double((self.time_count) % 1),
    	)
    	rx_cmd = pmt.make_dict()
    	rx_cmd = pmt.dict_add(rx_cmd, pmt.intern('time'), self.time)
    	rx_cmd = pmt.dict_add(rx_cmd, pmt.intern('freq'), pmt.from_double(self.current_freq))
    	self.message_port_pub(pmt.intern('rx_cmd'),rx_cmd)
    	count += 1
    	self.time_count += 0.5
    	time.sleep(2) 