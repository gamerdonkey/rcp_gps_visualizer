import csv
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

logfile = open(r'RC_54.LOG', 'r')

logreader = csv.reader(logfile, delimiter=',', quoting=csv.QUOTE_NONE)

lat = []
lon = []
speed = []

rownum = 0
for row in logreader:
        if rownum > 0:
                if row[5] and row[6] and row[7]:
                        lat.append(float(row[5]))
                        lon.append(float(row[6]))
                        speed.append(float(row[7]))
        rownum += 1
logfile.close()

m = Basemap(llcrnrlat=38.647,llcrnrlon=-90.139,urcrnrlat=38.6554,urcrnrlon=-90.1329, resolution='h',projection='merc')
fig = plt.figure(figsize=(30, 10))

x,y = m(lon,lat)
m.drawmapboundary(fill_color='black') # fill to edge
m.scatter(x,y,s=20,c=speed,marker="o",cmap=cm.spectral,alpha=0.1,edgecolors='none')

# The colorbar renders funny with alpha <1. Had to manually crop it in to get the look I wanted.
colorbar = m.colorbar(cmap=cm.spectral)
colorbar.set_label('Speed (MPH)')

#plt.savefig('gmp.png', bbox_inches='tight')
plt.show()
