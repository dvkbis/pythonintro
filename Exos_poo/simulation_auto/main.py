from model.car import Car
from model.racing import Racing

def main():
    car_a = Car("A", 50, 100)
    car_b = Car("B", 70, 80)
    car_c = Car("C", 10, 180)
    car_d = Car("D", 65, 65)
    car_e = Car("E", 40, 120)

    racing = Racing(4, 40)
    racing.add_car(car_a)
    racing.add_car(car_b)
    racing.add_car(car_c)
    racing.add_car(car_d)
    racing.add_car(car_e)

    while (not racing.is_finished()):
        racing.simulate_lap()
        racing.print_ranking()
        print("------------------")


    print("Best Time =", racing.find_best_time())

if __name__ == '__main__':
    main()