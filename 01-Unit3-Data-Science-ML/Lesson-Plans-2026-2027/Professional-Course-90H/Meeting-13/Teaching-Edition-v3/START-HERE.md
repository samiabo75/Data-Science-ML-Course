# יחידה 3 — מפגש 13: StandardScaler ו־MinMaxScaler
**מהדורת עומק v3 · כיתה י׳ · 90 דקות למידה ותרגול + 45 דקות פרויקט**

## סדר העבודה
1. [ספר התלמיד](Student-Book.md) — סיפור מחשבים, נוסחאות מפורקות, חישוב ביד, Python והקשר ל־AI.
2. [מדריך המורה](Teacher-Guide.md) — תכנון דקות, טעויות אופייניות ומדרג סיוע.
3. [פתרון ידני מלא למורה](Teacher-Worked-Example.md).
4. [השוואת שלושה סרגלים](train-test-three-scales.svg), [Fit ו־Transform בלי דליפה](fit-transform-no-leakage.svg), [שני מאפיינים שונים](two-feature-distance.svg).
5. [מחברת הדגמה עם בדיקות](Guided-Audited.ipynb); [מעבדת תלמיד בהשלמות](Student-Fill-Blanks-Audited.ipynb); [פתרון מורה עם assert](Teacher-Solution-Audited.ipynb).
6. [מקור מקצועי ל־NotebookLM](NotebookLM-Source.md), [פרומפט למצגת עד 10 שקפים](NotebookLM-Prompt.md).
7. [Quality-Check.md](Quality-Check.md) ו[דוח בדיקות מקומיות](Local-Code-Validation.md).

## מקורות ההשתלמות — נשמרו ללא שינוי
[מדריך מקור](../Teacher-Guide.md) · [מחברת הדגמה מקורית](../Guided-Lesson.ipynb) · [מעבדת מקור](../Student-Lab.ipynb) · [פתרון מקור](../Teacher-Solution.ipynb) · [מיפוי מצגות](../Presentation-Brief.md).

**ההדגמה אינה פתרון המעבדה:** במורה Train=[10,20,30],Test=[40]; בתלמיד Train=[100,200,300],Test=[50,400]. חובה לחשב את Standard עם **ddof=0**; Fit על Train בלבד. 

**סטטוס Candidate:** מבנה נבדק, דוגמאות מקומיות נבדקו; Run All ב־Colab, הגהת NotebookLM וניסוי בכיתה עדיין נדרשים לפני READY.