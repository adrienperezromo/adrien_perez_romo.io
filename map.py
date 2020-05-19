import folium
from csvreader import *


# map 
StartGPS=[48.8, 2.6972]
m= folium.Map(location=StartGPS ,
              zoom_start=2,
              titles='stamen Terrain')



importTable=importCSV("hotelstyle.csv",";")
covidH=importCSV("covidhosp.csv",";")
Longitude=filtrerColonne(importTable, ['LonDD'])
Latitude=filtrerColonne(importTable, ['LatDD'])
commune=filtrerColonne(importTable, ['Commune'])
dep=filtrerColonne(importTable, ["dep"])

dep2=filtrerColonne(covidH, ["dep"])
jour=filtrerColonne(covidH, ["jour"])
tri=triTable(dep2,["dep"] )


for j in range(len(tri)):
    huj=tri[j].get('dep')
    if huj == "01" :
        tri[j]=1
    elif huj == "02" :
        tri[j]=2
    elif huj == "03" :
        tri[j]=3    
    elif huj == "04" :
        tri[j]=4
    elif huj == "05" :
        tri[j]=5
    elif huj == "06" :
        tri[j]=6
    elif huj == "07" :
        tri[j]=7
    elif huj == "08" :
        tri[j]=8
    elif huj == "09" :
        tri[j]=9
    else:
        tri[j]=huj




v=[0,0]
for i in range(len(Longitude)):
    stock=0
    cas=0
    long=Longitude[i]
    lat=Latitude[i]
    com=commune[i] 
    pol=com.get('Commune')
    depa=dep[i]
    ghd=depa.get('dep')
    
     
    for cle in long.values():
        v[1]=cle
    for cle in lat.values():
        v[0]=cle
        
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        #j'essaye de faire fonction pour conter le nombre 
        # de fois qu'apparait chaque departement dans la liste tri . 
        # Pour l'isntant l'éxecution est beaucoup trop longue (plus de 5 min) 
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        
    # for k in range(len(tri)):
    #     if tri[k]==ghd :
    #         stock=stock+1
    #        # print(stock)
    #     print('2tri=',tri[k],'ghd=',ghd,'stock=',stock)
    #print(tri[k],"=",stock)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        
    
    folium.Marker(location=v, popup=pol,).add_to(m)

m.save("map.html") 

   
    
    
