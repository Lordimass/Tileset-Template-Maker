import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import os

TILE_WIDTH    = 128
TILE_HEIGHT   = TILE_WIDTH
TILESET_SIZE  = [5, 1] 
BUFFER        = 5
BUFFER_COLOUR = (0,0,0)

imageSize = [
    TILE_WIDTH*TILESET_SIZE[0] + BUFFER*(TILESET_SIZE[0]+1),
    TILE_HEIGHT*TILESET_SIZE[1] + BUFFER*(TILESET_SIZE[1]+1)
]

print(f"Creating image of size {imageSize}")

img = Image.new(
    mode="RGBA",
    size=imageSize,
    color=(0,0,0,0)
    )


startPos = (BUFFER/2, 0)
imgDraw = ImageDraw.Draw(img)
for vLine in range(TILESET_SIZE[0]+1):
    print(f"Drawing line at {startPos}")
    imgDraw.line([startPos, (startPos[0], imageSize[1])],
                  fill = BUFFER_COLOUR,
                  width = BUFFER)
    startPos = (startPos[0] + TILE_WIDTH + BUFFER, startPos[1])

startPos = (0, BUFFER/2)
for hLine in range(TILESET_SIZE[1]+1):
    print(f"Drawing line at {startPos}")
    imgDraw.line([startPos, (imageSize[0], startPos[1])],
                  fill = BUFFER_COLOUR,
                  width = BUFFER)
    startPos = (startPos[0], startPos[1] + TILE_WIDTH + BUFFER)
    
img.save("output.png")
os.startfile("output.png")