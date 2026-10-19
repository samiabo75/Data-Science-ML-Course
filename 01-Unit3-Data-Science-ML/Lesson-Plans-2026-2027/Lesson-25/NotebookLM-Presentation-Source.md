# מקור למצגת — שיעור 25 — מטריצת בלבול: מי סווג כמי?
**קהל:** תלמידי כיתה י׳ מתחילים. **מכסה:** 2 שעות לימוד (90 דקות), כולל תרגול; המצגת מחליפה חלק מההסבר ואינה מוסיפה זמן.
**שלב בתהליך החקר:** הערכה.
**פתיחה מוכרת:** סינון הודעות זבל עלול להחמיץ זבל או לחסום הודעה חשובה: אלה טעויות שונות.
**גבולות הליבה במצגת ובתרגול:** מטריצה ידנית עם חיובי מוגדר ואימות בספרייה; פירוש טעות בנתונים אמיתיים.
**המחשה חזותית מומלצת:** מטריצת2×2: שורות אמת ועמודות חיזוי. הגדירו חיובי לפני TP/FP/FN/TN; המחישו את שני סוגי הטעות בסיפור מוכר.
**זיקה להמשך:** הזיקה המרכזית היא לבסיס וקטורי, סטטיסטי או להערכת מודלים; השתמשו רק בזיקה המפורשת בחומר, כקדימות להמשך ולא כהוראת יחידה 5 מלאה.

## הוראות למניעת ערבוב דוגמה ותרגול
חלק א הוא דוגמה פתורה שאפשר להסביר ולפתור בשקפים. חלק ב הוא תרגול עצמאי: מציגים את הדרישה, מפרקים לשלבים ונותנים רמזים; אין מייצרים פתרון מלא,קוד מלא או תוצאות סופיות של המשימות הנבחרות. אין בקובץ פתרוןמתועד לתרגול. חומר עודף במחברות מיועד לחזרה; גבולותהליבה לעיל גוברים על שאיפה לכסותכל תא.
דוגמאות מומצאות אינן מאגר אמיתי. קישורים הם ייחוס; אין להניח שתוכנם נכלל אוטומטית במקור שהועלה. לא להמציא פלט,דיוק או גרף מאומת כשהם אינם מופיעים בטקסט.

## חלק א — הסבר ודוגמה פתורה
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 25 — מטריצת בלבול: מי סווג כמי?

**פתיחה:** דודו בודק מסווג שמסמן מוצרים פגומים. האם מספר התחזיות הנכונות לבדו מגלה כמה פגומים הוחמצו וכמה מוצרים תקינים נשלחו לבדיקה מיותרת?
נלמד לארגן זוגות אמת וחיזוי לטבלת ספירות. אחר כך נקרא את אותה טבלה עבור שלושת מיני Penguins, בלי לשנות את המודל.

עוגן: [סיכום מפגש השתלמות 6](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/08-Classification-Metrics/Meeting-06-Didactic-Summary.md) ו[המחברת המודרכת](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/08-Classification-Metrics/Meeting-06-Classification-Metrics-Guided.ipynb). זוהי התאמה דידקטית חדשה: דוגמת מוצרים מומצאת והמשך Penguins, במקום דוגמאות הבריאות והחתולים. המקורות נשמרו; אין כאן שחזור תרגיל מקור.

## למה לומדים את זה עכשיו?
סינון הודעות זבל עלול להחמיץ זבל או לחסום הודעה חשובה: אלה טעויות שונות.
**בתהליך הפרויקט:** הערכה.
**מסגרת פעילה:** 2 שעות לימוד — 90 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.

## 1. לפני הספרייה — סופרים זוגות
הנתונים הבאים מומצאים. ציירו ביד טבלה בת שתי שורות ושתי עמודות וספרו כל זוג. הסבירו שתי טעויות שונות במילים.

### תא קוד 4
```python
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt
```

### תא קוד 5
```python
# נתונים מומצאים לצורך למידה; אין CSV או מודל מאומן בדוגמה הזאת
actual = ["OK", "OK", "OK", "OK", "Defect", "Defect", "Defect", "Defect"]
predicted = ["OK", "OK", "Defect", "OK", "OK", "OK", "Defect", "Defect"]
pairs = pd.DataFrame({"actual": actual, "predicted": predicted})
display(pairs)
```

