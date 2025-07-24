from geometry import find_number_of_unique_radii
import matplotlib.pyplot as plt


def plot_myCircles(current_circle,graph_bounds):
    unique_radii = find_number_of_unique_radii(current_circle)
    # cmap = plt.get_cmap('hsv')
    # cmap = plt.get_cmap('nipy_spectral')
    # colors = [cmap(i / len(unique_radii)) for i in range(len(unique_radii))]
    # need to implement for loop that iterates through self.current_circle, come back to this later
    # Figure Generation
    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    ax.cla() # clear things for fresh plot
    # change default range so that new circles will work
    ax.set_xlim((-1*graph_bounds, graph_bounds))
    ax.set_ylim((-1*graph_bounds,  graph_bounds))
    for i in range(0,len(current_circle)):
        # color = colors[int(np.where(unique_radii == current_circle[i][2])[0])]
        # circle = plt.Circle((current_circle[i][0], current_circle[i][1]), -1*current_circle[i][2], color=color,fill=False)
        circle = plt.Circle((current_circle[i][0], current_circle[i][1]), -1*current_circle[i][2],fill=False)
        ax.add_patch(circle)
    plt.show()