# מקור מקצועי למצגת — מפגש 18 — מטריצת בלבול וסוגי טעויות
**קהל: ** כיתה י׳, תלמידים חדשים בנושא. **מכסה: ** 2 שעות הוראה ותרגול ו־ 1 שעות פרויקט; יחד 135 דקות.
המסמך מרכז את הסיפור, ההסבר, דוגמה פתורה וקוד, מטרות המעבדה והוראות ההמחשה. הוא מעבד את מצגות ההשתלמות המצורפות, ואינו מצגת שנוצרה או נבדקה ב־ NotebookLM.

## מצגות מקור שנבדקו
- [Performance Indicators updated.pptx](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/Performance%20Indicators%20updated.pptx) — שקפים 2–11,21.

## גבולות התוכן
כ־ 85% מזמן ההוראה המושגית בתכנון נשען על מושגי ההשתלמות, וכ־ 15% מוקדשים לפיגום, מניעת טעויות וגשרים להמשך. זהו יעד תכנון בקירוב, לא מדידת אחוזי העתקה. המקורות אינם מועתקים מילה במילה. הדוגמאות החדשות וההעברות מסומנות כדידקטיות. פירוש נכון ומניעת זליגה קודמים להעתקת טעות או API ישן.

# מפגש 18 — מטריצת בלבול וסוגי טעויות
## סיפור המסגרת ושאלת הלמידה
מסנן הודעות עלול לחסום הודעה חשובה או להחמיץ זבל. שתי הטעויות שונות במשמעותן, גם אם שתיהן נספרות כשגיאה.

## מה נלמד ומדוע
מטריצת בלבול מצליבה אמת וחיזוי. כאן השורות הן אמת והעמודות חיזוי. מגדירים מראש מחלקה חיובית. TP הוא זיהוי חיובי נכון, FP אזעקת שווא, FN החמצה ו־ TN זיהוי שלילי נכון. תמיד כותבים סדר תוויות וכותרות לצירים.

## דוגמה פתורה קטנה
לאמת [0,0,1,1] ולחיזוי [0,1,0,1] המטריצה [[1,1], [1,1]]. יש תחזית נכונה אחת מכל מחלקה וטעות אחת מכל סוג.

```python
from sklearn.metrics import confusion_matrix
y_true = [0, 0, 1, 1]
y_pred = [0, 1, 0, 1]
print(confusion_matrix(y_true, y_pred, labels=[0, 1]))
```

**פלט צפוי ופירוש: ** [[1 1]
 [1 1]]. זוהי דוגמה קטנה ומוצהרת; היא אינה ציון ביצוע של פרויקט אמיתי.

## הדרך לתרגול העצמאי
מטריצה בינרית קטנה ופירוש טעות במטריצה רב־מחלקתית. חישוב P/R/F1 מתחיל במפגש הבא.
עבדו לפי הסדר: נסחו את השאלה, זהו נתונים ויחידות, בחרו כלי שכבר נלמד, כתבו ציפייה, הריצו והסבירו תוצאה ומגבלה. במשימה שאינה מובנת חוזרים למושג או לדוגמה, ולא מחפשים שורת קוד להעתקה.

## תוצר לפרויקט
מפיקים מטריצה לפרויקט ומסבירים מי מושפע מכל סוג טעות ומה חשיבותה.

## קשר ללימודי ההמשך
מדדים, אימות והכללה משותפים ליחידה 5 ולניסויים ב־ DL. שומרים על אותה שיטת הערכה גם כאשר המודל משתנה.

## בדיקה עצמית
מדוע אותו אחוז טעויות יכול להיות חמור יותר בשימוש אחר?
כתבו תשובה במילים שלכם והצביעו על תא או נתון שתומך בה. אין פתרון לתרגול העצמאי במסמך התלמיד.


## יישום מודרך מלא וקוד לדוגמה
# מפגש 18 — מטריצת בלבול וסוגי טעויות
2 שעות הוראה ותרגול ו־ 1 שעות פרויקט; יחד 135 דקות.

## סיפור המסגרת
מסנן הודעות עלול לחסום הודעה חשובה או להחמיץ זבל. שתי הטעויות שונות במשמעותן, גם אם שתיהן נספרות כשגיאה.

## מטרות
- למלא מטריצה.
- להגדיר חיובי.
- לפרש שתי טעויות שונות.

