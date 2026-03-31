## Observations

1. Gradient descent without feature scaling took significantly more iterations to converge because the feature values (0–1000) caused steep and flat directions in the cost surface.
2. After applying z-score normalization, the convergence became much faster and smoother.
3. Feature scaling transforms the cost contours from highly elongated ellipses into near-circular shapes, allowing gradient descent to take larger, more efficient steps.
4. Proper scaling prevents oscillations and instability during optimization.
5. Hence, z-score normalization greatly enhances the stability and speed of convergence.
