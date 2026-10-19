# מקור למצגת — שיעור 26 — Precision, Recall ו־F1: מתוך איזו קבוצה מחשבים?
**קהל:** תלמידי כיתה י׳ מתחילים. **מכסה:** 3 שעות לימוד (135 דקות), כולל תרגול; המצגת מחליפה חלק מההסבר ואינה מוסיפה זמן.
**שלב בתהליך החקר:** הערכה.
**פתיחה מוכרת:** מסנן שמסמן כל הודעה כתקינה נראה מוצלח כשיש מעט זבל, אבל מה הוא מחמיץ?
**גבולות הליבה במצגת ובתרגול:** P/R/F1 ידניים והסבר מכנים; העברה למחלקה אחרת. macro/weighted כקריאת דוח בלבד.
**המחשה חזותית מומלצת:** אותה מטריצה, אבל Precision מדגישה את עמודת חיזוי חיובי ו־Recall את שורת האמת החיובית. F1 משלבשניהם; פרטו את המכנים במילים.
**זיקה להמשך:** הזיקה המרכזית היא לבסיס וקטורי, סטטיסטי או להערכת מודלים; השתמשו רק בזיקה המפורשת בחומר, כקדימות להמשך ולא כהוראת יחידה 5 מלאה.

## הוראות למניעת ערבוב דוגמה ותרגול
חלק א הוא דוגמה פתורה שאפשר להסביר ולפתור בשקפים. חלק ב הוא תרגול עצמאי: מציגים את הדרישה, מפרקים לשלבים ונותנים רמזים; אין מייצרים פתרון מלא,קוד מלא או תוצאות סופיות של המשימות הנבחרות. אין בקובץ פתרוןמתועד לתרגול. חומר עודף במחברות מיועד לחזרה; גבולותהליבה לעיל גוברים על שאיפה לכסותכל תא.
דוגמאות מומצאות אינן מאגר אמיתי. קישורים הם ייחוס; אין להניח שתוכנם נכלל אוטומטית במקור שהועלה. לא להמציא פלט,דיוק או גרף מאומת כשהם אינם מופיעים בטקסט.

## חלק א — הסבר ודוגמה פתורה
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 26 — Precision, Recall ו־F1: מתוך איזו קבוצה מחשבים?

**פתיחה:** דודו משתמש במסווג לסימון מוצרים פגומים. האחראי על הבדיקה שואל: "מתוך המוצרים שסומנו כפגומים, כמה באמת פגומים?" מנהלת האיכות שואלת: "מתוך כל הפגומים, כמה מצאנו?" אלה שתי קבוצות שונות ושני מכנים שונים.
מגדירים **Defect כחיובי**, שורות אמת ועמודות חיזוי. נשענים על אותה מטריצה מהשיעור הקודם.

עוגן: [סיכום מפגש השתלמות 6](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/08-Classification-Metrics/Meeting-06-Didactic-Summary.md) ו[המחברת המודרכת](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/08-Classification-Metrics/Meeting-06-Classification-Metrics-Guided.ipynb). הדוגמאות כאן הן התאמה דידקטית שלנו, לא תרגילי מקור; חומרי המקור נשמרו.

## למה לומדים את זה עכשיו?
מסנן שמסמן כל הודעה כתקינה נראה מוצלח כשיש מעט זבל, אבל מה הוא מחמיץ?
**בתהליך הפרויקט:** הערכה.
**מסגרת פעילה:** 3 שעות לימוד — 135 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.

### תא קוד 3
```python
import pandas as pd
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score,
    recall_score, f1_score, classification_report
)
```

### תא קוד 4
```python
# נתונים דידקטיים מומצאים, זהים למודרכת שיעור 25
actual = ["OK", "OK", "OK", "OK", "Defect", "Defect", "Defect", "Defect"]
predicted = ["OK", "OK", "Defect", "OK", "OK", "OK", "Defect", "Defect"]
labels_binary = ["OK", "Defect"]
cm_binary = confusion_matrix(actual, predicted, labels=labels_binary)
table_binary = pd.DataFrame(cm_binary, index=labels_binary, columns=labels_binary)
table_binary.index.name = "Actual"
table_binary.columns.name = "Predicted"
display(table_binary)
```

