# מפגש 25 — רגרסיה משולבת וניתוח גודל הטעות | Teaching Edition v3
**90 דקות הוראה ותרגול + 45 דקות פרויקט | Candidate עד בדיקות CI**

| רכיב | קישור |
|---|---|
| ספר תלמיד | [Student-Book.md](Student-Book.md) |
| מדריך מורה | [Teacher-Guide.md](Teacher-Guide.md) |
| חישוב ידני למורה | [Teacher-Worked-Example.md](Teacher-Worked-Example.md) |
| מחברת מודרכת — שתי מדידות ואי, seed42 | [Guided-Audited.ipynb](Guided-Audited.ipynb) |
| מעבדת תלמיד — שני מאפיינים אחרים ואי, seed17 | [Student-Fill-Blanks-Audited.ipynb](Student-Fill-Blanks-Audited.ipynb) |
| פתרון מורה למעבדה | [Teacher-Solution-Audited.ipynb](Teacher-Solution-Audited.ipynb) |
| מקור ופרומפט NotebookLM | [NotebookLM-Source.md](NotebookLM-Source.md) · [NotebookLM-Prompt.md](NotebookLM-Prompt.md) |
| בקרת איכות | [Quality-Check.md](Quality-Check.md) |

## שמירת המקור
[Guided-Lesson.ipynb](../Guided-Lesson.ipynb), [Student-Lab.ipynb](../Student-Lab.ipynb), [Teacher-Solution.ipynb](../Teacher-Solution.ipynb) לא שונו. ההדגמה משתמשת ב־bill_length_mm,flipper_length_mm,island והמעבדה ב־bill_depth_mm,flipper_length_mm,island. הנתון המנובא בשתיהן body_mass_g בגרמים.

## תהליך הלמידה
סיפור מחיר מחשב כהנעה, חישוב ידני של MAE=(10+20+30)/3=20, Pipeline מספרי וקטגוריאלי, KFold על Train בלבד, פירוש R² ו־MAE, השוואה ל־DummyRegressor וניתוח מגבלות. MAE אינו אחוז אלא ממוצע שגיאות מוחלטות ביחידות היעד; אין לכוון את המודל בעקבות Test.

**פתוח עד להוכחה:** Run All אמיתי של שלוש המחברות, הגהת מצגות NotebookLM ופיילוט בכיתה. שני האחרונים יבוצעו בסוף המסלול.
