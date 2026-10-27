# פתרון המורה — דוגמה ידנית 95/5
**לא פתרון מעבדת התלמיד (90/10).**

חיובי = Spam. יש 95 תקינות, 5 ספאם אמיתיות; הכלל חוזה OK תמיד.
| אמת \ חיזוי | OK | Spam |
|---|---:|---:|
| OK | TN=95 | FP=0 |
| Spam | FN=5 | TP=0 |

מספר תצפיות 100. דיוק = `(95+0)/100=0.95`. Recall לספאם = `0/(0+5)=0`. Precision לספאם = `0/(0+0)` אינו מוגדר מתמטית; `zero_division=0` מאפשר דיווח אפס בלבד. קו בסיס "המחלקה הנפוצה" צריך לקבוע את הכלל על Train. אין לטעון שכל מודל בעל Accuracy דומה נכשל באותו אופן: יש לבדוק מטריצה וסוגי טעויות.

```python
from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix
actual = ["OK"]*95 + ["Spam"]*5
prediction = ["OK"]*100
assert confusion_matrix(actual,prediction,labels=["OK","Spam"]).tolist()==[[95,0],[5,0]]
assert accuracy_score(actual,prediction)==0.95
assert recall_score(actual,prediction,pos_label="Spam")==0.0
assert precision_score(actual,prediction,pos_label="Spam",zero_division=0)==0.0
```

**שאלת העברה:** מה יקרה לציון Accuracy אם יהיו 99 תקינות ואחת ספאם אך הכלל לא ישתנה? Accuracy יעלה, אף שה־Recall לספאם יישאר אפס. זהו שינוי בנתוני דוגמה מומצאים, לא ניסוי כללי.
