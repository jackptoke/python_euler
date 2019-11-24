import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [2*(x**2)+100 for x in x_values]

# plt.style.use('tableau-colorblind10')
plt.style.use('seaborn') 
# plt.style.use('fivethirtyeight') #fivethirtyeight
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='red', s=10)
# ax.scatter(x_values, y_values, c=(0, 0.65, 0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ax.plot(input_values, squares, linewidth=3)

#Set chart title and label axes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)
# ax.plot(squares)
ax.axis([0, 1100, 0, 1100000])

# plt.show()
plt.savefig("square_plot.png", bbox_inches="tight")
