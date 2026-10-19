# מקור למצגת — שיעור 24 — KNN על Penguins: מהכנת נתונים לתחזית ולהערכה
**קהל:** תלמידי כיתה י׳ מתחילים. **מכסה:** 3 שעות לימוד (135 דקות), כולל תרגול; המצגת מחליפה חלק מההסבר ואינה מוסיפה זמן.
**שלב בתהליך החקר:** אימון וחיזוי.
**פתיחה מוכרת:** כדי לנחש סוג מוצר חדש צריך מאפיינים; את התשובה מסתירים מהמודל.
**גבולות הליבה במצגת ובתרגול:** מודל KNN על זוג מדידות אחר, fit/predict, Accuracy וטעות אחת; K נקבע מראש.
**המחשה חזותית מומלצת:** תהליך הכנה→fit עםX_train,y_train→predict עםX_test בלבד→השוואה לאמת. הציגו טעות אחת ו־Accuracy כמניה, לא כבטחון לכל תחזית.
**זיקה להמשך:** הזיקה המרכזית היא לבסיס וקטורי, סטטיסטי או להערכת מודלים; השתמשו רק בזיקה המפורשת בחומר, כקדימות להמשך ולא כהוראת יחידה 5 מלאה.

## הוראות למניעת ערבוב דוגמה ותרגול
חלק א הוא דוגמה פתורה שאפשר להסביר ולפתור בשקפים. חלק ב הוא תרגול עצמאי: מציגים את הדרישה, מפרקים לשלבים ונותנים רמזים; אין מייצרים פתרון מלא,קוד מלא או תוצאות סופיות של המשימות הנבחרות. אין בקובץ פתרוןמתועד לתרגול. חומר עודף במחברות מיועד לחזרה; גבולותהליבה לעיל גוברים על שאיפה לכסותכל תא.
דוגמאות מומצאות אינן מאגר אמיתי. קישורים הם ייחוס; אין להניח שתוכנם נכלל אוטומטית במקור שהועלה. לא להמציא פלט,דיוק או גרף מאומת כשהם אינם מופיעים בטקסט.

## חלק א — הסבר ודוגמה פתורה
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 24 — KNN על Penguins: מהכנת נתונים לתחזית ולהערכה

**הקשר:** תחנת מחקר רוצה להציע זיהוי מין פינגווין מתוך שתי מדידות. זהו תרגיל סיווג לימודי; אין כאן מערכת מאושרת לשימוש בשטח. המטרה היא לחזות species, לא לנבא מסה.

נגדיר מראש K=3, משקל שווה לשכנים ומרחק אוקלידי. K זה נבחר לצורך הלמידה, ואינו מוכרז כמיטבי. לא נשנה אותו על סמך Test.

עוגנים: [סיכום מפגש 5](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/07-KNN/Meeting-05-Didactic-Summary.md), [הכנת נתונים — מפגש 7](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/10-Data-Preparation/Meeting-07-Didactic-Summary.md). זוהי התאמה כיתתית חדשה של החומרים, ולא העתק של תרגיל מקור חסר.

## למה לומדים את זה עכשיו?
כדי לנחש סוג מוצר חדש צריך מאפיינים; את התשובה מסתירים מהמודל.
**בתהליך הפרויקט:** אימון וחיזוי.
**מסגרת פעילה:** 3 שעות לימוד — 135 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.

## לפני הקוד
בשיעור הקודם חישבנו מרחק והצבענו. כאן הספרייה עושה זאת עבורנו.
כתבו: מהי שורה? מהם שני מאפיינים? מה היעד? האם Id או species צריכים להיכלל ב־X?