## 1. שואלים לפני שמציבים
| מדד | השאלה במילים | המכנה במטריצה |
|---|---|---|
| Precision | מתוך החיזויים החיוביים, כמה נכונים? | עמודת החיובי: TP+FP |
| Recall | מתוך החיוביים האמיתיים, כמה זוהו? | שורת החיובי: TP+FN |

$$P=\frac{TP}{TP+FP},\qquad R=\frac{TP}{TP+FN}$$

לפני הרצה: סמנו את עמודת Defect ואז את שורת Defect. האם שתי הקבוצות מכילות בדיוק אותם מוצרים?
Accuracy הוא מספר ההצלחות מכל הדוגמאות; הוא אינו אף אחד משני היחסים האלה. נשמור את שמות המדדים באנגלית כדי שלא לבלבל בין תרגומים.

## 2. F1 — משלב את שני היחסים
$$F1=\frac{2PR}{P+R}=\frac{2TP}{2TP+FP+FN}$$

כאשר P ו־R חיוביים, זהו ממוצע הרמוני; אין לחשב (P+R)/2. למשל P=1 ו־R=0.25 נותנים F1=0.4, ולא 0.625. F1 אינו אחוז כל התחזיות הנכונות, ואינו מתחשב ב־TN בנוסחת הספירות.
הנוסחה הישירה ב־P,R דורשת טיפול אם שניהם אפס; גם נוסחת הספירות אינה מוגדרת אם המכנה שלה אפס. מדיניות הספרייה מוצגת בהמשך.

### תא קוד 6
```python
# החיובי הוא Defect; שורות אמת, עמודות חיזוי
tn = table_binary.loc["OK", "OK"]
fp = table_binary.loc["OK", "Defect"]
fn = table_binary.loc["Defect", "OK"]
tp = table_binary.loc["Defect", "Defect"]

# בדוגמה זו המכנים חיוביים
precision_manual = tp / (tp + fp)
recall_manual = tp / (tp + fn)
f1_manual = 2 * precision_manual * recall_manual / (precision_manual + recall_manual)
f1_counts = 2 * tp / (2 * tp + fp + fn)
print("Accuracy:", (tp + tn) / cm_binary.sum())
print("Precision:", precision_manual)
print("Recall:", recall_manual)
print("F1:", f1_manual, "F1 from counts:", f1_counts)
```

**פירוש:** שלושה מוצרים סומנו כפגומים ומתוכם שניים באמת פגומים: P=2/3. מארבעה פגומים אמיתיים זוהו שניים: R=1/2. לכן F1=4/7≈0.5714. כל תוצאה מתייחסת לקבוצה אחרת; כתבו את הקבוצה לפני האחוז.

## 3. מאמתים בספרייה
pos_label בוחר את התווית החיובית. zero_division קובע כיצד לדווח במכנה אפס; בדוגמה הזאת אין מכנה אפס. הספרייה אינה מחליפה את הנימוק המילולי.

### תא קוד 9
```python
# pos_label מגדיר מה נחשב חיובי; average="binary" כי יש שתי מחלקות
p_library = precision_score(actual, predicted, pos_label="Defect", average="binary", zero_division=0)
r_library = recall_score(actual, predicted, pos_label="Defect", average="binary", zero_division=0)
f_library = f1_score(actual, predicted, pos_label="Defect", average="binary", zero_division=0)
print("Precision:", p_library, "Recall:", r_library, "F1:", f_library)
```

