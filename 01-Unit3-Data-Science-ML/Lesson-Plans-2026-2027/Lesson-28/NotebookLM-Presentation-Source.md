# מקור למצגת — שיעור 28 — הכללה ובחירת K בלי לבחור לפי Test
**קהל:** תלמידי כיתה י׳ מתחילים. **מכסה:** 4 שעות לימוד (180 דקות), כולל תרגול; המצגת מחליפה חלק מההסבר ואינה מוסיפה זמן.
**שלב בתהליך החקר:** אימות ובחירה.
**פתיחה מוכרת:** תרגול חוזר של אותן שאלות אינו בחינה חדשה: איך בוחרים מודל בלי להציץ בתשובות הבחינה?
**גבולות הליבה במצגת ובתרגול:** חלוקות, Over/Underfit, טבלת CV ובחירת K בתוך אימון; Pipeline מוסבר בשלבים.
**המחשה חזותית מומלצת:** Train החיצוני מתפצל לקיפוליCV, ו־Test נשארבתיבה נפרדת עדהסוף. בכל קיפול הכנה נלמדת מחדש. הציגו טבלת מועמדים, לא לולאתציוניTest.
**זיקה להמשך:** הזיקה המרכזית היא לבסיס וקטורי, סטטיסטי או להערכת מודלים; השתמשו רק בזיקה המפורשת בחומר, כקדימות להמשך ולא כהוראת יחידה 5 מלאה.

## הוראות למניעת ערבוב דוגמה ותרגול
חלק א הוא דוגמה פתורה שאפשר להסביר ולפתור בשקפים. חלק ב הוא תרגול עצמאי: מציגים את הדרישה, מפרקים לשלבים ונותנים רמזים; אין מייצרים פתרון מלא,קוד מלא או תוצאות סופיות של המשימות הנבחרות. אין בקובץ פתרוןמתועד לתרגול. חומר עודף במחברות מיועד לחזרה; גבולותהליבה לעיל גוברים על שאיפה לכסותכל תא.
דוגמאות מומצאות אינן מאגר אמיתי. קישורים הם ייחוס; אין להניח שתוכנם נכלל אוטומטית במקור שהועלה. לא להמציא פלט,דיוק או גרף מאומת כשהם אינם מופיעים בטקסט.

## חלק א — הסבר ודוגמה פתורה
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 28 — הכללה ובחירת K בלי לבחור לפי Test

**פתיחה:** דודו קיבל ציון גבוה אחרי שתרגל את אותן שאלות שוב ושוב. האם זה מעיד שיצליח בשאלות חדשות? גם מודל עלול להתאים היטב לדוגמאות האימון ולהתקשות בדוגמאות אחרות.
היום קובעים מראש מדד וערכי K, בוחרים ב־CV על אימון בלבד, ומתאימים מודל סופי לפני הערכת Test.

עוגן: [סיכום מפגש 8](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/09-ML-Fundamentals/Meeting-08-Didactic-Summary.md) ו[מחברת בחירת מודל](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/09-ML-Fundamentals/Meeting-08-Model-Selection-Guided.ipynb). זו התאמה דידקטית: בלי לולאת ציוני Test, עם השלמה בתוך Pipeline ועם macro-F1 קבוע מראש. חומרי המקור לא שונו.
**גבול ההדגמה:** Penguins כבר נבדק בכיתה/בחומרי ההוראה הקודמים. הקוד מדגים הפרדה נכונה בהרצה זו, אך הציון אינו מבחן עצמאי חדש של מאגר שלא הכרנו. בפרויקט חדש שומרים Test מתחילת העבודה ומדווחים אם השפיע על החלטות. אין טענה שהשיעורים הועברו בכיתה בלי דיווח המורה.

## למה לומדים את זה עכשיו?
תרגול חוזר של אותן שאלות אינו בחינה חדשה: איך בוחרים מודל בלי להציץ בתשובות הבחינה?
**בתהליך הפרויקט:** אימות ובחירה.
**מסגרת פעילה:** 4 שעות לימוד — 180 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.

## 1. התאמת חסר, התאמת יתר והכללה
- **Underfitting — התאמת חסר:** המודל מוגבל מדי ביחס לדפוס שנרצה ללמוד; יכול להתקשות כבר באימון וגם באימות.
- **Overfitting — התאמת יתר:** התאמה לפרטים ולרעש באימון שאינם מועילים בנתונים אחרים; לעיתים רואים ציון אימון גבוה ופער לאימות.
- **הכללה:** הצלחה על דוגמאות חדשות מן ההקשר שאליו רוצים להפעיל את המודל.

