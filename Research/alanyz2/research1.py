class Person:

    # java variable types just for reference:
    #
    # String name
    #
    # int age
    #
    # Map<String, Integer> nutrition
    # (keys: nutrition categories like Calories, Carbohydrates. values: numerical values of each category)
    #
    # int exercise (hours of exercise? could also use another data structure for more info)
    #
    # int sleep (hours of sleep)

    def __init__(self, name, age, nutrition, exercise, sleep):
        self.name = name
        self.age = age
        self.nutrition = nutrition
        self.exercise = exercise
        self.sleep = sleep


dailyNutrition = {
    "Calories": 2156,
    "Total fat (g)": 21,
    "Cholesterol (mg)": 0,
    "Sodium (mg)": 35,
    "Total carbohydrates (g)": 37,
    "Protein (g)": 3
}

Alan = Person("Alan Zhang", 18, dailyNutrition, 2, 7)
print(Alan.nutrition)
