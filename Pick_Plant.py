def plant_logic(num_row_plants, pumpkin_tally, sunflower_list):
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
			
		if pumpkin_tally >= (max_pumpkin/1)**2:
			harvest()
			pumpkin_tally = 0

		if get_ground_type() == Grounds.Grassland:
			till()

		plant(Entities.Pumpkin)



	else:
		if  (x+y) % num_row_plants == 0:
			change_hat(Hats.Straw_Hat)
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Soil:
				till()
			plant(Entities.Grass)

		if (x+y) % num_row_plants == 1:
			change_hat(Hats.Tree_Hat)
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Soil:
				till()
			plant(Entities.Tree)

		if (x+y) % num_row_plants == 2:
			change_hat(Hats.Carrot_Hat)
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)

		if (x+y) % num_row_plants == 3:
			#change_hat(Hats.Sunflower_Hat)
			
			is_max = False
			count_array_compare = 0
			if len(sunflower_list) > 1:
				for i in range(len(sunflower_list)-1):
					if sunflower_list[i][0] == 15:
						if sunflower_list[i][1][0] == x and sunflower_list[i][1][1] == y:
							is_max = True
							sunflower_list.pop(i)
					else:			
						if sunflower_list[i][1][0] == x and sunflower_list[i][1][1] == y:			
							for j in range(len(sunflower_list)-1):
								if sunflower_list[j][0] <= sunflower_list[i][0]:
									count_array_compare += 1
							if count_array_compare == len(sunflower_list)-1:
								is_max = True
								sunflower_list.pop(i)
			if is_max == True:
				harvest()
				enable_plant = False
			
			if get_entity_type() != Entities.Sunflower:
				if can_harvest():
					harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			
			in_list = False
			if len(sunflower_list) > 1:
				for i in range(len(sunflower_list)-1):
					if sunflower_list[i][1][0] == x and sunflower_list[i][1][1] == y:
						in_list = True
			
			if len(sunflower_list) < 1:
				enable_plant = True
			if enable_plant == True:
				if in_list == False:	
					if get_entity_type() == None:
						plant(Entities.Sunflower)
					count = measure()
					sunflower_list.append([count, [x,y]])
					#print(sunflower_list)
			else:
				plant_logic(num_row_plants-1,pumpkin_tally,sunflower_list)

			
	
	return pumpkin_tally, sunflower_list