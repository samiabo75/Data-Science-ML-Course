# מקור למצגת — שיעור 37 — Pipeline, param_grid ו־GridSearchCV — חקר פרמטרים מלא
**קהל:** תלמידי כיתה י׳ מתחילים. **מכסה:** 4 שעות לימוד (180 דקות), כולל תרגול; המצגת מחליפה חלק מההסבר ואינה מוסיפה זמן.
**שלב בתהליך החקר:** הכנה ואימות.
**פתיחה מוכרת:** כדי להשוות המלצות על מחשבים משנים K באופן מסודר ומשווים על אותן חלוקות.
**גבולות הליבה במצגת ובתרגול:** שעה הכנה משולבת, שעה קו בסיס, שעתיים GridSearch ותוצאות. לא מוסיפים זמן בחלקי הכנה אחרים.
**המחשה חזותית מומלצת:** שני מסלולי ColumnTransformer מתאחדיםל־Pipeline;param_grid הוא רשימתמועמדים;CV→cv_results_→best_params_→refit→Test. mean_test_score הואאימותבקיפולים, לאTest החיצוני.
**זיקה להמשך:** הזיקה המרכזית היא לבסיס וקטורי, סטטיסטי או להערכת מודלים; השתמשו רק בזיקה המפורשת בחומר, כקדימות להמשך ולא כהוראת יחידה 5 מלאה.

## הוראות למניעת ערבוב דוגמה ותרגול
חלק א הוא דוגמה פתורה שאפשר להסביר ולפתור בשקפים. חלק ב הוא תרגול עצמאי: מציגים את הדרישה, מפרקים לשלבים ונותנים רמזים; אין מייצרים פתרון מלא,קוד מלא או תוצאות סופיות של המשימות הנבחרות. אין בקובץ פתרוןמתועד לתרגול. חומר עודף במחברות מיועד לחזרה; גבולותהליבה לעיל גוברים על שאיפה לכסותכל תא.
דוגמאות מומצאות אינן מאגר אמיתי. קישורים הם ייחוס; אין להניח שתוכנם נכלל אוטומטית במקור שהועלה. לא להמציא פלט,דיוק או גרף מאומת כשהם אינם מופיעים בטקסט.

## חלק א — הסבר ודוגמה פתורה
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 37 — Pipeline, param_grid ו־GridSearchCV — חקר פרמטרים מלא
**פתיחה:** דודו צריך לבחור K,לשחזר את הניסוי ולהסביר לבוחן מה החיפוש עשה. נחבר גם מאפיינים מספריים וקטגוריאליים,כמו בפרויקטי FTC והמכוניות.

**עוגן:** [סיכום מפגש 8](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/09-ML-Fundamentals/Meeting-08-Didactic-Summary.md) ו[מחברת GridSearch](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/09-ML-Fundamentals/Meeting-08-GridSearch-Extension.ipynb). אף שכותרת המקור מסמנת רשות,ברשימת הבחינה שהמורה מסר האובייקטים מופיעים במפורש,ולכן הם יעד הוראה והערכה בתכנון שלנו.
אלה חומרים מותאמים חדשים,לא שחזור תרגיל מקור. חומרי ההשתלמות לא שונו.


## למה לומדים את זה עכשיו?
כדי להשוות המלצות על מחשבים משנים K באופן מסודר ומשווים על אותן חלוקות.
**בתהליך הפרויקט:** הכנה ואימות.
**מסגרת פעילה:** 4 שעות לימוד — 180 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.

## משמעות מתמטית ומושגים
param_grid מגדיר מועמדים ולא פרמטרים שנלמדו. עבור 3 ערכי K וחמישה קיפולים יש 15 התאמות CV;refit=True מוסיף התאמה 16 על כל Train. mean_test_score הוא ממוצע ציוני האימות הפנימיים ולא ציון Test החיצוני. best_params_ מציג את המועמד שנבחר לפי המדד;best_score_ הוא ממוצע CV שלו. std_test_score הוא פיזור תיאורי של קיפולים,לא רווח סמך. בשוויון GridSearchCV בוחר את המועמד הראשון בדירוג סדר החיפוש;אין הבטחה לעליונות מובהקת.

## בחירת קלטים והפרדה
Penguins:344×7,יעד species. משתמשים בעותק הקורס;אי אינו מזהה גאוגרפי הנמדד במרחק מספרי. מקור Gorman ו־Palmer Station LTER;תיעוד palmerpenguins,Horst,Hill & Gorman (2020),DOI:10.5281/zenodo.3960218. Penguins כבר מוכר מהשיעורים הקודמים ולכן זו הדגמת פרוטוקול,לא מבחן עצמאי חדש.

