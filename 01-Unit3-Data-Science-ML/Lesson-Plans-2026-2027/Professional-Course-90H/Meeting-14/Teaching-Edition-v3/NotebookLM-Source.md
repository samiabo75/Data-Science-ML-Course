# מקור מקצועי ל־NotebookLM — מפגש 14: קידוד קטגוריות והכנה משולבת
**יחידה 3 · כיתה י׳ · מקור למצגת 9–10 שקפים בהירים · 90 דקות הוראה ותרגול + 45 דקות פרויקט**

## עוגני מקור ואמינות
המקור העיקרי הוא ספר התלמיד Student-Book.md החדש והמחברות Guided/Student-Lab המקוריות של Meeting-14. ההשתלמות ממפה **Data Preparation2.pptx שקפים 7–15**; לפני הקרנה יש לצפות בהם ולהשוות את התוכן בפועל. אין להשתמש במחברת Teacher-Solution ליצירת מצגת תלמידים. כל דוגמאות A/B/age הן **נתונים מומצאים להוראה**, לעומת קובץ Penguins המדעי.

## סיפור תלמיד
אתר למכירת מחשבים מכיל מחיר בשקלים, RAM ב־GB וצבע. תלמיד טוען שכחול=1, אדום=2, ירוק=3 ולכן הצבעים מסודרים במרחק שווה. שאלו: מה נלמד מהשם עצמו? **אין סדר טבעי במשתנה שמי.** שדה סדור כמו נמוך/בינוני/גבוה מאפשר מיפוי סדר אך לא מוכיח מרחקים שווים בין רמות.

## חישוב One-Hot — צעד אחר צעד
Train=[A,B,A]. העמודות הנלמדות: group_A,group_B (בדיוק בסדר הזה). לכל קטגוריה k:
\[
I_k(x)=1 \text{ if }x=k,\quad I_k(x)=0 \text{ otherwise}.
\]
כלומר A→[1,0], B→[0,1], A→[1,0]. Test=[B,C] נותן [0,1],[0,0] כאשר C לא נראתה ב־Train, עם OneHotEncoder(handle_unknown="ignore",sparse_output=False) וללא drop. C **אינה דומה** ל־A ול־B. גם D חדשה תקבל [0,0]; זהו איבוד מידע לקטגוריות לא מוכרות.

השתמשו באיור **onehot-train-unknown.svg**; בדקו את הכותרות group_A,group_B ואת שורת C לפני הקרנה.

## סדר עבודה ב־Python
1. מגדירים OneHotEncoder עם handle_unknown="ignore", sparse_output=False.
2. מפעילים fit על **Train בלבד** — כאן נלמדים אוצר הקטגוריות וסדר העמודות.
3. מפעילים transform על Train ועל Test/New. **לא מבצעים fit מחדש** על Test.
4. קוראים categories_ ואת שמות העמודות. ב־DataFrame ניתן להשתמש ב־set_output(transform="pandas"), כפי שנעשה במקור.

~~~python
from sklearn.preprocessing import OneHotEncoder
encoder=OneHotEncoder(handle_unknown="ignore",sparse_output=False)
encoder.fit([["A"],["B"],["A"]])
print(encoder.transform([["B"],["C"]]))
~~~

פלט צפוי: [0,1] ו־[0,0]. כל וקטור הוא **מאפייני קלט**, לא הסתברות למין ולא דירוג מרחק בין שמות.

## גשר מדורג: Numeric + Categorical
בטבלה עם גיל age (שנים) ו־group (שם קבוצה), בונים ColumnTransformer:
- numeric: SimpleImputer(strategy="median") ואז StandardScaler;
- categorical: OneHotEncoder(handle_unknown="ignore",sparse_output=False);
- תוצאה: שילוב מספרי של העמודות באותו סדר בשני הצדדים.
המחישו באמצעות **two-path-preparation.svg**, שבו ההפרדה לשני המסלולים ברורה.

