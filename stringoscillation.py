# cf https://www.geeksforgeeks.org/how-to-update-a-plot-in-matplotlib/

# the following line is only needed in jupyter and similar environments
# for getting animated plot in separate window in jupyter (not used in .exe)
# %matplotlib
import matplotlib.pyplot as plt
import numpy as np

def mode(sigma, phase, k=1):
    # k is related to the relative speed of both waves: for k=1, we get a standing wave on the circle.
    # For k != 1 the roots of the wave move along the circle.
    # Note: there are no longitudinal degrees of freedom for strings as the physical solutions of the string
    # are described by 2(D-2) solutions
    wave1 = np.cos(sigma + phase) + np.sin(sigma + phase) # left mover
    wave2 = np.cos(-sigma + phase*k) + np.sin(-sigma + phase*k) # right mover
    return np.array([wave1, wave2])

# set up three unit circles
sigma = np.linspace(0, 2*np.pi, 360) # circle coordinate
X1, Y1 = np.cos(sigma), np.sin(sigma)
X2, Y2 = np.cos(sigma), np.sin(sigma)
Xeff, Yeff = (X1+X2)/2, (Y1+Y2)/2

# set up plot
print('setting up!')
fig = plt.figure()
plt.ion() # interactive plotting -> animations
ax = fig.add_subplot()
ax.axis('equal')
circle1, = ax.plot(X1, Y1, linewidth=.5)
circle2, = ax.plot(X2, Y2, linewidth=.5)
circleeff, = ax.plot(Xeff, Yeff)


for phase in np.linspace(0, 6*np.pi, 6*180):
    for ind, s in enumerate(sigma):
        # draw a circle and shift every point radially by the mode function at that point
        x, y = np.cos(s), np.sin(s)
        shifts = mode(5*s, phase, 5)*0.25
        r = np.array([x, y]) # unit vector in radial direction
        X1[ind], Y1[ind] = x + r[0]*shifts[0], y + r[1]*shifts[0]
        X2[ind], Y2[ind] = x + r[0]*shifts[1], y + r[1]*shifts[1]
        Xeff, Yeff = (X1 + X2)/2, (Y1 + Y2)/2 # the string is the sum of both movers
        
    # update plots
    circle1.set_xdata(X1), circle1.set_ydata(Y1)
    circle2.set_xdata(X2), circle2.set_ydata(Y2)
    circleeff.set_xdata(Xeff), circleeff.set_ydata(Yeff)
    fig.canvas.draw()
    fig.canvas.flush_events()

print('Done!')