### תא קוד 5
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score
url="https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df=pd.read_csv(url)
data=df.dropna(subset=["species"]).copy()
numeric=["bill_length_mm","bill_depth_mm"]
categorical=["island"]
X=data[numeric+categorical].copy()
y=data["species"].copy()
X_train,X_test,y_train,y_test=train_test_split(
 X,y,test_size=.25,random_state=42,stratify=y)
print("Train:",X_train.shape,"Test:",X_test.shape)

```

## הכנה משולבת בתוך המודל
ColumnTransformer מחיל כל מסלול על העמודות שנבחרו ומצרף את התוצאות. מספריים:השלמת חציון ותקנון;קטגוריאלי:השלמת שכיח ו־One-Hot. כל fit יתבצע בתוך אימון הקיפול. sparse_output=False מפשט את צורת הפלט בתרגיל.

### תא קוד 7
```python
numeric_pipeline=Pipeline([
 ("fill",SimpleImputer(strategy="median")),
 ("scale",StandardScaler())
])
categorical_pipeline=Pipeline([
 ("fill",SimpleImputer(strategy="most_frequent")),
 ("encode",OneHotEncoder(handle_unknown="ignore",sparse_output=False))
])
prepare=ColumnTransformer([
 ("numeric",numeric_pipeline,numeric),
 ("categorical",categorical_pipeline,categorical)
],remainder="drop")
pipe=Pipeline([
 ("prepare",prepare),
 ("knn",KNeighborsClassifier(weights="uniform",metric="euclidean"))
])

```

## המועמדים והחיפוש
הקידומת knn היא שם שלב ה־Pipeline;שני קווים תחתונים מעבירים לפרמטר של אותו שלב. clf הוא אובייקט החיפוש,pipe הוא מתכון מודל. מסבירים מה כל אחד מקבל ומה נשמר לאחר fit.

### תא קוד 9
```python
# ההגדרות נבחרו מראש,בלי שימוש בציוני Test
param_grid={"knn__n_neighbors":[3,5,9]}
cv=StratifiedKFold(n_splits=5,shuffle=True,random_state=42)
clf=GridSearchCV(
 estimator=pipe,param_grid=param_grid,cv=cv,scoring="f1_macro",
 refit=True,return_train_score=True,n_jobs=1,error_score="raise"
)
clf.fit(X_train,y_train)
print("Best params:",clf.best_params_)
print("Best CV macro-F1:",clf.best_score_)
cv_results=pd.DataFrame(clf.cv_results_)
display(cv_results[[
 "param_knn__n_neighbors","mean_train_score","mean_test_score",
 "std_test_score","rank_test_score"
]].sort_values("rank_test_score"))

```

## קריאה והערכה
cv_results_ הוא מילון תוצאות;DataFrame הופך אותו לטבלה קריאה. refit=True מתאים אוטומטית מודל נבחר לכל Train. predict מפעיל את כל ההכנה על Test בלי fit נוסף. קו הבסיס מתעלם מן המדידות ולומד מחלקת רוב מ־y_train.

### תא קוד 11
```python
# בודקים קו בסיס באותו מדד CV
baseline=DummyClassifier(strategy="most_frequent")
baseline_cv=cross_val_score(baseline,X_train,y_train,cv=cv,scoring="f1_macro")
baseline.fit(X_train,y_train)
print("Baseline CV macro-F1:",baseline_cv.mean())

# refit=True כבר התאים את המודל הנבחר לכל Train
predictions=clf.predict(X_test)
baseline_predictions=baseline.predict(X_test)
print("Final model Test macro-F1:",f1_score(y_test,predictions,average="macro"))
print("Baseline Test macro-F1:",f1_score(y_test,baseline_predictions,average="macro"))
print("Final model Test Accuracy:",accuracy_score(y_test,predictions))
print(classification_report(y_test,predictions,zero_division=0))

