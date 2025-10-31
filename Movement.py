def Movement(dirValue):
	x=get_pos_x()
	y=get_pos_y()

	if x==0 and y==0:
		move(North)
	elif x == y:
		if dirValue == 0:
			dirValue = 3
		elif dirValue == 1:
			dirValue = 2
	elif x == 0:
		if dirValue == 3:
			dirValue = 0
		elif dirValue == 0:
			dirValue = 1
	elif y == 0:
		if dirValue == 2:
			dirValue = 1
		elif dirValue == 1:
			dirValue = 0
		
	if x!=0 or y!=0:
		if dirValue == 0:
			move(North)
		elif dirValue == 1:
			move(East)
		elif dirValue == 2:
			move(South)
		elif dirValue == 3:
			move(West)
			
	return dirValue

	
