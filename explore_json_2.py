import json

infile = open('eq_data_30_day_m1.json','r')
outfile = open('readable_eq_data.json','w')


eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data['features']

print(len(list_of_eqs))

mags, lons, lats, hover_text = [],[],[],[]


for eq in list_of_eqs:
    mags.append(eq['properties']['mag'])
    lons.append(eq['geometry']['coordinates'][0])
    lats.append(eq['geometry']['coordinates'][1])
    hover_text.append(eq['properties']['title'])



print(mags[:10]) #printing out the first 10 in the list
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
        'size': [5*mag for mag in mags], #just spaces in between
        'color':mags,
        'colorscale': 'Viridis',
        'reversescale':True,
        'colorbar': {'title': 'Magnitude'}
    },
    }]

my_layout = Layout(title='Global Earthquakes')

fig = {'data':data,'layout':my_layout}

offline.plot(fig,filename='globalearthquakes.html')