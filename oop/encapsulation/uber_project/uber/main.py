from driver import Driver

def main():
    driver1 = Driver(name="Rahul", rating=1.4)
    driver2 = Driver("Bob", 4.5, 29, True)
    driver3 = Driver(name="Rahul", rating=1.4)
    driver4 = Driver("Bob", 4.5, 29, True)

    print(Driver.total_drivers)
    print(Driver.manual())

if __name__ == "__main__":
    main()
