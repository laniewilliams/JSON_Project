
import json


infile = open('univ.json','r')
outfile = open('readable_univ_data.json','w')

#conf = open('ValueLabels.csv','r')
#conf_file = csv.reader(conf,delimiter=',')
#header_row = next(conf_file)


univ_data = json.load(infile)
json.dump(univ_data, outfile, indent=4)
list_of_univ = univ_data
list_of_sel_univ = [102,108,107,127,130]




enroll, lons, lats, hover_text = [],[],[],[]

type()

for record in list_of_univ:
    type(record['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'])
    '''
    if record['NCAA']['NAIA conference number football (IC2020)'] in list_of_sel_univ:
        if record["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
            enroll.append(record['Total  enrollment (DRVEF2020)'])
            lons.append(record['Longitude location of institution (HD2020)'])
            lats.append(record['Latitude location of institution (HD2020)'])
            hover_text.append([record['instnm'],str(record['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'])+'%'])


from plotly.graph_objs import Scattergeo, Layout #use the uppercase S even though it's not an option
from plotly import offline
#print(enroll[:10]) #printing out the first 10 in the list
#print(lons[:10])
#print(lats[:10]) 


data = [
    {'type':'scattergeo',
    'lon':lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [0.001*size for size in enroll], #just spaces in between
    
    },
    }]

my_layout = Layout(title='Universities with Total Price for In-state Students Living Off-Campus > $50,000')
fig3 = {'data':data,'layout':my_layout}
offline.plot(fig3,filename='Instate_offcampus_price.html')
'''