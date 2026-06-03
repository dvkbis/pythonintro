from model.car import Car
from tool.time_converter import TimeConverter

class Racing:
    def __init__(self, __nb_laps = 10, distance = 10):
        self.__cars = []
        self.__nb_laps = __nb_laps
        self.__distance = distance
        self.__current_laps = 0

    @property
    def current_laps(self):
        return self.__current_laps
    
    @property
    def nb_laps(self):
        return self.__nb_laps
    
    @property
    def distance(self):
        return self.__distance
    
    def add_car(self, car):
        self.__cars.append([car, 0])
    
    def simulate_lap(self):
        if self.__current_laps + 1 > self.nb_laps:
            raise 

        for car_time in self.__cars:
            car = car_time[0]
            time = self.distance / car.simulate_speed() * 3600
            car_time[1] = car_time[1] + time

        self.__cars.sort(key= lambda item: item[1])
        self.__current_laps += 1

    def find_best_time(self):
        if len(self.__cars) == 0:
            raise Exception
        
        best_car_time = self.__cars[0]
        for i in range(1, len(self.__cars)):
            if  self.__cars[i][1] < best_car_time[1]:
                best_car_time = self.__cars[i]
        
        return (best_car_time[0], TimeConverter.convert_to_day_hour_min_sec(best_car_time[1]))

    def print_ranking(self):
        for car_time in self.__cars:
            time = TimeConverter.convert_to_day_hour_min_sec(car_time[1])
            
            print(f"{car_time[0].name} -- {time[1]} hour(s),  {time[2]} min(s), {time[3]:.2f} sec(s)")

    def is_finished(self):
        return self.__current_laps >= self.__nb_laps