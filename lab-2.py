def filter_numbers(ainymalylar, wek):
    return list(filter(lambda san: san > wek, ainymalylar))


bastapky_list = [1, 8, 2, 56, 100]
wek_mani = 5

filter_list = filter_numbers(bastapky_list, wek_mani)

print("Бастапқы тізім:", bastapky_list)
print("Сүзгіден өткен тізім({} - артық сандар): {}".format(wek_mani, filter_list))
