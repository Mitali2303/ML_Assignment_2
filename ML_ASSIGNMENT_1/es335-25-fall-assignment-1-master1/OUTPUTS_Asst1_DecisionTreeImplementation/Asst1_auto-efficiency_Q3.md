Q.3.


Results from Custom Decision Tree:
RMSE: 3.3108517994068576
MAE: 2.526477778342185
? (weight <= 2818.5)
Y:     ? (horsepower <= 78.0)
    Y:         ? (acceleration <= 17.0)
        Y:             ? (displacement <= 98.0)
            Y:                 ? (model year <= 77.5)
                Y:                     Leaf: 30.0
                N:                     Leaf: 35.52727272727273   
            N:                 ? (model year <= 80.0)
                Y:                     Leaf: 28.9375
                N:                     Leaf: 34.9
        N:             ? (displacement <= 90.0)
            Y:                 ? (model year <= 78.0)
                Y:                     Leaf: 33.75454545454546   
                N:                     Leaf: 39.9625
            N:                 ? (model year <= 78.5)
                Y:                     Leaf: 27.857142857142858  
                N:                     Leaf: 33.04285714285715   
    N:         ? (displacement <= 121.0)
        Y:             ? (acceleration <= 15.0)
            Y:                 ? (model year <= 75.0)
                Y:                     Leaf: 24.272727272727273  
                N:                     Leaf: 27.5625
            N:                 ? (model year <= 75.5)
                Y:                     Leaf: 25.125
                N:                     Leaf: 29.3125
        N:             ? (model year <= 79.0)
            Y:                 ? (acceleration <= 15.5)
                Y:                     Leaf: 23.380000000000003  
                N:                     Leaf: 23.4
            N:                 ? (acceleration <= 14.45)
                Y:                     Leaf: 29.599999999999998  
                N:                     Leaf: 27.657142857142855  
N:     ? (displacement <= 302.0)
    Y:         ? (acceleration <= 16.5)
        Y:             ? (horsepower <= 110.0)
            Y:                 ? (model year <= 75.0)
                Y:                     Leaf: 18.692307692307693  
                N:                     Leaf: 20.75
            N:                 ? (model year <= 78.0)
                Y:                     Leaf: 16.508333333333333  
                N:                     Leaf: 24.975
        N:             ? (model year <= 78.0)
            Y:                 ? (horsepower <= 95.0)
                Y:                     Leaf: 19.560000000000002  
                N:                     Leaf: 17.833333333333332  
            N:                 ? (horsepower <= 88.0)
                Y:                     Leaf: 27.944444444444446  
                N:                     Leaf: 22.51666666666667   
    N:         ? (horsepower <= 150.0)
        Y:             ? (acceleration <= 13.2)
            Y:                 ? (model year <= 73.0)
                Y:                     Leaf: 15.11111111111111   
                N:                     Leaf: 16.4
            N:                 ? (model year <= 76.0)
                Y:                     Leaf: 13.833333333333334  
                N:                     Leaf: 18.728571428571428  
        N:             ? (acceleration <= 12.0)
            Y:                 ? (model year <= 71.0)
                Y:                     Leaf: 13.9
                N:                     Leaf: 14.055555555555555  
            N:                 ? (model year <= 72.0)
                Y:                     Leaf: 11.714285714285714  
                N:                     Leaf: 13.6

Results from scikit-learn Decision Tree:
RMSE: 3.1751205206902453
MAE: 2.2961593623269154