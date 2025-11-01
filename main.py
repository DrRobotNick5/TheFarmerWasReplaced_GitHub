import Pick_Plant
import Movement

num_row_plants = 3
number_of_plants = 4

dirValue = 0
pumpkin_tally = 0

while 1:
	
	dirValue = Movement.Movement(dirValue)
	
	pumpkin_tally = Pick_Plant.plant_logic(num_row_plants, pumpkin_tally)
	
	if get_water() < .75:
		use_item(Items.Water)
	elif get_water() < .5:
		use_item(Items.Water)
		use_item(Items.Water)