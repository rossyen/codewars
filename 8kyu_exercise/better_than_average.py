# better_than_average.py

class_point =[41, 75, 72, 56, 80, 82, 81, 33]
your_point = 50

def better_than_average(class_points, your_points):
    if len(class_points)/sum(class_points) < your_points:
        print('True')
        print(sum(class_point)/len(class_points))
    else:
        print('False')
    
better_than_average(class_point, your_point)