## מוסכמה שחייבים לקרוא
**שורות = אמת (Actual), עמודות = חיזוי (Predicted)**. במטריצת ספירות כל רשומה נספרת בתא אחד. סכום השורה מספר כמה רשומות אמיתיות יש במחלקה; סכום העמודה מספר כמה חיזויים ניתנו למחלקה.
labels קובע במפורש את סדר המחלקות בשני הצירים. אין לקבוע את משמעות התאים לפי מיקום בלבד ללא קריאת תוויות. הסדר כאן מתחיל בשלילי OK; בחומר אחר החיובי עשוי להופיע ראשון.
האלכסון מכיל סיווגים נכונים; מחוץ לאלכסון נמצאות טעויות. הצבע מייצג ספירה, לא רמת ביטחון.

### תא קוד 7
```python
labels_binary = ["OK", "Defect"]
cm_binary = confusion_matrix(actual, predicted, labels=labels_binary)
table_binary = pd.DataFrame(
    cm_binary, index=labels_binary, columns=labels_binary
)
table_binary.index.name = "Actual"
table_binary.columns.name = "Predicted"
display(table_binary)
```

## ארבע תוצאות — לאחר שמגדירים חיובי
המחלקה החיובית היא **Defect**, כלומר "דורש טיפול". חיובי אינו אומר "טוב".
| אמת | חיזוי | שם | משמעות |
|---|---|---|---|
| OK | OK | TN | תקין שזוהה כתקין |
| OK | Defect | FP | אזעקת שווא |
| Defect | OK | FN | פגם שהוחמץ |
| Defect | Defect | TP | פגם שזוהה |

חשבו קודם מתוך הזוגות, ואז השוו לקוד. loc הוא קיצור קריאה לפי תווית שורה ותווית עמודה: table.loc[אמת, חיזוי]. הוא מובא כאן לקריאת תאים; אפשר לחשב גם ביד.
$$Accuracy=\frac{TN+TP}{N}$$
N הוא סכום כל תאי המטריצה. אין לחשב ממוצע פשוט של אחוז ההצלחה בכל שורה ולקרוא לו Accuracy.

### תא קוד 9
```python
tn = table_binary.loc["OK", "OK"]
fp = table_binary.loc["OK", "Defect"]
fn = table_binary.loc["Defect", "OK"]
tp = table_binary.loc["Defect", "Defect"]
n = cm_binary.sum()
accuracy_from_matrix = (tn + tp) / n
print("TN:", tn, "FP:", fp, "FN:", fn, "TP:", tp)
print("Total:", n, "Accuracy:", accuracy_from_matrix)
print("Accuracy from pairs:", accuracy_score(actual, predicted))
```

**פירוש:** יש 5 הצלחות מתוך 8, כלומר 62.5%. שני פגמים הוחמצו ומוצר תקין אחד סומן כפגום. ציון אחד מאחד טעויות שיש להן משמעות שונה.
אם נגדיר חיובי כ־OK, שמות ארבעת המצבים ישתנו; זוגות האמת והחיזוי וה־Accuracy לא ישתנו.

## ממשיכים את אותו מודל משיעור 24
התא הבא הוא **קוד הכנה נתון שכבר נלמד**, להרצה מלמעלה; אין צורך לכתוב אותו מחדש בשיעור זה.
הוא משחזר בדיוק את המודרכת: סנפיר ומסה, חלוקה 25%, seed=42, stratify, השלמה ותקנון מאימון בלבד ו־K=3 קבוע. כעת מוסיפים דרך תיאור לתחזיות שכבר התקבלו; לא בוחרים פרמטרים לפי Test.
Penguins: עותק הקורס בן 344 שורות ו־7 עמודות. מקור: Kristen Gorman ו־Palmer Station LTER; ייחוס ותיעוד [palmerpenguins](https://github.com/allisonhorst/palmerpenguins), Horst, Hill & Gorman (2020), DOI:10.5281/zenodo.3960218. התאמה לפרויקט גמר טעונה בדיקה נפרדת.

### תא קוד 12
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

model_df = df.dropna(subset=["species"]).copy()
features = ["flipper_length_mm","body_mass_g"]
X = model_df[features].copy()
y = model_df["species"].copy()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
print("Train:", len(X_train), "Test:", len(X_test))

training_means = X_train.mean()
X_train_ready = X_train.fillna(training_means)
X_test_ready = X_test.fillna(training_means)

scaler = StandardScaler().set_output(transform="pandas")
scaler.fit(X_train_ready)
X_train_scaled = scaler.transform(X_train_ready)
X_test_scaled = scaler.transform(X_test_ready)
display(X_train_scaled.head())

model = KNeighborsClassifier(n_neighbors=3, weights="uniform", metric="euclidean")
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)
print(predictions[:5])

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

