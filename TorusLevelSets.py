import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.widgets import  Slider

nPlot=300
R, r = 2, 1

sliderMinMax = (-1,1)

t=0


def ScalarFunc(u,v):
    # Put f:torus -> \R here 
    return np.sin(2*np.pi*u)*(np.cos(8*np.pi*v**2) +np.sin(6*np.pi*v**2))*(1/2)


# Indicator function, returns 1 when f<t, and null otherwise
def ind(u,v,t):
    f=ScalarFunc(u,v)
    u=np.sqrt(t-f)
    return u/u
    # hacky - but works :)


# Plot view stuff
xLocPlot = np.linspace(0, 1, nPlot)
yLocPlot = np.linspace(0, 1, nPlot)
xLocPlot, yLocPlot = np.meshgrid(xLocPlot, yLocPlot)
xPlot = (R + r*np.cos(2*np.pi*xLocPlot)) * np.cos(2*np.pi*yLocPlot)
yPlot = (R + r*np.cos(2*np.pi*xLocPlot)) * np.sin(2*np.pi*yLocPlot)
zPlot = r * np.sin(2*np.pi*xLocPlot) * ind(xLocPlot,yLocPlot,t)


fig = plt.figure(figsize=(4, 4))
ax1 = plt.axes(projection='3d',computed_zorder=False)
f=2.1
ax1.set_xlim3d(-f,f)
ax1.set_ylim3d(-f,f)
ax1.set_zlim3d(-f,f)

ax1.view_init(36, 36)
sf = ax1.plot_surface(xPlot, yPlot, zPlot, rstride=15, cstride=15, cmap=cm.copper, edgecolors='w',alpha = 0.7)
ax1.set_axis_off()
axfreq = fig.add_axes([0.1, 0.1, 0.75, 0.03])
t_slider = Slider(
    ax=axfreq,
    label='t=',
    valmin=sliderMinMax[0]-0.01,
    valmax=sliderMinMax[1]+0.01,
    valinit=t,
)


def OnSliderUpdate(v):
    t=t_slider.val
    zPlot = r * np.sin(2*np.pi*xLocPlot) * ind(xLocPlot,yLocPlot,t)
    global sf
    sf.remove()
    sf=ax1.plot_surface(xPlot, yPlot, zPlot, rstride=15, cstride=15, cmap=cm.copper, edgecolors='w',alpha = 0.7)

t_slider.on_changed(OnSliderUpdate)

# plt.savefig(f'{NAME}.png',dpi=800)

plt.show()
