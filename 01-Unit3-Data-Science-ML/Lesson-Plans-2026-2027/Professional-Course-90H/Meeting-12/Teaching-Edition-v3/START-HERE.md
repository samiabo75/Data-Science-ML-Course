# יחידה 3 — מפגש 12: יעד, חלוקה והשלמת חסרים
**כיתה י׳ · 90 דקות הוראה ותרגול + 45 דקות פרויקט · מהדורת עומק v3**

## סדר שימוש
1. [ספר תלמיד](Student-Book.md) — סיפור, הגדרת X/y, חישוב אימון ביד, מניעת דליפה וקישור ל־AI.
2. [מדריך מורה](Teacher-Guide.md) — תכנון דקות, הבחנת demo/lab ומדרג רמזים.
3. [פתרון מורה ידני](Teacher-Worked-Example.md).
4. [תרשים חלוקה](xy-split-flow.svg), [תרשים אימוץ ממוצע אימון](train-mean-imputation.svg), [נתוני חסרים מאומתים של Penguins](penguins-missing-by-field.svg).
5. [מחברת הדגמה — seed 42 ותכונות מקור](Guided-Audited.ipynb).
6. [מעבדת תלמיד בהשלמות — seed 17 ושתי התכונות המקוריות למעבדה](Student-Fill-Blanks-Audited.ipynb).
7. [פתרון מורה עם בדיקות](Teacher-Solution-Audited.ipynb).
8. [מקור ל־NotebookLM](NotebookLM-Source.md) ו[פרומפט למצגת עד 10 שקפים](NotebookLM-Prompt.md).
9. [יומן בקרת איכות](Quality-Check.md) ו[דוח בדיקות קוד](Local-Code-Validation.md).

**מקורות נשמרו ללא שינוי:** [מדריך מורה מקורי](../Teacher-Guide.md), [מחברת Guided](../Guided-Lesson.ipynb), [מעבדת תלמיד](../Student-Lab.ipynb), [פתרון מקור](../Teacher-Solution.ipynb), [תוכן למצגת](../Presentation-Brief.md).

**הבחנה חשובה:** הדגמת הקורס משתמשת ב־bill_length_mm/bill_depth_mm ו־seed 42; מטלת התלמיד משתמשת ב־flipper_length_mm/body_mass_g ו־seed 17. אסור להעתיק את תוצאות ההדגמה כתוצאות המעבדה.

**סטטוס:** חומר ובדיקות מייצגות; לפני READY נדרשים Run All ב־Colab, הפקה והגהה של מצגת NotebookLM וניסוי בכיתה.