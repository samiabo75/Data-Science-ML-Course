# מקור מקצועי למצגת — מפגש 19 — Precision, Recall ו־ F1
**קהל:** כיתה י׳, תלמידים חדשים בנושא. **מכסה:** 2 שעות הוראה ותרגול ושעת פרויקט אחת; יחד 135 דקות.
המסמך מרכז את הסיפור, ההסבר, דוגמה פתורה וקוד, מטרות המעבדה והוראות ההמחשה. הוא מעבד את מצגות ההשתלמות המצורפות, ואינו מצגת שנוצרה או נבדקה ב־ NotebookLM.

## מצגות מקור שנבדקו
- [Performance Indicators updated.pptx](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/Performance%20Indicators%20updated.pptx) — שקפים 12–18,22.

## גבולות התוכן
כ־ 85% מזמן ההוראה המושגית בתכנון נשען על מושגי ההשתלמות, וכ־ 15% מוקדשים לפיגום, מניעת טעויות וגשרים להמשך. זהו יעד תכנון בקירוב, לא מדידת אחוזי העתקה. המקורות אינם מועתקים מילה במילה. הדוגמאות החדשות וההעברות מסומנות כדידקטיות. פירוש נכון ומניעת זליגה קודמים להעתקת טעות או API ישן.

# מפגש 19 — Precision, Recall ו־ F1
## סיפור המסגרת ושאלת הלמידה
מסנן שמסמן הרבה הודעות כזבל עשוי לתפוס את רובן, אבל גם לחסום דואר חשוב. נבדוק שתי שאלות שונות.

## מה נלמד ומדוע
Precision בודק כמה מהחזויים כחיוביים הם חיוביים באמת: TP/(TP+FP). Recall בודק כמה מהחיוביים האמיתיים זוהו: TP/(TP+FN). F1=2TP/(2TP+FP+FN). כשאין חיזויים חיוביים, Precision אינו מוגדר מתמטית; מדיניות דיווח בקוד יכולה להציג אפס.

## דוגמה פתורה קטנה
עבור TP=6, FP=2, FN=4 מתקבלים P=0.75, R=0.6, F1≈0.667. המכנים מתייחסים לקבוצות שונות, ולכן המדדים אינם ניתנים להחלפה.

```python
TP = 6
FP = 2
FN = 4
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * TP / (2 * TP + FP + FN)
print(precision, recall, f1)
```

**פלט צפוי ופירוש:** 0.75 0.6 0.6666666666666666. זוהי דוגמה קטנה ומוצהרת; היא אינה ציון ביצוע של פרויקט אמיתי.

## הדרך לתרגול העצמאי
חישוב מהמטריצה ואימות בקוד. בהעברה משנים מחלקת מטרה. macro ו־ weighted נלמדים כקריאה מונחית של הדוח.
עבדו לפי הסדר: נסחו את השאלה, זהו נתונים ויחידות, בחרו כלי שכבר נלמד, כתבו ציפייה, הריצו והסבירו תוצאה ומגבלה. במשימה שאינה מובנת חוזרים למושג או לדוגמה, ולא מחפשים שורת קוד להעתקה.

## תוצר לפרויקט
מקבעים מדד בחירה לפרויקט ומנמקים את מחיר ההחמצה ואת מחיר אזעקת השווא.

## קשר ללימודי ההמשך
מדדים, אימות והכללה משותפים ליחידה 5 ולניסויים ב־DL. שומרים על אותה שיטת הערכה גם כאשר המודל משתנה.

## בדיקה עצמית
איזה מדד מתחיל מכל מי שסומן חיובי?
כתבו תשובה במילים שלכם והצביעו על תא או נתון שתומך בה. אין פתרון לתרגול העצמאי במסמך התלמיד.


## יישום מודרך מלא וקוד לדוגמה
# מפגש 19 — Precision, Recall ו־ F1
2 שעות הוראה ותרגול ושעת פרויקט אחת; יחד 135 דקות.

## סיפור המסגרת
מסנן שמסמן הרבה הודעות כזבל עשוי לתפוס את רובן, אבל גם לחסום דואר חשוב. נבדוק שתי שאלות שונות.

## מטרות
- לחשב Precision ו־ Recall.
- לחשב F1.
- להסביר את המכנים.

