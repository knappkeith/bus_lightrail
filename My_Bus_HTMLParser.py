from HTMLParser import HTMLParser
import urllib2

# create a subclass and override the handler methods
class Bus_HTMLParser(HTMLParser):
    def __init__(self, schedule_url):
        HTMLParser.__init__(self)
        response = urllib2.urlopen(schedule_url)
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