הנתונים הם עותק Penguins במאגר הקורס: 344 רשומות, 7 עמודות. מקור המחקר: Kristen Gorman ו־Palmer Station LTER; תיעוד וייחוס: [palmerpenguins](https://github.com/allisonhorst/palmerpenguins). העותק אינו זהה לכל גרסה אחרת. נתונים אלה משמשים ללמידה; התאמה לפרויקט גמר דורשת בדיקה נפרדת.

### תא קוד 4
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

url = "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df = pd.read_csv(url)
display(df.head())
display(df.isna().sum())
```

## 1. מפרידים קלט ויעד ומחלקים יחד
המאפיינים: אורך סנפיר במ״מ ומסה בגרמים. היעד טקסטואלי; KNN ב־sklearn מקבל תוויות טקסט ואין צורך ב־One-Hot ל־y.
שורה ללא יעד לא יכולה לשמש בדיקה מפוקחת. בעותק הנוכחי אין חסרים ב־species, ולכן הסינון אינו מסיר שורות.
stratify שומר בקירוב על יחסי המינים; random_state מאפשר שחזור, ואינו מבטיח חלוקה טובה מכל חלוקה אחרת.

### תא קוד 6
```python
model_df = df.dropna(subset=["species"]).copy()
features = ["flipper_length_mm","body_mass_g"]
X = model_df[features].copy()
y = model_df["species"].copy()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
print("Train:", len(X_train), "Test:", len(X_test))
```

## 2. חוזרים על הכנה מוכרת
קודם מחלקים, ואז מחשבים ממוצעי השלמה ומדדי תקנון **רק מאימון**. ל־Test מפעילים אותם פרמטרים.
לא כל מדידה מתחילה באותו קנה מידה: גרמים יכולים לשלוט במרחק על פני מ״מ. לאחר התקנון, כל מאפיין נמדד בסטיות תקן לפי האימון. זו בחירה למודל, לא הוכחת נורמליות.
עצירה: היכן מחושב מידע מהנתונים? מדוע אין כאן fit על Test?

### תא קוד 8
```python
training_means = X_train.mean()
X_train_ready = X_train.fillna(training_means)
X_test_ready = X_test.fillna(training_means)

scaler = StandardScaler().set_output(transform="pandas")
scaler.fit(X_train_ready)
X_train_scaled = scaler.transform(X_train_ready)
X_test_scaled = scaler.transform(X_test_ready)
display(X_train_scaled.head())
```

## 3. fit לעומת predict
fit מקבל מדידות ותוויות אימון. ב־KNN הוא שומר את דוגמאות האימון הדרושות לחיפוש שכנים; הוא אינו לומד קו מפריד כמו רגרסיה.
predict מקבל מדידות בלבד ומחזיר תחזית לכל שורה באותו סדר. y_test אינו משתתף ביצירת התחזיות.
כל שכן מצביע קול אחד. המרחק מחושב בין המדידות המתוקננות.

### תא קוד 10
```python
model = KNeighborsClassifier(n_neighbors=3, weights="uniform", metric="euclidean")
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)
print(predictions[:5])
```

## 4. השוואה ליעד שנשמר בצד
רק עכשיו משתמשים ב־y_test. האינדקס המקורי נשמר כדי לחבר כל תחזית לרשומה המתאימה; המערך predictions מסודר כמו X_test.

$$Accuracy=\frac{\text{מספר תחזיות נכונות}}{\text{מספר רשומות הבדיקה}}$$

לדוגמה מומצאת: 8 נכונות מתוך 10 נותנות 0.8, כלומר 80%. זה אינו הפלט הצפוי של Penguins.
לפני הרצה: הסבירו מה ההבדל בין תווית חזויה לבין ציון המודל.

### תא קוד 12
```python
comparison = pd.DataFrame(
    {"actual": y_test, "predicted": predictions}, index=y_test.index
)
comparison["correct"] = comparison["actual"] == comparison["predicted"]
display(comparison.head(10))
correct_count = comparison["correct"].sum()
accuracy = accuracy_score(y_test, predictions)
print("Correct:", correct_count, "out of", len(y_test))
print("Accuracy:", accuracy, "Percent:", 100 * accuracy)
```

## 5. מבינים טעויות ומגבלות
ספרו טעויות וקראו עד שלוש דוגמאות. אם הטבלה ריקה, כתבו שלא נמצאו טעויות בחלוקה הזאת; אין לייצר שגיאות מלאכותיות.
Accuracy מסכם התאמה על חלוקה אחת. הוא אינו הסתברות שהתחזית המסוימת נכונה ואינו מבטיח ביצועים על אתר או אוכלוסייה אחרים.
איזה מין הוחלף באיזה מין? האם מחיר הטעות זהה לכל המינים? נלמד בהמשך מדדים לפי מחלקה.

### תא קוד 14
```python
errors = comparison[comparison["correct"] == False]
print("Errors:", len(errors))
display(errors.head(10))
```

## כרטיס מודל לפרויקט
תעדו שאלה, יחידת תצפית, מקור, X ו־y, חלוקה, טיפול בחסרים, תקנון, K, מדד, דוגמת טעות ומגבלה.
אין להוסיף species למאפיינים, להשלים לפי כל המאגר, או לבחור K לפי Test. בחירת פרמטרים באימות בתוך האימון תילמד בהמשך, עם הכנה בכל קיפול.
**כרטיס יציאה:** הסבירו ללא קוד מה fit מקבל, מה predict מקבל, ומה צריך לדעת כדי לחשב Accuracy.


---

## חלק ב — תרגול תלמיד ללא פתרון
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 24 — KNN על Penguins: תרגול עצמאי

**הקשר:** תחנת מחקר רוצה להציע זיהוי מין פינגווין מתוך שתי מדידות. זהו תרגיל סיווג לימודי; אין כאן מערכת מאושרת לשימוש בשטח. המטרה היא לחזות species, לא לנבא מסה.

נגדיר מראש K=3, משקל שווה לשכנים ומרחק אוקלידי. K זה נבחר לצורך הלמידה, ואינו מוכרז כמיטבי. לא נשנה אותו על סמך Test.

עוגנים: [סיכום מפגש 5](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/07-KNN/Meeting-05-Didactic-Summary.md), [הכנת נתונים — מפגש 7](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/10-Data-Preparation/Meeting-07-Didactic-Summary.md). זוהי התאמה כיתתית חדשה של החומרים, ולא העתק של תרגיל מקור חסר.

## למה לומדים את זה עכשיו?
כדי לנחש סוג מוצר חדש צריך מאפיינים; את התשובה מסתירים מהמודל.
**בתהליך הפרויקט:** אימון וחיזוי.
**מסגרת פעילה:** 3 שעות לימוד — 135 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.
**התרגול הנבחר למסגרת זו:** מודל KNN על זוג מדידות אחר, fit/predict, Accuracy וטעות אחת; K נקבע מראש.

עבדו לפי הסדר. זמן מוצע לתרגול: 25 דקות ועוד השלמה לפי הצורך. תאי הקוד ריקים בכוונה; אפשר להיעזר במחברת המודרכת. משנים את המאפיינים ואת seed, ושומרים על אותו תהליך. אין תוצאה מספרית שנדרשת מראש.

### תא קוד 4
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

url = "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df = pd.read_csv(url)
display(df.head())
display(df.isna().sum())
```

