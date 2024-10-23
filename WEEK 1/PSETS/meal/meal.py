def main():
    time = input("What time is it? ")
    meal_time = convert(time)
    # print(meal_time)

    if meal_time >= 7.0 and meal_time <= 8.0:
        print("breakfast time")
    elif meal_time >= 12.0 and meal_time <= 13.0:
        print("lunch time")  
    elif meal_time >= 18.0 and meal_time <= 19.0:
        print("dinner time")   


def convert(time):
    hours_mins = time.split(":")  
    hours = int(hours_mins[0])
    mins = int(hours_mins[1]) / 60
    return   hours + mins  


if __name__ == "__main__":
    main()