## 2. משלוש מחלקות לטבלה
כל מין מקבל שורה ועמודה. אין "חיובי" יחיד בלי לבחור מחלקת מטרה מול כל היתר. היום נקרא תאים, סכומי שורות ואלכסון; מדדים לכל מחלקה בשיעור הבא.
לפני הרצה: מה מבטא התא בשורת Chinstrap ובעמודת Adelie? האם התא ההפוך אומר אותו דבר?

### תא קוד 14
```python
labels_species = ["Adelie", "Chinstrap", "Gentoo"]
cm_species = confusion_matrix(y_test, predictions, labels=labels_species)
table_species = pd.DataFrame(
    cm_species, index=labels_species, columns=labels_species
)
table_species.index.name = "Actual"
table_species.columns.name = "Predicted"
display(table_species)

# אלכסון ראשי: החיזוי זהה לאמת
correct_from_matrix = (
    table_species.loc["Adelie", "Adelie"]
    + table_species.loc["Chinstrap", "Chinstrap"]
    + table_species.loc["Gentoo", "Gentoo"]
)
print("N:", cm_species.sum())
print("Accuracy from diagonal:", correct_from_matrix / cm_species.sum())
print("Actual Chinstrap:", table_species.loc["Chinstrap"].sum())
print("Predicted Chinstrap:", table_species["Chinstrap"].sum())
print("Actual Chinstrap predicted Adelie:", table_species.loc["Chinstrap", "Adelie"])

chart = ConfusionMatrixDisplay(
    confusion_matrix=cm_species, display_labels=labels_species
)
chart.plot(cmap="Blues", values_format="d", colorbar=False)
plt.title("Penguins — fixed K=3; test split from lesson 24")
plt.tight_layout()
plt.show()
```

## 3. תיעוד לפרויקט וכרטיס יציאה
בחרו תא שגיאה שאינו אפס ותארו: כמה דוגמאות ממין אמת מסוים סווגו כמין אחר? אם אין טעויות, ציינו זאת.
דווחו את סדר התוויות, משמעות הצירים, מספר הנבדקים וסכום האלכסון. סכום כל התאים צריך להתאים למספר זוגות הבדיקה.
המטריצה מתארת את החלוקה המסוימת; אי אפשר להכריז ממנה לבדה על התאמה לאוכלוסייה חדשה. גם ספירה קטנה של טעויות במחלקה נדירה אינה מוכיחה ביצוע טוב ללא ידיעת גודלה.
**כרטיס יציאה:** מה ההבדל בין סכום שורת Chinstrap לסכום עמודת Chinstrap? איזו טעות היא FN כאשר החיובי הוא מוצר פגום?


---

## חלק ב — תרגול תלמיד ללא פתרון
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 25 — מטריצת בלבול: תרגול עצמאי

**פתיחה:** דודו בודק מסווג שמסמן מוצרים פגומים. האם מספר התחזיות הנכונות לבדו מגלה כמה פגומים הוחמצו וכמה מוצרים תקינים נשלחו לבדיקה מיותרת?
נלמד לארגן זוגות אמת וחיזוי לטבלת ספירות. אחר כך נקרא את אותה טבלה עבור שלושת מיני Penguins, בלי לשנות את המודל.

עוגן: [סיכום מפגש השתלמות 6](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/08-Classification-Metrics/Meeting-06-Didactic-Summary.md) ו[המחברת המודרכת](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/08-Classification-Metrics/Meeting-06-Classification-Metrics-Guided.ipynb). זוהי התאמה דידקטית חדשה: דוגמת מוצרים מומצאת והמשך Penguins, במקום דוגמאות הבריאות והחתולים. המקורות נשמרו; אין כאן שחזור תרגיל מקור.

## למה לומדים את זה עכשיו?
סינון הודעות זבל עלול להחמיץ זבל או לחסום הודעה חשובה: אלה טעויות שונות.
**בתהליך הפרויקט:** הערכה.
**מסגרת פעילה:** 2 שעות לימוד — 90 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.
**התרגול הנבחר למסגרת זו:** מטריצה ידנית עם חיובי מוגדר ואימות בספרייה; פירוש טעות בנתונים אמיתיים.

