# מקור מקצועי למצגת — מפגש 23 — GridSearchCV וקריאת תוצאות
**קהל:** כיתה י׳, תלמידים חדשים בנושא. **מכסה:** 2 שעות הוראה ותרגול ושעת פרויקט אחת; יחד 135 דקות.
המסמך מרכז את הסיפור, ההסבר, דוגמה פתורה וקוד, מטרות המעבדה והוראות ההמחשה. הוא מעבד את מצגות ההשתלמות המצורפות, ואינו מצגת שנוצרה או נבדקה ב־ NotebookLM.

## מצגות מקור שנבדקו
- [יישום מכונה לומדת.pptx](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/%D7%99%D7%99%D7%A9%D7%95%D7%9D%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94%20%D7%9C%D7%95%D7%9E%D7%93%D7%AA.pptx) — שקפים 26–30.

## גבולות התוכן
כ־ 85% מזמן ההוראה המושגית בתכנון נשען על מושגי ההשתלמות, וכ־ 15% מוקדשים לפיגום, מניעת טעויות וגשרים להמשך. זהו יעד תכנון בקירוב, לא מדידת אחוזי העתקה. המקורות אינם מועתקים מילה במילה. הדוגמאות החדשות וההעברות מסומנות כדידקטיות. פירוש נכון ומניעת זליגה קודמים להעתקת טעות או API ישן.

# מפגש 23 — GridSearchCV וקריאת תוצאות
## סיפור המסגרת ושאלת הלמידה
דודו משווה שלושה ערכי K. נרשום מראש את המועמדים ונבקש מחיפוש שיטתי לבדוק אותם באותה דרך.

## מה נלמד ומדוע
param_grid מגדיר מועמדים. שם כמו knn__n_neighbors מפנה לפרמטר בתוך שלב Pipeline. GridSearchCV בודק מועמדים באמצעות CV. cv_results_ מכיל תוצאות, ו־ best_params_ מחזיר בחירה. refit מתאים את המודל הנבחר לכל Train. mean_test_score הוא אימות פנימי ולא Test חיצוני.

## דוגמה פתורה קטנה
שלושה ערכי K כפול חמישה קיפולים דורשים 15 התאמות מועמדים. כאשר refit=True מתווספת התאמה לכל Train. זה אינו מספר הדוגמאות.

```python
candidate_k = [3, 5, 9]
folds = 5
print(len(candidate_k) * folds)
```

**פלט צפוי ופירוש:** 15. זוהי דוגמה קטנה ומוצהרת; היא אינה ציון ביצוע של פרויקט אמיתי.

## הדרך לתרגול העצמאי
במעבדת 37 מבצעים מועמדים, חיפוש וקריאת פלט. ההכנה המשולבת היא חזרה ממפגש 14.
עבדו לפי הסדר: נסחו את השאלה, זהו נתונים ויחידות, בחרו כלי שכבר נלמד, כתבו ציפייה, הריצו והסבירו תוצאה ומגבלה. במשימה שאינה מובנת חוזרים למושג או לדוגמה, ולא מחפשים שורת קוד להעתקה.

## תוצר לפרויקט
נועלים מודל והיפר־פרמטרים לפרויקט על סמך האימות, ומתעדים את הנימוק ואת המדד.

## קשר ללימודי ההמשך
מדדים, אימות והכללה משותפים ליחידה 5 ולניסויים ב־DL. שומרים על אותה שיטת הערכה גם כאשר המודל משתנה.

## בדיקה עצמית
מה שונה בין best_params_ לבין ממוצע Scaler?
כתבו תשובה במילים שלכם והצביעו על תא או נתון שתומך בה. אין פתרון לתרגול העצמאי במסמך התלמיד.


## יישום מודרך מלא וקוד לדוגמה
# מפגש 23 — GridSearchCV וקריאת תוצאות
2 שעות הוראה ותרגול ושעת פרויקט אחת; יחד 135 דקות.

## סיפור המסגרת
דודו משווה שלושה ערכי K. נרשום מראש את המועמדים ונבקש מחיפוש שיטתי לבדוק אותם באותה דרך.

## מטרות
- להגדיר param_grid.
- לקרוא cv_results_.
- להסביר best_params_ ו־ refit.

## המושגים הנחוצים
param_grid מגדיר מועמדים. שם כמו knn__n_neighbors מפנה לפרמטר בתוך שלב Pipeline. GridSearchCV בודק מועמדים באמצעות CV. cv_results_ מכיל תוצאות, ו־ best_params_ מחזיר בחירה. refit מתאים את המודל הנבחר לכל Train. mean_test_score הוא אימות פנימי ולא Test חיצוני.

