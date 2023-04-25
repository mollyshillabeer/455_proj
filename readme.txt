How to execute this code:
-Ensure the following packages are installed: pandas, numpy, matplotlib, seaborn
-type "python main.py" in the command line and hit enter

The entry point for the code is the stats function in main.py, it takes as input 
a number of trials to run and a threshold value for SR.

Each python file contains a seperate component of the EA:
-initialization.py includes code to make the hotel and guest objects, as well as the initial EA population
-mutation.py include a function to perform permutation swap
-recombination.py includes a function to perform 1 point cross-over
-Guest.py and Hotel.py have classes for each type of object
-evaluation.py has a function to calculate the fitness of a candidate solution
-survivor_selection.py implements both mu+lambda and replacement operators
-parent_selection.py implements both MPS and tournament selection operators
-main.py controls the flow of execution of the EA, visualization of results, parameter tuning, and statistics calculation

Other related files:
-other_approaches.py contains a non-EA based approach to solving the problem
-guests.csv contains a list of 1000 guests that can be used as sample data
-HotelReservations.csv contains the unprocessed form of this data
