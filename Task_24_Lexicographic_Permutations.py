
def lexicographic_Permutations(limit):
	count = 0
	for n_0 in range(limit):
		for n_1 in range(limit):
			for n_2 in range(limit):
				for n_3 in range(limit):
					for n_4 in range(limit):
						for n_5 in range(limit):
							for n_6 in range(limit):
								for n_7 in range(limit):
									for n_8 in range(limit):
										for n_9 in range(limit):
											if n_0 != n_1:
												if n_0 != n_2:
													if n_0 != n_3:
														if n_0 != n_4:
															if n_0 != n_5:
																if n_0 != n_6:
																	if n_0 != n_7:
																		if n_0 != n_8:
																			if n_0 != n_9:
																				if n_1 != n_2:
																					if n_1 != n_3:
																						if n_1 != n_4:
																							if n_1 != n_5:
																								if n_1 != n_6:
																									if n_1 != n_7:
																										if n_1 != n_8:
																											if n_1 != n_9:
																												if n_2 != n_3:
																													if n_2 != n_4:
																														if n_2 != n_5:
																															if n_2 != n_6:
																																if n_2 != n_7:
																																	if n_2 != n_8:
																																		if n_2 != n_9:
																																			if n_3 != n_4:
																																				if n_3 != n_5:
																																					if n_3 != n_6:
																																						if n_3 != n_7:
																																							if n_3 != n_8:
																																								if n_3 != n_9:																																					
																																									if n_4 != n_5:
																																										if n_4 != n_6:
																																											if n_4 != n_7:
																																												if n_4 != n_8:
																																													if n_4 != n_9:
																																														if n_5 != n_6:
																																															if n_5 != n_7:
																																																if n_5 != n_8:
																																																	if n_5 != n_9:																																																	
																																																		if n_6 != n_7:
																																																			if n_6 != n_8:
																																																				if n_6 != n_9:
																																																					if n_7 != n_8:
																																																						if n_7 != n_9:
																																																							if n_8 != n_9:
																																																								count += 1	
																																																								if count == 1000000:
																																																									file = open('result.txt', 'w')
																																																									result = str(n_0) + str(n_1) + str(n_2) + str(n_3) + str(n_4) + str(n_5) + str(n_6) + str(n_7) + str(n_8) + str(n_9)
																																																									file.write(result)
																																																									file.close()	
																																																									return		
																																																								
lexicographic_Permutations(10)