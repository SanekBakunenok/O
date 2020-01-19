import time
import keyboard
import mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()

def mostik():
    mc.setBlocks(0,100,0,10,100,0,24)


while True:
    if keyboard.is_pressed("o"):
        mostik()