## המושגים הנחוצים
מטריצת בלבול מצליבה אמת וחיזוי. כאן השורות הן אמת והעמודות חיזוי. מגדירים מראש מחלקה חיובית. TP הוא זיהוי חיובי נכון, FP אזעקת שווא, FN החמצה ו־ TN זיהוי שלילי נכון. תמיד כותבים סדר תוויות וכותרות לצירים.

## דוגמה פתורה לפני קוד
לאמת [0,0,1,1] ולחיזוי [0,1,0,1] המטריצה [[1,1], [1,1]]. יש תחזית נכונה אחת מכל מחלקה וטעות אחת מכל סוג.

```python
from sklearn.metrics import confusion_matrix
y_true = [0, 0, 1, 1]
y_pred = [0, 1, 0, 1]
print(confusion_matrix(y_true, y_pred, labels=[0, 1]))
```

**פלט צפוי: ** [[1 1]
 [1 1]]

## מדוע זה חשוב?
מדדים, אימות והכללה משותפים ליחידה 5 ולניסויים ב־ DL. שומרים על אותה שיטת הערכה גם כאשר המודל משתנה.

## יישום מודרך — חלק 1
מקור הקוד: ערכה 25 הקיימת. בהמשך עוברים לתרגול עצמאי באותו נושא.

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

```python
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt
```

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

```python
# נתונים מומצאים לצורך למידה; אין CSV או מודל מאומן בדוגמה הזאת
actual = ["OK", "OK", "OK", "OK", "Defect", "Defect", "Defect", "Defect"]
predicted = ["OK", "OK", "Defect", "OK", "OK", "OK", "Defect", "Defect"]
pairs = pd.DataFrame({"actual": actual, "predicted": predicted})
display(pairs)
```

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

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

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

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

### המחשה חזותית
לפני הרצה הגדירו שאלה, סוגי משתנים ויחידות. אחרי הרצה פרשו את הצירים ואת הממצא. אין להסיק סיבתיות או למחוק קצה רק מן הציור.

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

## עצירה לפני המעבדה
מדוע אותו אחוז טעויות יכול להיות חמור יותר בשימוש אחר?

**התוצר הנדרש: ** מטריצה בינרית קטנה ופירוש טעות במטריצה רב־מחלקתית. חישוב P/R/F1 מתחיל במפגש הבא.

## המשימות שהמצגת חייבת להכין לקראתן
מטריצה בינרית קטנה ופירוש טעות במטריצה רב־מחלקתית. חישוב P/R/F1 מתחיל במפגש הבא.
**מבחן התאמה: ** כל פקודה או רעיון במשימת ליבה צריכים להיות מוסברים קודם בדוגמה, או להופיע כקוד תשתית נתון. בהכנה לתרגול הציגו נתונים, תוצר וצעדי חשיבה; אין לפתור את משימת התלמיד. המעבדה המדויקת היא Student-Lab.ipynb, ופתרונה אינו מקור למצגת התלמיד.

## הוראות חזותיות
רקע לבן או בהיר מאוד, טקסט כהה, ניגודיות גבוהה וגופן גדול. רעיון מרכזי אחד בשקף. המושג יופיע לצד דוגמה קטנה, חישוב או תרשים מדויק. משתמשים בסיפור כדי להסביר את הצורך; אין להציג את נתוני הסיפור המומצאים כאילו נאספו בפועל. לתרשים נתונים אמיתי מצרפים פלט מאומת או מסמנים שהוא סכמטי. אין להמציא ציון מודל או לקרוא ציון החלטה כהסתברות.

## מקורות משלימים מוגבלים
מניעת זליגה והכנה בתוך אימות: [תיעוד scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html). פירוש R²: [תיעוד המדד](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html). משתמשים רק בקטע הרלוונטי לנושא, ללא הוספת יחידת לימוד או ספרייה חדשה.


## נספח — נוסח המעבדה העצמאית ללא פתרון
הנספח מאפשר לבדוק שהמצגת מכינה למשימה בפועל. בחרו רק את משימות הליבה שהוגדרו במדריך. אין להפוך את הנספח לפתרון בשקפים.

# מפגש 18 — מטריצת בלבול וסוגי טעויות
2 שעות הוראה ותרגול ו־1 שעות פרויקט; יחד 135 דקות.

## סיפור המסגרת
מסנן הודעות עלול לחסום הודעה חשובה או להחמיץ זבל. שתי הטעויות שונות במשמעותן, גם אם שתיהן נספרות כשגיאה.

## מטרות
- למלא מטריצה.
- להגדיר חיובי.
- לפרש שתי טעויות שונות.

