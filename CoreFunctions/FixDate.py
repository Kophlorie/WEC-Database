class FixDate:
	fdCount = 0	
	
	def __init__(self, year_month_day_hour_minute = "",country = ""):
		
		number = 0
		if "/" in year_month_day_hour_minute:
			temp = year_month_day_hour_minute.split("/")
		else:
			if "\\" in year_month_day_hour_minute:
				temp = year_month_day_hour_minute.split("\\")
			else:
				if "." in year_month_day_hour_minute:
					temp = year_month_day_hour_minute.split(".")			
				else:
					if "_" in year_month_day_hour_minute:
						temp = year_month_day_hour_minute.split("_")
					else:
						number = 1
		if number == 0:
			if len(temp) == 1:
				self.year = temp[0]
			if len(temp) > 1:
				self.month = temp[1]
			if len(temp) > 2:
				self.day = temp[2]
			if lent(temp) > 3 :
				self.hour = temp[3]
			if len(temp) > 4:
				self.minute = temp[4]
		else:
			self.year = year_month_day_hour_minute[0:4]
			self.month = year_month_day_hour_minute[4:6]
			self.day = year_month_day_hour_minute[6:8]
			self.hour = year_month_day_hour_minute[8:10]
			self.minute = year_month_day_hour_minute[10:]
			
		self.country = country

		FixDate.fdCount += 1
		
	def __str__(self):
		print("year = "+str(self.year))
		print("month = "+str(self.month))
		print("day = "+str(self.day))
		print("hour = "+str(self.hour))
		print("minute = "+str(self.minute))
		return "Country_time = {0}".format(self.country)
		
