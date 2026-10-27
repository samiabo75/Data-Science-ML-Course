# מדריך מורה — מפגש 23 GridSearchCV
**90 דקות הוראה ותרגול + 45 דקות פרויקט**

## מקור וגבולות
מקורות: מחברות Guided/Student/Teacher המקוריות ומפת המצגת `יישום מכונה לומדת.pptx`, שקפים 26–30 (מיפוי מקור; הגהה חזותית פתוחה). **המורה משתמש ב־bill_length_mm/bill_depth_mm/island ו־seed42; התלמיד ב־flipper_length_mm/body_mass_g/island ו־seed17.** בכל המסלולים `[3,5,9]`, CV חמישה קיפולים `random_state=42`, המדד `f1_macro`, Test רבע מהנתונים, `refit=True`, השלמת חציון/שכיח ותקנון/OneHot בתוך Pipeline.

## מטרות
להסביר 3×5=15, לחבר `knn__n_neighbors` לשם שלב הצינור, לקרוא `cv_results_`, להבחין בין `mean_test_score` לבין Test חיצוני, לנמק `best_params_`, ולהעריך מודל נבחר וקו בסיס רק לאחר קיבוע הבחירה.

| זמן | תוכן | עדות |
|---|---|---|
| 0–10 | סיפור תחרות הוגנת של מודלים | שתי הצעות לבחירה מראש |
| 10–25 | חישוב התאמות: 3×5 ועוד refit | 15 ו־16, בלי להתבלבל עם תצפיות |
| 25–40 | Pipeline/ColumnTransformer ותכונות מעורבות | הסבר מניעת זליגה |
| 40–55 | `param_grid` וקריאת `cv_results_` | הבדל CV מול Test |
| 55–80 | מעבדת תלמיד מודרכת־עצמאית על Penguins | טבלה וקוד |
| 80–90 | כרטיס יציאה | `best_params_` לעומת Scaler |
| 90–135 | 45 דקות פרויקט | כרטיס ניסוי והשוואת Baseline |

## עצירות סוקרטיות
למה בחרנו K לפני Test? האם השלמת חציון מחושבת מחדש בכל קיפול? האם `best_score_` הוא ציון מבחן סופי? אם `rank_test_score` הוא 1, האם המודל בהכרח טוב יותר באוכלוסייה? כיצד נעדיף מודל מול DummyClassifier בשיקול עסקי?

## טעויות ותיקונים
לא לקודד island כ־0,1,2 עבור מדדי מרחק; לא להריץ `ColumnTransformer.fit` לפני CV; לא לבחור לפי Train; אין לבלבל בין `test_score` של CV ל־Outer Test; `std_test_score` אינו רווח סמך; אין להבטיח שה־K הנבחר יהיה 3/5/9 מסוים מראש; אין ללמוד מה־Test לאחר חשיפתו.

## התאמות וכרטיס יציאה
מתקשים: טבלת 3×5 וריבועים; רמת ביניים: בניית חיפוש וקריאת תוצאה; מתקדמים: שוויון בין מועמדים ושאלת השפעת המדד. כרטיס יציאה: ״מה ההבדל בין פרמטר שנלמד ב־Scaler לבין היפר־פרמטר שנבחר בחיפוש?״

## כלים
[Colab](https://colab.research.google.com), [NotebookLM](https://notebooklm.google.com), [GridSearchCV — תיעוד](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html), [Pipeline](https://scikit-learn.org/stable/modules/compose.html).

**Candidate:** בדיקות Colab, מצגת ופיילוט עדיין פתוחים.
