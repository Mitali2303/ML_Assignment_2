## Observation 1: The Effect of Rank on Reconstruction Quality

The primary observation is the direct relationship between the rank (r) and the visual quality of the reconstructed patch.

Low Rank (r=5): This represents a very high level of compression. The reconstruction is blurry, blocky, and loses almost all fine details. It only captures the most general color and brightness information of the patch.

Medium Ranks (r=10,r=25): As the rank increases, the reconstruction quality improves dramatically. Details begin to emerge, edges become sharper, and the image is much more recognizable.

High Rank (r=50): This represents the lowest level of compression. For a 50x50 patch, a rank of 50 allows for a near-perfect reconstruction, as the number of parameters in the factor matrices is sufficient to capture all the information in the original patch. The reconstructed patch is visually almost identical to the original.

## Observation 2: The Impact of Image Complexity

The effectiveness of a given rank is highly dependent on the complexity of the image patch being compressed.

Patch A (Simple Background): This patch has low complexity (low spatial frequency). Even at a very low rank like r=5, the reconstruction is reasonably good because there are no sharp details to preserve. The difference in quality between r=25 and r=50 is minimal, suggesting that a low rank is sufficient to represent this simple area.

Patch B (Medium Complexity): For patch B, a rank of r=5 is poor, creating a blurry mess. However, at r=10 and r=25, the key features (like the nose, whiskers, and mouth line) become clearly visible. This shows that a moderate rank is needed to capture a moderate level of detail.

Patch C (High Complexity): Patch C is a high-complexity patch with fine fur texture, sharp edges, and reflections. At low ranks (r=5,r=10), the reconstruction completely fails to capture these details. A high rank (r=25 and especially r=50) is necessary to produce a visually faithful reconstruction of this complex area. The quality improvement with each step up in rank is most pronounced for this patch.