התרגול בודק קריאת ספירות והסבר. תאי המשימה ריקים בכוונה. קוד ההכנה הוא חומר שכבר נלמד ואינו פתרון למטריצות.

### תא קוד 4
```python
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt
```

### תא קוד 5
```python
# דוגמה דידקטית מומצאת — מסווג קבוע שאינו מאומן
actual = ["OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK", "Defect", "Defect"]
predicted = ["OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK"]
pairs = pd.DataFrame({"actual": actual, "predicted": predicted})
display(pairs)
```

## 1. מטריצה ידנית
בנו על נייר מטריצת ספירות בסדר OK, Defect. כתבו כותרת לכל ציר וספרו כל זוג בדיוק פעם אחת. מה סכום התאים?

### תא קוד 7
```python
# כתבו כאן את הקוד שלכם
```

**תשובה והסבר:** כתבו כאן.

## 2. אימות בקוד
הפעילו confusion_matrix עם labels מפורש והציגו DataFrame מתויג כמו במודרכת. בדקו מול הטבלה הידנית. אין צורך ליצור תרשים לדוגמה הבינרית.

### תא קוד 10
```python
# כתבו כאן את הקוד שלכם
```

**תשובה והסבר:** כתבו כאן.

## 3. פירוש ואחוז הצלחה
הגדירו Defect כחיובי. זהו TN, FP, FN, TP, חשבו Accuracy מהאלכסון והשוו ל־accuracy_score. הסבירו מדוע המסווג עלול להיות לא שימושי לזיהוי פגמים למרות הציון.

### תא קוד 13
```python
# כתבו כאן את הקוד שלכם
```

**תשובה והסבר:** כתבו כאן.

## 4. חזרה ל־Penguins
הריצו את קוד ההכנה הנתון להלן. צרו מטריצה מתויגת בסדר Adelie, Chinstrap, Gentoo ותרשים ספירות. הראו שסכום התאים שווה למספר דוגמאות הבדיקה ושסכום האלכסון מתאים למספר ההצלחות. אין לשנות K, מאפיינים או חלוקה.

## ממשיכים את אותו מודל משיעור 24
התא הבא הוא **קוד הכנה נתון שכבר נלמד**, להרצה מלמעלה; אין צורך לכתוב אותו מחדש בשיעור זה.
הוא משחזר בדיוק את המודרכת: סנפיר ומסה, חלוקה 25%, seed=42, stratify, השלמה ותקנון מאימון בלבד ו־K=3 קבוע. כעת מוסיפים דרך תיאור לתחזיות שכבר התקבלו; לא בוחרים פרמטרים לפי Test.
Penguins: עותק הקורס בן 344 שורות ו־7 עמודות. מקור: Kristen Gorman ו־Palmer Station LTER; ייחוס ותיעוד [palmerpenguins](https://github.com/allisonhorst/palmerpenguins), Horst, Hill & Gorman (2020), DOI:10.5281/zenodo.3960218. התאמה לפרויקט גמר טעונה בדיקה נפרדת.

### תא קוד 17
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

model_df = df.dropna(subset=["species"]).copy()
features = ["flipper_length_mm","body_mass_g"]
X = model_df[features].copy()
y = model_df["species"].copy()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
print("Train:", len(X_train), "Test:", len(X_test))

training_means = X_train.mean()
X_train_ready = X_train.fillna(training_means)
X_test_ready = X_test.fillna(training_means)

scaler = StandardScaler().set_output(transform="pandas")
scaler.fit(X_train_ready)
X_train_scaled = scaler.transform(X_train_ready)
X_test_scaled = scaler.transform(X_test_ready)
display(X_train_scaled.head())

model = KNeighborsClassifier(n_neighbors=3, weights="uniform", metric="euclidean")
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)
print(predictions[:5])

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

### תא קוד 18
```python
# כתבו כאן את הקוד שלכם
```

**תשובה והסבר:** כתבו כאן.

## 5. כרטיס הערכה
פרשו תא שגיאה אחד וסכום שורה אחת מהנתונים האמיתיים. הסבירו מה מבטא סכום העמודה של אותו מין. כתבו מגבלה אחת והסבירו מדוע שם המחלקה החיובית חיוני לפירוש FN. אין צורך לחשב עדיין Precision, Recall או F1.

### תא קוד 21
```python
# כתבו כאן את הקוד שלכם
```

**תשובה והסבר:** כתבו כאן.