## דוגמה פתורה לפני קוד
שלושה ערכי K כפול חמישה קיפולים דורשים 15 התאמות מועמדים. כאשר refit=True מתווספת התאמה לכל Train. זה אינו מספר הדוגמאות.

```python
candidate_k = [3, 5, 9]
folds = 5
print(len(candidate_k) * folds)
```

**פלט צפוי:** 15

## מדוע זה חשוב?
מדדים, אימות והכללה משותפים ליחידה 5 ולניסויים ב־DL. שומרים על אותה שיטת הערכה גם כאשר המודל משתנה.

## יישום מודרך — חלק 1
מקור הקוד: ערכה 37 הקיימת. בהמשך עוברים לתרגול עצמאי באותו נושא.

### תשתית הנתונים והחלוקה
קראו תחילה את היעד ואת שמות המאפיינים. החלוקה שומרת התאמה בין שורות X ל־ y. הפרמטר random_state מאפשר שחזור ואינו משפר דיוק בפני עצמו.

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

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

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

### חיפוש מועמדים
קראו את שמות השלבים, רשימת המועמדים ומדד הבחירה. החיפוש מקבל נתוני אימון בלבד; נתוני האימות הפנימיים אינם Test חיצוני.

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

### אימות בתוך הפיתוח
ההכנה נמצאת בתוך Pipeline. כל קיפול לומד את פרמטריו מתת־האימון שלו. נקרא את ממוצע האימות לפני שנחליט על מודל.

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

## עצירה לפני המעבדה
מה שונה בין best_params_ לבין ממוצע Scaler?

**התוצר הנדרש:** במעבדת 37 מבצעים מועמדים, חיפוש וקריאת פלט. ההכנה המשולבת היא חזרה ממפגש 14.

## המשימות שהמצגת חייבת להכין לקראתן
במעבדת 37 מבצעים מועמדים, חיפוש וקריאת פלט. ההכנה המשולבת היא חזרה ממפגש 14.
**מבחן התאמה:** כל פקודה או רעיון במשימת ליבה צריכים להיות מוסברים קודם בדוגמה, או להופיע כקוד תשתית נתון. בהכנה לתרגול הציגו נתונים, תוצר וצעדי חשיבה; אין לפתור את משימת התלמיד. המעבדה המדויקת היא Student-Lab.ipynb, ופתרונה אינו מקור למצגת התלמיד.

## הוראות חזותיות
רקע לבן או בהיר מאוד, טקסט כהה, ניגודיות גבוהה וגופן גדול. רעיון מרכזי אחד בשקף. המושג יופיע לצד דוגמה קטנה, חישוב או תרשים מדויק. משתמשים בסיפור כדי להסביר את הצורך; אין להציג את נתוני הסיפור המומצאים כאילו נאספו בפועל. לתרשים נתונים אמיתי מצרפים פלט מאומת או מסמנים שהוא סכמטי. אין להמציא ציון מודל או לקרוא ציון החלטה כהסתברות.

## מקורות משלימים מוגבלים
מניעת זליגה והכנה בתוך אימות: [תיעוד scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html). פירוש R²: [תיעוד המדד](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html). משתמשים רק בקטע הרלוונטי לנושא, ללא הוספת יחידת לימוד או ספרייה חדשה.


## נספח — נוסח המעבדה העצמאית ללא פתרון
הנספח מאפשר לבדוק שהמצגת מכינה למשימה בפועל. בחרו רק את משימות הליבה שהוגדרו במדריך. אין להפוך את הנספח לפתרון בשקפים.

# מפגש 23 — GridSearchCV וקריאת תוצאות
2 שעות הוראה ותרגול ושעת פרויקט אחת; יחד 135 דקות.

## סיפור המסגרת
דודו משווה שלושה ערכי K. נרשום מראש את המועמדים ונבקש מחיפוש שיטתי לבדוק אותם באותה דרך.

## מטרות
- להגדיר param_grid.
- לקרוא cv_results_.
- להסביר best_params_ ו־refit.

## תרגול עצמאי
במעבדת 37 מבצעים מועמדים, חיפוש וקריאת פלט. ההכנה המשולבת היא חזרה ממפגש 14.

תאי משימות ריקים בכוונה. תשתית טעינה או מודל נתון, אם קיימים, אינם פתרון לחישוב ולפירוש שלכם. הפעילו רק את משימות הליבה שהוגדרו למפגש. שאר משימות המקור הן מאגר חזרה, ללא חובת בית נוספת.

## חלק 1 — תרגול העברה
הנתונים וההוראות מופיעים להלן. עובדים על משימות הליבה של המפגש.

