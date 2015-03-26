from My_Bus_HTMLParser import Bus_HTMLParser
from schedule_builder import My_Schedule
from datetime import time
import sys

transit_options = []


# Bus Lines
# H Route, from Target to 18th and California (F Line)
# East Bound
transit_options.append({})
transit_options[0]['url'] = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=12&routeId=HX&serviceType=3'
transit_options[0]['start'] = 1
transit_options[0]['end'] = 6
transit_options[0]['direction'] = 'east'
transit_options[0]['days_valid'] = ['M','T','W','Th','F']
transit_options[0]['type'] = 'bus'

# West Bound
transit_options.append({})
transit_options[1]['url'] = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeId=HX&routeType=12&direction=W-Bound&serviceType=3'
transit_options[1]['start'] = 2
transit_options[1]['end'] = 7
transit_options[1]['direction'] = 'west'
transit_options[1]['days_valid'] = ['M','T','W','Th','F']
transit_options[1]['type'] = 'bus'

# B Route, Boulder Transit Center to Union Station
# East Bound
transit_options.append({})
transit_options[2]['url'] = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeId=HX&routeType=12&direction=W-Bound&serviceType=3'
transit_options[2]['start'] = 2
transit_options[2]['end'] = 7
transit_options[2]['direction'] = 'west'
transit_options[2]['days_valid'] = ['M','T','W','Th','F']
transit_options[2]['type'] = 'bus'

for i in transit_options:
	for key in i:
		print key + " - " + str(i[key])
	print ''

sys.exit(0)


b_url = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=0&routeId=B&serviceType=3'
hline_url = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeId=101&routeType=2&branch=F&lineName=SE&direction=S-Bound&serviceType=4'
efhline_url = 'http://www3.rtd-denver.com/schedules/getSchedule.action?routeType=2&routeId=101&lineName=SE'
# Get html
# response = urllib2.urlopen('http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=0&routeId=B&serviceType=3')
# html = response.read()
    
# instantiate the parser and fed it some HTML
parser = Bus_HTMLParser(efhline_url)

my_schedule = My_Schedule('efh', 'north', ['M','T','W','Th','F'])

# print parser.tables[0]

my_schedule.add_schedule_by_array(parser.tables[0])
my_schedule.filter_by_station_index(6, 13)
my_schedule.filter_by_time_range('400P', '800P')

for route in my_schedule.filtered_routes:
	print '%s:  %s - %s' % (route['ViaRoute'], route['Arapahoe at Village Center Station (S Fiddlers Green Cir - Peakview Ave)'], route['Louisiana - Pearl Station (Louisiana Ave - Buchtel Blvd)'])
# parser.feed(html)
# for i in parser.tables:
#     for j in i:
#         print_row = ""
#         for k in j:
#             print_val = " " + k
#             while len(print_val)<8:
#                 print_val = " " + print_val

#             print_row += print_val
#         print print_row

# for i in parser.tables[0]:
#     print str(len(i))
# for i in parser.tables[0]:
#     print i
# for i in parser.tables[0]:
#     print "%s    %s" % (i[transit_options['HX']['start']], i[transit_options['HX']['end']])


