import csv 
from difflib import SequenceMatcher

#Food csv
# Row 1 = name
# Row 4 = kcal
# Row 5 = protein
# Row 6 = carbs
# Row 9 = total fats

#Calculates similarity ratio between two strings (0 to 1.0)
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def register(mealist):
    def foodin(foodnum, folist):
        if foodnum == -1:
            register()
        else:
            if (foodnum - 1) <= len(folist):
                return(foodnum)
            else:
                foodin(foodnum, folist)
    food_name = str(input("Name of the meal you ate: "))
    mealdict = {}
    with open("food.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        num = 0
        foodlist = []
        print("\n")
        print("I have found the following dishes: \n")
        for line in reader:
            if similar(food_name.lower(), line[1].lower()) > 0.7 or food_name.lower() in line[1].lower():
                num += 1
                mealdict["name"] = line[1]
                mealdict["kcal"] = round(float(line[4]), 2)
                mealdict["protein"] = round(float(line[5]), 2)
                mealdict["carbs"] = round(float(line[6]), 2)
                mealdict["fats"] = round(float(line[9]), 2)
                foodlist.append(mealdict)
                mealdict = {}
                print(f"{num}) {line[1]}")
    print("\n")
    foodnum = int(input('Input the number of the meal you ate. If you want to search again, type 0: '))
    if foodnum != 0:
        element = foodin(foodnum-1, foodlist)
        print(foodlist[element])

        print("\nRemember: " 
               "\n *55 grams is roughly the same size as an egg"
               "\n *A tennis ball is about 110 grams"
               "\n *A softball is around 220 grams"
               "\n *85 grams is around the same size as a deck of cards"
               "\n *29 grams of cheese is three dice"
               "\n *A baseball is around the same size as 110 grams of pasta or rice"
               "\n *Ping pong balls are about 2 tablespoons each")

        size = int(input("How much did you eat? (grams): "))
        foodlist[element]["kcal"] = round(foodlist[element]["kcal"] / (100/size), 2) 
        foodlist[element]["protein"] = round(foodlist[element]["protein"] / (100/size), 2) 
        foodlist[element]["carbs"] = round(foodlist[element]["carbs"] / (100/size), 2) 
        foodlist[element]["fats"] = round(foodlist[element]["fats"] / (100/size), 2)
        mealist.append(foodlist[element])
        print(foodlist[element])
        restart = str(input("Search again? (Y/N): "))
        if restart.lower() == "y":
            register(mealist)
        else:
            writecsv = str(input("Do you want to save your meals on your csv file? (Y/N): "))
            if writecsv.lower() == "y":
                savefile = open("foodcalendar.csv", "w")
                writer = csv.writer(savefile)
                writer.writerow(("name", "kcal", "protein", "carbs", "fats"))
                for item in mealist:
                    writer.writerow((item["name"], item["kcal"], item["protein"], item["carbs"], item["fats"]))
                savefile.close()
                return 0
    else:
        register(mealist)

mealist = []
register(mealist)