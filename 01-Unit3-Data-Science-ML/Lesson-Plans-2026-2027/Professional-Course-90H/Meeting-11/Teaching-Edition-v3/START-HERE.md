# יחידה 3 — מפגש 11: Boxplot ואיכות נתונים
**מהדורת עומק Teaching-Edition-v3 | כיתה י׳ | 90 דקות הוראה ותרגול + 45 דקות פרויקט**

## סדר שימוש
1. [ספר תלמיד מפורט](Student-Book.md) — סיפור → תשע מדידות → רבעונים בשיטת חצאים → גדרות ושפמים → Python → איכות נתונים → פרויקט.
2. [מדריך מורה לפי דקות](Teacher-Guide.md) ו[פתרון מתמטי/לוגיקת ניקוי](Teacher-Worked-Example.md).
3. [מחברת הדגמה](Guided-Audited.ipynb), [מעבדת תלמיד בהשלמות](Student-Fill-Blanks-Audited.ipynb), [פתרון מורה עם assert](Teacher-Solution-Audited.ipynb).
4. [תרשים רבעונים ידני](quartiles-hand-trace.svg) ו[Boxplot מסומן](delivery-boxplot.svg).
5. [תרשים Penguins המבוסס על נתונים אמיתיים](penguins-species-boxplots.svg) — **למורה או אחרי התרגול בלבד**, מכיל תוצאות שתלמידים אמורים למצוא.
6. [מקור ל־NotebookLM](NotebookLM-Source.md), [פרומפט 9–10 שקפים](NotebookLM-Prompt.md).
7. [בדיקת איכות](Quality-Check.md) ו[דוח בדיקות קוד](Local-Code-Validation.md).

**קובצי המקור נשמרו ללא שינוי:** [מדריך](../Teacher-Guide.md), [הדגמה](../Guided-Lesson.ipynb), [מעבדת מקור](../Student-Lab.ipynb), [פתרון מקור](../Teacher-Solution.ipynb), [מיפוי מצגות](../Presentation-Brief.md).

## דגשים
שיטת **חצאים ללא החציון** משמשת להמחשת תשע מדידות, ואילו **Pandas linear** משמשת במעבדת המקור וב־Boxplot של Seaborn. עבור תשע המדידות בחרנו נתונים שבהם שתי השיטות מסכימות; הן אינן שקולות בכלל.

המקור האמיתי Penguins הוא 344×7, שתי מדידות סנפיר חסרות. אין למחוק נקודה חריגה ללא ראיה. מחברות קוד נבדקות בשלבים; עדיין נדרשות הרצה מלאה ב־Colab, הגהת NotebookLM וניסוי בכיתה לפני READY.