### הצבה ידנית של דוגמת המורה — לא הפתרון של המעבדה
Train age=[10,20,חסר], group=[A,B,A].
חציון האימון של age הידועים (10,20) הוא 15. אחרי השלמה: [10,20,15], ממוצע 15, סכום ריבועי סטיות 25+25+0=50. StandardScaler משתמש ב־ddof=0, ולכן:
\[
\sigma=\sqrt{50/3}\approx4.0824829.
\]
תקנון age: [−1.2247449,+1.2247449,0]. קידוד group: [1,0],[0,1],[1,0]. לכן שלוש שורות הפלט הן:
- [−1.2247,1,0]
- [+1.2247,0,1]
- [0,1,0]

New=(age=15,group=C) => [0,0,0] באותן שלוש עמודות, כי הגיל שווה לממוצע אחרי ההשלמה ו־C אינה מוכרת. **המספר 0 בעמודת הגיל אינו אותה משמעות כמו 0 בעמודת קטגוריה!**

איור **combined-schema-example.svg** מבוסס בדיוק על הערכים האלה, עם שמות העמודות numeric__age,categorical__group_A,categorical__group_B. מקור שתי עמודות הופך לשלוש עמודות קלט, **מספר שורות המקור אינו גדל**.

## מעבר למטלה עצמאית — ללא תשובות!
בקובץ Penguins אמיתי היעד species והמאפיין island (שמי). במטלת התלמיד test_size=.25,random_state=17,stratify=y, ולכן X_train ו־X_test נשארים באותו סדר שורות עם y. מקודדים את island על Train בלבד, ומפרשים שלוש עמודות One-Hot. במטלת צורות נפרדת מקודדים circle/square ואחר כך triangle חדשה. במטלת ColumnTransformer התלמיד משתמש **בנתונים אחרים**: Train age=[5,15,חסר] ו־group=[C,D,D], New=(10,E). **אין להציג את תוצאות התרגילים העצמאיים במצגת ההכנה.** די בשאלות מוכוונות.

## רצף מומלץ של 10 שקפים
1. סיפור אתר מחשבים, צבע לעומת מחיר/RAM.
2. הבחנה nominal/ordinal עם דוגמת island ורמות.
3. טבלת Train A,B,A ושאלת יצירת עמודות.
4. הפונקציה I_k והצבה של A,B.
5. איור onehot-train-unknown.svg ודיון על C→[0,0].
6. קוד Python קצר: Fit על Train, Transform על Test, סכמה קבועה.
7. מעבר ל־Penguins: תצפית אחת, X=island, y=species, split 258/86, משימות ולא פתרון.
8. תרשים two-path-preparation.svg; סדר השלמת חציון, Standard ו־One-Hot.
9. החישוב הידני של age=10/20/חסר ו־group=A/B/A; איור combined-schema-example.svg והסבר שתי משמעויות של אפס.
10. כרטיס יציאה והכנה למעבדה ול־45 דקות הפרויקט: מה Fit לומד? כמה עמודות? מה עושים עם קטגוריה חדשה?

## גבולות נושא ומניעת טעויות
לא מלמדים GridSearch לפני מפגש 23, לא מאמנים KNN לפני מפגש 15, לא לומדים קטגוריות מ־Test, ולא טוענים שסכמה כוללת את כל הערכים העתידיים. אם המשמעות של שדה היא סדורית, אין להסיק אוטומטית פערים שווים בקוד מספרי. אין לאמן מודל באמצעות יעד species בתוך X. אין Accuracy, לא הסתברות ולא טענת סיבתיות.

## הוראות הגהה
9–10 שקפים, רקע בהיר, כתב עברי תקין RTL, קוד ומשוואות LTR, ציורים חשבוניים מדויקים, יחידות ומקורות לכל נתון. חובה לבצע בקרת כתיב/כיווניות ושמות העמודות שקף־שקף אחרי הפקת NotebookLM. מסמך מקור ופרומפט אינם מצגת מוכנה.

## כלים מומלצים למורה
NotebookLM https://notebooklm.google.com/ — הפקה ממקור מבוקר והגהה.
Google Colab https://colab.research.google.com/ — הרצת שלבי Fit ו־Transform ולמידת השפעת שינוי קלט.
Scikit-learn https://scikit-learn.org/stable/modules/compose.html — תיעוד מקצועי של ColumnTransformer.