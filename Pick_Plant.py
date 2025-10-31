def plant_logic(num_row_plants):
	x = get_pos_x()
	y = get_pos_y()
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