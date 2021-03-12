from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

x = -31
y = 84
z =	-54
block = 0

for y in range(64, 0, -1): 
	mc.setBlock(x, y, z, block)
	time.sleep(0.5)
