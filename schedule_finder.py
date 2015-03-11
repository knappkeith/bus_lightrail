from HTMLParser import HTMLParser
import urllib2

# create a subclass and override the handler methods
class Bus_HTMLParser(HTMLParser):
    def __init__(self, schedule_url):
        HTMLParser.__init__(self)
        response = urllib2.urlopen('http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=0&routeId=B&serviceType=3')
        html = response.read()

        # add a check for bad url/error codes

        self.print_it = False
        self.print_row = False
        self.print_cell = False
        self.row_text = ""
        self.tables = []
        self.table_count = 0
        self.cur_head = False




        self.feed(html)

        

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.print_it = True
            self.row_count = 0
            self.tables.append([])

        if self.print_it:
            if tag == 'tr':
                self.tables[self.table_count].append([])
                self.print_row = True

            if self.print_row:
                if tag == 'td' or tag == 'th':
                    self.print_cell = True
                    self.row_text = ""


    def handle_endtag(self, tag):
        if tag == 'table':
            self.print_it = False
            if len(self.tables[self.table_count]) == 0:
                self.tables.pop(self.table_count)
            else:
                self.table_count += 1

        if self.print_it:
            if tag == 'tr':
                if len(self.tables[self.table_count][self.row_count]) == 0:
                    self.tables[self.table_count].pop(self.row_count)
                else:
                    self.row_count += 1
                self.print_row = False

            if self.print_row:
                if tag == 'td' or tag == 'th':
                    if tag == 'th':
                        self.cur_head = True
                    else:
                        self.cur_head = False
                    if not self.row_text == '':
                        self.tables[self.table_count][self.row_count].append(self.row_text)
                    self.print_cell = False

                

    def handle_data(self, data):
        if self.print_it and self.print_row:
            # print "Encountered some data  :", data
            new_data = data.replace("\n",'')
            new_data = new_data.replace("\r",'')
            new_data = new_data.replace("\t",'')
            if not self.cur_head:
                new_data = new_data.replace(" ",'')
            else:
                new_data = self.remove_first_blanks(new_data)
            if not new_data == '':
                self.row_text += new_data

    def remove_first_blanks(self, string):
        ret_str = ""
        remove_letter = True
        for letter in string:
            if remove_letter:
                if not letter == " ":
                    remove_letter = False
                    ret_str += letter
            else:
                ret_str += letter
        return ret_str
                

transit_options = {}
transit_options['HX'] = {}
transit_options['HX']['url']
transit_options['HX']['start']
transit_options['HX']['end']
transit_options['BV/BF/BX/BMX'] = {}


b_url = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=0&routeId=B&serviceType=3'
hline_url = 'http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeId=101&routeType=2&branch=F&lineName=SE&direction=S-Bound&serviceType=4'

# Get html
# response = urllib2.urlopen('http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=0&routeId=B&serviceType=3')
# html = response.read()
    
# instantiate the parser and fed it some HTML
parser = Bus_HTMLParser(b_url)
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
    # print str(len(i))
    # print i
    print "%s    %s" % (i[1], i[10 ])