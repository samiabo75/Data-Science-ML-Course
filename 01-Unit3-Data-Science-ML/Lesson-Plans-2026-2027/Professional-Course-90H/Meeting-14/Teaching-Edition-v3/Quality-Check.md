# בקרת איכות — Meeting-14
**27.10.2026 | תוכן נבדק; חישוב/קוד מייצג נבדק; עדיין Candidate ולא READY**

## בדיקת המקור
נבדקו מחברות Guided-Lesson, Student-Lab ו־Teacher-Solution. שתי משימות החובה נשמרו: (1) One-Hot של island לאחר חלוקה משותפת X/y עם species, test_size=.25, seed17 ו־stratify=y, ומדיניות unknown על shapes חדשה; (2) מסלול numeric של חציון ותקנון ו־categorical של One-Hot בתוך ColumnTransformer על age=[5,15,None], group=[C,D,D], new=(10,E). מטלת רשות: מיפוי נמוך/בינוני/גבוה. הפתרון של המורה נשאר במיקום נפרד.

## ערכים מאומתים במקור ובדוגמאות
- מאגר הקורס Penguins: 344 שורות, שלושה שמות island Biscoe/Dream/Torgersen; species יעד; החלוקה עם 25% מניבה 258 Train ו־86 Test.
- Train A,B,A ⇒ One-Hot [1,0],[0,1],[1,0]. קטגוריה C חדשה במדיניות ignore וללא drop ⇒ [0,0].
- דוגמת מורה משולבת: age=[10,20,None],group=[A,B,A]; חציון 15, גיל תקני [−1.224745,+1.224745,0], New=(15,C)⇒[0,0,0], סכמה numeric__age,categorical__group_A,categorical__group_B.
- מטלת תלמיד המשולבת: age=[5,15,None],group=[C,D,D]; חציון 10, גיל תקני [−1.224745,+1.224745,0], New=(10,E)⇒[0,0,0], סכמה numeric__age,categorical__group_C,categorical__group_D.
- בדיקה מקומית באמצעות Scikit-learn מאשרת OneHotEncoder ו־ColumnTransformer; זאת בדיקה מייצגת, לא Run All של כל מחברות GitHub.

## רכיבי הערכה
ספר תלמיד, מדריך, פתרון ידני; שלוש מחברות ipynb עם קוד מדורג, השלמות ובדיקות; שלושה SVG הנאמנים למספרים; מסמך מקור למצגת ופרומפט NotebookLM; מדריך פתיחה ויומן בדיקות.

## שערים שעדיין פתוחים
1. אימות קיום ומבנה כל הקבצים בענף הראשי, והפרשים ללא מחיקות/שינוי קובצי מקור.
2. Run All מלא של שתי מחברות מורה בתוך Google Colab, כולל טעינת Raw Penguins, פלט, סדר שורות ועובדת אי־השינוי של המקור.
3. הפקה והגהה שקף־שקף של NotebookLM, כולל צפייה חזותית בשקפי Data Preparation2 המקוריים (7–15).
4. פיילוט עם תלמידים, שיפור קצב במעבדה והצלבת דרישות הבחינה הרשמיות.

**איסורים בהסקה:** אפס unknown אינו קרבה, fit על Test אינו מותר, One-Hot אינו מודל חיזוי, ואין להכריז על הצלחת מסווג שטרם אומן.