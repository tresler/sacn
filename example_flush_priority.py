import time
import sacn

unv = 1

# setup sacn sender server
sender = sacn.sACNsender()
sender.activate_output(unv, dmxStartCodeWithChanPriority=True)
sender[unv].priority = 1
sender[unv].multicast = True
sender[unv].manual_flush = True
sender.start()

# send dmx data and active channel
sender[unv].dmx_priority = (1, 0, 1, 1, 1)
sender[unv].dmx_data = (235, 128, 16, 85, 0)

# sending loop
sender_time = round(time.time())
while True:
    if round(time.time()) > sender_time + 0.5:
        sender.flush()
        sender_time = round(time.time())
        print("FLASH")
    else:
        time.sleep(0.1)