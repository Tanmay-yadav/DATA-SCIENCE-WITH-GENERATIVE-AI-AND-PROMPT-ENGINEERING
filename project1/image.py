import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the image
image = imageio.imread(r'C:\Users\tanma\OneDrive\Pictures\IMG20221118173611.jpg')

# Create a figure and axes
fig, ax = plt.subplots()

# Create an empty image plot
im = ax.imshow(image)

# Define the animation function
def animate(i):
  # Shift the image horizontally
  shifted_image = np.roll(image, i, axis=1)
  # Update the image plot
  im.set_array(shifted_image)
  return im,

# Create the animation object
ani = animation.FuncAnimation(fig, animate, frames=image.shape[1], interval=50, blit=True)

# Show the animation
plt.show()
