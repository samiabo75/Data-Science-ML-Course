# מפגש 18 — פתרון מורה מדורג (ללא פתרון מעבדת התלמיד)
**דוגמת ההוראה שונה ממטלת התלמיד.** חיובי: Defect.

## חישוב ידני, שלב אחר שלב
| מס' | אמת | חיזוי | תא |
|---:|---|---|---|
| 1 | OK | OK | TN |
| 2 | OK | OK | TN |
| 3 | OK | Defect | FP |
| 4 | OK | OK | TN |
| 5 | Defect | OK | FN |
| 6 | Defect | OK | FN |
| 7 | Defect | Defect | TP |
| 8 | Defect | Defect | TP |

מטריצה בסדר התוויות OK, Defect (שורות אמת ועמודות חיזוי): `[[3,1],[2,2]]`.
סכום תאים: 3+1+2+2=8. האלכסון: 3+2=5. `Accuracy=5/8=0.625=62.5%`.

## למה זו טעות מסוג FN ולא FP?
המוצר באמת פגום (חיובי), אך סווג תקין (שלילי): False Negative. הפוך: מוצר תקין שסווג פגום הוא False Positive.

## אימות מעשי
```python
from sklearn.metrics import confusion_matrix, accuracy_score
actual = ["OK","OK","OK","OK","Defect","Defect","Defect","Defect"]
predicted = ["OK","OK","Defect","OK","OK","OK","Defect","Defect"]
cm = confusion_matrix(actual, predicted, labels=["OK","Defect"])
assert cm.tolist() == [[3, 1], [2, 2]]
assert accuracy_score(actual, predicted) == 0.625
print(cm)
```

## שינוי הגדרת המחלקה החיובית
אם נגדיר OK כחיובי, הספירות נשארות במקומן **כל עוד סדר התוויות נשאר קבוע**, אבל תוויות TP,FP,FN,TN משתנות: TP החדש=3, TN החדש=2, FP החדש=2, FN החדש=1. Accuracy נשאר 5/8.

## המשך ל־Penguins
במטריצה רב־מחלקתית על אמת וחיזוי של המינים: שורה של מין היא כל הדוגמאות האמיתיות שלו; עמודה היא כל הדוגמאות שנחזו כמין זה. התא `Chinstrap→Adelie` מייצג Chinstrap אמיתי שנחזה Adelie; התא ההפוך שונה. סכום האלכסון חלקי סכום כל התאים משחזר Accuracy. ספירות מדויקות של Penguins ייקראו מפלט ההרצה, לא מהדוגמה הסינתטית.

## הערות למורה
מעבדת התלמיד המקורית מכילה עשר דוגמאות אחרות; אין לחשוף את פתרונה בספר או במצגת. חישובי Precision/Recall/F1 יידחו למפגש 19.
