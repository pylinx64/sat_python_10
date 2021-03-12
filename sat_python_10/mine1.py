from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time

while True:

	x = random.randint(-250, 250)
	z = random.randint(-250, 250)
	y = mc.getHeight(x, z)

	time.sleep(4)

	mc.player.setTilePos(x, y, z)
