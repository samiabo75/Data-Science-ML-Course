# פתרון ידני ומדריך בקרה — מפגש 17 (למורה)

## דוגמת Accuracy שאינה תלויה ב־Penguins
אמת [1,0,0,1], תחזית [1,0,1,1], נכונות [True,True,False,True], לכן 3 נכונות מתוך 4 ו־Accuracy=3/4=0.75=75%. השגיאה השלישית היא אמת=0, חיזוי=1. אין כאן סיבתיות או חיזוי לעתיד.

## צורות הנתונים
במאגר Penguins של הקורס: 344 שורות, 7 עמודות ויעד species. split של 25% מפיק 258 אימון ו־86 בדיקה. הדגמת מורה: flipper_length_mm, body_mass_g עם seed=42; מעבדת תלמיד: bill_length_mm, bill_depth_mm עם seed=17. אי אפשר להסיק עדיפות מאפיינים מהשוואה בין שני ציוני הערכה הנוצרים תחת שני Seeds שונים.

## סדר תהליך ו־DataFrame
כדי לשמור על תוויות:
~~~python
comparison = pd.DataFrame(
    {"actual": y_test, "predicted": predictions},
    index=y_test.index
)
comparison["correct"] = comparison["actual"] == comparison["predicted"]
correct_count = int(comparison["correct"].sum())
accuracy_hand = correct_count / len(comparison)
accuracy_library = accuracy_score(y_test, predictions)
assert abs(accuracy_hand - accuracy_library) < 1e-12
~~~
אין ליצור pd.Series(predictions) עם RangeIndex ולהניח שהיא תתיישר ל־y_test. אסור להשתמש ב־y_test ב־predict: הוא נדרש רק להערכת התוצאות.

## סיכום טעויות
errors = comparison[comparison["correct"] == False] מציג רשומות שבהן actual != predicted. מספר נכון + מספר טעויות = 86. רשמו בפועל את האינדקס, מין אמת, מין חזוי ואת ערכי שתי המדידות מהמקור; **אל תמציאו** את מספר הטעויות או את Accuracy. עד שלוש שורות ראשונות אינן מדגם אקראי ואינן מוכיחות סיבה לטעות.

## שאלות הגנה
מדוע StandardScaler נלמד רק מ־Train? מה נלמד ב־fit של KNN? מה ההבדל בין תווית חיזוי ליעד אמת? מהו המכנה בנוסחת Accuracy? מהי מגבלת ההכללה לחלוקות אחרות ולאוכלוסייה? למה אין לשנות K לאחר התבוננות בתוצאה של Test?