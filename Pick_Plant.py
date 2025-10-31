from main import num_row_plants

def plant_logic():
	if get_pos_x() % num_row_plants == 0:
		if get_ground_type() == Grounds.Soil:
			till()
		plant(Entities.Grass)
	if get_pos_x() % num_row_plants == 1:
		if get_ground_type() == Grounds.Soil:
			till()
		plant(Entities.Bush)
	if get_pos_x() % num_row_plants == 2:
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Carrot)