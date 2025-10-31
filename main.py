import Pick_Plant

col = 6
row = 6
num_row_plants = 3
number_of_plants = 4

while 1:
	if can_harvest():
		harvest()
		Pick_Plant.plant_logic()
		move(North)
	if get_entity_type() == None:
		Pick_Plant.plant_logic()
		move(North)
		
			
	
	if get_water() < .75:
		use_item(Items.Water)
	
	if get_pos_y() == 0:
		move(East)
		