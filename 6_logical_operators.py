temp = 25 
is_sunny = False

# temp > 35 or temp < 0 or is_raining (at least one condition must be True)

if temp >= 28 and is_sunny:
    print("It is Hot outside")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold outside")
    print("It is Sunny")
elif 28 > temp > 0  and is_sunny:
    print("It is warm outside")
    print("It is Sunny")
elif temp >= 28 and  not is_sunny:
    print("It is Hot outside")
    print("It is cloudy")
elif temp <= 0 and  not is_sunny:
    print("It is Cold outside")
    print("It is cloudy")
elif 28 > temp > 0  and  not is_sunny:
    print("It is warm outside")
    print("It is cloudy")
    
 