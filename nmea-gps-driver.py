#!/usr/bin/env python
import serial

verboseMode = True

if __name__ == "__main__":
	# Initialize GPS USB Port.
	GPSport = "/dev/ttyUSB0"
	GPSrate = 4800
	print("GPS driver initialized.")
	
	try:
		print("hello")

		GPS = serial.Serial(GPSport, baudrate=GPSrate, timeout=5)
		GPS.isOpen()
		
		# Main Loop.
		while 1:
			# Read in NMEA Data.
			data = GPS.readline().strip()
			fields = data.split(",")
			for i in fields:
				i = i.strip(",")
			try:
				# Parse NMEA sentence.
				if fields[0]=="$GPGGA":
					gps_time 	= int(fields[1])
					lat 		= fields[2]
					lat_dir 	= fields[3]
					lon 		= fields[4]
					lon_dir 	= fields[5]
					pos_fix_status 	= int(fields[6])
					num_satellites 	= int(fields[7])
					hdop 		= int(fields[8])
					altitude 	= int(fields[9])


					# Separate DD and mm.mmmm from DDmm.mmmm format.
					lat_deg = lat[:-7]
					lat_min = lat[-7:]
					lon_deg = lon[:-7]
					lon_min = lon[-7:]

					# Transform to Decimal Degrees format.
					lat_dec_deg = float(lat_deg) + (float(lat_min)/60.0)
					lon_dec_deg = float(lon_deg) + (float(lon_min)/60.0)

					# Flip sign if in Southern Hemisphere.
					if lat_dir == "N":
						north_south_indicator = True
					else:
						north_south_indicator = False
						lat_dec_deg = -lat_dec_deg

					# Flip sign if in Western Hemisphere.
					if lon_dir == "E":
						east_west_indicator = True
					else:
						east_west_indicator = False
						lon_dec_deg = -lon_dec_deg

					if verboseMode:
						print(fields)
						print("Position in Decimal Degrees: " + str(lat_dec_deg) + ", " + str(lon_dec_deg))

			#except ValueError as e:
			except ValueError:
				#print("Value Error: Likely due to missing fields in the NMEA messages. Error was :%s" % e)
				print("Value Error: ya dangus")
			# End of the loop.
			break
	except:
		print("Failure to connect to GPS USB device.")
print("GPS driver exited.")
# End of Code.