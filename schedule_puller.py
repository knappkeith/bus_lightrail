from My_Bus_HTMLParser import Bus_HTMLParser

transit_options = {}
transit_options['HX'] = {}
transit_options['HX']['url'] = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=12&routeId=HX&serviceType=3'
transit_options['HX']['start'] = 1
transit_options['HX']['end'] = 5



b_url = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=0&routeId=B&serviceType=3'
hline_url = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeId=101&routeType=2&branch=F&lineName=SE&direction=S-Bound&serviceType=4'

# Get html
# response = urllib2.urlopen('http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=0&routeId=B&serviceType=3')
# html = response.read()
    
# instantiate the parser and fed it some HTML
parser = Bus_HTMLParser(transit_options['HX']['url'])
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

for i in parser.tables[0]:
    print str(len(i))
for i in parser.tables[0]:
    print i
for i in parser.tables[0]:
    print "%s    %s" % (i[transit_options['HX']['start']], i[transit_options['HX']['end']])