## המושגים הנחוצים
Precision בודק כמה מהחזויים כחיוביים הם חיוביים באמת: TP/(TP+FP). Recall בודק כמה מהחיוביים האמיתיים זוהו: TP/(TP+FN). F1=2TP/(2TP+FP+FN). כשאין חיזויים חיוביים, Precision אינו מוגדר מתמטית; מדיניות דיווח בקוד יכולה להציג אפס.

## דוגמה פתורה לפני קוד
עבור TP=6, FP=2, FN=4 מתקבלים P=0.75, R=0.6, F1≈0.667. המכנים מתייחסים לקבוצות שונות, ולכן המדדים אינם ניתנים להחלפה.

```python
TP = 6
FP = 2
FN = 4
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * TP / (2 * TP + FP + FN)
print(precision, recall, f1)
```

**פלט צפוי:** 0.75 0.6 0.6666666666666666

## מדוע זה חשוב?
מדדים, אימות והכללה משותפים ליחידה 5 ולניסויים ב־DL. שומרים על אותה שיטת הערכה גם כאשר המודל משתנה.

## יישום מודרך — חלק 1
מקור הקוד: ערכה 26 הקיימת. בהמשך עוברים לתרגול עצמאי באותו נושא.

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

```python
import pandas as pd
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score,
    recall_score, f1_score, classification_report
)
```

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

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

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

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

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

```python
# pos_label מגדיר מה נחשב חיובי; average="binary" כי יש שתי מחלקות
p_library = precision_score(actual, predicted, pos_label="Defect", average="binary", zero_division=0)
r_library = recall_score(actual, predicted, pos_label="Defect", average="binary", zero_division=0)
f_library = f1_score(actual, predicted, pos_label="Defect", average="binary", zero_division=0)
print("Precision:", p_library, "Recall:", r_library, "F1:", f_library)
```

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

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

### תשתית הנתונים והחלוקה
קראו תחילה את היעד ואת שמות המאפיינים. החלוקה שומרת התאמה בין שורות X ל־ y. הפרמטר random_state מאפשר שחזור ואינו משפר דיוק בפני עצמו.

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

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

```python
labels_species = ["Adelie", "Chinstrap", "Gentoo"]
cm_species = confusion_matrix(y_test, predictions, labels=labels_species)
table_species = pd.DataFrame(cm_species, index=labels_species, columns=labels_species)
table_species.index.name = "Actual"
table_species.columns.name = "Predicted"
display(table_species)
```

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

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

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

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

## עצירה לפני המעבדה
איזה מדד מתחיל מכל מי שסומן חיובי?

**התוצר הנדרש:** חישוב מהמטריצה ואימות בקוד. בהעברה משנים מחלקת מטרה. macro ו־ weighted נלמדים כקריאה מונחית של הדוח.

## המשימות שהמצגת חייבת להכין לקראתן
חישוב מהמטריצה ואימות בקוד. בהעברה משנים מחלקת מטרה. macro ו־ weighted נלמדים כקריאה מונחית של הדוח.
**מבחן התאמה:** כל פקודה או רעיון במשימת ליבה צריכים להיות מוסברים קודם בדוגמה, או להופיע כקוד תשתית נתון. בהכנה לתרגול הציגו נתונים, תוצר וצעדי חשיבה; אין לפתור את משימת התלמיד. המעבדה המדויקת היא Student-Lab.ipynb, ופתרונה אינו מקור למצגת התלמיד.

## הוראות חזותיות
רקע לבן או בהיר מאוד, טקסט כהה, ניגודיות גבוהה וגופן גדול. רעיון מרכזי אחד בשקף. המושג יופיע לצד דוגמה קטנה, חישוב או תרשים מדויק. משתמשים בסיפור כדי להסביר את הצורך; אין להציג את נתוני הסיפור המומצאים כאילו נאספו בפועל. לתרשים נתונים אמיתי מצרפים פלט מאומת או מסמנים שהוא סכמטי. אין להמציא ציון מודל או לקרוא ציון החלטה כהסתברות.

## מקורות משלימים מוגבלים
מניעת זליגה והכנה בתוך אימות: [תיעוד scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html). פירוש R²: [תיעוד המדד](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html). משתמשים רק בקטע הרלוונטי לנושא, ללא הוספת יחידת לימוד או ספרייה חדשה.


