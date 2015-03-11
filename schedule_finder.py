from HTMLParser import HTMLParser
import urllib2

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.print_it = False
        self.print_row = False
        self.tables = []
        self.table_count = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.print_it = True
            self.row_count = 0
            self.tables.append([])

        if self.print_it:
            if tag == 'tr':
                self.tables[self.table_count].append([])
                self.print_row = True                

    def handle_endtag(self, tag):
        if tag == 'table':
            self.print_it = False
            self.table_count += 1

        if self.print_it:
            if tag == 'tr':
                if len(self.tables[self.table_count][self.row_count]) == 0:
                    self.tables[self.table_count].pop(self.row_count)
                else:
                    self.row_count += 1
                self.print_row = False
                

    def handle_data(self, data):
        if self.print_it and self.print_row:
            # print "Encountered some data  :", data
            new_data = data.replace("\n",'')
            new_data = new_data.replace(" ",'')
            new_data = new_data.replace("\r",'')
            new_data = new_data.replace("\t",'')
            if not new_data == '':
                self.tables[self.table_count][self.row_count].append(new_data)

# Get html
response = urllib2.urlopen('http://www3.rtd-denver.com/schedules/getSchedule.action?runboardId=151&routeType=0&routeId=B&serviceType=3')
html = response.read()
    
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(html)
for i in parser.tables:
    for j in i:
        print_row = ""
        for k in j:
            print_val = " " + k
            while len(print_val)<8:
                print_val = " " + print_val

            print_row += print_val
        print print_row