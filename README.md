# VBC-Data (Python3)

Data analysis, visualization, and optimization for the Fall 2020 Future Business Leaders of America Virtual Business Challenge - Management.
This business simulation involves altering factory layout, sale price, and bid speed to maximize profit in 6 months. 

On profit optimization (WeekOptimization.py):
Each bid placed has value in terms of dollar amount paid, and weight in number of units orders. 
Given a factory production limit on units produced, the brute-force optimization algorithm sums all subsets of all combinations of orders. 
Cases exceeding the production limit are discarded, and the combination producing the maximum price is returned.

Team "No Chance": placed 5th nationally.
