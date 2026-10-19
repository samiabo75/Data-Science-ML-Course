# מקור למצגת — שיעור 27 — רגרסיה ליניארית: ממדידה לתחזית מספרית
**קהל:** תלמידי כיתה י׳ מתחילים. **מכסה:** 2 שעות לימוד (90 דקות), כולל תרגול; המצגת מחליפה חלק מההסבר ואינה מוסיפה זמן.
**שלב בתהליך החקר:** מודל רגרסיה.
**פתיחה מוכרת:** לחזות מחיר מחשב הוא לנבא מספר, בניגוד לסיווג סוג המחשב.
**גבולות הליבה במצגת ובתרגול:** קו בעל מאפיין אחד, שאריות, R² וקו בסיס; MAE וכמה מאפיינים ב־39.
**המחשה חזותית מומלצת:** Scatterplot וקוŷ=wx+b עם חץ אנכי לשארית. הפרידו את קו המודל מקו הזהותActual=Predicted. הסבירוR² מולקובסיס ולא כאחוזדיוק.
**זיקה להמשך:** רגרסיה ופרספטרון הם גשר ל־DL; אינם אלגוריתמי חובה ביחידה 5. SVM נשאר בגלל מפרט יחידה 3. אין להמציא חפיפה בין שלוש התכניות.

## הוראות למניעת ערבוב דוגמה ותרגול
חלק א הוא דוגמה פתורה שאפשר להסביר ולפתור בשקפים. חלק ב הוא תרגול עצמאי: מציגים את הדרישה, מפרקים לשלבים ונותנים רמזים; אין מייצרים פתרון מלא,קוד מלא או תוצאות סופיות של המשימות הנבחרות. אין בקובץ פתרוןמתועד לתרגול. חומר עודף במחברות מיועד לחזרה; גבולותהליבה לעיל גוברים על שאיפה לכסותכל תא.
דוגמאות מומצאות אינן מאגר אמיתי. קישורים הם ייחוס; אין להניח שתוכנם נכלל אוטומטית במקור שהועלה. לא להמציא פלט,דיוק או גרף מאומת כשהם אינם מופיעים בטקסט.

## חלק א — הסבר ודוגמה פתורה
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 27 — רגרסיה ליניארית: ממדידה לתחזית מספרית

**פתיחה:** דודו שואל אם אורך סנפיר יכול לעזור להעריך מסה של פינגווין שלא נשקל. הפלט הוא מספר בגרמים, לא שם מין. זו דוגמת מחקר לימודית; תחזית אינה תחליף אוטומטי למדידה.
באותו מאגר אפשר להגדיר שאלות שונות: סיווג species לעומת רגרסיה של body_mass_g. מספר שמשמש קוד קטגוריה אינו הופך יעד לרגרסיה — המשמעות קובעת.

עוגן: [סיכום הרגרסיה ביחידה 3](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/04-Introduction-to-ML/Linear-Regression-Intro/Didactic-Summary.md) ו[מחברת המבוא](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/04-Introduction-to-ML/Linear-Regression-Intro/Linear-Regression-Intro.ipynb). זוהי התאמה שלנו מ־Iris ל־Penguins והוספת הערכה ב־Test. חומרי המקור נשמרו; אין כאן תרגיל מקור חדש מהמרצה.

## למה לומדים את זה עכשיו?
לחזות מחיר מחשב הוא לנבא מספר, בניגוד לסיווג סוג המחשב.
**בתהליך הפרויקט:** מודל רגרסיה.
**מסגרת פעילה:** 2 שעות לימוד — 90 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.

