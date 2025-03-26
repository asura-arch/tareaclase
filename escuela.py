from sklearn.metrics import accuracy_score,
precision_score ,f1s_core

TP=40
TN=30
FP=20
FN=10

Total= TP + TN + FP +FN
rentabilidad= (TP+TN)/ Total

precision= TP/(TP+FP) 
if (TP+FP)>0 else 0

llamada= TP / (TP + FN) 

f1_measure = 2 * (precision * llamada ) / (precision + llamada )
if (precision + llamada) > 0 else 0

print(f"rentabilidad: {rentabilidad:.2f}")
print(f"Precision: {precision:.2f}")
print(f"F1-Measure: {f1_measure:.2f}"
