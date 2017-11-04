import datetime
import sys
import time

hoog_tarief = 0.2212 #0.2320
laag_tarief = 0.2019 #0.2100

totaal_hoog = 0.0
totaal_laag = 0.0


seconds_year = 24.0 * 3600.0 * 365.0
dtime_seconds = 60.0
watt_hour_factor = dtime_seconds/3600.0

first_timestamp = 9999999999
last_timestamp = 0000000000

#fd = open("watt.csv", 'r')
fd = sys.stdin

if len(sys.argv) < 4:
	print "Usage: " + sys.argv[0] + " begin_year begin_month begin_day"
	sys.exit(-1)

year = int(sys.argv[1])
month = int(sys.argv[2])
day = int(sys.argv[3])


begin_time = datetime.datetime(year, month, day)
begin_timestamp = time.mktime(begin_time.timetuple())

for line in fd.readlines():
	try:
		elements = line.split(",")
		time = int(elements[0])
		watts = float(elements[1])
		
		if watts > 5000.0 or time < begin_timestamp:
			continue

		#Real work
		first_timestamp = min(first_timestamp, time)
		last_timestamp = max(last_timestamp, time)

		date_time = datetime.datetime.fromtimestamp(time)		
		
		kilowatt_hour = (watts/1000.0) * watt_hour_factor
		if(	date_time.weekday() > 4 or 
			date_time.time().hour > 23 or 
			date_time.time().hour < 06): #Saturday or sunday
			totaal_laag += kilowatt_hour
#			print date_time.strftime("%A") + " " + str(date_time) + " laag: " + str(kilowatt_hour) + " " + str(watts)
		else:
			totaal_hoog += kilowatt_hour
	except:
		pass

kosten_hoog = (totaal_hoog) * hoog_tarief
kosten_laag = (totaal_laag) * laag_tarief

aandeel_hoog = (totaal_hoog/(totaal_hoog + totaal_laag))
aandeel_laag = (totaal_laag/(totaal_hoog + totaal_laag))

total_dtime_secs = last_timestamp - first_timestamp
total_dtime_years = total_dtime_secs / seconds_year

kwh_hoog_jaar = totaal_hoog / total_dtime_years
kwh_laag_jaar = totaal_laag / total_dtime_years
kwh_totaal_jaar = kwh_hoog_jaar + kwh_laag_jaar

print "Kosten hoog: " + str(kosten_hoog)
print "Kosten laag: " + str(kosten_laag)
print "Kosten variabel tarief: " + str(kosten_hoog + kosten_laag)

print "Aandeel hoog: " + str(aandeel_hoog)
print "Aandeel laag: " + str(aandeel_laag)

print "Jaren bekeken: " + str(total_dtime_years)
print "KWh hoog jaarlijks: " + str(kwh_hoog_jaar)
print "KWh laag jaarlijks: " + str(kwh_laag_jaar)
print "KWh totaal jaarlijks: " + str(kwh_totaal_jaar)