```

## בדיקת הבנה בעל־פה
1. הגדירו יעד species ושני המספריים הנתונים לצד island. הסבירו למה לא לקודד אי כ־0,1,2 ולמה לא לחשוף species ב־X.
2. בנו שני מסלולי הכנה ו־ColumnTransformer,וחברו KNN בשם השלב knn. הסבירו היכן נלמדים החציון,השכיח והתקנון.
3. הגדירו param_grid={'knn__n_neighbors':[3,5,9]} וחיפוש GridSearchCV בחמישה קיפולים,macro-F1,refit=True. התאימו לאימון בלבד. הסבירו את שם הפרמטר ואת מספר ההתאמות.
4. הציגו clf.cv_results_ בטבלה,מיינו rank_test_score והציגו clf.best_params_. הסבירו mean_test_score,std_test_score,best_score_ והבדל Test החיצוני.
5. העריכו את המודל הנבחר מול DummyClassifier באותו מדד,בלי כוונון נוסף. הסבירו כיצד ההכנה נשמרת ב־CV ומה תפקיד refit. כתבו מגבלה על מאגר Penguins המוכר.

לא מעבירים X_test ל־clf.fit;לא בוחרים לפי mean_train_score;לא מפרשים test_score הפנימי כמבחן חיצוני;לא מוחקים __ בשם הפרמטר;לא מתאימים Encoder לפני CV. מודל על אי ומינים אינו מבטיח הכללה לאי חדש. אין הבטחת דיוק נדרש בתרגיל.


---

## חלק ב — תרגול תלמיד ללא פתרון
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 37 — תרגול תלמיד: Pipeline, param_grid ו־GridSearchCV — חקר פרמטרים מלא
**פתיחה:** דודו צריך לבחור K,לשחזר את הניסוי ולהסביר לבוחן מה החיפוש עשה. נחבר גם מאפיינים מספריים וקטגוריאליים,כמו בפרויקטי FTC והמכוניות.

**עוגן:** [סיכום מפגש 8](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/09-ML-Fundamentals/Meeting-08-Didactic-Summary.md) ו[מחברת GridSearch](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/09-ML-Fundamentals/Meeting-08-GridSearch-Extension.ipynb). אף שכותרת המקור מסמנת רשות,ברשימת הבחינה שהמורה מסר האובייקטים מופיעים במפורש,ולכן הם יעד הוראה והערכה בתכנון שלנו.
אלה חומרים מותאמים חדשים,לא שחזור תרגיל מקור. חומרי ההשתלמות לא שונו.


## למה לומדים את זה עכשיו?
כדי להשוות המלצות על מחשבים משנים K באופן מסודר ומשווים על אותן חלוקות.
**בתהליך הפרויקט:** הכנה ואימות.
**מסגרת פעילה:** 4 שעות לימוד — 180 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.
**התרגול הנבחר למסגרת זו:** שעה הכנה משולבת, שעה קו בסיס, שעתיים GridSearch ותוצאות. לא מוסיפים זמן בחלקי הכנה אחרים.

התאים ריקים בכוונה. כתבו קודם מה אתם מצפים לקבל,ואחר כך הסבירו את הפלט. השתמשו במודרכת כתבנית אך הסבירו כל קוד שנכנס למחברתכם.

### תא קוד 4
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score
url="https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df=pd.read_csv(url)
data=df.dropna(subset=["species"]).copy()
numeric=["flipper_length_mm","body_mass_g"]
categorical=["island"]
X=data[numeric+categorical].copy()
y=data["species"].copy()
X_train,X_test,y_train,y_test=train_test_split(
 X,y,test_size=.25,random_state=17,stratify=y)
print("Train:",X_train.shape,"Test:",X_test.shape)

```

## משימה 1
הגדירו יעד species ושני המספריים הנתונים לצד island. הסבירו למה לא לקודד אי כ־0,1,2 ולמה לא לחשוף species ב־X.

### תא קוד 6
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 2
בנו שני מסלולי הכנה ו־ColumnTransformer,וחברו KNN בשם השלב knn. הסבירו היכן נלמדים החציון,השכיח והתקנון.

### תא קוד 9
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 3
הגדירו param_grid={'knn__n_neighbors':[3,5,9]} וחיפוש GridSearchCV בחמישה קיפולים,macro-F1,refit=True. התאימו לאימון בלבד. הסבירו את שם הפרמטר ואת מספר ההתאמות.

### תא קוד 12
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 4
הציגו clf.cv_results_ בטבלה,מיינו rank_test_score והציגו clf.best_params_. הסבירו mean_test_score,std_test_score,best_score_ והבדל Test החיצוני.

### תא קוד 15
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 5
העריכו את המודל הנבחר מול DummyClassifier באותו מדד,בלי כוונון נוסף. הסבירו כיצד ההכנה נשמרת ב־CV ומה תפקיד refit. כתבו מגבלה על מאגר Penguins המוכר.

### תא קוד 18
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