K קטן נוטה לתת החלטה רגישה לדוגמאות בודדות; K גדול מחליק אותה ועלול להיות מוגבל מדי. אלה נטיות, לא חוק. פער קטן אינו הוכחת Overfit, וציון נמוך יכול לנבוע גם ממאפיינים חלשים או מרעש.
בטבלה הבאה הציונים מומצאים. בחרו K לפי Validation, לא לפי Train. הסבירו איזה דפוס מתאים לחשש להתאמת יתר ואיזה להתאמת חסר. אין לדרוש מאותה מגמה להופיע בדיוק בנתונים האמיתיים.

### תא קוד 4
```python
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
```

### תא קוד 5
```python
# ציונים דידקטיים מומצאים, לא תוצאות Penguins
illustration = pd.DataFrame({
    "K": [1, 7, 101],
    "Train": [0.99, 0.92, 0.60],
    "Validation": [0.71, 0.90, 0.58]
})
display(illustration)
```

## 2. מי עושה מה?
| חלק | תפקיד | מה מותר ללמוד ממנו? |
|---|---|---|
| אימון פנימי | התאמת הכנה ומודל בקיפול | ממוצעי השלמה, תקנון ודוגמאות KNN |
| Validation פנימי | השוואת K | ציונים לבחירת היפר־פרמטר |
| Test חיצוני | הערכה אחרי סגירת הבחירה | דיווח ביצועים, ללא כוונון נוסף |

K הוא היפר־פרמטר שמחליטים להשוות. ברגרסיה w,b הם פרמטרים שהאימון לומד. KNN שומר דוגמאות לצורך חיפוש שכנים; אין בו מקדם קו כמו ברגרסיה.
CV ממלא כאן את תפקיד ה־Validation, ואינו דורש ליצור בנוסף קבוצת Validation קבועה.

**המחשה בלבד בשלושה קיפולים בתוך Train:**
| סבב | אימון פנימי | Validation |
|---|---|---|
| 1 | B+C | A |
| 2 | A+C | B |
| 3 | A+B | C |

Test אינו A, B או C. בקוד נעשה חמישה קיפולים. כל רשומת Train משמשת לאימות פעם אחת עבור כל K, ובאימון בארבעה סבבים. אין חמש קבוצות Test חיצוניות.

