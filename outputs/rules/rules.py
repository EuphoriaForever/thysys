def findDecision(obj): #obj[0]: age, obj[1]: sex, obj[2]: pregnant, obj[3]: trimester, obj[4]: goitre, obj[5]: smoker, obj[6]: hairloss, obj[7]: constipation, obj[8]: diarrhoea, obj[9]: family-history, obj[10]: nervousness, obj[11]: skin, obj[12]: menstrual-bleeding, obj[13]: feeling-tired, obj[14]: sleepiness, obj[15]: weight, obj[16]: heart-rate, obj[17]: body-temperature
	# {"feature": "body-temperature", "instances": 774, "metric_value": 71.3457, "depth": 1}
	if obj[17] == 'NORMAL':
		# {"feature": "sleepiness", "instances": 422, "metric_value": 46.2057, "depth": 2}
		if obj[14] == 'NORMAL':
			# {"feature": "heart-rate", "instances": 257, "metric_value": 37.7374, "depth": 3}
			if obj[16] == 'NORMAL':
				# {"feature": "weight", "instances": 174, "metric_value": 33.9163, "depth": 4}
				if obj[15] == 'NORMAL':
					# {"feature": "nervousness", "instances": 134, "metric_value": 25.3662, "depth": 5}
					if obj[10] == 'NO':
						# {"feature": "diarrhoea", "instances": 108, "metric_value": 25.6863, "depth": 6}
						if obj[8] == 'NO':
							# {"feature": "age", "instances": 92, "metric_value": 29.6834, "depth": 7}
							if obj[0]<=36.380434782608695:
								# {"feature": "sex", "instances": 52, "metric_value": 13.6146, "depth": 8}
								if obj[1] == 'F':
									# {"feature": "trimester", "instances": 37, "metric_value": 12.3823, "depth": 9}
									if obj[3] == '2ND':
										return 'NORMAL'
									elif obj[3] == '1ST':
										return 'NORMAL'
									elif obj[3] == '3RD':
										return 'NORMAL'
									else: return 'NORMAL'
								elif obj[1] == 'M':
									return 'NORMAL'
								else: return 'NORMAL'
							elif obj[0]>36.380434782608695:
								# {"feature": "sex", "instances": 40, "metric_value": 18.904, "depth": 8}
								if obj[1] == 'F':
									# {"feature": "pregnant", "instances": 25, "metric_value": 8.6726, "depth": 9}
									if obj[2] == 'NO':
										return 'NORMAL'
									elif obj[2] == 'YES':
										# {"feature": "hairloss", "instances": 7, "metric_value": 4.8783, "depth": 10}
										if obj[6] == 'NO':
											return 'NORMAL'
										elif obj[6] == 'YES':
											return 'HYPER'
										else: return 'HYPER'
									else: return 'NORMAL'
								elif obj[1] == 'M':
									# {"feature": "goitre", "instances": 15, "metric_value": 6.7057, "depth": 9}
									if obj[4] == 'NO':
										return 'NORMAL'
									elif obj[4] == 'YES':
										return 'HYPO'
									else: return 'HYPO'
								else: return 'NORMAL'
							else: return 'NORMAL'
						elif obj[8] == 'YES':
							# {"feature": "menstrual-bleeding", "instances": 16, "metric_value": 5.2779, "depth": 7}
							if obj[12] == 'NORMAL':
								return 'HYPER'
							elif obj[12] == 'ABNORMAL':
								return 'HYPO'
							else: return 'HYPO'
						else: return 'HYPER'
					elif obj[10] == 'YES':
						# {"feature": "age", "instances": 26, "metric_value": 6.6188, "depth": 6}
						if obj[0]<=89:
							# {"feature": "constipation", "instances": 24, "metric_value": 6.5862, "depth": 7}
							if obj[7] == 'NO':
								# {"feature": "pregnant", "instances": 15, "metric_value": 5.2779, "depth": 8}
								if obj[2] == 'YES':
									return 'HYPER'
								elif obj[2] == 'NO':
									return 'HYPER'
								else: return 'HYPER'
							elif obj[7] == 'YES':
								# {"feature": "sex", "instances": 9, "metric_value": 4.7589, "depth": 8}
								if obj[1] == 'F':
									# {"feature": "menstrual-bleeding", "instances": 6, "metric_value": 4.2426, "depth": 9}
									if obj[12] == 'NORMAL':
										return 'HYPER'
									elif obj[12] == 'ABNORMAL':
										return 'HYPO'
									else: return 'HYPO'
								elif obj[1] == 'M':
									return 'HYPER'
								else: return 'HYPER'
							else: return 'HYPER'
						elif obj[0]>89:
							return 'HYPO'
						else: return 'HYPO'
					else: return 'HYPER'
				elif obj[15] == 'LOSS':
					return 'HYPER'
				elif obj[15] == 'GAIN':
					return 'HYPO'
				else: return 'HYPO'
			elif obj[16] == 'LOW':
				return 'HYPER'
			elif obj[16] == 'HIGH':
				return 'HYPO'
			else: return 'HYPO'
		elif obj[14] == 'LESS':
			return 'HYPER'
		elif obj[14] == 'MORE':
			return 'HYPO'
		else: return 'HYPO'
	elif obj[17] == 'HIGH':
		return 'HYPER'
	elif obj[17] == 'LOW':
		return 'HYPO'
	else: return 'HYPO'
