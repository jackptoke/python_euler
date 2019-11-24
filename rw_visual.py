import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep making new walk
while True:

    #make a random walk 
    rw = RandomWalk()
    rw.fill_walk()

    #plot the point in the walkk
    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)

    plt.show()

    keep_running = input("Make another walk? (Y|n): ")

    if keep_running == "n":
        break