## 4. מכנה אפס וחוסר איזון
אם אין כלל חיזויי Defect, הביטוי Precision הוא 0/0 ואינו מוגדר מתמטית. zero_division=0 היא החלטת דיווח מפורשת של הקוד: להחזיר 0 במקרה כזה. אין פירושה ש־0/0 שווה לאפס.
בדוגמה הבאה יש פגומים אמיתיים, לכן Recall מוגדר ושווה לאפס. F1 לפי נוסחת הספירות מוגדר ושווה לאפס, כי FN חיובי. Accuracy יכול עדיין להיות גבוה.
אם גם אין חיוביים אמיתיים, גם Recall עלול להיות לא מוגדר; קוראים תמיד את support ואת מדיניות הדיווח. כפל רשימה כאן רק מקצר בניית דוגמה מומצאת.

### תא קוד 11
```python
# דוגמה מומצאת מהתרגול בשיעור 25: תמיד חוזים תקין
actual_zero = ["OK"] * 8 + ["Defect"] * 2
predicted_zero = ["OK"] * 10
print("Accuracy:", accuracy_score(actual_zero, predicted_zero))
print("Precision (chosen zero policy):", precision_score(
    actual_zero, predicted_zero, pos_label="Defect", zero_division=0
))
print("Recall:", recall_score(actual_zero, predicted_zero, pos_label="Defect", zero_division=0))
print("F1:", f1_score(actual_zero, predicted_zero, pos_label="Defect", zero_division=0))
```

## 5. חיבור לאותו מודל Penguins
זהו קוד הכנה נתון משיעורים 24–25; אין צורך לכתוב אותו מחדש. סנפיר ומסה, seed=42, test_size=0.25, stratify, השלמה ותקנון מאימון בלבד ו־K=3 קבוע מראש.
היום מוסיפים מדדים לתחזיות האלה; לא משנים K או מאפיינים לאחר ראיית Test.

