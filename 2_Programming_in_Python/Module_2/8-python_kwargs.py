def sum_of(**kwargs):
    print ("kwargs: ", kwargs)
    sum = 0
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        sum += value
    return round(sum, 2)

print ("sum_of(1, 2, 3): ", sum_of(coffee=2.99, cake=4.55, juice=2.99))