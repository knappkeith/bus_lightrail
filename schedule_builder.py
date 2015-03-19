from datetime import time
from copy import deepcopy

class My_Schedule(object):
	def __init__(self, schedule_name, schedule_direction, days_valid):
		self.schedule = {}
		self.schedule_name = schedule_name
		self.direction = schedule_direction
		self.valid_days = days_valid
		self.via_str = 'ViaRoute'


	def add_schedule_by_array(self, schedule_array):
		if schedule_array[0][0] != self.via_str:
			schedule_array[0].insert(0,self.via_str)
		self.stops = list(schedule_array[0][1:])
		self.stops_w_via = list(schedule_array[0])
		self.routes = []
		for route in schedule_array[1:]:
			self.routes.append(self._get_route(route))


	def _get_route(self, route):
		rtn_route = {}
		for stop in range(0,len(self.stops_w_via)):
			rtn_route[self.stops_w_via[stop]] = self._convert_time(route[stop])
		if not rtn_route[self.via_str]:
			rtn_route[self.via_str] = self.schedule_name
		return rtn_route


	def _convert_time(self, time_to_convert):
		hour = 0
		minute = 0
		time_to_convert = time_to_convert.upper()
		is_pm = True
		if 'P' in time_to_convert:
			hour = 12
			time_to_convert = time_to_convert[0:time_to_convert.index('P')] 
		elif 'A' in time_to_convert:
			time_to_convert = time_to_convert[0:time_to_convert.index('A')]
			is_pm = True
		else:
			return time_to_convert
		if len(time_to_convert) == 4:
			hour += int(time_to_convert[0:2])
			minute = int(time_to_convert[2:])
		else:
			hour += int(time_to_convert[0:1])
			minute = int(time_to_convert[1:])
		if is_pm and hour > 23:
			hour = 12
		return time(hour, minute)


	def _set_filtered_routes(self):
		try:
			len(self.filtered_routes)
		except:
			self.filtered_routes = deepcopy(self.routes)


	def _check_stops(self, route, stops):
		for stop in stops:
			if not route[stop]:
				return False
			elif type(route[stop]) != time:
				return False
		return True


	def _filter_out_stations(self, good_stations):
		# Set the Filtered array
		self._set_filtered_routes()

		# Remove all routes without stations
		check_list = list(good_stations)
		check_list.remove(self.via_str)
		for route in list(self.filtered_routes):
			if not self._check_stops(route, check_list):
				self.filtered_routes.remove(route)

		# Remove all other stations
		for route_index in range(0,len(self.filtered_routes)):
			for stop in self.filtered_routes[route_index].keys():
				if not stop in good_stations:
					del self.filtered_routes[route_index][stop]


	def filter_by_station(self, start_station, end_station):
		self._filter_out_stations([start_station, end_station, self.via_str])


	def filter_by_station_index(self, start_index, end_index):
		self.filter_by_station(self.stops_w_via[start_index], self.stops_w_via[end_index])


	def _get_time(self, route, min_or_max):
		temp_time = []
		for stop in route:
			if type(route[stop]) is time:
				temp_time.append(route[stop])
		temp_time.sort()
		if min_or_max.upper() == 'MAX':
			temp_time = temp_time[::-1]
		return temp_time[0]


	def _filter_by_time_arrive(self, max_time):
		self._set_filtered_routes()
		for route in list(self.filtered_routes):
			if self._get_time(route, 'MAX') > max_time:
				self.filtered_routes.remove(route)


	def _filter_by_time_depart(self, min_time):
		self._set_filtered_routes()
		for route in list(self.filtered_routes):
			if self._get_time(route, 'MIN') < min_time:
				self.filtered_routes.remove(route)


	def _set_time(self, time_ck, default):
		if time_ck == None:
			time_ck = default
		if type(time_ck) is not time:
			time_ck = self._convert_time(time_ck)
		try:
			assert type(time_ck) is time
		except:
			print 'Not Valid time' + format(time_ck)
		return time_ck


	def filter_by_time_range(self, depart_time=None, arrive_time=None):
		depart_time = self._set_time(depart_time, time(0,0,0))
		arrive_time = self._set_time(arrive_time, time(23,59,59))
		self._filter_by_time_depart(depart_time)
		self._filter_by_time_arrive(arrive_time)

