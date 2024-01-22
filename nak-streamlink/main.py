import cec

cec.init()

tv = cec.Device(cec.CECDEVICE_TV)
tv.power_on()