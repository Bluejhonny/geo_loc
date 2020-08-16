from geo_loc.geo_loc import*

a='points.txt'
b='area.txt'

area_coord, points, points_coord=read_data(a,b)
p=poly_creation(area_coord)
position=find_points(area_coord, points)
df_points=save_position(position, points_coord)

#Visualization
fig, ax = plt.subplots()
ax.add_collection(p)
ax.scatter(points_coord['X'], points_coord['Y'], color='r')
ax.scatter(df_points['X'], df_points['Y'], color='g')
ax.set_title('Points inside Area')
ax.autoscale_view() 
plt.show()