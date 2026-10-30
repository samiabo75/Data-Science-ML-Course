# מפגש 6 — Pandas: מהמערך לטבלה ולחקירה ראשונית
**מהדורת בנייה מחדש 30.10.2026 | מבוססת מקורות השתלמות, לא על פרומפטים ישנים.**
## מקור העבודה
- `2.1 Python for DS.pptx` — 22 שקפים: Iris ותכונות; import/read_csv; head/info/describe; columns; Series/DataFrame; בחירת שורות; תנאים ועוד.
- `Pandas_01.ipynb` — Series/index/DataFrame/loc/iloc/עמודה מחושבת/drop.
- `Pandas_02.ipynb` — מסכות, תנאי משולב, head/info/describe, dropna/fillna.
- `Pandas_03.ipynb` — Diamonds, groupby, מיון, unique/nunique/value_counts. *רובו שייך למפגש המשך*.
- `PandasQ1.ipynb` — משימות עצמאיות של בחירה, יצירה, הסרה וסינון.
- `PandasQ2.ipynb` — משימות חסרים, thresh, חישוב ממוצע, groupby, מיון.
- נתונים: [Penguins מתוך המאגר](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/Datasets/penguins.csv), [קטלוג](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/Datasets/README.md).

## מדוע Penguins
344 תצפיות, מאפיינים קטגוריאליים ומספריים, חסרים אמיתיים, זיקה לפרק EDA ול-KNN. מצגת המורה משתמשת בנתוני הדגמה מומצאים במועדון הרובוטיקה כדי ללמד תחביר; **המעבדות משתמשות ב-Penguins**, ולכן אין חשיפת תשובות. בדוגמאות צמצום יש לציין "נתונים להמחשה" ולא לייחס אותם לתצפיות המאגר.

## סדר הוראה (מצגות קצרות להפקה בנפרד)
1. 6א — גשר List/NumPy → DataFrame, מילון רשימות, יצירת טבלה, טעינת CSV: 10 שקפים.
2. 6ב — head/shape/columns/info, שורה/עמודה/טיפוס וחסרים: 10 שקפים.
3. 6ג — Series מול DataFrame, loc/iloc ובחירת שורות: 10 שקפים.
4. 6ד — מסכה בוליאנית, & וסינון; השוואה ללולאת for: 9 שקפים.
5. 6ה — describe, חישוב ממוצע ידני, isna/count ומבט איכות נתונים: 10 שקפים.
**סה״כ מתוכנן 49 שקפים**, לפני ביקורת ואיחוד. אין צורך למחוק חזרות שהן תיווך מכוון. אין להעלות פתרון מורה ל-NotebookLM.

## תרגול
- `Colab/Workbook-01-Student.ipynb` ו־`...Teacher.ipynb`: קריאה, מבנה, טיפוסים.
- `Colab/Workbook-02-Student.ipynb` ו־`...Teacher.ipynb`: בחירה, loc/iloc, מסכה ותנאי כפול.
- `Colab/Workbook-03-Student.ipynb` ו־`...Teacher.ipynb`: חסרים, ממוצע, unique, value_counts; מעבר לחקר, בלי groupby מורכב.
- `06-Source-Coverage.md`: מיפוי שקפים-מקורות-תרגולים.
## גבולות המפגש
dropna/fillna מורחב, thresh, groupby, מיון מתקדם ו-Diamonds עוברים **למפגש הבא** עם PandasQ2/Pandas_03; אין לטעון שכוסו במלואם.
