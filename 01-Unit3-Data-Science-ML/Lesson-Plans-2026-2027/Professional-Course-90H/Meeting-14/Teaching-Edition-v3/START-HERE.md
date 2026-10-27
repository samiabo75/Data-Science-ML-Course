# יחידה 3 — מפגש 14: One-Hot וקדם־עיבוד משולב
**כיתה י׳ • 90 דקות הוראה ותרגול + 45 דקות פרויקט • Teaching-Edition-v3 • מועמדת לבקרה, לא READY**

## סדר העבודה
1. [ספר התלמיד המלא](Student-Book.md) — סיפור מחשבים; שמי/סדור; One-Hot ידני; קטגוריה חדשה; שני מסלולים וחישוב ידני.
2. [מדריך מורה לפי דקות](Teacher-Guide.md) ו[פתרון ידני ופתרון מטלת המקור למורה](Teacher-Worked-Example.md).
3. [מחברת הדגמה מדורגת](Guided-Audited.ipynb), [מעבדת תלמיד בהשלמות](Student-Fill-Blanks-Audited.ipynb), [פתרון מורה עם בדיקות](Teacher-Solution-Audited.ipynb).
4. [טבלת One-Hot מדויקת](onehot-train-unknown.svg), [תרשים שני מסלולים](two-path-preparation.svg), [סכמת פלט מספרית וקטגוריאלית](combined-schema-example.svg).
5. [מסמך מקור מקצועי ל־NotebookLM](NotebookLM-Source.md) ו[פרומפט 9–10 שקפים](NotebookLM-Prompt.md).
6. [יומן בקרת איכות](Quality-Check.md) ו[תיעוד בדיקות מקומיות](Local-Code-Validation.md).

## חומרי ההשתלמות נשמרו ללא שינוי
[מדריך מקורי](../Teacher-Guide.md) · [הדגמה מקורית](../Guided-Lesson.ipynb) · [מעבדה מקורית](../Student-Lab.ipynb) · [פתרון מקורי](../Teacher-Solution.ipynb) · [מיפוי מצגת](../Presentation-Brief.md).

**הבחנה:** הדגמת המקור משתמשת ב־Penguins island ו־seed42; מעבדת התלמיד ב־seed17. חלק ColumnTransformer בנתוני age/group של התלמיד הוא חלק ליבה, ולא הרחבה שאפשר לדלג עליה. אין GridSearch או אימון מודל במפגש.

**מעמד:** המסמכים, המחברות והמחשות נוצרו ונבדקו מבנית, ודוגמאות Python מייצגות נבדקו מקומית. נדרשים Run All מלא ב־Colab, הגהת מצגת ובדיקת ניסיון כיתה לפני READY.