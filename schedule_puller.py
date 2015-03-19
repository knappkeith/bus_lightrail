from My_Bus_HTMLParser import Bus_HTMLParser
from schedule_builder import My_Schedule
from datetime import time

transit_options = {}
transit_options['HX'] = {}
transit_options['HX']['url'] = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=12&routeId=HX&serviceType=3'
transit_options['HX']['start'] = 1
transit_options['HX']['end'] = 5



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
my_schedule.filter_by_time_range('1000A', '200P')

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


