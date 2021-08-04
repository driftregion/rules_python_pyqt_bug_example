"""
By inspecting *dynamic!* path and breaking with ipdb, I can remove
the pygame .dlls in question before
```
import pygame, sys
from pygame.locals import *
```
This results in the same error seen with PyQt6: ImportError: DLL load failed
"""
# import sys
# print("\n".join(sys.path))
# import ipdb; ipdb.set_trace()

import pygame, sys
from pygame.locals import *

pygame.init()


DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
