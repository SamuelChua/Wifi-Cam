"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr, uhd
import time

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Issue Stream Cmds',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = input_items[0] * self.example_param
        count = 0 
        num_samples = 1000000*1
        while (count < 5):
            time.sleep(1.0)
            uhd.usrp_source_sptr.clear_command_time(self)
            uhd.usrp_source_sptr.get_time_now()
            uhd.usrp_source_sptr.set_command_time(now_time + uhd.time_spec.from_ticks(2,1.0)) 
            uhd.usrp_source_sptr.issue_stream_cmd(num_samples)
        count += 1
        time.sleep(2) 
        return len(output_items[0])