## תרגול עצמאי
מטריצה בינרית קטנה ופירוש טעות במטריצה רב־מחלקתית. חישוב P/R/F1 מתחיל במפגש הבא.

תאי משימות ריקים בכוונה. תשתית טעינה או מודל נתון, אם קיימים, אינם פתרון לחישוב ולפירוש שלכם. הפעילו רק את משימות הליבה שהוגדרו למפגש. שאר משימות המקור הן מאגר חזרה, ללא חובת בית נוספת.

## חלק 1 — תרגול העברה
הנתונים וההוראות מופיעים להלן. עובדים על משימות הליבה של המפגש.

התרגול בודק קריאת ספירות והסבר. תאי המשימה ריקים בכוונה. קוד ההכנה הוא חומר שכבר נלמד ואינו פתרון למטריצות.

```python
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt
```

```python
# דוגמה דידקטית מומצאת — מסווג קבוע שאינו מאומן
actual = ["OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK", "Defect", "Defect"]
predicted = ["OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK"]
pairs = pd.DataFrame({"actual": actual, "predicted": predicted})
display(pairs)
```

## 1. מטריצה ידנית
בנו על נייר מטריצת ספירות בסדר OK, Defect. כתבו כותרת לכל ציר וספרו כל זוג בדיוק פעם אחת. מה סכום התאים?

```python
# כתבו כאן את הקוד שלכם
```

**תשובה והסבר: ** כתבו כאן.

## 2. אימות בקוד
הפעילו confusion_matrix עם labels מפורש והציגו DataFrame מתויג כמו במודרכת. בדקו מול הטבלה הידנית. אין צורך ליצור תרשים לדוגמה הבינרית.

```python
# כתבו כאן את הקוד שלכם
```

**תשובה והסבר: ** כתבו כאן.

## 3. פירוש ואחוז הצלחה
הגדירו Defect כחיובי. זהו TN, FP, FN, TP, חשבו Accuracy מהאלכסון והשוו ל־ accuracy_score. הסבירו מדוע המסווג עלול להיות לא שימושי לזיהוי פגמים למרות הציון.

```python
# כתבו כאן את הקוד שלכם
```

**תשובה והסבר: ** כתבו כאן.

## 4. חזרה ל־ Penguins
הריצו את קוד ההכנה הנתון להלן. צרו מטריצה מתויגת בסדר Adelie, Chinstrap, Gentoo ותרשים ספירות. הראו שסכום התאים שווה למספר דוגמאות הבדיקה ושסכום האלכסון מתאים למספר ההצלחות. אין לשנות K, מאפיינים או חלוקה.

## ממשיכים את אותו מודל משיעור 24
התא הבא הוא **קוד הכנה נתון שכבר נלמד**, להרצה מלמעלה; אין צורך לכתוב אותו מחדש בשיעור זה.
הוא משחזר בדיוק את המודרכת: סנפיר ומסה, חלוקה 25%, seed=42, stratify, השלמה ותקנון מאימון בלבד ו־ K=3 קבוע. כעת מוסיפים דרך תיאור לתחזיות שכבר התקבלו; לא בוחרים פרמטרים לפי Test.
Penguins: עותק הקורס בן 344 שורות ו־ 7 עמודות. מקור: Kristen Gorman ו־ Palmer Station LTER; ייחוס ותיעוד [palmerpenguins](https://github.com/allisonhorst/palmerpenguins), Horst, Hill & Gorman (2020), DOI:10.5281/zenodo.3960218. התאמה לפרויקט גמר טעונה בדיקה נפרדת.

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

**תשובה והסבר: ** כתבו כאן.

## 5. כרטיס הערכה
פרשו תא שגיאה אחד וסכום שורה אחת מהנתונים האמיתיים. הסבירו מה מבטא סכום העמודה של אותו מין. כתבו מגבלה אחת והסבירו מדוע שם המחלקה החיובית חיוני לפירוש FN. אין צורך לחשב עדיין Precision, Recall או F1.

```python
# כתבו כאן את הקוד שלכם
```

**תשובה והסבר: ** כתבו כאן.

## יישום בפרויקט
מפיקים מטריצה לפרויקט ומסבירים מי מושפע מכל סוג טעות ומה חשיבותה.

## לפני הגשה
הריצו לפי הסדר, בדקו פלטים עדכניים, כתבו פירוש ומגבלה והצהירו היכן נעזרתם. פתרונות נמצאים בנפרד למורה אך גלויים במאגר הציבורי.