def update_snake_array():
	
	snake_array.append([get_pos_x(),get_pos_y()])
	snake_set.add((get_pos_x(),get_pos_y()))
	
	if len(snake_array) > length+tail_buffer:
		snake_set.remove((snake_array[0][0],snake_array[0][1]))
		snake_array.pop(0)
		tail_index = snake_array[0]
		
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
snake_set = set()
hamltonian = {}
length = 1
tail_buffer = 3
end = False

To_Center = True

temp_x = 0
temp_y = 0

for i in range(world**2):
	
	hamltonian[i+1] = (temp_x,temp_y)
	hamltonian[(temp_x,temp_y)] = i+1
	
	even_col = temp_x % 2 == 0
	odd_col = temp_x % 2 == 1
	
	top_half = temp_y >= (world-1)//2+1
	bottom_half = temp_y <= (world-1)//2
	top_map = temp_y == world-1
	bottom_map = temp_y == 0
	top_partition = temp_y == (world-1)//2
	bottom_partition = temp_y == (world-1)//2+1
	
	if temp_x == 0 and temp_y != world-1:
		temp_y += 1
	elif temp_x == 0 and temp_y == world-1:
		temp_x += 1
	elif temp_x == world-1 and temp_y != 0:
		temp_y -= 1
	elif temp_x == world-1 and temp_y != 0:
		temp_x -= 1

	elif odd_col and bottom_map:
		temp_x -= 1
	elif even_col and top_partition:
		temp_x -= 1
	elif even_col and top_map:
		temp_x += 1	
	elif odd_col and bottom_partition:
		temp_x += 1
		
	elif odd_col:
		temp_y -= 1
	elif even_col:
		temp_y += 1
	
apple_index = hamltonian[(apple_x,apple_y)]
tail_index = 0

quick_print(hamltonian)
	

while 1:
	
	x = get_pos_x()
	y = get_pos_y()
	
	check_up = 0
	check_down = 0
	check_right = 0
	check_left = 0
	collition_up = True
	collition_down = True
	collition_right = True
	collition_left = True
	shortcut = False

	current_index = hamltonian[(x,y)]
	if current_index+1 < world**2:
		next_x, next_y = hamltonian[current_index+1]
	else: 
		next_x, next_y = hamltonian[1]
	
	direction_x = apple_x - x
	direction_y = apple_y - y
	
	if direction_x == 0 and direction_y == 0:
		apple_x, apple_y = measure()
		apple_index = hamltonian[(apple_x,apple_y)]
		length += 1
	

	if y != world-1:
		check_up = hamltonian[(x,y+1)]
		if hamltonian[check_up] in snake_set:
			collition_up = True
		else:
			collition_up = False
	if y != 0:
		check_down = hamltonian[(x,y-1)]
		if hamltonian[check_down] in snake_set:
			collition_down = True
		else:
			collition_down = False
	if x != world-1:
		check_right = hamltonian[(x+1,y)]
		if hamltonian[check_right] in snake_set:
			collition_right = True
		else:
			collition_right = False
	if x != 0:
		check_left = hamltonian[(x-1,y)]
		if hamltonian[check_left] in snake_set:
			collition_left = True
		else:
			collition_left = False

	short_apple_dist = {}
	short_apple_direction = {}
	if collition_up == False:
		if check_up < tail_index or check_up > current_index:
			shortcut = True
			short_apple_dist[1] = ((apple_x-hamltonian[check_up][0])**2+(apple_y-hamltonian[check_up][1])**2)
			short_apple_direction[((apple_x-hamltonian[check_up][0])**2+(apple_y-hamltonian[check_up][1])**2)] = North
	if collition_down == False:
		if check_down < tail_index or check_down > current_index:
			shortcut = True
			short_apple_dist[2] = ((apple_x-hamltonian[check_down][0])**2+(apple_y-hamltonian[check_down][1])**2)
			short_apple_direction[((apple_x-hamltonian[check_down][0])**2+(apple_y-hamltonian[check_down][1])**2)] = South
	if collition_right == False:
		if check_right < tail_index or check_right > current_index:
			shortcut = True
			short_apple_dist[3] = ((apple_x-hamltonian[check_right][0])**2+(apple_y-hamltonian[check_right][1])**2)
			short_apple_direction[((apple_x-hamltonian[check_right][0])**2+(apple_y-hamltonian[check_right][1])**2)] = East
	if collition_left == False:
		if check_left < tail_index or check_left > current_index:
			shortcut = True
			short_apple_dist[4] = ((apple_x-hamltonian[check_left][0])**2+(apple_y-hamltonian[check_left][1])**2)
			short_apple_direction[((apple_x-hamltonian[check_left][0])**2+(apple_y-hamltonian[check_left][1])**2)] = West


	if shortcut == True:
		shortcut_index = 987654321
		for i in short_apple_dist:
			if short_apple_dist[i] < shortcut_index:
				shortcut_index = short_apple_dist[i]
		if shortcut_index != 987654321:
			check_move(short_apple_direction[shortcut_index])
		else:
			shortcut = False
			
	if shortcut == False:
		if next_x-x == 1:
			check_move(East)
		elif next_x-x == -1:
			check_move(West)
		elif next_y-y == 1:
			check_move(North)
		elif next_y-y == -1:
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