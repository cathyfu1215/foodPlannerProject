'''
NEU, 2024 Summer , CS5800
Cong(Cathy) Fu
Final Project - an application of simplex method in diet optimization
Inspired by The Stigler diet problem.
'''

from ortools.linear_solver import pywraplp


def main():

    """Entry point of the program."""
    # Instantiate the data problem.

    # Nutrient minimums.
    # The values are based on the Daily Values for nutrients from:
    # https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/dietary-reference-intakes/tables/reference-values-macronutrients.html
    # https://www.canada.ca/en/health-canada/services/technical-documents-labelling-requirements/table-daily-values/nutrition-labelling.html

    # Note: I am assuming 2000 calories per day,
    # but the actual values are based on gender, age, height, weight,
    # and physical activity level.
    nutrients = [
        ["Calories (cal)", 2000],
        ["Protein (g)", 46],
        # a male needs 56g of protein per day, while a female needs 46g
        ["Calcium (g)", 1.3],
        ["Iron (mg)", 18],
        ["Vitamin B6 (mg)", 1.7],
        ["Vitamin B12 (ug)", 2.4],
        ["Niacin (mg)", 16],
        ["Vitamin C (mg)", 90],
        ["Fibre (g)", 28],
        ["Sodium (mg)", 2300],
        ["Potassium (mg)", 3400],
        ["Vitamin D (ug)", 20],
    ]

    # Food data.

    # The nutrient data is based on 100g of each food.
    # Source of nutrient data: https://food-nutrition.canada.ca/api/canadian-nutrient-file
    # And Google search for some of the nutirents that are not available in the above source.

    # Prices data are from https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810024501

    # The foods_data is in the following format:
    # Commodity, Unit, May 2024 price (Canadian Cents)/unit, Calories (cal),
    # Protein (g),Calcium (g), Iron (mg),  Vitamin B6 (mg),
    # Vitamin B12 (ug), Niacin (mg), Vitamin C (mg), Fibre (g)
    # Sodium (mg),Potassium (mg), Vitamin D (ug)
    
    foods_data = [
        ["Wheat Flour", "100g", 20.88, 369, 14.639, 26.441, 3.396, 0.213, 0, 4.93, 0, 2.7, 2, 107, 0],
        ["White Rice", "100g", 64.66, 357, 14.73, 21, 1.96, 0.391, 0, 6.733, 0, 0.4, 1, 35, 0],
        ["Milk", "100g", 30.10, 61, 3.15, 113, 0.03, 0.036, 0.45, 0.089, 0, 0, 44, 150, 0.025],
        ["Butter", "100g", 127.75, 717, 0.85, 24, 0.16, 0.003, 0.13, 0.042, 0, 0, 11, 24, 1.5],
        ["Bacon", "100g", 126.8, 417, 12.62, 5, 0.41, 0.266, 0.5, 4.022, 0, 0, 1717, 565, 1.05],
        ["Apple", "100g", 54.7, 52, 0.26, 6, 0.12, 0.041, 0, 0.091, 4.6, 2.4, 1, 107, 0],
        ["Carrots", "100g", 30.96, 41, 0.93, 33, 0.3, 0.138, 0, 0.983, 5.9, 2.8, 69, 320, 0],
        ["Ground Beef", "100g", 125.5, 207, 19.575, 10.2, 1.8, 0.2375, 2.35, 5.375, 0, 0, 67, 218, 0.125],
        ["Salmon", "100g", 265.2, 142, 19.84, 12, 0.8, 0.818, 3.18, 7.86, 0, 0, 59, 363, 13.15],
        ["Pork", "100g", 88.4, 255, 26.29, 5, 0.92, 0.31, 0.44, 4.311, 0.3, 0, 62, 423, 1.325],
        ["Orange", "100g", 40.8, 49, 1.04, 40, 0.09, 0.063, 0, 0.274, 48.5, 2.4, 0, 181, 0],
        ["Potato", "100g", 49.8, 78, 2.38, 8, 1.01, 0.256, 0, 1.68, 14.2, 1.7, 3, 484, 0],
        ["Cabbage", "100g", 28.4, 16, 1.2, 77, 0.31, 0.232, 0, 0.4, 27, 1.2, 18, 170, 0],
        ["tomato", "100g", 43, 16, 1.16, 5, 0.47, 0.06, 0, 0.593, 16, 0.9, 42, 212, 0],
        ["Banana", "100g", 16.5, 89, 1.09, 5, 0.26, 0.367, 0, 0.665, 8.7, 1.74, 1, 358, 0],
        ["Green beans", "100g", 56.13, 39, 1.977, 31.117, 0.738, 0.115, 0, 0.558, 29.321, 2.376, 20.133, 171.592, 0],
        ["Chicken", "100g", 60.1, 124, 17.88, 10, 5.86, 0.42, 11.41, 6.662, 16.2, 0, 77, 228, 0.05],
        ["Cheese", "100g", 135.8, 371, 23.24, 674, 0.43, 0.065, 1.26, 0.118, 0, 0, 560, 136, 0.5],
        ["grapes", "100g", 92.3, 67, 0.063, 14, 0.29, 0.11, 0, 0.3, 4, 0.9, 2, 191, 0],
        ["Yogurt", "100g", 69, 50, 4.6, 147, 0.12, 0.032, 0.24, 0.075, 0.5, 0, 40, 174, 0],
    ]

    # Instantiate a Glop solver and naming it.
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return

    # Declare an array to hold our solutions.
    # The method NumVar creates one variable, food_amounts[i], for each row of the foods_data table.
    # The value of food_amounts[i] is greater than 0.0, and there is no upper bound.
    # food_amounts[i] is the amount of servings(100g) of food in the ith row to purchase.
    food_amounts = [solver.NumVar(0.0, solver.infinity(), item[0]) for item in foods_data]

    
    # This is how many food items we have.
    print("Number of variables(food items) =", solver.NumVariables())

    # Create the constraints, one per nutrient.
    constraints = []

    for i, nutrient in enumerate(nutrients):

        # We should have at least nutrient[1] of nutrient i to satisfy the Daily Value.
        constraints.append(solver.Constraint(nutrient[1], solver.infinity()))

        for j, item in enumerate(foods_data):
            # item[i + 3] is the amount of nutrient i in the food item j per 100g.
            # food_amount[j] is the amount of servings(100g) of food j to purchase to meet the nutrient constraint.
            constraints[i].SetCoefficient(food_amounts[j], item[i + 3])

    print("Number of constraints =", solver.NumConstraints())

    # Objective function: Minimize the sum of price of foods * number of servings of foods.

    objective = solver.Objective()

    # food prices per 100g, in Canadian cents
    food_prices = [item[2] for item in foods_data]


    for i, food_amount in enumerate(food_amounts):
        # the coefficient of the objective function should be :
        # the sum of each price multiplied by the amount of food
        # We want this result in Canadian dollars, and the price was in Canadian cents befre,
        # so we divide it by 100.
        objective.SetCoefficient(food_amount, food_prices[i])

    # We want to minimize the total cost.
    objective.SetMinimization()

    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    # Check that the problem has an optimal solution.
    if status != solver.OPTIMAL:
        print("The problem does not have an optimal solution!")
        if status == solver.FEASIBLE:
            print("A potentially suboptimal solution was found.")
        else:
            print("The solver could not solve the problem.")
            exit(1)

    # Display the amounts of servings(100g) to purchase of each food.

    # this creates a list of length equal to the number of nutrients,containing 0s.
    nutrients_result = [0] * len(nutrients)
    
    print("\nDaily Foods consumption (kg):")
    for i, food_amount in enumerate(food_amounts):
        if food_amount.solution_value() > 0.0:
            print("{}: {:.4f} kg".format(foods_data[i][0], 1/10 * food_amount.solution_value()))
            print("Costs: ${:.2f}".format(food_prices[i]/ 100 * food_amount.solution_value()))
            for j, _ in enumerate(nutrients):
                nutrients_result[j] += foods_data[i][j + 3] * food_amount.solution_value()
    print("\nOptimal daily price: ${:.2f}".format(objective.Value()/100))
    print("\nOptimal annual price: ${:.2f}".format(365 * objective.Value()/100))

    print("\nNutrients per day:")
    for i, nutrient in enumerate(nutrients):
        print(
            "{}: {:.2f} (min {})".format(nutrient[0], nutrients_result[i], nutrient[1])
        )

    print("\nAdvanced usage:")
    print(f"Problem solved in {solver.wall_time():d} milliseconds")
    print(f"Problem solved in {solver.iterations():d} iterations")


if __name__ == "__main__":
    main()