## 1. קלט, יעד וחלוקה
בחרו bill_length_mm ו־bill_depth_mm בלבד, ו־species כיעד. הסירו רק שורות ללא יעד בעותק עבודה. חלקו יחד, test_size=0.25, random_state=17, stratify=y. לפני ההרצה הסבירו מדוע היעד אינו מאפיין.

### תא קוד 6
```python
# כתבו כאן את הפתרון
```

**תיעוד תלמיד:** כתבו כאן את ההסבר והמסקנה.

## 2. הכנה ללא זליגה
חשבו ממוצעים מאימון והשלימו בשתי הקבוצות לפיהם. התאימו StandardScaler לאימון המושלם בלבד והמירו את שתי הקבוצות. הסבירו מדוע אין fit נוסף לבדיקה.

### תא קוד 9
```python
# כתבו כאן את הפתרון
```

**תיעוד תלמיד:** כתבו כאן את ההסבר והמסקנה.

## 3. אימון ותחזית
הגדירו מראש K=3, weights='uniform', metric='euclidean'. הפעילו fit על האימון המתוקנן והתוויות, ו־predict על הבדיקה המתוקננת. ודאו שמספר התחזיות שווה למספר רשומות הבדיקה.

### תא קוד 12
```python
# כתבו כאן את הפתרון
```

**תיעוד תלמיד:** כתבו כאן את ההסבר והמסקנה.

## 4. הערכה
צרו comparison עם actual ו־predicted ובאינדקס y_test. הוסיפו correct, ספרו נכונות וחשבו Accuracy ביד וב־accuracy_score. דווחו שבר, יחס ואחוז.

### תא קוד 15
```python
# כתבו כאן את הפתרון
```

**תיעוד תלמיד:** כתבו כאן את ההסבר והמסקנה.

## 5. ניתוח טעויות
סננו שגיאות והשוו actual ל־predicted בעד שלוש רשומות. אם אין טעויות, ציינו זאת. כתבו מגבלה אחת של החלוקה ואחת של המדד. אין לכוון K לפי התוצאות.

### תא קוד 18
```python
# כתבו כאן את הפתרון
```

**תיעוד תלמיד:** כתבו כאן את ההסבר והמסקנה.

## 6. תיעוד
כתבו כרטיס מודל לפרויקט ופסקה המסבירה את ההבדל בין fit, predict והערכה. אין להשוות ציון זה לציון המחברת המודרכת כהוכחה שמאפיינים מסוימים טובים יותר: גם החלוקה שונה.

### תא קוד 21
```python
# כתבו כאן את הפתרון
```

**תיעוד תלמיד:** כתבו כאן את ההסבר והמסקנה.

