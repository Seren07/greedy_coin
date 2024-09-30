def check(amount):
    coin_list = [10,5,2,1]
    coin_names = ["coin 10", "coin 5", "coin 2", "coin 1"]
    count = {
        "coin 10":0,
        "coin 5":0,
        "coin 2":0,
        "coin 1":0
        }

    for i in range(len(coin_list)):
        while amount >= coin_list[i]:
            amount -= coin_list[i]
            count[coin_names[i]] += 1
    if amount == 0:
        print("The amount of coin change :")
        for category in count:
            print(f"{category} = {count[category]}")
    else:
        print("Ini gabisa")    
    
total_money = float(input("Please insert the money : "))
check(total_money)