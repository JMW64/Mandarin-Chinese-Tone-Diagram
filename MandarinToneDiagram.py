import matplotlib.pyplot as plt

ax = plt.subplot()
# ax.plot(x, y)

# The data
x = [1, 2, 3]
y = [5, 5, 5]
y1 = [3, 4, 5]
y2 = [2, 1, 4]
y3 = [5, 2.5, 0]

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

#choose linestyles and colors
plt.plot(x,y, label='Tone 1',color='r', linewidth=3)
plt.plot(x,y1,label='Tone 2',color='b', linewidth=3)
plt.plot(x,y2,label='Tone 3',color='g', linewidth=3)
plt.plot(x,y3,label='Tone 4',color='y', linewidth=3)

# label the axes
plt.xlabel('Time')
plt.ylabel('Pitch level')

# include a background grid
plt.grid(True)

# get rid of the ticks on the x-axis
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

# place the legend on the righthand side, outside the figure
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.6, chartBox.height])
ax.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8), shadow=True, ncol=1)

plt.show()
