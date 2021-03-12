from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
pos = mc.player.getTilePos()

while True:
	id_block = 5
	mc.setBlocks(pos.x, pos.y - 1, pos.z, 
				pos.x + 5, pos.y -1 , pos.z + 5, id_block)
	time.sleep(0.4)
