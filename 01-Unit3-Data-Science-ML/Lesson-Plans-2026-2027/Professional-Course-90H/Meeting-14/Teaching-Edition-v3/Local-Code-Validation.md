# בדיקות קוד ומתמטיקה מייצגות — מפגש 14
**27.10.2026 • בדיקות מקומיות עברו • עדיין לא Run All מלא ב־Colab**

## בדיקת Python שבוצעה בפועל
הורצה סביבת Python עם Scikit-learn 1.8.0, Pandas 2.2.3, NumPy 2.3.5:
1. OneHotEncoder(handle_unknown="ignore",sparse_output=False) הותאם ל־A,B. transform של B,C החזיר [[0,1],[0,0]].
2. ColumnTransformer על age=[5,15,None],group=[C,D,D],New=(10,E): SimpleImputer(strategy="median") החזיר גיל מושלם [5,15,10]; StandardScaler החזיר ציוני Z [−1.22474487,+1.22474487,0]. ה־One-Hot החזיר ל־group את [1,0],[0,1],[0,1]. התוצאה החדשה היא [0,0,0].
3. get_feature_names_out החזירה בדיוק numeric__age,categorical__group_C,categorical__group_D. צורת טבלת האימון (3,3) ושל החדש (1,3). הקטגוריה E לא הוסיפה עמודה.
4. נתוני Penguins ושמות האיים הוצלבו עם קובץ המקור ב־GitHub. קוד seed17 על קובץ CSV עצמו **טרם הורץ ב־Colab**; אין לטעון שנמדדו מחדש כל תוצאות פיצול האיים באמצעות Python מקומי.

## מה לא נבדק עדיין
לא הורצו כל תאי מחברות GitHub ברצף בממשק Colab, לא הוצגה מצגת NotebookLM מלאה, לא נבדקו מחדש השקפים 7–15 חזותית, ולא נערך ניסוי בכיתה. בדיקות מבנה של SVG אינן בדיקה חזותית של הקרנתם.

## לפני READY
Run All שתי מחברות המורה, בדיקת סדר עמודות והיעדר Fit על Test, ביקורת המחשות ומצגת, פיילוט כיתה, ובקרה מול מפרט רשמי תקף.