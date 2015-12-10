all_hours=int(input('Enter hours:')) 
day=29700 #8 hours 15 minutes in seconds
all_hours=all_hours * 3600
days=all_hours // day
days_h = all_hours % day // 3600
days_m = all_hours % day % 3600 // 60
print ('days: ' + str(days) + ' hours: ' + str(days_h) + ' minutes: ' + str(days_m))