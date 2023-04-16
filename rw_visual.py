import matplotlib.pyplot as plt

from random_walk import RandomWalk
# Keep making new walks, as long as the porgram is active.
while True:
  # Make a random walk.
  rw = RandomWalk()
  rw.fill_walk()

  # Plot the points in the walk.
  plt.style.use("classic")
  fig, ax = plt.subplots()
  ax.scatter(rw.x_values, rw.y_values, s=15)
  plt.show()

  keep_running = input("Make another walk? (y/n): ")
  keep_running = keep_running.lower()
  if keep_running == 'n':
    break