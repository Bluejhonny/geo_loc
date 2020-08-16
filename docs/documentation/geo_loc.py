import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.path as mpltPath



def read_data(a,b):
	"""
	Read data of points and exclution zone.

	:param a: Point coordinates to locate inside area.
	:param b: Area boundaries coordinates. A polygon with X,Y coordinate of its vertices

	:return:

				1. area_coord : List. Area limits coordinates. An exclution zone.
				2. points: List. Point coordinates.
				3. points_coord: Dataframe. Point coordinates 

"""
	df=pd.read_csv(a)#Point coordinate
	df2=pd.read_csv(b)#Area limits coordinates. Exclution zone.
	#df2.drop('Unnamed: 2', axis=1, inplace=True)# to remove some column from data

	#Dataframe to list
	area_coord = [df2.columns.values.tolist()] + df2.values.tolist() #Exclution zone
	del area_coord[0] #delete name columns

	points_coord=df[['X', 'Y']] #point coordinates
	points = [points_coord.columns.values.tolist()] + points_coord.values.tolist()
	del points[0] #delete name columns

	return area_coord, points, points_coord

#........................................................................
def poly_creation(area_coord):
	"""
	Polygon creation.

	:param area_coord: List. Area limits coordinates. An exclution zone.

	:return: polygon boundaries (class 'matplotlib.collections.PatchCollection')
"""
	patches = []
	num_polygons = 1

	for i in range(num_polygons):
	    polygon = Polygon(area_coord, True)
	    patches.append(polygon)

	p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)

	return p

def find_points(area_coord, points):
	"""
	Find points inside the polygon or exclution zone.

	:param area_coord: List. Area limits coordinates. An exclution zone.
	:param points: List. Point coordinates.

	:return: position (class 'numpy.ndarray'). Position index on path.contains_points(points) wich value is "True".

"""
	path = mpltPath.Path(area_coord)
	inside = path.contains_points(points)

	#...........................................................................
	position=np.where(inside)[0] #find in list the points inside exclution zone.
								
	#............................................................................
	return position

def save_position(position, points_coord):
	"""
	Save in dataframe the point coordinates found inside area.

	:param position: Class 'numpy.ndarray'. Position index on path.contains_points(points) wich value is "True".
	:param points_coord: Dataframe. Point coordinates 

	:return: Dataframe with points coordinates inside area.
"""
	df = pd.DataFrame(columns=['X', 'Y'])

	for i in position: 
		df =df.append(points_coord.iloc[[i]], ignore_index=True)

	df['position']=position
	return df


