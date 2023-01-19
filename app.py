from datetime import datetime
import helper
import bnn
import jib
import advice

# main
now = datetime.today()

### bnn
bnn_desktop = bnn.get_bnn("https://www.bnn.in.th/en/p/desktop-and-all-in-one/desktop?page=pagesize")
helper.export("_".join(["bnn_desktop", now.strftime("%d%m%Y")]), bnn_desktop, ['Title','Info','Price','Stock'])

bnn_gaming_desktop = bnn.get_bnn("https://www.bnn.in.th/en/p/desktop-and-all-in-one/gaming-desktop?page=pagesize")
helper.export("_".join(["bnn_gaming_desktop", now.strftime("%d%m%Y")]), bnn_gaming_desktop, ['Title','Info','Price','Stock'])

bnn_mini_pc = bnn.get_bnn("https://www.bnn.in.th/en/p/desktop-and-all-in-one/mini-pc?page=pagesize")
helper.export("_".join(["bnn_mini_pc", now.strftime("%d%m%Y")]), bnn_mini_pc, ['Title','Info','Price','Stock'])

bnn_aio = bnn.get_bnn("https://www.bnn.in.th/en/p/desktop-and-all-in-one/all-in-one?page=pagesize")
helper.export("_".join(["bnn_aio", now.strftime("%d%m%Y")]), bnn_aio, ['Title','Info','Price','Stock'])


### jib
jib_desktop = jib.get_jib(27)
helper.export("_".join(["jib_desktop", now.strftime("%d%m%Y")]), jib_desktop, ['Title','Info','Price','Stock'])

jib_aio = jib.get_jib(28)
helper.export("_".join(["jib_aio", now.strftime("%d%m%Y")]), jib_aio, ['Title','Info','Price','Stock'])

jib_mini_pc = jib.get_jib(1496)
helper.export("_".join(["jib_mini_pc", now.strftime("%d%m%Y")]), jib_mini_pc, ['Title','Info','Price','Stock'])

### advice
av_aio = advice.get_av("all-in-one-pc", ["acer","asus", "lenovo", "dell", "hp"])
helper.export("_".join(["av_aio", now.strftime("%d%m%Y")]), av_aio, ['Title','Info','Price','Stock'])

av_desktop = advice.get_av("desktop-pc", ["acer","asus", "lenovo", "dell", "hp"])
helper.export("_".join(["av_desktop", now.strftime("%d%m%Y")]), av_desktop, ['Title','Info','Price','Stock'])

av_mini_pc = advice.get_av("mini-pc", ["asus", "intel", "msi"])
helper.export("_".join(["av_mini_pc", now.strftime("%d%m%Y")]), av_mini_pc, ['Title','Info','Price','Stock'])

av_gaming_desktop = advice.get_av("gaming-desktop-pc", ["acer","asus", "msi", "dell", "hp"])
helper.export("_".join(["av_gaming_desktop", now.strftime("%d%m%Y")]), av_gaming_desktop, ['Title','Info','Price','Stock'])
    