## נספח — נוסח המעבדה העצמאית ללא פתרון
הנספח מאפשר לבדוק שהמצגת מכינה למשימה בפועל. בחרו רק את משימות הליבה שהוגדרו במדריך. אין להפוך את הנספח לפתרון בשקפים.

# מפגש 19 — Precision, Recall ו־F1
2 שעות הוראה ותרגול ושעת פרויקט אחת; יחד 135 דקות.

## סיפור המסגרת
מסנן שמסמן הרבה הודעות כזבל עשוי לתפוס את רובן, אבל גם לחסום דואר חשוב. נבדוק שתי שאלות שונות.

## מטרות
- לחשב Precision ו־Recall.
- לחשב F1.
- להסביר את המכנים.

## תרגול עצמאי
חישוב מהמטריצה ואימות בקוד. בהעברה משנים מחלקת מטרה. macro ו־weighted נלמדים כקריאה מונחית של הדוח.

תאי משימות ריקים בכוונה. תשתית טעינה או מודל נתון, אם קיימים, אינם פתרון לחישוב ולפירוש שלכם. הפעילו רק את משימות הליבה שהוגדרו למפגש. שאר משימות המקור הן מאגר חזרה, ללא חובת בית נוספת.

## חלק 1 — תרגול העברה
הנתונים וההוראות מופיעים להלן. עובדים על משימות הליבה של המפגש.

עבדו לפי הסדר. תאי המשימה ריקים בכוונה; אפשר להיעזר במודרכת. נתוני התרגול הבינרי מומצאים. הקוד הנתון של Penguins משחזר מודל שכבר נלמד ואינו פתרון למשימות המדדים.

```python
import pandas as pd
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score,
    recall_score, f1_score, classification_report
)
```

```python
# דוגמה דידקטית מומצאת חדשה
actual = ["OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK",
          "Defect", "Defect", "Defect", "Defect"]
predicted = ["OK", "OK", "OK", "OK", "OK", "Defect", "Defect", "Defect",
             "OK", "Defect", "Defect", "Defect"]
```

## 1. מטריצה ומשמעות המכנים
בנו מטריצת ספירות עם labels=['OK', 'Defect'], שורות אמת ועמודות חיזוי. הגדירו Defect כחיובי וסמנו TP, FP, FN, TN. כתבו במילים מהי קבוצת המכנה של Precision ומהי קבוצת המכנה של Recall.

```python
# כתבו כאן את הקוד שלכם
```

**תיעוד והסבר:** כתבו כאן.

## 2. חישוב ואימות
חשבו ידנית Accuracy, Precision, Recall ו־ F1. הציגו F1 גם מנוסחת הספירות, והשוו לספרייה עם pos_label מפורש ו־ zero_division=0. הוסיפו משפט פירוש לכל אחד מ־ P ו־ R.

```python
# כתבו כאן את הקוד שלכם
```

**תיעוד והסבר:** כתבו כאן.

## 3. מקרה קצה
צרו את דוגמת תמיד־ OK מהשיעור הקודם: שמונה OK ושני Defect אמיתיים, וכל התחזיות OK. חשבו מדדים בספרייה. איזה יחס אינו מוגדר מתמטית ומדוע? מה הקוד מדווח ולמה? הסבירו כיצד Accuracy עלול להסתיר כישלון בזיהוי פגומים.

```python
# כתבו כאן את הקוד שלכם
```

**תיעוד והסבר:** כתבו כאן.

## 4. העברה ל־ Penguins
הריצו את קוד ההכנה הנתון. בנו מטריצה בסדר Adelie, Chinstrap, Gentoo. הפעם בחרו Adelie כמחלקת המטרה מול היתר. חשבו TP, FP, FN, TN, Precision, Recall ו־ F1 מתוך השורה והעמודה. אין לשנות את המודל או את החלוקה.

## 5. חיבור לאותו מודל Penguins
זהו קוד הכנה נתון משיעורים 24–25; אין צורך לכתוב אותו מחדש. סנפיר ומסה, seed=42, test_size=0.25, stratify, השלמה ותקנון מאימון בלבד ו־ K=3 קבוע מראש.
היום מוסיפים מדדים לתחזיות האלה; לא משנים K או מאפיינים לאחר ראיית Test.

