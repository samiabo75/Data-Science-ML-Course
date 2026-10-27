# יחידה 3 — מפגש 15: KNN ביד, מרחקים, שכנים והצבעה
**מהדורת עומק Teaching-Edition-v3 · כיתה י׳ · 90 דקות הוראה/תרגול + 45 דקות פרויקט**

## סדר שימוש מומלץ
1. [ספר תלמיד מדורג](Student-Book.md) — סיפור פעילות, פיתגורס, נוסחה, חישוב חמשת המרחקים, דירוג, הצבעה, תיקו ומגבלות.
2. [מדריך מורה לפי דקות](Teacher-Guide.md) ו[פתרון חישובי מפורט](Teacher-Worked-Example.md).
3. [מחברת הדגמה](Guided-Audited.ipynb) (A–E ושאילתה 3,3); [מעבדת תלמיד להשלמה](Student-Fill-Blanks-Audited.ipynb) (P1–P5 ושאילתה 2,2); [פתרון מורה עם assert](Teacher-Solution-Audited.ipynb).
4. [איור נקודות לפני פתרון](knn-points-first.svg), [שלושת השכנים הקרובים](knn-neighbors.svg), [דירוג והצבעה K1/K3/K5](knn-ranked-votes.svg).
5. [מקור מקצועי ל־NotebookLM](NotebookLM-Source.md), [פרומפט עד 10 שקפים](NotebookLM-Prompt.md).
6. [יומן בקרת איכות](Quality-Check.md) ו[בדיקות מקומיות](Local-Code-Validation.md).

## קובצי מקור — נשמרו ללא שינוי
[מדריך מקור](../Teacher-Guide.md) · [מחברת Guided מקורית](../Guided-Lesson.ipynb) · [מעבדת תלמיד מקורית](../Student-Lab.ipynb) · [פתרון מקורי](../Teacher-Solution.ipynb) · [מפת שקפים](../Presentation-Brief.md).

**הפרדה מחייבת:** בדוגמת המורה K1=Red,K3=Blue,K5=Red; בתלמיד הסדרה והצבעות שונות. אין לחשוף את פתרון P1–P5 במצגת. אין לחשב Accuracy ללא תווית אמת. אין להקדים KNeighborsClassifier של מפגש 17.

**סטטוס Candidate — לא Ready:** נתונים והדגמה נבדקו מקומית בפייתון, מבנה קבצי הערכה נבדק; Run All מלא ב־Colab, הפקת/הגהת מצגת NotebookLM ופיילוט כיתה עדיין פתוחים.