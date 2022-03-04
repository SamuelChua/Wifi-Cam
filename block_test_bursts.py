"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, burst=False):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        
        self.burst = burst
        self.burst_state = False

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        
        if self.burst != self.burst_state:        
            self.burst_state = self.burst
        
            key = pmt.intern("burst")
            value = pmt.from_bool(self.burst_state)
            self.add_item_tag(0, self.nitems_written(0), key, value)
        
        output_items[0][:] = input_items[0] 
        return len(output_items[0])
