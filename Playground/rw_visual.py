import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep making new walk
while True:

    #make a random walk 
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #plot the point in the walkk
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=1)
    plt.plot(rw.x_values, rw.y_values, linewidth=0.5)
    # ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    #remove the axes
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (Y|n): ")

    if keep_running == "n":
        break