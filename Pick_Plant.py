def plant_logic(num_row_plants, pumpkin_tally):
	x = get_pos_x()
	y = get_pos_y()
	size = get_world_size()

	if size/1.5 > 6:
		max_pumpkin = 6
	else:
		max_pumpkin = size/1.5


	if x<max_pumpkin and y<max_pumpkin:
		change_hat(Hats.Pumpkin_Hat)
		if get_entity_type() != Entities.Pumpkin:
			if can_harvest():
				harvest()
			pumpkin_tally = 0
		else:
			pumpkin_tally +=1
			
		if pumpkin_tally == max_pumpkin**2:
			harvest()
			pumpkin_tally = 0

		if get_ground_type() == Grounds.Grassland:
			till()

		plant(Entities.Pumpkin)



	else:
		if can_harvest():
			harvest()
		
		if  (x+y) % num_row_plants == 0:
			change_hat(Hats.Straw_Hat)
			if get_ground_type() == Grounds.Soil:
				till()
			plant(Entities.Grass)
		if (x+y) % num_row_plants == 1:
			change_hat(Hats.Tree_Hat)
			if get_ground_type() == Grounds.Soil:
				till()
			plant(Entities.Tree)
		if (x+y) % num_row_plants == 2:
			change_hat(Hats.Carrot_Hat)
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)
			
	
	return pumpkin_tally