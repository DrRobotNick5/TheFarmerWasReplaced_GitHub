def update_snake_array():
	
	snake_array.append([get_pos_x(),get_pos_y()])
	
	if len(snake_array) > length:
		snake_array.pop(0)

clear()

change_hat(Hats.Dinosaur_Hat)

apple_x, apple_y = measure()
snake_array = []
length = 1
end = False

# Generate hameltonian



move(East)

while 1:
	
	
	
	x = get_pos_x()
	y = get_pos_y()
	
	direction_x = apple_x - x
	direction_y = apple_y - y
	
	if direction_x > 0:
		if move(East):
			update_snake_array()
		else:
			end = True
	elif direction_x < 0:
		if move(West):
			update_snake_array()
		else:
			end = True
		
	if direction_y > 0:
		if move(North):
			update_snake_array()
		else:
			end = True
	elif direction_y < 0:
		if move(South):
			update_snake_array()
		else:
			end = True
		
	if direction_x == 0 and direction_y == 0:
		apple_x, apple_y = measure()
		length += 1
	
	#if end == True:
		#change_hat(Hats.Brown_Hat)
		#change_hat(Hats.Dinosaur_Hat)
		#apple_x, apple_y = measure()
		#snake_array = []
		#length = 1
		#end = False
		

	# untill met tail, then lowest value to find apple