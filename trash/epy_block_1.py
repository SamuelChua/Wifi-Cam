"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr, blocks
import pmt

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, value=1):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Swap File Sink',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.value = value
        self.enabled = 0    
        

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = input_items[0]
        if (self.enabled == self.value):
            self.default()
        else:
            self.rebuild_blocks()
        return len(output_items[0])

    def default(self):   
        self.lock()
        self.disconnect_all()
        self.connect(self, blocks.null_sink(gr.sizeof_gr_complex))
        self.unlock() 
    
    def rebuild_blocks(self):
        self.lock()
        self.disconnect_all()
        self.connect(self, blocks.file_sink(gr.sizeof_gr_complex, self.filename))
        self.unlock() 