עותק הקורס של Penguins כולל 344 רשומות ו־ 7 עמודות; מקור Gorman ו־ Palmer Station LTER. תיעוד וייחוס: [palmerpenguins](https://github.com/allisonhorst/palmerpenguins), Horst, Hill & Gorman (2020), DOI:10.5281/zenodo.3960218. זו דוגמת הוראה, ולא אישור התאמת מאגר לפרויקט גמר.

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

```python
# כתבו כאן את הקוד שלכם
```

**תיעוד והסבר:** כתבו כאן.

## 5. דוח והחלטה לפרויקט
הפיקו classification_report עם כל התוויות ו־ zero_division=0. השוו את שורת Adelie לחישובכם. מהו support שלה? הסבירו במילים מה ההבדל בין macro ל־ weighted, בלי צורך בחישוב ידני. בחרו מדד מתאים לתרחיש בקרת האיכות ונמקו לפי מחיר טעות; ציינו מדד נוסף ומגבלה.

```python
# כתבו כאן את הקוד שלכם
```

**תיעוד והסבר:** כתבו כאן.

## יישום בפרויקט
מקבעים מדד בחירה לפרויקט ומנמקים את מחיר ההחמצה ואת מחיר אזעקת השווא.

## לפני הגשה
הריצו לפי הסדר, בדקו פלטים עדכניים, כתבו פירוש ומגבלה והצהירו היכן נעזרתם. פתרונות נמצאים בנפרד למורה אך גלויים במאגר הציבורי.

## תכנון מדורג למצגת של מפגש 19

**שאלת פתיחה:** מסנן שמסמן הרבה הודעות כזבל עשוי לתפוס את רובן, אבל גם לחסום דואר חשוב. נבדוק שתי שאלות שונות.

**המחשה מרכזית:** הדגש בנפרד את קבוצת החיוביים החזויים ואת החיוביים האמיתיים, ואז חשב את המדדים בדוגמה.

| שלב | מה מציגים לתלמיד | בדיקת הבנה |
|---|---|---|
| צורך ומטרה | הסיפור ומטרה אחת: לחשב Precision ו־Recall | מה נרצה לדעת בסיום? |
| מושג לפני קוד | Precision בודק כמה מהחזויים כחיוביים הם חיוביים באמת: TP/(TP+FP). Recall בודק כמה מהחיוביים האמיתיים זוהו: TP/(TP+FN). F1=2TP/(2TP+FP+FN). כשאין חיזויים חיוביים, Precision אינו מוגדר מתמטית; מדיניות דיווח בקוד יכולה להציג אפס. | התלמיד מסביר את המושג באמצעות הדוגמה. |
| דוגמה פתורה | עבור TP=6,FP=2,FN=4 מתקבלים P=0.75,R=0.6,F1≈0.667. המכנים מתייחסים לקבוצות שונות, ולכן המדדים אינם ניתנים להחלפה. | עוצרים לפני חישוב או חשיפת פלט ומבקשים ציפייה מנומקת. |
| מעבר לקוד | קטע קצר מתוך הדוגמה הקיימת, עם שמות משתנים ויחידות ללא שינוי | התלמיד מקשר פעולה בקוד לשלב בדוגמה. |
| תרגול בסיוע | בוחרים משימת ליבה מתוך Student-Lab.ipynb ומציגים רק נתון, דרישה ורמז | התלמיד מציע פעולה ומנמק אותה לפני כתיבת קוד. |
| העברה עצמאית | ממשיכים במשימת הליבה עם מאפיין או הקשר השונים מהדוגמה הפתורה | התלמיד מגיש ביצוע ופירוש ללא העתקת הפתרון. |
| סיום | איזה מדד מתחיל מכל מי שסומן חיובי? | התלמיד מצביע על ראיה ומציין מגבלה. |

**תוצר בתוך מכסת הזמן:** מקבעים מדד בחירה לפרויקט ומנמקים את מחיר ההחמצה ואת מחיר אזעקת השווא.

**הקשר להמשך:** מדדים, אימות והכללה משותפים ליחידה 5 ולניסויים ב־DL. שומרים על אותה שיטת הערכה גם כאשר המודל משתנה.

הטבלה מפרטת את חומר המפגש הקיים; אין להפוך כל שורה לשקף נוסף אם היא חורגת ממכסת השקפים. במפגש הגנה משתמשים בה כשאלות ומשוב על הפרויקט האישי, ללא מעבדה נוספת.
