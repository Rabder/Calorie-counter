# Uses Miffllin St. Jeor equation to calculate caloric needs for the day
import csv

x = str(input("Sex: \n A) Man. \n B) Woman. :"))
w = float(input("Weight: \n"))
h = int(input("Height (cm): \n"))
a = int(input("Age: \n"))

# Miffllin St. Jeor equation
cal = (10*w)+(6.25*h)-(5*a)+5
if x == "B" or x == "b":
    cal -= 166

st1 = ["Sedentary (little to no exercise a day)", 1.2]
st2 = ["Slightly active (light exercise 1-3 days a week)", 1.375]
st3 = ["Moderately active (moderate exercise 3-5 days a week)", 1.55]
st4 = ["Very active (intense exercise 5-7 days a week)", 1.725]
st5 = ["Extra active (very intense exercise/physical job every day of the week)", 1.9]

actlevel = [st1, st2, st3, st4, st5]

act = int(input(f"How active are you?: \n 1) {st1[0]}. \n 2) {st2[0]}. \n 3) {st3[0]}. \n 4) {st4[0]}. \n 5) {st5[0]}."))

cal *= actlevel[act-1][1]

print(f"Your caloric needs are aproximately {cal}.")

save = str(input("Do you want to save your information as a profile? [Y/N]: \n"))



if save == "Y" or save == "y":
    if x == "A" or x == "a":
        gend = "Male"
    else:
        gend = "Female"
    savefile = open("calorie_profile.csv", "w")
    writer = csv.writer(savefile)
    writer.writerow(("Gender", "Weight (kg.)", "Height (cm)", "Age", "Calories (keep weight)", "Calories (lose weight)", "Calories (lose weight fast)"))
    writer.writerow((gend, w, h, a, cal, cal*0.9, cal*0.9*0.9))
    savefile.close()




