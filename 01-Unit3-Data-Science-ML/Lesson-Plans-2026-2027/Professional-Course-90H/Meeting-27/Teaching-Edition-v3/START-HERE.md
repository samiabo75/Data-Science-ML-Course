# מפגש 27 — SVM והשוואת מודלים | Teaching Edition v3

**90 דקות הוראה ותרגול + 45 דקות פרויקט. מעמד Candidate עד תוצאת CI.**

| רכיב | קישור |
|---|---|
| ספר תלמיד | [Student-Book.md](Student-Book.md) |
| מדריך מורה | [Teacher-Guide.md](Teacher-Guide.md) |
| חישוב/דוגמה ידנית | [Teacher-Worked-Example.md](Teacher-Worked-Example.md) |
| מודרכת Audited (4 מאפיינים) | [Guided-Audited.ipynb](Guided-Audited.ipynb) |
| מעבדת תלמיד Audited (2 מאפיינים, 18 השלמות) | [Student-Fill-Blanks-Audited.ipynb](Student-Fill-Blanks-Audited.ipynb) |
| פתרון מורה Audited (2 מאפיינים) | [Teacher-Solution-Audited.ipynb](Teacher-Solution-Audited.ipynb) |
| חומרי NotebookLM | [NotebookLM-Source.md](NotebookLM-Source.md) · [NotebookLM-Prompt.md](NotebookLM-Prompt.md) |
| בקרת איכות | [Quality-Check.md](Quality-Check.md) |

## רצף למידה
סיפור גבולות החלטה ושוליים, הסבר SVM לעומת פרספטרון, משמעות `C`, חישוב סימן ציון החלטה סינתטי, Pipeline (SimpleImputer → StandardScaler → SVC ליניארי), מטריצת בלבול והפרדה ברורה בין `decision_function` להסתברות. **אין לייחס 0.7 ל־70%**.

מחברות המקור המקבילות נשמרו: [Guided-Lesson](../Guided-Lesson.ipynb), [Student-Lab](../Student-Lab.ipynb), [Teacher-Solution](../Teacher-Solution.ipynb). בדוגמת המורה 4 מאפיינים והחלוקה seed42, במעבדה 2 מאפיינים והחלוקה seed17. C=1 ו־kernel ליניארי נקבעו מראש; אין להשתמש ב־Test לבחירתם.

בקרת מצגות NotebookLM ופיילוט כיתה נדחים לסיום המסלול לבקשת המורה.
