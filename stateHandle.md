# plan
we can separate this to multiple smaller bits to make the process easier.
the sections required to be handled are as followed
1. life system
    > really simple. all we need to do is to have a variable called something like
    `life_count` and `max_life_count` to keep track of the life system required
    for the other parts. basically, loose 3 lives, and reset.
2. score system
    > based on the number of OBs that disappeared, we will configure your score
3. reset system
    > loosing enough lives means restarting. to do so, we have to handle various different things
    - stopping time when you run out of lives and wait for the player to click on the screen and continue
    - reset all the OBs (wipe it all and then generate (8) new ones)
    - reset the player rotation and all
    - start back up the time