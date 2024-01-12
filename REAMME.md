# purpose

> nothing, just for fun, don't bother for now :)

# branch plans

- OBspawn:
    - spawning of obs
    > basically we will a layer value that shows the distance of each OB from the bottom of the screen. then we will have an offset value (just being the abs(animation value) to move only on positive postion). the display and the collision will update based on the offset and layer
    - moving obs based on the rotation speed
    - adding collision to the player
    - creating the mighty *infinite loop*

    if possible:
    - moving obs
    - color spill on the obs upon collision
    - saving ob pattern to return upon respawn (will be done on the game event branch)

- Events:
    - handing an start button
    - death state
    - keeping track of score

- Touches:
    - flashing background upon start and death
    - using the ob pattern to retain upon dieing 
    - saving the top score
- crazy touches:
    - saving top score on a server with their names 💾
    - adding online battles and races 🎮
    - a web version ? [maybe] 🕸