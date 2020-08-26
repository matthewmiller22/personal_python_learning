import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure() #create a figure window
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2)) #set up the axis in the figure
line, = ax.plot([], [], lw=2) #create line object which will be modified in the animation

#Let's visualize some grids:
grids = []
for i in range(20):
    new_grid = np.random.normal(loc=0.0, scale=1.0, size=(20,20))
    grids.append(new_grid)

#we are essentially making an empty line above, to which we will later
#add data.

##Below are the functions which make the animation happen
# initialization function: plot the background of each frame
#init() function below creates the *base frame* upon which the animation
#takes place. Here it's just us setting the line data to nothing. It is
#important to make this function return the line object, because
#this tells the animator which objects on the plot to update after each
#frame...

def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially.
#It takes the frame number, i, and draws a sine wave that depends
#on that frame number. Note that .set_data below is a method of the
#Line2D class. It adds a new (x,y) point to the line for each num
#argument, returning a tuple (line,). We end the below function
#by returning a tuple of the plot objects which have been modified.
#This thus tells the animation framework what parts of the plots
#are to be modified:

def animate(i):

    line.set_data(x, y) #a way of doing the 2 lines below in one line only

    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
#interva = ... means the ms delay between frames.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=10, blit=True)

plt.show()
#Finally, if you want to save, then you can run the line below:
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