עותק הקורס של Penguins כולל 344 רשומות ו־7 עמודות; מקור Gorman ו־Palmer Station LTER. תיעוד וייחוס: [palmerpenguins](https://github.com/allisonhorst/palmerpenguins), Horst, Hill & Gorman (2020), DOI:10.5281/zenodo.3960218. זו דוגמת הוראה, ולא אישור התאמת מאגר לפרויקט גמר.

### תא קוד 13
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

### תא קוד 14
```python
labels_species = ["Adelie", "Chinstrap", "Gentoo"]
cm_species = confusion_matrix(y_test, predictions, labels=labels_species)
table_species = pd.DataFrame(cm_species, index=labels_species, columns=labels_species)
table_species.index.name = "Actual"
table_species.columns.name = "Predicted"
display(table_species)
```

## 6. Chinstrap מול כל היתר
סמנו את התא באלכסון, את כל שורת Chinstrap ואת כל עמודתו. TP הוא התא באלכסון; יתר השורה הוא FN ויתר העמודה FP. יתר התאים הם TN ביחס למחלקת המטרה. הסבירו קודם מהי החמצה של Chinstrap.

### תא קוד 16
```python
# מחלקת מטרה מול כל היתר; אין מאמנים כאן מודל בינרי חדש
target = "Chinstrap"
tp_target = table_species.loc[target, target]
support_target = table_species.loc[target].sum()
predicted_target = table_species[target].sum()
fn_target = support_target - tp_target
fp_target = predicted_target - tp_target
tn_target = cm_species.sum() - tp_target - fn_target - fp_target

# במחלקה ובחלוקה הנוכחית שני המכנים אינם אפס
p_target = tp_target / predicted_target
r_target = tp_target / support_target
f_target = 2 * tp_target / (2 * tp_target + fp_target + fn_target)
print("Target:", target, "TP:", tp_target, "FP:", fp_target, "FN:", fn_target, "TN:", tn_target)
print("Support:", support_target, "Predicted target:", predicted_target)
print("Precision:", p_target, "Recall:", r_target, "F1:", f_target)
```

## 7. קוראים דוח לפי מחלקה
לכל מין מתייחסים בנפרד כחיובי מול כל יתר המינים. זו דרך **הערכה** של אותן תחזיות רב־מחלקתיות; לא מאמנים שלושה מודלים חדשים.
support הוא מספר דוגמאות האמת של המחלקה בבדיקה, כלומר סכום השורה, ולא מספר התחזיות שניתנו לה.
הסברים לשורות הסיכום: macro avg הוא ממוצע פשוט של המדד בין המחלקות; weighted avg הוא ממוצע משוקלל לפי support. בריבוי מחלקות עם מחלקה אחת לכל דוגמה ועם כל התוויות, Recall המשוקלל שווה ל־Accuracy. אין פירוש הדבר ששאר המדדים זהים לו.
weighted F1 הוא ממוצע של ערכי F1 לפי support; אין לחשבו על ידי הצבת Precision ו־Recall המשוקללים בנוסחת F1.
שורות הסיכום הן קריאת דוח מסייעת, לא יעד לתרגול נוסחאות נוספות בשיעור זה. גם ממוצע גבוה יכול להסתיר מחלקה חלשה.

### תא קוד 18
```python
# קטע נתון לקריאת דוח; output_dict מאפשר להציגו בטבלה
report = classification_report(
    y_test, predictions, labels=labels_species,
    output_dict=True, zero_division=0
)
report_table = pd.DataFrame(report).T
display(report_table.loc[labels_species, ["precision", "recall", "f1-score", "support"]])
display(report_table.loc[["macro avg", "weighted avg"], ["precision", "recall", "f1-score"]])
print("Overall Accuracy:", accuracy_score(y_test, predictions))
```

## 8. בוחרים מדד מתוך שימוש
אם המטרה לצמצם החמצות של פגומים, Recall של Defect חשוב; עדיין בודקים כמה אזעקות שווא נוצרו. אם בדיקה נוספת יקרה, Precision חשוב גם הוא. F1 שימושי כשרוצים לשקול את שניהם באופן סימטרי, אך אינו מתאר כל עלות טעות ואינו תמיד המדד הנכון.
אין כלל שתמיד צריך "למקסם Recall": מסווג שמכריז על הכול כפגום עשוי לקבל Recall=1 תוך אזעקות שווא רבות. גם אין חוק שכל שינוי מעלה אחד ומוריד את האחר; כוונון סף אינו נלמד כאן.
**לתיק הפרויקט:** הגדירו מחלקת מטרה, סוגי טעויות, מדד מועדף ונימוק, ולצדו מטריצה, support ושאר המדדים. אין סף ציון מחייב בתרגיל.
**כרטיס יציאה:** השלימו במילים "מתוך..." עבור Precision ו־Recall; הסבירו מה support ומה מדיניות אפס.


---

## חלק ב — תרגול תלמיד ללא פתרון
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 26 — Precision, Recall ו־F1: תרגול עצמאי

**פתיחה:** דודו משתמש במסווג לסימון מוצרים פגומים. האחראי על הבדיקה שואל: "מתוך המוצרים שסומנו כפגומים, כמה באמת פגומים?" מנהלת האיכות שואלת: "מתוך כל הפגומים, כמה מצאנו?" אלה שתי קבוצות שונות ושני מכנים שונים.
מגדירים **Defect כחיובי**, שורות אמת ועמודות חיזוי. נשענים על אותה מטריצה מהשיעור הקודם.

עוגן: [סיכום מפגש השתלמות 6](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/08-Classification-Metrics/Meeting-06-Didactic-Summary.md) ו[המחברת המודרכת](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/08-Classification-Metrics/Meeting-06-Classification-Metrics-Guided.ipynb). הדוגמאות כאן הן התאמה דידקטית שלנו, לא תרגילי מקור; חומרי המקור נשמרו.

## למה לומדים את זה עכשיו?
מסנן שמסמן כל הודעה כתקינה נראה מוצלח כשיש מעט זבל, אבל מה הוא מחמיץ?
**בתהליך הפרויקט:** הערכה.
**מסגרת פעילה:** 3 שעות לימוד — 135 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.
**התרגול הנבחר למסגרת זו:** P/R/F1 ידניים והסבר מכנים; העברה למחלקה אחרת. macro/weighted כקריאת דוח בלבד.

עבדו לפי הסדר. תאי המשימה ריקים בכוונה; אפשר להיעזר במודרכת. נתוני התרגול הבינרי מומצאים. הקוד הנתון של Penguins משחזר מודל שכבר נלמד ואינו פתרון למשימות המדדים.

### תא קוד 4
```python
import pandas as pd
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score,
    recall_score, f1_score, classification_report
)
```

### תא קוד 5
```python
# דוגמה דידקטית מומצאת חדשה
actual = ["OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK",
          "Defect", "Defect", "Defect", "Defect"]
predicted = ["OK", "OK", "OK", "OK", "OK", "Defect", "Defect", "Defect",
             "OK", "Defect", "Defect", "Defect"]
```

## 1. מטריצה ומשמעות המכנים
בנו מטריצת ספירות עם labels=['OK','Defect'], שורות אמת ועמודות חיזוי. הגדירו Defect כחיובי וסמנו TP,FP,FN,TN. כתבו במילים מהי קבוצת המכנה של Precision ומהי קבוצת המכנה של Recall.

### תא קוד 7
```python
# כתבו כאן את הקוד שלכם
```

**תיעוד והסבר:** כתבו כאן.

## 2. חישוב ואימות
חשבו ידנית Accuracy, Precision, Recall ו־F1. הציגו F1 גם מנוסחת הספירות, והשוו לספרייה עם pos_label מפורש ו־zero_division=0. הוסיפו משפט פירוש לכל אחד מ־P ו־R.

### תא קוד 10
```python
# כתבו כאן את הקוד שלכם
```

**תיעוד והסבר:** כתבו כאן.

## 3. מקרה קצה
צרו את דוגמת תמיד־OK מהשיעור הקודם: שמונה OK ושני Defect אמיתיים, וכל התחזיות OK. חשבו מדדים בספרייה. איזה יחס אינו מוגדר מתמטית ומדוע? מה הקוד מדווח ולמה? הסבירו כיצד Accuracy עלול להסתיר כישלון בזיהוי פגומים.

### תא קוד 13
```python
# כתבו כאן את הקוד שלכם
```

**תיעוד והסבר:** כתבו כאן.

## 4. העברה ל־Penguins
הריצו את קוד ההכנה הנתון. בנו מטריצה בסדר Adelie, Chinstrap, Gentoo. הפעם בחרו Adelie כמחלקת המטרה מול היתר. חשבו TP,FP,FN,TN, Precision, Recall ו־F1 מתוך השורה והעמודה. אין לשנות את המודל או את החלוקה.

## 5. חיבור לאותו מודל Penguins
זהו קוד הכנה נתון משיעורים 24–25; אין צורך לכתוב אותו מחדש. סנפיר ומסה, seed=42, test_size=0.25, stratify, השלמה ותקנון מאימון בלבד ו־K=3 קבוע מראש.
היום מוסיפים מדדים לתחזיות האלה; לא משנים K או מאפיינים לאחר ראיית Test.

עותק הקורס של Penguins כולל 344 רשומות ו־7 עמודות; מקור Gorman ו־Palmer Station LTER. תיעוד וייחוס: [palmerpenguins](https://github.com/allisonhorst/palmerpenguins), Horst, Hill & Gorman (2020), DOI:10.5281/zenodo.3960218. זו דוגמת הוראה, ולא אישור התאמת מאגר לפרויקט גמר.

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

**תיעוד והסבר:** כתבו כאן.

## 5. דוח והחלטה לפרויקט
הפיקו classification_report עם כל התוויות ו־zero_division=0. השוו את שורת Adelie לחישובכם. מהו support שלה? הסבירו במילים מה ההבדל בין macro ל־weighted, בלי צורך בחישוב ידני. בחרו מדד מתאים לתרחיש בקרת האיכות ונמקו לפי מחיר טעות; ציינו מדד נוסף ומגבלה.

### תא קוד 21
```python
# כתבו כאן את הקוד שלכם
```

**תיעוד והסבר:** כתבו כאן.