## 1. לפני אימון — מה אומר ישר?
$$\hat y=wx+b$$
x הוא מאפיין נמדד; ŷ היא תחזית; w שיפוע ו־b חיתוך.
בדוגמה **מומצאת** למחיר באלפי שקלים: ŷ=10x+200 כאשר x הוא שטח במ״ר. עבור x=50 התחזית היא 700; אם המחיר האמיתי הוא 750, השארית actual−predicted היא +50. המחיר האמיתי גבוה מהתחזית: המודל העריך בחסר. זו אינה הערכת מחיר שוק.
ב־Penguins השיפוע יהיה ביחידות גרם למ״מ. שיפוע חיובי מתאר עלייה בתחזית עם המאפיין, לא הוכחה שהגדלת המדידה גורמת לעלייה במסה.
LinearRegression מתאים w,b כך שסכום ריבועי השאריות באימון יהיה קטן ככל האפשר בין הישרים. אין צורך בגזירה או בחישוב מקדמים ידני בשיעור זה.

### תא קוד 4
```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import r2_score
```

## 2. מקור ושינוי תפקיד העמודות
משתמשים בעותק Penguins של הקורס, 344 שורות ו־7 עמודות. מקור: Gorman ו־Palmer Station LTER; תיעוד וייחוס [palmerpenguins](https://github.com/allisonhorst/palmerpenguins), Horst, Hill & Gorman (2020), DOI:10.5281/zenodo.3960218.
X הוא מאפיין מספרי אחד, y הוא מסה בגרמים. המסה אינה ב־X; species אינו היעד הפעם. נשמור מקור ללא שינוי.
המאגר משמש להוראה, ואין בכך אישור התאמה לפרויקט גמר.

### תא קוד 6
```python
url = "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df = pd.read_csv(url)
display(df.head())
display(df[["flipper_length_mm", "bill_length_mm", "body_mass_g"]].isna().sum())
```

## 3. חלוקה והכנה מוכרת
לא משלימים y חסר: תחזית שמשווים ליעד מומצא אינה בדיקה תקפה. נשארות 342 תצפיות בעלות מסה ידועה. מחלקים יחד 75%/25%, ואז לומדים ממוצע השלמה מ־X_train בלבד.
אין stratify לפי y המספרי הרציף. ההשלמה נשמרת בקוד כדי לתעד תהליך; בעותק הנוכחי שני חסרי המדידות חופפים לשתי המסות החסרות, ולכן לאחר בחירת יעד ידוע לא נותרו חסרים במאפיין.
לא מוסיפים StandardScaler באופן אוטומטי: ברגרסיה ליניארית רגילה עם חיתוך ומאפיין אחד הוא אינו נדרש כדי למנוע שליטת יחידות במרחק. כאן אין הצבעת שכנים. שמירת היחידות המקוריות מקלה על פירוש השיפוע.

### תא קוד 8
```python
# לא משלימים יעד חסר; משתמשים בעותק עבודה
model_df = df.dropna(subset=["body_mass_g"]).copy()
feature = "flipper_length_mm"
X = model_df[[feature]].copy()
y = model_df["body_mass_g"].copy()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
training_means = X_train.mean()
X_train_ready = X_train.fillna(training_means)
X_test_ready = X_test.fillna(training_means)
print("Eligible:", len(model_df), "Train:", len(X_train), "Test:", len(X_test))
print("Train feature range:", X_train_ready[feature].min(), X_train_ready[feature].max())
```

## 4. מאמנים ומנבאים
fit מקבל מדידות ותוויות אימון מספריות; predict מקבל X בלבד. coef_[0] הוא השיפוע היחיד; intercept_ הוא החיתוך. הקריאה הזו למקדמים נתונה ואינה דורשת לימוד תכנות מונחה עצמים.
פרשו את השיפוע כגידול בתחזית בגרמים לכל מ״מ נוסף. החיתוך מתאר תחזית ב־x=0, אך אפס אינו בהכרח ערך רלוונטי לפינגווין. אין להסיק ממנו טענה ביולוגית.

### תא קוד 10
```python
model = LinearRegression()
model.fit(X_train_ready, y_train)
predictions = model.predict(X_test_ready)
w = model.coef_[0]
b = model.intercept_
print("Slope (g/mm):", w, "Intercept (g):", b)
new_penguin = pd.DataFrame({feature: [200]})
new_prediction = model.predict(new_penguin)
print("New feature value (mm):", 200, "Predicted mass (g):", new_prediction[0])
```

## 5. מסתכלים על קו ועל נקודות
הישר מותאם לאימון בלבד; נקודות הבדיקה מסומנות בנפרד. קוד הציור נתון. צבע הנקודות אינו מחלקת מין כאן. הקו לא חייב לעבור דרך כל תצפית, ותחזית אינה חייבת להיות מסה שהופיעה במאגר.

### תא קוד 12
```python
# קטע ציור נתון; ממיינים את X כדי לצייר ישר בלי חיבור בזיגזג
line_X = X_train_ready.sort_values(feature)
line_y = model.predict(line_X)
plt.figure()
plt.scatter(X_train_ready[feature], y_train, alpha=0.35, label="Train")
plt.scatter(X_test_ready[feature], y_test, alpha=0.65, label="Test")
plt.plot(line_X[feature], line_y, color="black", label="Line fitted on Train")
plt.xlabel(feature + " (mm)")
plt.ylabel("body_mass_g (g)")
plt.title("Penguins — one-feature linear regression")
plt.legend()
plt.tight_layout()
plt.show()
```

## 6. שאריות — מה הכיוון ומה היחידה?
$$e_i=y_i-\hat y_i$$
שארית חיובית: המסה האמיתית גבוהה מהתחזית, כלומר הערכת חסר. שלילית: הערכת יתר. שארית אפס: התאמה באותה תצפית.
היחידה היא גרם; ריבוע שארית בגרם². לא מחברים רק שאריות חתומות כדי למדוד גודל טעות, מפני שטעויות יכולות להתקזז.
התרשים הבא הוא בדיקה ראשונית של פיזור הטעויות, לא מבחן נורמליות ולא הוכחת תקינות כל הנחות המודל. אין חובה שממוצע שאריות Test יהיה אפס.

### תא קוד 14
```python
comparison = pd.DataFrame(
    {"actual_g": y_test, "predicted_g": predictions}, index=y_test.index
)
comparison["residual_g"] = comparison["actual_g"] - comparison["predicted_g"]
display(comparison.head(8))
plt.figure()
plt.scatter(comparison["predicted_g"], comparison["residual_g"], alpha=0.6)
plt.axhline(0, color="black")
plt.xlabel("Predicted mass (g)")
plt.ylabel("Residual: actual - predicted (g)")
plt.title("Test residuals")
plt.tight_layout()
plt.show()
```

## 7. R² — השוואת סכומי ריבועים
$$R^2=1-\frac{\sum_i(y_i-\hat y_i)^2}{\sum_i(y_i-\bar y_{Test})^2}=1-\frac{SSE}{SST}$$
SSE הוא סכום ריבועי טעויות המודל; SST מתאר את הפיזור סביב ממוצע היעדים בקבוצת ההערכה.
R²=1 מציין תחזיות מושלמות בקבוצה זו; R²=0 מציין SSE השווה ל־SST; ערך שלילי אומר ש־SSE גדול מ־SST. זה אינו אחוז התחזיות הנכונות, אינו Accuracy ואינו ביחידות גרם.
**דוגמה ידנית מומצאת:** אמת [10,20,30], תחזית [12,18,30]. הממוצע 20, SSE=8,SST=200 ולכן R²=0.96. תחזית קבועה 40 לכל שלוש הדוגמאות נותנת SSE=1400 ולכן R²=−6 — המדד אינו חייב להיות בין 0 ל־1.
ממוצע Test מופיע בהגדרת מדד לאחר החיזוי. אין להשתמש בו כמידע לבניית תחזית. קו הבסיס המעשי שנריץ לומד ממוצע מ־Train, ולכן ה־R² שלו ב־Test אינו חייב להיות בדיוק אפס.
הנוסחה הידנית דורשת לפחות שתי דוגמאות ויעדי בדיקה שאינם כולם זהים; כאן תנאים אלה מתקיימים.

### תא קוד 16
```python
# בדיקת הדוגמה הידנית בלבד, ללא אימון או CSV
toy_actual = pd.Series([10.0, 20.0, 30.0])
toy_predicted = pd.Series([12.0, 18.0, 30.0])
toy_sse = ((toy_actual - toy_predicted) ** 2).sum()
toy_sst = ((toy_actual - toy_actual.mean()) ** 2).sum()
print("Toy SSE:", toy_sse, "SST:", toy_sst, "R²:", 1 - toy_sse / toy_sst)
print("Poor prediction R²:", r2_score(toy_actual, [40, 40, 40]))
```

### תא קוד 17
```python
# ממוצע y_test משמש רק להגדרת המדד, לא ליצירת תחזיות
sse = (comparison["residual_g"] ** 2).sum()
test_mean = y_test.mean()
sst = ((y_test - test_mean) ** 2).sum()
r2_manual = 1 - sse / sst
r2_test = r2_score(y_test, predictions)
print("SSE:", sse, "SST:", sst)
print("R² manual:", r2_manual, "R² library:", r2_test)

# קו בסיס מעשי: חיזוי ממוצע שנלמד מאימון בלבד
baseline = DummyRegressor(strategy="mean")
baseline.fit(X_train_ready, y_train)
baseline_predictions = baseline.predict(X_test_ready)
baseline_r2 = r2_score(y_test, baseline_predictions)
print("Training mean baseline (g):", baseline.constant_[0, 0])
print("Baseline R² on same Test:", baseline_r2)
```

## 8. תיעוד והעברה לפרויקט
כתבו שאלה, X/y ויחידות, מקור, מדיניות חסרים וחלוקה, משוואת הישר שנלמדה, תחזית לדוגמה, שארית אחת, R² של Test ושל קו הבסיס ומגבלה.
אין להשתמש ב־confusion_matrix או ב־Precision ליעד מסה רציף, ואין לעגל תחזיות כדי לספור "נכונות".
מודל עם מאפיין אחד אינו מתאר את כל ההבדלים בין מינים/פרטים. קשר סטטיסטי אינו סיבתיות; קו יחיד על קבוצות מעורבות עשוי להסתיר דפוסים שונים. אין לשנות מאפיינים לאחר צפייה ב־Test ואז להציגו כהערכה עצמאית.
תחזיות מחוץ לטווח האימון הן אקסטרפולציה: התבנית עלולה להשתנות, ואין להניח שהקו ממשיך להיות מתאים. גם בתוך הטווח אין התחייבות לשגיאה קטנה.
**כרטיס יציאה:** מה שונה ב־y לעומת שיעור KNN? מה אומרת שארית של −300 גרם? מדוע R²=0.8 אינו "80% מהתחזיות נכונות"?


---

## חלק ב — תרגול תלמיד ללא פתרון
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 27 — רגרסיה ליניארית: תרגול עצמאי

**פתיחה:** דודו שואל אם אורך סנפיר יכול לעזור להעריך מסה של פינגווין שלא נשקל. הפלט הוא מספר בגרמים, לא שם מין. זו דוגמת מחקר לימודית; תחזית אינה תחליף אוטומטי למדידה.
באותו מאגר אפשר להגדיר שאלות שונות: סיווג species לעומת רגרסיה של body_mass_g. מספר שמשמש קוד קטגוריה אינו הופך יעד לרגרסיה — המשמעות קובעת.

עוגן: [סיכום הרגרסיה ביחידה 3](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/04-Introduction-to-ML/Linear-Regression-Intro/Didactic-Summary.md) ו[מחברת המבוא](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/04-Introduction-to-ML/Linear-Regression-Intro/Linear-Regression-Intro.ipynb). זוהי התאמה שלנו מ־Iris ל־Penguins והוספת הערכה ב־Test. חומרי המקור נשמרו; אין כאן תרגיל מקור חדש מהמרצה.

## למה לומדים את זה עכשיו?
לחזות מחיר מחשב הוא לנבא מספר, בניגוד לסיווג סוג המחשב.
**בתהליך הפרויקט:** מודל רגרסיה.
**מסגרת פעילה:** 2 שעות לימוד — 90 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.
**התרגול הנבחר למסגרת זו:** קו בעל מאפיין אחד, שאריות, R² וקו בסיס; MAE וכמה מאפיינים ב־39.

התרגול משתמש באורך מקור במקום סנפיר ובחלוקה אחרת. אין צורך לכתוב קוד ציור מאפס; מותר להיעזר בקטעים הנתונים במודרכת. תאי המשימות ריקים בכוונה. אין ציון R² נדרש מראש.

### תא קוד 4
```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import r2_score
```

### תא קוד 5
```python
url = "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df = pd.read_csv(url)
display(df.head())
display(df[["flipper_length_mm", "bill_length_mm", "body_mass_g"]].isna().sum())
```

## 1. הגדרת חקר והכנה
נחזה body_mass_g לפי bill_length_mm בלבד. כתבו סוג בעיה ויחידות. השאירו בעותק עבודה רק יעד ידוע; הגדירו X כטבלה ו־y כסדרה. חלקו test_size=0.25, random_state=17 ללא stratify לפי המסה, ולמדו ממוצע השלמה מאימון בלבד.

### תא קוד 7
```python
# כתבו כאן את הקוד שלכם
```

**תיעוד ומסקנה:** כתבו כאן.

## 2. התאמת ישר ותחזית
אמנו LinearRegression, הציגו שיפוע וחיתוך ופרשו את יחידותיהם. חזו מסה עבור אורך מקור 45 מ״מ באמצעות DataFrame בעל שם העמודה המתאים. בדקו אם 45 נמצא בטווח האימון; הסבירו מגבלה גם אם כן.

### תא קוד 10
```python
# כתבו כאן את הקוד שלכם
```

**תיעוד ומסקנה:** כתבו כאן.

## 3. תרשים ושאריות
הציגו נקודות אימון/בדיקה וקו מותאם לאימון. צרו טבלת actual_g,predicted_g,residual_g באינדקס הבדיקה ותרשים שאריות. בחרו שתי דוגמאות ופרשו את סימן השארית ואת יחידתה.

### תא קוד 13
```python
# כתבו כאן את הקוד שלכם
```

**תיעוד ומסקנה:** כתבו כאן.

## 4. R² וקו בסיס
חשבו SSE ו־SST לפי ממוצע y_test, ו־R² ביד וב־r2_score. הסבירו מדוע שימוש בממוצע זה לצורך הגדרת מדד אינו היתר ללמוד ממנו תחזיות. אמנו DummyRegressor(strategy='mean') על האימון והשוו ב־Test. האם קו הבסיס חייב לקבל בדיוק אפס? נמקו.

### תא קוד 16
```python
# כתבו כאן את הקוד שלכם
```

**תיעוד ומסקנה:** כתבו כאן.

## 5. פירוש ותיעוד לפרויקט
השלימו כרטיס מודל עם התוצאות שהתקבלו, מגבלה אחת של שימוש במאפיין יחיד ואחת של הכללה. מדוע אין להשתמש ב־Accuracy? האם R² שלילי אפשרי? אין להשוות את ציוני שתי המחברות כהוכחה לעדיפות מאפיין, כי גם החלוקה שונה.

### תא קוד 19
```python
# כתבו כאן את הקוד שלכם
```

**תיעוד ומסקנה:** כתבו כאן.

