# מקור NotebookLM — מפגש 23 GridSearchCV
**8–10 שקפים, רקע בהיר, עברית RTL, קוד ונוסחאות LTR**

## סיפור
דודו משווה שלושה ערכי K, באותו מדד ובאותם קיפולי אימות. אינו מציץ בתוצאות Test כדי לבחור.

## נתוני ההמחשה המותרים
שלושה ערכי K: 3,5,9. חמישה קיפולים. 3×5=15 התאמות חיפוש ועוד 1 `refit`. ציוני קיפול *מומצאים* עבור מועמד יחיד [0.80,0.85,0.75,0.90,0.70], ממוצע 0.80. אינם תוצאות Penguins.

## מונחים וחומר מקצועי
`param_grid`, שם שלב `knn`, הפרמטר `knn__n_neighbors`, `GridSearchCV`, `cv_results_`, `mean_test_score` כאימות פנימי, `best_params_`, `best_score_`, `refit=True`. ColumnTransformer מספרי עם median ו־StandardScaler, קטגוריאלי island עם most_frequent ו־OneHotEncoder. הכול בתוך Pipeline. השוואת DummyClassifier לפי אותו macro-F1; Test פעם אחת בסוף.

## רצף 9 שקפים
1. סיפור פתיחה: למה השוואה הוגנת דורשת אותו מבחן.
2. בחירת מועמדים ומדד מראש.
3. מטריצת התאמות 3×5, חישוב 15.
4. הממוצע של חמישה ציונים מומצאים.
5. Pipeline/ColumnTransformer והכנת נתונים בתוך CV.
6. שדה `knn__n_neighbors` והגדרת החיפוש.
7. עמודות `cv_results_` ופירושן, בלי ציוני Penguins.
8. `best_params_`, `refit`, הבחנה בין CV ל־Test.
9. כרטיס יציאה, השוואה ל־Baseline וקישור לפרויקט.

השתמשו ב־`grid-search-3x5.svg` וב־`gridsearch-pipeline-flow.svg`. אין לחשוף את K של מעבדת התלמיד, אין להמציא תוצאות Penguins ואין להפוך prompt למצגת "מאושרת".
