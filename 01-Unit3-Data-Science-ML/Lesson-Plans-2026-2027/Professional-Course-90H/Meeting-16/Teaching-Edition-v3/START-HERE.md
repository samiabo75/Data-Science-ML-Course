# מפגש 16 — KNN בפונקציות ו־NumPy · ערכת הוראה מעמיקה v3
**כיתה י׳ · יחידה 3 · 90 דקות הוראה ותרגול + 45 דקות פרויקט**

## מתחילים כאן — סדר שימוש מומלץ
1. [ספר תלמיד](Student-Book.md): מסיפור דודו ל־return/print, מרחק ביד, for, NumPy, predict_one, תיקו והשוואת Scikit-learn.
2. [מדריך מורה](Teacher-Guide.md): לוח זמנים קשיח, שאלות סוקרטיות, טעויות נפוצות והקשר לרצף.
3. [פתרון ידני למורה](Teacher-Worked-Example.md): דוגמאות A–E ו־P1–P5 בנפרד וניתוח תיקו.
4. [מחברת הדגמה](Guided-Audited.ipynb): קלט A–E, פונקציות, K1/K3/K5, NumPy והשוואת ספרייה.
5. [מעבדת תלמיד בהשלמות](Student-Fill-Blanks-Audited.ipynb): קלט P1–P5 שונה, מימוש עצמאי ושתי שאילתות.
6. [פתרון מורה עם בדיקות](Teacher-Solution-Audited.ipynb): מימוש מלא, assert, תיקו ומקור ללא שינוי.
7. [איור מעקב לולאה](knn-distance-loop-trace.svg), [איור שלבי NumPy](knn-numpy-stages.svg), [תרשים זרימת חיזוי](knn-prediction-flow.svg).
8. [מסמך מקור ל־NotebookLM](NotebookLM-Source.md) ו[פרומפט 9–10 שקפים](NotebookLM-Prompt.md).
9. [Quality Gate](Quality-Check.md) ו[דוח בדיקות קוד מקומיות](Local-Code-Validation.md).

## חומרי המקור נשמרו ללא שינוי
[מחברת מקור מודרכת](../Guided-Lesson.ipynb) · [מעבדה מקורית](../Student-Lab.ipynb) · [פתרון מקור](../Teacher-Solution.ipynb) · [מדריך מקור](../Teacher-Guide.md) · [מפת ההשתלמות](../Presentation-Brief.md).

**שימו לב:** במפגש זה כבר נדרשת *השוואת מימוש פונקציונלי ל־KNeighborsClassifier*, כפי שמופיע במקור. אימון וניתוח הספרייה כמסלול לימוד מרכזי עדיין מיועדים למפגש 17. בחבילת v3 יש מדיניות מפורשת במקרה של תיקו (None) במקום mode().iloc[0] שאינו נימוק לרוב.

**סטטוס Candidate:** בדיקות מקומיות מקבילות לתאי המחברות עברו, אבל Run All מלא של קובצי המחברות ב־Colab, בדיקת מצגת NotebookLM והגהה, בדיקת השקפים המקוריים ופיילוט כיתה טרם בוצעו.