from mcpi.minecraft import Minecraft

def hi():
    "_mcp: just saying hello"
    mc = Minecraft.create()
    mc.postToChat("Hello!")

def blk():
    "_mcp: place 10 blocks of diamond"
    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    for i in range(10):
        mc.setBlock(pos.x+1, pos.y+i, pos.z, 57)

def castleBase():
    "_mcp: build castle base"
    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    count = 0
    for i in range(20):
        for j in range(4):
            for k in range(10):
                if j == 0 and count % 2 == 0:
                    mc.setBlock(pos.x+1, pos.y+i, pos.z+k, 57)
                elif j == 0:
                    mc.setBlock(pos.x+1, pos.y+i, pos.z+k, 41)
                elif j == 1 and count % 2 == 0:
                    mc.setBlock(pos.x+1+k, pos.y+i, pos.z, 57)
                elif j == 1:
                    mc.setBlock(pos.x+1+k, pos.y+i, pos.z, 41)
                elif j == 2 and count % 2 == 0:
                    mc.setBlock(pos.x+11, pos.y+i, pos.z+k, 41) 
                elif j == 2:
                    mc.setBlock(pos.x+11, pos.y+i, pos.z+k, 57)
                elif j == 3 and count % 2 == 0:
                    mc.setBlock(pos.x+1+k, pos.y+i, pos.z+10, 57)
                elif j == 3:
                    mc.setBlock(pos.x+1+k, pos.y+i, pos.z+10, 41)
                count += 1
        count += 1


def test():
    "_mcp: place area dimension block, by blockID"
    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    look = mc.player.getDirection()

    x = round(pos.x + look.x)
    y = round(pos.y + look.y + 2)
    z = round(pos.z + look.z)
    
    mc.setBlock(x, y, z, 41)


 
