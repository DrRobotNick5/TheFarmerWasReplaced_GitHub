def update_snake_array():
	
	snake_array.append([get_pos_x(),get_pos_y()])
	snake_set.add((get_pos_x(),get_pos_y()))
	
	if len(snake_array) > length+tail_buffer:
		snake_set.remove((snake_array[0][0],snake_array[0][1]))
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

quick_print(hamltonian)
	

while 1:
	
	x = get_pos_x()
	y = get_pos_y()
	
	current_index = hamltonian[(x,y)]
	next_x, next_y = hamltonian[current_index]
	
	direction_x = apple_x - x
	direction_y = apple_y - y
	
	if direction_x == 0 and direction_y == 0:
		apple_x, apple_y = measure()
		apple_index = hamltonian[(apple_x,apple_y)]
		length += 1
	
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