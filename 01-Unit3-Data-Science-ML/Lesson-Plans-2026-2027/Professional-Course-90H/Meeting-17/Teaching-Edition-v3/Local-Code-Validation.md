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

## עדכון בקרת עומק — הרצת Penguins אמיתית
ב־27.10.2026 בוצעה גם **הרצת Python של שני מסלולי KNN על קובץ Penguins האמיתי**, שנמצא כעותק מקומי של Datasets/penguins.csv והוזהה ב־Git blob SHA הבדוק b5093336d83d99d8835c606b455d00065ab7cdcf. הבדיקות אינן רק נתונים קטנים מדומים:
- Guided flipper_length_mm/body_mass_g, seed42: ‏258 Train ו־86 Test; **60 נכונות, 26 טעויות, Accuracy=0.6976744186**.
- Student teacher-solution bill_length_mm/bill_depth_mm, seed17: ‏258 Train ו־86 Test; **83 נכונות, 3 טעויות, Accuracy=0.9651162791**.
- שני המסלולים השתמשו ב־Train-only mean imputation, StandardScaler fitted to Train, KNeighborsClassifier(K=3, uniform, euclidean), accuracy_score וחישוב ידני. יישור אינדקסים, היעדר חסרים ושמירת מקור עברו.
- קוד שחזור: [Verify-Real-Penguins.py](Verify-Real-Penguins.py), דוח מלא: [Real-Penguins-Validation-Teacher.md](Real-Penguins-Validation-Teacher.md).
- אלה **לא Run All של קובצי ipynb**, ואסור להסיק עדיפות של מאפיינים מהציונים כי גם ה־seed שונה.