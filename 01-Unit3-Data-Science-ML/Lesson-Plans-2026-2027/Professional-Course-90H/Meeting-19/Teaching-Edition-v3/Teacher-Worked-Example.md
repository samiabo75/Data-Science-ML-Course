# מפגש 19 — פתרון ידני למורה
דוגמת המורה בלבד: 8 מוצרים, חיובי Defect, מטריצה בשורות אמת ובעמודות חיזוי עם סדר OK, Defect: `[[3,1],[2,2]]`.

| שלב | פעולה | תוצאה |
|---|---|---|
| 1 | מספר חזויים חיוביים: TP+FP | 2+1=3 |
| 2 | מספר חיוביים אמיתיים: TP+FN | 2+2=4 |
| 3 | Precision: TP/(TP+FP) | 2/3 ≈ 0.6667 |
| 4 | Recall: TP/(TP+FN) | 2/4 = 0.5 |
| 5 | F1: 2TP/(2TP+FP+FN) | 4/7 ≈ 0.5714 |
| 6 | Accuracy: (TN+TP)/8 | 5/8 = 0.625 |

למה F1 איננו `(Precision+Recall)/2`? כי F1 הוא ממוצע הרמוני. הצבת P=2/3 ו־R=1/2 נותנת `(2×2/3×1/2)/(2/3+1/2)=4/7` בדיוק.

## בדיקה בקוד
```python
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score
actual=["OK","OK","OK","OK","Defect","Defect","Defect","Defect"]
predicted=["OK","OK","Defect","OK","OK","OK","Defect","Defect"]
assert confusion_matrix(actual,predicted,labels=["OK","Defect"]).tolist()==[[3,1],[2,2]]
assert abs(precision_score(actual,predicted,pos_label="Defect")-2/3)<1e-12
assert abs(recall_score(actual,predicted,pos_label="Defect")-1/2)<1e-12
assert abs(f1_score(actual,predicted,pos_label="Defect")-4/7)<1e-12
assert accuracy_score(actual,predicted)==5/8
```

## העברה לסיטואציית ספאם
המכנה של Precision הוא **כל מה שהמערכת סימנה כספאם**. המכנה של Recall הוא **כל הספאם שהיה באמת**. אותה הגדרה תעבוד גם אם המחלקה החיובית היא Defect או Chinstrap, ובלבד שידועה מחלקת המטרה.

## מקרה הקצה
אם אין תחזיות חיוביות, Precision הוא 0/0 ולא מוגדר מתמטית. `zero_division=0` בוחר אפס לתצוגה. אם יש 2 פגומים אמיתיים וכולם הוחמצו, Recall=0/2=0.

## מפתח למשימת התלמיד
פתרון 12 המוצרים ו־Adelie נמצא במחברת `../Teacher-Solution.ipynb`. **לא להציג במצגת או בספר לתלמיד**.
