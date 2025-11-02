import Pick_Plant
import Movement

num_row_plants = 4
number_of_plants = num_row_plants + 1

dirValue = 0
pumpkin_tally = 0
sunflower_list = []
enable_sunflower = True

while 1:
	
	dirValue = Movement.Movement(dirValue)
	
	pumpkin_tally, sunflower_list, enable_sunflower = Pick_Plant.plant_logic(num_row_plants, pumpkin_tally, sunflower_list, enable_sunflower)
	
	if get_water() < .5:
		use_item(Items.Water)
		use_item(Items.Water)
	elif get_water() < .75:
		use_item(Items.Water)