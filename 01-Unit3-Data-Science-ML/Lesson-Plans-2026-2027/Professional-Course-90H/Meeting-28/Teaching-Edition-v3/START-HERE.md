# מפגש 28 — חקר מלא והערכת סוף | Teaching Edition v3

**כיתה י׳ · 90 דקות הוראה ותרגול + 45 דקות פרויקט · Candidate עד CI**

| ערכה | קישור |
|---|---|
| ספר תלמיד | [Student-Book.md](Student-Book.md) |
| מדריך מורה | [Teacher-Guide.md](Teacher-Guide.md) |
| דוגמה ידנית | [Teacher-Worked-Example.md](Teacher-Worked-Example.md) |
| הדגמה מודרכת Titanic, seed42 | [Guided-Audited.ipynb](Guided-Audited.ipynb) |
| מעבדת Titanic עצמאית, seed17 | [Student-Fill-Blanks-Audited.ipynb](Student-Fill-Blanks-Audited.ipynb) |
| פתרון מלא למורה, seed17 | [Teacher-Solution-Audited.ipynb](Teacher-Solution-Audited.ipynb) |
| מקור מצגת | [NotebookLM-Source.md](NotebookLM-Source.md) |
| פרומפט למצגת | [NotebookLM-Prompt.md](NotebookLM-Prompt.md) |
| שער איכות | [Quality-Check.md](Quality-Check.md) |

המקור המקורי נשמר: [Guided-Lesson](../Guided-Lesson.ipynb), [Student-Lab](../Student-Lab.ipynb), [Teacher-Solution](../Teacher-Solution.ipynb). קובץ הנתונים המקורי של Titanic מ־`arielb30/datasets` נוסף לעותק בדיקה מקומי `Datasets/titanic_data.csv` לצורך שחזור ללא רשת, תוך שמירת כתובת המקור במחברות.

## עקרונות
יחידת התצפית נוסע, היעד `Survived`, החיובי 1. במודרכת Age, Fare, Sex, Pclass, ובמעבדה גם SibSp. שומרים 25% Test לפני EDA, מאמנים השלמה וקידוד בתוך Pipeline, מבצעים 5-fold Stratified CV, משווים KNN (K=3,5,9), SVM ליניארי וקו בסיס באותו F1, נועלים בחירה **לפני** Test ומודדים פעם אחת. אין לכוונן לפי Test. חלוקת נוסעים אינה בהכרח הכללה למשפחות שלא נראו באימון.

מצגות NotebookLM ופיילוט ייבדקו בסיום המסלול לבקשת המורה.
