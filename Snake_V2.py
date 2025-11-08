def update_snake_array():
	
	snake_array.append([get_pos_x(),get_pos_y()])
	
	if len(snake_array) > length+tail_buffer:
		snake_array.pop(0)
		
def check_move(direction):
	if move(direction):
		update_snake_array()
	else:
		end = True

#######Start of code############
clear()

change_hat(Hats.Dinosaur_Hat)


world = get_world_size()

x = get_pos_x()
y = get_pos_y()
apple_x, apple_y = measure()
direction_x = apple_x - x
direction_y = apple_y - y

snake_array = []
length = 1
tail_buffer = 3
end = False

To_Center = True

while 1:
	
	x = get_pos_x()
	y = get_pos_y()
	
	if y < world/2:
		bottom_half_of_world = True
	else:
		bottom_half_of_world = False
	
	direction_x = apple_x - x
	direction_y = apple_y - y
	
	if direction_x == 0 and direction_y == 0:
		apple_x, apple_y = measure()
		length += 1
		To_Center = True
	
	if To_Center == True:
		if x % 2 == 0 and y < (world-1)//2:
			check_move(North)
		elif x % 2 == 1 and y < (world-1)//2:
			check_move(West)
		elif x % 2 == 1 and y > (world-1)//2+1:
			check_move(South)
		elif x % 2 == 0 and y > (world-1)//2+1:
			check_move(East)
		else:
			To_Center = False
	
	else:
		if length + tail_buffer < world*2:
			if x % 2 == 0 and direction_x <= 1 and direction_y > 0 and bottom_half_of_world == False :
				check_move(North)
			elif x % 2 == 0 and direction_y == 0 and bottom_half_of_world == False and:
				check_move(East)
			elif x == world-1 and bottom_half_of_world == False:
				check_move(South)
			elif bottom_half_of_world == False:
				check_move(East)
			
			if x % 2 == 1 and direction_x >= -1 and direction_y < 0 and bottom_half_of_world == True:
				check_move(South)
			elif x % 2 == 1 and direction_y == 0 and bottom_half_of_world == True :
				check_move(West)
			elif x == 0 and bottom_half_of_world == True:
				check_move(North)
			elif bottom_half_of_world == True:
				check_move(West)
		else:
			follow_x = snake_array[0][0] - x
			follow_y = snake_array[0][1] - y
			if direction_x > 0:
				check_move(East)
			elif direction_x < 0:
				check_move(West)
			if direction_y > 0:
				check_move(North)
			elif direction_y < 0:
				check_move(South)
	
	if end == True:
		#change_hat(Hats.Brown_Hat)
		#change_hat(Hats.Dinosaur_Hat)
		#apple_x, apple_y = measure()
		#snake_array = []
		#length = 1
		#end = False
		break
		

	# untill met tail, then lowest value to find apple