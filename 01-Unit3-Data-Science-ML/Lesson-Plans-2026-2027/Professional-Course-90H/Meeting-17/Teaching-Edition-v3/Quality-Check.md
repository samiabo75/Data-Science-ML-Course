# Quality Gate — מפגש 17 (27.10.2026)
**Content Checked + Source CSV Checked + Representative Local Code Checked; NOT READY**

## שמירת מטלת המקור
נבדקו שלוש מחברות המקור; Guided על flipper_length_mm/body_mass_g ב־seed42, Student-Lab ופתרונה על bill_length_mm/bill_depth_mm ב־seed17. שתיהן מפצלות X/y יחד, test_size=.25, stratify=y, משלימות חסרים לפי ממוצעי Train, מתאימות StandardScaler על Train שהושלם, מריצות KNeighborsClassifier(K=3,weights=uniform,metric=euclidean), fit, predict, comparison עם actual/predicted/correct, Accuracy, עד 3 שגיאות וכרטיס מודל. אין לשנות K לפי Test.

## אימות מקור
קובץ Datasets/penguins.csv נבדק ישירות במחבר GitHub, SHA b5093336d83d99d8835c606b455d00065ab7cdcf: 344 רשומות, 7 עמודות, species ללא חסרים, 3 מינים Adelie=152,Gentoo=124,Chinstrap=68, ארבע מדידות מספריות עם 2 חסרים בכל אחת, sex עם 11 חסרים. בגודל Test 25% מתקבלות 258 Train/86 Test. **לא נמדד Accuracy אמיתי של שתי המחברות בעזרת הרצה מלאה כאן**; ערכי הציון יחושבו מתוך פלט המחברות.

## דוגמת Accuracy מחושבת
דוגמה סינתטית y_true=[1,0,0,1], y_pred=[1,0,1,1], נכונות True,True,False,True, לכן 3/4=0.75=75%. אינה תוצאת Penguins. טבלת השגיאות השנייה היא המחשה סכמטית בלבד.

## רכיבי הערכה
ספר תלמיד, מדריך מורה ופתרון ידני מפורטים; שלוש מחברות Audited (Guided עם 33 assert, מעבדת תלמיד עם 49 השלמות, Teacher עם 37 assert); שלושה SVG מחושבים או מסומנים כסכמטיים; מקור/פרומפט NotebookLM (עד 10 שקפים); START-HERE ודוחות QA/Local.

## מה אומת ומה לא
- נתוני המקור ומטלות המקור נבדקו; Code מקומי מייצג עבר על פיצול עם stratify, השלמת חסרים, תקנון, KNN, אינדקסים ו־accuracy_score.
- מבנה קבצים, תקינות JSON ו־SVG, והפרשים לעומת main ייבדקו בענף לפני מיזוג.
- **לא בוצעו** Run All מלא על מחברות GitHub ב־Colab, הפקת NotebookLM מוגהת, צפייה חזותית בשקפי השתלמות מקוריים או פיילוט כיתה.
- יש לבצע את אלה, ולבדוק התאמה למפרט הערכה רשמי תקף, לפני הסימון READY.

## בדיקות איכות הנחוצות ל־Run All
1. קובץ Raw CSV נטען ומדווח 344×7; מוצגות עמודות והחסרים.
2. Xtrain/Xtest בגודל 258/86 ושמירת אינדקסים y.
3. X_train_ready/X_test_ready ללא חסרים בשתי התכונות; StandardScaler.fit נערך רק ב־Train.
4. len(predictions)=86; טבלת comparison משמרת אינדקס y_test.
5. correct_count/86 זהה ל־accuracy_score, 0≤Accuracy≤1, correct+errors=86.
6. שורות שגויות נשלפות באמצעות האינדקס ומוצגות רק אם קיימות; אין הנחת טעות מסוימת מראש.
7. אף מסקנה אינה מפרשת את הציון כבחירה של K או כביצוע מובטח בטבע.

**זהו Candidate, לא חבילת READY לשימוש בלי ביקורת.**