## 3. נתונים והפרדה
היעד species והמאפיינים הם שתי מדידות מספריות. שורות ללא יעד אינן דוגמאות מפוקחות; לא ממלאים יעד חסר.
הנתונים: עותק Penguins של הקורס, 344 רשומות ו־7 עמודות. מקור Gorman ו־Palmer Station LTER; [תיעוד וייחוס](https://github.com/allisonhorst/palmerpenguins), Horst, Hill & Gorman (2020), DOI:10.5281/zenodo.3960218. אין בכך אישור התאמה לפרויקט גמר.
משאירים חסרי X לטיפול בתוך כל קיפול; לא משלימים או מתקננים את כל X_train מראש.

### תא קוד 8
```python
url = "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df = pd.read_csv(url)
model_df = df.dropna(subset=["species"]).copy()
features = ["flipper_length_mm","body_mass_g"]
X = model_df[features].copy()
y = model_df["species"].copy()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
print("Outer Train:", len(X_train), "Outer Test:", len(X_test))
display(X_train.isna().sum())
```

## 4. Pipeline — אותו מתכון בכל קיפול
1. SimpleImputer(strategy="mean") לומד ממוצעים רק מהאימון הפנימי. זו אותה מדיניות fillna שנלמדה, בתוך כלי שמתחבר ל־CV.
2. StandardScaler לומד מהאימון הפנימי לאחר ההשלמה.
3. KNN שומר את דוגמאות האימון שעברו הכנה.

באימות מפעילים את ההמרות שנלמדו, ללא fit על חלק האימות. cross_validate יוצר התאמות נפרדות לכל קיפול ולכל K; הוא אינו מעביר ידע שנלמד בקיפול אחד לאחר.
הקוד מובא כתבנית נתונה עם לולאה מוכרת. אין צורך בלימוד מחלקות, פונקציות מתקדמות, GridSearchCV או רשימות מקוננות מאפס.

נקבע מראש scoring="f1_macro": ממוצע F1 פשוט לכל המינים, כדי לתת לכל מין משקל שווה. זהו שינוי מסומן מ־Accuracy שבדוגמת המקור. אין בוחרים את המדד לאחר שרואים איזה מהם גבוה יותר.
$$\overline{F1}_{CV}=\frac{F1_1+F1_2+F1_3+F1_4+F1_5}{5}$$
cv_std היא סטיית תקן תיאורית בין חמשת הציונים (ddof=0); היא אינה רווח סמך ואינה הוכחת יציבות בכל אוכלוסייה.

### תא קוד 10
```python
# ההגדרות נקבעות לפני צפייה בהערכת Test
candidates = [1, 3, 5, 15, 51]
metric = "f1_macro"
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
results = []

# קוד תהליך נתון: המטרה להבין מה נכנס ל-CV ומה נשאר בחוץ
for k in candidates:
    pipe = make_pipeline(
        SimpleImputer(strategy="mean"),
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=k, weights="uniform", metric="euclidean")
    )
    fold_results = cross_validate(
        pipe, X_train, y_train,
        cv=cv, scoring=metric, return_train_score=True, n_jobs=1
    )
    # test_score כאן הוא Validation פנימי של הקיפול, לא ה-Test החיצוני
    results.append([
        k,
        fold_results["train_score"].mean(),
        fold_results["test_score"].mean(),
        fold_results["test_score"].std(ddof=0)
    ])

results_df = pd.DataFrame(results, columns=["K", "train_mean", "cv_mean", "cv_std"])
display(results_df)
```

**עצירת הבנה:** השוו train_mean ל־cv_mean. בחרו את שורת הממוצע הגבוה לפני המשך. האם K עם ציון האימון הגבוה נבחר בהכרח? אל תכפו על הנתונים האמיתיים את דפוס הטבלה המומצאת.

## 5. בוחרים ומאמנים מחדש
נבחר את ממוצע CV הגבוה ביותר מבין המועמדים שנקבעו. אם יש שוויון מספרי מדויק, כלל ההכרעה הנתון בוחר K קטן יותר; זו מדיניות תרגיל ולא טענה ש־K קטן תמיד עדיף.
כאשר ההבדלים קטנים, אין להכריז על עליונות ודאית. הבחירה היא בין המועמדים שנבדקו, לא "K הטוב בעולם".
אחרי הבחירה מתאימים Pipeline חדש לכל Train החיצוני: ממוצעי ההשלמה והתקנון נלמדים מחדש מכל Train זה. חמשת מודלי הקיפולים אינם מצביעים יחד במודל הסופי.

### תא קוד 13
```python
# כלל שנקבע מראש: ממוצע CV הגבוה ביותר; בשוויון מדויק K הקטן יותר
# המיון והגישה לשורה הם קטע עזר נתון
ranked = results_df.sort_values(["cv_mean", "K"], ascending=[False, True])
best_k = int(ranked.iloc[0]["K"])
print("Selected K by CV only:", best_k)

# מתאימים צינור חדש לכל קבוצת האימון החיצונית
final_model = make_pipeline(
    SimpleImputer(strategy="mean"),
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=best_k, weights="uniform", metric="euclidean")
)
final_model.fit(X_train, y_train)
```

## 6. רק עכשיו — הערכה
הריצו את התא הבא לאחר סגירת הבחירה. מפיקים כמה מדדים מאותן תחזיות לצורך דיווח; לא בוחרים מודל מחדש באמצעותם. השימוש ב־Penguins הוא הדגמת פרוטוקול על נתונים מוכרים, כפי שסויג בתחילת המחברת.

### תא קוד 15
```python
# רק לאחר בחירת K והתאמה מחדש: הערכה אחת על Test החיצוני
predictions = final_model.predict(X_test)
test_accuracy = accuracy_score(y_test, predictions)
labels_species = ["Adelie", "Chinstrap", "Gentoo"]
report = classification_report(
    y_test, predictions, labels=labels_species,
    output_dict=True, zero_division=0
)
report_table = pd.DataFrame(report).T
display(report_table.loc[labels_species, ["precision", "recall", "f1-score", "support"]])
test_macro_f1 = report["macro avg"]["f1-score"]
print("CV selection metric:", metric)
print("Selected model Test macro-F1:", test_macro_f1)
print("Selected model Test Accuracy:", test_accuracy)
```

## 7. מסקנה לפרויקט
תעדו מראש מאפיינים, יעד, רשימת K, מדד, חלוקה וקיפולים; צרפו את טבלת ה־CV, K שנבחר, הערכת Test ומגבלה.
אין להשוות ציוני CV ו־Test כאילו אחד מהם חייב להיות גדול מהאחר. אינם אותם דוגמאות או אותם גדלי אימון. CV אינו מבטיח הצלחה באוכלוסייה חדשה.
אם חוזרים לשנות K/מאפיינים/מדד לפי Test, יש לדווח שהתוצאה כבר אינה הערכה בלתי תלויה; אין "לאפס" זאת באמצעות שינוי seed.
בנתונים תלויי זמן או בכמה רשומות לאותו אדם/מוצר, חלוקה אקראית רגילה עשויה לא להתאים. צריך חלוקה לפי זמן או קבוצות בהתאם לשאלת הפרויקט.
**כרטיס יציאה:** למה Pipeline חייב להיות בתוך CV? מה ההבדל בין test_score שבמילון הקיפולים לבין Test החיצוני? מה עושים אחרי בחירת K ולפני הערכה סופית?


---

## חלק ב — תרגול תלמיד ללא פתרון
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 28 — תרגול עצמאי — אימות ובחירת K

**פתיחה:** דודו קיבל ציון גבוה אחרי שתרגל את אותן שאלות שוב ושוב. האם זה מעיד שיצליח בשאלות חדשות? גם מודל עלול להתאים היטב לדוגמאות האימון ולהתקשות בדוגמאות אחרות.
היום קובעים מראש מדד וערכי K, בוחרים ב־CV על אימון בלבד, ומתאימים מודל סופי לפני הערכת Test.

עוגן: [סיכום מפגש 8](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/09-ML-Fundamentals/Meeting-08-Didactic-Summary.md) ו[מחברת בחירת מודל](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/09-ML-Fundamentals/Meeting-08-Model-Selection-Guided.ipynb). זו התאמה דידקטית: בלי לולאת ציוני Test, עם השלמה בתוך Pipeline ועם macro-F1 קבוע מראש. חומרי המקור לא שונו.
**גבול ההדגמה:** Penguins כבר נבדק בכיתה/בחומרי ההוראה הקודמים. הקוד מדגים הפרדה נכונה בהרצה זו, אך הציון אינו מבחן עצמאי חדש של מאגר שלא הכרנו. בפרויקט חדש שומרים Test מתחילת העבודה ומדווחים אם השפיע על החלטות. אין טענה שהשיעורים הועברו בכיתה בלי דיווח המורה.

## למה לומדים את זה עכשיו?
תרגול חוזר של אותן שאלות אינו בחינה חדשה: איך בוחרים מודל בלי להציץ בתשובות הבחינה?
**בתהליך הפרויקט:** אימות ובחירה.
**מסגרת פעילה:** 4 שעות לימוד — 180 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.
**התרגול הנבחר למסגרת זו:** חלוקות, Over/Underfit, טבלת CV ובחירת K בתוך אימון; Pipeline מוסבר בשלבים.

קוד ה־Pipeline וה־CV במודרכת הוא תבנית עבודה נתונה; אפשר להעתיקו לתאי העבודה ולנמק כל שלב. הנתונים חדשים מבחינת משימת התרגול אך אינם מאגר חדש שלא הכרנו. התאים ריקים בכוונה ואין K נדרש מראש.

### תא קוד 4
```python
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
```

## 1. מסבירים ובונים חלוקה
הסבירו מה תפקיד Train,Validation,Test ומהו K. בחרו מראש bill_length_mm,bill_depth_mm לניבוי species. חלקו test_size=0.25,random_state=17,stratify=y; אל תמלאו או תתקננו את הנתונים מראש.

### תא קוד 6
```python
# כתבו כאן את הקוד שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## 2. משלימים תהליך CV
השתמשו בתבנית הלולאה במודרכת, עם candidates=[1,3,5,15,51],scoring='f1_macro' וחמישה קיפולים משוכבים,shuffle=True,random_state=42. בכל קיפול Pipeline עם השלמת ממוצע,תקנון ו־KNN. הציגו train_mean,cv_mean,cv_std. אילו נתונים נמסרים לפונקציית CV?

### תא קוד 9
```python
# כתבו כאן את הקוד שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## 3. בוחרים K ומנמקים
בחרו לפי ממוצע CV הגבוה ביותר ובשוויון מדויק K הקטן יותר. כתבו נימוק מתוך הטבלה. אין לדרוש K מסוים ואין לבחור לפי ציון Train. הסבירו אם יש חשש להתאמת יתר/חסר ומה אי אפשר להסיק מהטבלה לבדה.

### תא קוד 12
```python
# כתבו כאן את הקוד שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## 4. התאמה מחדש והערכה
אמנו Pipeline חדש עם K שנבחר על כל Train החיצוני. רק עכשיו צרו תחזיות Test והציגו macro-F1,Accuracy ודוח לפי מין. אין לשנות החלטות לפי התוצאה. הסבירו מדוע זו עדיין הדגמה על נתונים מוכרים ולא מבחן בלתי תלוי חדש.

### תא קוד 15
```python
# כתבו כאן את הקוד שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## 5. תיעוד והעברה לפרויקט
כתבו כרטיס ניסוי: רשימת מועמדים,מדד,חלוקה,קיפולים,כלל הכרעה,K נבחר,דוח ומגבלה. הסבירו מה יזלוג אם נתקנן את כל X_train לפני CV, ומהו ההבדל בין cv_std לרווח סמך. הציעו חלוקה מתאימה אם כמה רשומות שייכות לאותו אדם.

### תא קוד 18
```python
# כתבו כאן את הקוד שלכם
```

**הסבר ומסקנה:** כתבו כאן.

