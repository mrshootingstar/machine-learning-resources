## Precision-Recall curve
- For classification problems
- x axis: Precision: Tp/(Tp+Fp)
- y axis: Recall: Tp/(Tp+Fn)
- Ideal: Recall: 1.0, Precision: 1.0 [Top Right corner]

- Note that F1 Score is 2(Precision x Recall)/(Precision + Recall)
- Note that Precision may not decrease with Recall.

## ROC curve
- For classification problems
- x axis: False Positive Rate
- y axis: True positive Rate
- Ideal: (x, y) = (0, 1) [Top Left corner]

## Multiclass Evaluation
- extension of binary classification evaluatoin
- Confusion matrices are useful
    - sometimes it is useful to display a confusion matrix as a heatmap to see the frequencies
- Average across multiple class. There are several ways to do that.
### Micro vs Macro average:
#### Macro average
- Macro average: all classes have equal weights. We can compute macro average precision and macro average recall
- If there are 3 classes, each with n1, n2, n3 data points, and we detect c1, c2, c3 instances correctly, macro average precision would be
    - (1/3)*(c1/n1 + c2/n2 + c3/n3)
#### Micro average
- each instance has an equal weight

## Multilable classification
- Not covered here