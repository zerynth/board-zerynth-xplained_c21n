from base import *
from devices import *
import time

class XplainedProSamC21N(Board):
    ids_vendor = {
        "03EB":frozenset(("2111","2169"))
    }

    @staticmethod
    def match(dev):
        return dev["vid"] in XplainedProSamC21N.ids_vendor and dev["pid"] in XplainedProSamC21N.ids_vendor[dev["vid"]]

    def reset(self):
        # hack to reset
        proc.runcmd("edbg_c21n", "-F", "r,1,1", "-t", "atmel_cm0p")

    def burn(self,bin,outfn=None):
        fname = fs.get_tempfile(bin)
        outfn(fname)
        res,out,err= proc.runcmd("edbg_c21n", "-ebpv", "-t", "atmel_cm0p","-s",self.sid,"-f", fname,outfn=outfn)
        fs.del_tempfile(fname)
        if res:
            return False,out
        return True,out