# דוח בדיקות קוד מקומיות — מפגש 17
**2026-10-27 · בדיקות Python על נתונים מייצגים: PASS · Colab Run All: NOT DONE**

## בדיקה שבוצעה בפועל
Python מקומי עם NumPy 2.3.5, Pandas 2.2.3, Scikit-learn 1.8.0:
- מערך DataFrame מדומה בן 8 שורות, 2 שדות מספריים, חסר בשדה אחד, אינדקסים מקוריים לא רציפים, ושתי מחלקות מאוזנות.
- train_test_split(X,y,test_size=.25,random_state=17,stratify=y) יצר חלוקה, שמירת אינדקס X/y.
- ממוצעים נלמדו מ־Train בלבד; StandardScaler עם set_output("pandas") הותאם ל־Train המושלם והמיר Test ללא חסרים.
- KNeighborsClassifier(n_neighbors=3, weights="uniform",metric="euclidean") אומן על Train בלבד וחזה Test.
- comparison עם index=y_test.index שמרה על סדר ואינדקס; correct_count/len(Test) הושווה ל־accuracy_score. במקרה המייצג המדידה הייתה Accuracy=0.5; **זו אינה תוצאת Penguins ואינה מוזכרת במצגת**.
- בדיקות assert עברו עבור אורך וצורת פלט, שמירת אינדקס, היעדר חסרים והסכמה בין שתי דרכי חישוב Accuracy.

## אימות CSV בנפרד
דרך מחבר GitHub אומתו 344×7, 0 חסרים species, 2 חסרים בכל אחת מארבע המדידות המספריות, 11 חסרים sex; SHA b5093336d83d99d8835c606b455d00065ab7cdcf. בדיקה זו אינה Run All של המחברות על הנתונים.

## עדיין פתוח
יש להריץ את שני קובצי ה־ipynb של המורה מתוך GitHub ב־Google Colab ב־Run All ולהשוות את טבלת השגיאות והמדד בפועל. יש לבדוק חזותית איורי SVG, להפיק ולהגיה מצגת NotebookLM, לבחון שקפים מקוריים ולבצע פיילוט בכיתה. עד אז הסטטוס Candidate ולא READY.