Pygame can display graphics in 2 ways:
Show an image or text via a surface & draw pixels

Show an image/text ( surface )
A "surface" in Pygame is usually an image (png,jpg)
a plain area or rendered text

# How to create?

plain surface: pygame.Surface((w,h))
imported surface: pygame.image.load(path)
text surface:font.render(text, AntiAlias, Color)

# Display surface vs surface?

- The display surface is the main surface that we draw on and there can only be
  one, and it is always visible.

- A regular surface is an image of some kind, you can have any number, but
  they are only visible when attached to the display surface!

  -------------------------------------------------------------------------------

- display blit : Block image transfer


                 Width
-------------------------------------------
| * (0, 0)                                |
|  Increasing x moves right               |
|  Increasing y moves down                |
|                                         |
|                                         |
|                                         | Height
|                                         |
|                                         |
|                                         |
|                                         |
|                                         |
|                                         |
|                                         |
-------------------------------------------
            Display Surface

-----------------------------------------------------------------------------------

# Rects

- Places surfaces more elegantly
- Detect collisions
- Can be drawn

- Rects are just rectangles with a size and position

They also have lots of points:
- Tuples with an x and y position
- X or y positions
- There is also width, height and size
- Each point can be measured and changed
- The points stay relative to each other! Moving one means you move all


                    Top-left             Mid-top               Top-right
                        *-------------------*---------------------*
                        |      -Top                               |
                        |                                         |
                - Left  |                                         | - Right
                        |                                         |
                        |                                         |
                        |                                         | 
               Mid-left *                   *                     * Mid-right
                        |                center                   |
                        |         - center x, -center y           |
                        |                                         |
                        |                                         |
                        |                                         |
                        |                                         |
                        |    - Bottom                             |
                        *-------------------*---------------------*
                  Bottom-left           Mid-bottom            Bottom-right






----------------------------------------------------------------------------------

# There are 2 kinds of rects

Rects and FRects

- They are nearly identical, the only difference is that FRects store data as 
  floating point values while Rects use integers

- FRects are usually better since they are more precise

-----------------------------------------------------------------------------------

# Creating rects

- You can create a rect from scratch : 

pygame.Rect(pos, size)
pygame.FRect(pos, size)

Or you can create it from a surface (rect will have same size as surface)

surface.get_rect(point = pos)
surface.get_fRect(point = pos)

----------------------------------------------------------------------------------

# Vectors

- Basically a list with 2 values : x and y
- You can read/change the values

vector(x = 1, y = 5)
vector.x = 10

# Vector math
vector(4,2) * 2 = vector(8,4)
vector(4,2) + vector(1,5)
rect.center + vector(1,5)

---------------------------------------------------------------------------------

# Sprites

- Best way to use classes in pygame
- It's an inbuilt pygame class that always contains a surface and a rect

pygame class pygame.sprite.Sprite

We create a custom class that inherits from it

For this class we need to set
- self.image = surface
- self.rect = rect

# Displaying a sprite

- Bad ( but possible ) approach: surface.blit(sprite.image, sprite.Rect)
- Good approach: Use a pygame group

# Sprite groups

- Most games have dozens, if not hundreds, of sprites
- Pygame is expecting that and sprite groups are designed around that


Groups draw, update and organize sprites

- group.draw(surface) -> draws all sprites on surface
- group.update(args) -> calls update with arg on every sprite
- You can loop over sprites and use them in other methods as well, making it easy to sort
  them into logical groups

------------------------------------------------------------------------------------------

Interval Timer

- A timer that triggers every x seconds
- You first need to create an event and then set a timer with that event
- You can then capture the event in the event loop

Custom Timer

- Pygame lets you capture the time since that start of the game
- You can use that to create a custom timer
- Get a starting point and then measure the time passed since that point

------------------------------------------------------------------------------------------