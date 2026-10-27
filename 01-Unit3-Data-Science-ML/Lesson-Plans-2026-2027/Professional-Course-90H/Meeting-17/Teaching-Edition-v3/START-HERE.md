# יחידה 3 — מפגש 17: KNN בספרייה — אימון, חיזוי והערכה
**מהדורת עומק Teaching-Edition-v3 · כיתה י׳ · 90 דקות הוראה ותרגול + 45 דקות פרויקט**

## תוספת מושגית למעבר ממפגש 16
[גשר דידקטי: מה בדיוק עושים fit ו־predict?](KNN-Fit-Predict-Concept-Bridge.md) — סיפור, חישוב מרחקים ביד, קוד קצר מאומת ועצירות חשיבה. קובץ הרחבה בלבד; אינו מחליף את המעבדה המקורית.

## סדר עבודה
1. [ספר התלמיד](Student-Book.md) — סיפור, אמת מול חיזוי, Accuracy ידני, Penguins, חלוקת Train/Test, הכנה ללא דליפה, KNN, טעויות.
2. [מדריך המורה לפי דקות](Teacher-Guide.md) ו[פתרון ידני ומפתח למורה](Teacher-Worked-Example.md).
3. [מחברת הדגמה](Guided-Audited.ipynb) — flipper_length_mm/body_mass_g, seed42; [מעבדת תלמיד עם השלמות](Student-Fill-Blanks-Audited.ipynb) — bill_length_mm/bill_depth_mm, seed17; [פתרון מורה עם בדיקות](Teacher-Solution-Audited.ipynb).
4. [דיוק בארבע תצפיות מומצאות](accuracy-four-observations.svg), [תרשים Train/Test והערכה](knn-train-test-evaluation.svg), [בדיקת שגיאות סכמטית](error-inspection-table.svg).
5. [מקור מקצועי ל־NotebookLM](NotebookLM-Source.md) ו[פרומפט ל־10 שקפים](NotebookLM-Prompt.md).
6. [דוח בקרת איכות](Quality-Check.md) ו[דוח בדיקות קוד מקומיות](Local-Code-Validation.md).

## מקורות ההשתלמות — לא שונו
[Guided מקורית](../Guided-Lesson.ipynb) · [מעבדת מקור](../Student-Lab.ipynb) · [פתרון מקור](../Teacher-Solution.ipynb) · [מדריך מקור](../Teacher-Guide.md) · [מפת שקפים](../Presentation-Brief.md).

**הדגמה אינה פתרון תלמיד:** משימות המקור עם שני זוגות תכונות ושני Seeds נשמרו. בכל מסלול משלימים חסרים ומתקננים מתוך Train בלבד; K3 נקבע מראש. לא בוחרים K או תכונות לפי Test, ולא מתייחסים לטבלת שגיאות סכמטית כאל תוצאות Penguins.

**סטטוס Candidate:** נתוני CSV אומתו במקור וקוד מייצג נבדק מקומית; עדיין נדרשים Run All מלא בקובצי המחברות ב־Colab, בדיקה חזותית/הגהה של NotebookLM, פיילוט כיתה והצלבה למפרט הרשמי לפני READY.

## תוספת בקרה אמיתית — 27.10.2026
- [דוח שחזור KNN על Penguins האמיתי (למורה בלבד)](Real-Penguins-Validation-Teacher.md).
- [סקריפט Python שחזורי, עם בדיקת Git blob SHA של קובץ הנתונים](Verify-Real-Penguins.py).
- בנתוני המקור אומתו חישוב 60/86 בדוגמת המורה ו־83/86 בפתרון המעבדה; אלה תוצאות מקומיות של אותו רצף חישוב, **לא** Run All של מחברות Colab. אין להעלות את דוח התוצאות המלא למצגת התלמיד.
