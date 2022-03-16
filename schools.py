"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.


Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000

"""
import json
import csv

infile = open('univ.json','r')
outfile = open('readable_univ_data.json','w')

#conf = open('ValueLabels.csv','r')
#conf_file = csv.reader(conf,delimiter=',')
#header_row = next(conf_file)


univ_data = json.load(infile)
json.dump(univ_data, outfile, indent=4)

#MAP 1 ---------------------------------------------------

list_of_univ = univ_data
list_of_sel_univ = [102,108,107,127,130]

print(len(list_of_univ))

size, lons, lats, hover_text = [],[],[],[]


for eq in list_of_univ:
    if eq['NCAA']['NAIA conference number football (IC2020)'] in list_of_sel_univ:
        if eq['Graduation rate  women (DRVGR2020)'] > 50:
            size.append(eq['Total  enrollment (DRVEF2020)'])
            lons.append(eq['Longitude location of institution (HD2020)'])
            lats.append(eq['Latitude location of institution (HD2020)'])
            hover_text.append([eq['instnm'],eq['Graduation rate  women (DRVGR2020)']])



print(size[:10]) #printing out the first 10 in the list
print(lons[:10])
print(lats[:10]) 


from plotly.graph_objs import Scattergeo, Layout #use the uppercase S even though it's not an option
from plotly import offline

data = [
    {'type':'scattergeo',
    'lon':lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [5*size for size in size], #just spaces in between
        #'color':mags,
        #'colorscale': 'Viridis',
        #'reversescale':True,
        #'colorbar': {'title': 'Magnitude'}
    },
    }]

my_layout = Layout(title='Global Earthquakes')

fig = {'data':data,'layout':my_layout}

offline.plot(fig,filename='globalearthquakes.html')
'''