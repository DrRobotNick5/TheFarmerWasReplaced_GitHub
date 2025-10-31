import Pick_Plant
import Movement

num_row_plants = 3
number_of_plants = 4

dirValue = 0

while 1:
	
	dirValue = Movement.Movement(dirValue)
	
	if can_harvest():
		harvest()
		Pick_Plant.plant_logic(num_row_plants)
	if get_entity_type() == None:
		Pick_Plant.plant_logic(num_row_plants)
		
			
	
	if get_water() < .75:
		use_item(Items.Water)
		