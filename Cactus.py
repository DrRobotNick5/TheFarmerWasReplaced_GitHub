import Movement

clear()

dirValue = 0
run_once = 0
sorted_tally = 0
world = get_world_size()

while 1:
	x = get_pos_x()
	y = get_pos_y()

	if run_once == 0:
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Cactus)
		
	else:
		change_hat(Hats.Traffic_Cone)
		n = measure(North)
		e = measure(East)
		s = measure(South)
		w = measure(West)
		if y != world-1:
			if measure() > n:
				swap(North)
				sorted_tally = 0
		if x != 0: 
			if measure() < w:
				swap(West)
				sorted_tally = 0
		if y != 0:
			if measure() < s:
				swap(South)
				sorted_tally = 0
		if x != world-1:
			if measure() > e:
				swap(East)
				sorted_tally = 0
				
		m = measure()
		if (m <= n or y == world-1) and (m <= e or x == world-1) and (m >= w or x == 0) and (m >= s or y == 0):
			sorted_tally += 1
		
		if sorted_tally >= world*world:
			harvest()
			run_once = 0
		
		quick_print(sorted_tally, world*world)

	# if get_water() < .5:
	# 	use_item(Items.Water)
	# 	use_item(Items.Water)
	# elif get_water() < .75:
	# 	use_item(Items.Water)

	dirValue = Movement.Movement(dirValue)
	
	if measure()!=None:
		run_once = 1