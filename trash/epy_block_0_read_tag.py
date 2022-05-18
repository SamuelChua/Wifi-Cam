"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt
 
class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,name='Read Tags', in_sig=[np.float32], out_sig=[np.float32])
 
    def work(self, input_items, output_items):
        tags = self.get_tags_in_window(0, 0, len(input_items[0]))
        for tag in tags:
            key = pmt.to_python(tag.key) # convert from PMT to python string
            value = pmt.to_python(tag.value) # Note that the type(value) can be several things, it depends what PMT type it was
            print ('key:', key)
            print ('value:', value, type(value))
            print ('')
        return len(input_items[0])