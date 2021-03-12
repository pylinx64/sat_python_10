from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z =	pos.z
block = 20
air = 10

l = 20
h = 20
w = 20

x2 = x + l
y2 = y + h
z2 = z + w

mc.setBlocks(x, y, z, x2, y2, z2, block)
mc.setBlocks(x + 1, y + 1, z + 1, x2 -1, y2 - 1, z2 -1, air)
