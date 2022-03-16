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


infile = open('univ.json','r')
outfile = open('readable_univ_data.json','w')

#conf = open('ValueLabels.csv','r')
#conf_file = csv.reader(conf,delimiter=',')
#header_row = next(conf_file)


univ_data = json.load(infile)
json.dump(univ_data, outfile, indent=4)
list_of_univ = univ_data
list_of_sel_univ = [102,108,107,127,130]

#MAP 1 ---------------------------------------------------

#print(len(list_of_univ))

enroll, lons, lats, hover_text = [],[],[],[]


for record in list_of_univ:
    if record['NCAA']['NAIA conference number football (IC2020)'] in list_of_sel_univ:
        if record['Graduation rate  women (DRVGR2020)'] > 50:
            enroll.append(record['Total  enrollment (DRVEF2020)'])
            lons.append(record['Longitude location of institution (HD2020)'])
            lats.append(record['Latitude location of institution (HD2020)'])
            hover_text.append([record['instnm'],str(record['Graduation rate  women (DRVGR2020)'])+'%'])



#print(enroll[:10]) #printing out the first 10 in the list
#print(lons[:10])
#print(lats[:10]) 


from plotly.graph_objs import Scattergeo, Layout #use the uppercase S even though it's not an option
from plotly import offline



data = [
    {'type':'scattergeo',
    'lon':lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [0.001*size for size in enroll], #just spaces in between
    
    },
    }]

my_layout = Layout(title='Universities with Female Graduation Rate > 50%')
fig1 = {'data':data,'layout':my_layout}
offline.plot(fig1,filename='FemaleGradRate.html')

# MAP 2 ---------------------------------------------------------------------------

enroll, lons, lats, hover_text = [],[],[],[]


for record in list_of_univ:
    if record['NCAA']['NAIA conference number football (IC2020)'] in list_of_sel_univ:
        if record['Percent of total enrollment that are Black or African American (DRVEF2020)'] > 10:
            enroll.append(record['Total  enrollment (DRVEF2020)'])
            lons.append(record['Longitude location of institution (HD2020)'])
            lats.append(record['Latitude location of institution (HD2020)'])
            hover_text.append([record['instnm'],str(record['Percent of total enrollment that are Black or African American (DRVEF2020)'])+'%'])



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

my_layout = Layout(title='Universities with Black or African American Enrollment > 10%')
fig2 = {'data':data,'layout':my_layout}
offline.plot(fig2,filename='BorAA_Enrollment.html')

# MAP 3 -----------------------------------------------------------------------------------------------

enroll, lons, lats, hover_text = [],[],[],[]


for record in list_of_univ:
    if record['NCAA']['NAIA conference number football (IC2020)'] in list_of_sel_univ:
        if record["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] != None:
            if record["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
                enroll.append(record['Total  enrollment (DRVEF2020)'])
                lons.append(record['Longitude location of institution (HD2020)'])
                lats.append(record['Latitude location of institution (HD2020)'])
                hover_text.append([record['instnm'],'$'+str(record['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'])])



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