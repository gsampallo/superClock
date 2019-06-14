import mcp
import time

io = mcp.MCP23017()
io1 = mcp.MCP23017(0x24)

outPins = list(range(0,16))

for pinNum in outPins:
    io.setup(pinNum, mcp.OUT)
    io1.setup(pinNum, mcp.OUT)

while True:
    for pinNum in outPins:
        io.output(pinNum,1)
        time.sleep_ms(120)

    for pinNum in outPins:
        io1.output(pinNum,1)
        time.sleep_ms(120)

    for pinNum in outPins:
        io.output(pinNum,0)
        time.sleep_ms(120)

    for pinNum in outPins:
        io1.output(pinNum,0)
        time.sleep_ms(120)
    