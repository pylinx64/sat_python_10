from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()

mc.setBlocks(pos.x, pos.y, pos.z,
			pos.x, pos.y, pos.z, 56)
