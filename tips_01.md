### 1.skeleton  
make window with black background.  
And frame rate = 20.  

```python
import pygame
from pygame.locals import *
import sys

wHeight = 480
wWidth = 640
wStrings = "Window Title."
wFPS = 20

# initialize
pygame.init()
screen = pygame.display.set_mode((wWidth, wHeight))
pygame.display.set_caption(wStrings)
FPSClock = pygame.time.Clock()

  def main():

    while True:
        screen.fill((0, 0, 0))
        pygame.display.update()
        
        # WindowClose
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
       FPSClock.tick(wFPS)

if __name__ == "__main__":
    main()
```
  
### 2.write words  
Draw text in the center of the window.  

```python
# after init ...

# drawWords
dStrings = "Hello PyGame."
font = pygame.font.SysFont(None, 60)
Word = font.render(dStrings, True, (0, 80, 150))
Word_rect = Word.get_rect()
Word_rect.center = (wWidth/2, wHeight/2)

# in main func
    while True:
        screen.fill((0, 0, 0))
        screen.blit(Word, Word_rect)
        pygame.display.update()
```

![2_done](https://user-images.githubusercontent.com/58809086/72351111-1097fa80-3723-11ea-9889-ab7b22684dff.png)


### 3.get key event
it's very simple key event.  
if press space key, the text move (0~10, 0~10)  

```python
# in loop(while True:) section
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    Word_rect.move_ip(10 * random(), 10 * random())
        pygame.display.update()
```