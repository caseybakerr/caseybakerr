import matplotlib.pyplot as plt

from random_walk import Randomwalk

#Keep making new walks, as long as the program is active
while True:
    #Make a random walk and plot the points
    rw = Randomwalk(50000)
    rw.fill_walk()

    #Set size of the plotting window
    plt.figure(figsize=(10, 6))

    #Plot the points and show the plot
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    #Emphasize the first and last points
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    ax = plt.gca()

    #Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
