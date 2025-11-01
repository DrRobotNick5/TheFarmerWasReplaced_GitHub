def plant_logic(num_row_plants, pumpkin_tally):
	x = get_pos_x()
	y = get_pos_y()
	size = get_world_size()

	if size/2 > 6:
		max_pumpkin = 6
	else:
		max_pumpkin = size/2


	if x<max_pumpkin and y<max_pumpkin:
		if get_entity_type() != Entities.Pumpkin:
			if can_harvest():
				harvest()
			pumpkin_tally = 0
		else:
			pumpkin_tally +=1
			
		if pumpkin_tally == 9:
			harvest()
			pumpkin_tally = 0

		if get_ground_type() == Grounds.Grassland:
			till()

		plant(Entities.Pumpkin)



	else:
		if can_harvest():
			harvest()
		
		if  (x+y) % num_row_plants == 0:
			if get_ground_type() == Grounds.Soil:
				till()
			plant(Entities.Grass)
		if (x+y) % num_row_plants == 1:
			if get_ground_type() == Grounds.Soil:
				till()
			plant(Entities.Tree)
		if (x+y) % num_row_plants == 2:
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)
	
	return pumpkin_tally