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
---
  
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

---

### 3.get key event
it's very simple key event.  
press space key, the text random move. (0~10, 0~10)  
press arrow keys, the text move 10 points in the direction of the arrow.  
"KEYDOWN" event only once execute.  
Keep pressing the key, not be executed continuously.　　

```python
# in loop(while True:) section
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    Word_rect.move_ip(10 * random(), 10 * random())
                elif event.key == K_LEFT:
                    Word_rect.move_ip(-10, 0)
                elif event.key == K_RIGHT:
                    Word_rect.move_ip(10, 0)
                elif event.key == K_UP:
                    Word_rect.move_ip(0, -10)
                elif event.key == K_DOWN:
                    Word_rect.move_ip(0, 10)
        pygame.display.update()
```
---


### 4.get pressed keys
Between pressing keys, execute key event continuously.  
Use get_pressed(). and adjust framerate.
(20 FPS is too fast to recognaze that the word moving.)  

```python
wFPS = 10
# in loop(while True:) section
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            Word_rect.move_ip(-1, 0)
        if pressed[K_RIGHT]:
            Word_rect.move_ip(1, 0)
        if pressed[K_UP]:
            Word_rect.move_ip(0, -1)
        if pressed[K_DOWN]:
            Word_rect.move_ip(0, 1)
```