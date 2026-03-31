Observations:

Real Input, Discrete Output and Real Input Real Output
Training Time:

For P=10 (orange line), training time is higher than for P=5 (blue line). This makes sense because training complexity grows with N⋅P⋅logN. The lines are not perfectly smooth (notice the dip at N=40) - this is because the dataset is small and runtime is averaged over 100 runs, so there is randomness and measurement noise.Overall, as N increases, training time tends to increase, especially when P is larger.

Prediction Time:
Prediction time increases with N. The curve is nearly linear — which matches the theory:
Predicting a single sample is O(tree depth)=O(logN). Predicting N samples is O(NlogN).
The jaggedness is again due to small sample sizes and system noise.


Discrete Input, Real Output and Discrete Input, Discrete Output
Training Time:
In the training time vs. N plot (left), the blue curve (P=5) shows an initial increase in training time up to N=40, followed by a decrease as N grows, while the orange curve (P=10) exhibits the opposite behavior, starting higher at N=20, decreasing until N=40, and then rising again. This crossing or fluctuation is not a theoretical outcome but rather an artifact caused by small dataset sizes where randomness dominates, noise in timing measurements, and the nature of regression trees where splits are based on variance reduction, which can behave unpredictably for small N. Theoretically, training time should scale as O(N⋅P⋅logN), and although the curves are jagged due to randomness, the general trend shows that larger P=10 tends to be costlier than P=5. 

Prediction Time:
On the other hand, in the prediction time vs. N plot (right), both curves increase with N, consistent with theory. The orange curve (P=10) is generally higher than the blue curve (P=5) but displays a peak around N=40 before decreasing, which again is due to randomness and small dataset effects rather than theoretical behavior. In principle, prediction complexity per sample is tree depth O(tree depth)=O(logN), so predicting N samples scales as O(NlogN), explaining why the overall trend across both curves is growth with N.