weight=int(input("enter weight in kg"))

height=int(input("enter height in cm"))

age=int(input("enter age"))

gender=(input("enter gender")).lower()

print(weight,height,age,gender)

"""
the basal metabolic rate (BMR)=

10 * weight (kg) + 6.25 * height(cm) - 5 * age(y) + 5 for (male)

10 * weight (kg) + 6.25 * height(cm) - 5 * age(y) - 161 for (female)

"""

if gender == "male":

    BMR= 10*weight + 6.25*height - 5*age + 5


elif gender == "female":


    BMR= 10*weight + 6.25*height -5*age -161


else:

    print("please enter valid gender")

print(BMR)


activity_level=int(input("""
    select activity level
       press 1 for sedentary
       press 2 for lightly active
       press 3 for moderatly active
       press 4 for very active
       press 5 for extra active
            
        """ ))

if activity_level==1:

    colorie=BMR*1.2

elif activity_level==2:

    colorie=BMR*1.375

elif activity_level==3:

    colorie=BMR*1.55

elif activity_level==4:

    colorie=BMR*1.725

elif activity_level==5:

    colorie=BMR*1.9

else:
    print("select valid choice for activity level")

print(f"total number of colories you need in order to maintain your current weight={colorie}")   


target_weight=int(input("enter weight to reduce"))

durasion=int(input("enter durasion in weeks"))

# 1kg=>7700


colorie_deficit=target_weight*7700

days=durasion*7

daily_colorie_deficit=colorie_deficit/days

print("daily_colorie_deficit",daily_colorie_deficit)