התאים ריקים בכוונה. כתבו קודם מה אתם מצפים לקבל, ואחר כך הסבירו את הפלט. השתמשו במודרכת כתבנית אך הסבירו כל קוד שנכנס למחברתכם.

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
הגדירו יעד species ושני המספריים הנתונים לצד island. הסבירו למה לא לקודד אי כ־ 0,1,2 ולמה לא לחשוף species ב־ X.

```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 2
בנו שני מסלולי הכנה ו־ ColumnTransformer, וחברו KNN בשם השלב knn. הסבירו היכן נלמדים החציון, השכיח והתקנון.

```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 3
הגדירו param_grid={'knn__n_neighbors': [3,5,9]} וחיפוש GridSearchCV בחמישה קיפולים, macro-F1, refit=True. התאימו לאימון בלבד. הסבירו את שם הפרמטר ואת מספר ההתאמות.

```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 4
הציגו clf.cv_results_ בטבלה, מיינו rank_test_score והציגו clf.best_params_. הסבירו mean_test_score, std_test_score, best_score_ והבדל Test החיצוני.

```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 5
העריכו את המודל הנבחר מול DummyClassifier באותו מדד, בלי כוונון נוסף. הסבירו כיצד ההכנה נשמרת ב־ CV ומה תפקיד refit. כתבו מגבלה על מאגר Penguins המוכר.

```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## יישום בפרויקט
נועלים מודל והיפר־פרמטרים לפרויקט על סמך האימות, ומתעדים את הנימוק ואת המדד.

## לפני הגשה
הריצו לפי הסדר, בדקו פלטים עדכניים, כתבו פירוש ומגבלה והצהירו היכן נעזרתם. פתרונות נמצאים בנפרד למורה אך גלויים במאגר הציבורי.

## תכנון מדורג למצגת של מפגש 23

**שאלת פתיחה:** דודו משווה שלושה ערכי K. נרשום מראש את המועמדים ונבקש מחיפוש שיטתי לבדוק אותם באותה דרך.

**המחשה מרכזית:** טבלת מועמדים וציוני CV מתוך המקור; קשר param_grid אל cv_results_ ואל best_params_ בלי להמציא ציונים.

| שלב | מה מציגים לתלמיד | בדיקת הבנה |
|---|---|---|
| צורך ומטרה | הסיפור ומטרה אחת: להגדיר param_grid | מה נרצה לדעת בסיום? |
| מושג לפני קוד | param_grid מגדיר מועמדים. שם כמו knn__n_neighbors מפנה לפרמטר בתוך שלב Pipeline. GridSearchCV בודק מועמדים באמצעות CV. cv_results_ מכיל תוצאות, ו־best_params_ מחזיר בחירה. refit מתאים את המודל הנבחר לכל Train. mean_test_score הוא אימות פנימי ולא Test חיצוני. | התלמיד מסביר את המושג באמצעות הדוגמה. |
| דוגמה פתורה | שלושה ערכי K כפול חמישה קיפולים דורשים 15 התאמות מועמדים. כאשר refit=True מתווספת התאמה לכל Train. זה אינו מספר הדוגמאות. | עוצרים לפני חישוב או חשיפת פלט ומבקשים ציפייה מנומקת. |
| מעבר לקוד | קטע קצר מתוך הדוגמה הקיימת, עם שמות משתנים ויחידות ללא שינוי | התלמיד מקשר פעולה בקוד לשלב בדוגמה. |
| תרגול בסיוע | בוחרים משימת ליבה מתוך Student-Lab.ipynb ומציגים רק נתון, דרישה ורמז | התלמיד מציע פעולה ומנמק אותה לפני כתיבת קוד. |
| העברה עצמאית | ממשיכים במשימת הליבה עם מאפיין או הקשר השונים מהדוגמה הפתורה | התלמיד מגיש ביצוע ופירוש ללא העתקת הפתרון. |
| סיום | מה שונה בין best_params_ לבין ממוצע Scaler? | התלמיד מצביע על ראיה ומציין מגבלה. |

**תוצר בתוך מכסת הזמן:** נועלים מודל והיפר־פרמטרים לפרויקט על סמך האימות, ומתעדים את הנימוק ואת המדד.

**הקשר להמשך:** מדדים, אימות והכללה משותפים ליחידה 5 ולניסויים ב־DL. שומרים על אותה שיטת הערכה גם כאשר המודל משתנה.

הטבלה מפרטת את חומר המפגש הקיים; אין להפוך כל שורה לשקף נוסף אם היא חורגת ממכסת השקפים. במפגש הגנה משתמשים בה כשאלות ומשוב על הפרויקט האישי, ללא מעבדה נוספת.
