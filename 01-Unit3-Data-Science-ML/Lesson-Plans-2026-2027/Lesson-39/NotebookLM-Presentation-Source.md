# מקור למצגת — שיעור 39 — גשר לפרויקט: רגרסיה משולבת,MAE ו־CV
**קהל:** תלמידי כיתה י׳ מתחילים. **מכסה:** 2 שעות לימוד (90 דקות), כולל תרגול; המצגת מחליפה חלק מההסבר ואינה מוסיפה זמן.
**שלב בתהליך החקר:** מודל רגרסיה ואימות.
**פתיחה מוכרת:** הערכת מחיר מחשב מכמה תכונות: משלבים מספרים וקטגוריה ובודקים גם גודל טעות ביחידות המקור.
**גבולות הליבה במצגת ובתרגול:** רגרסיה משולבת, MAE ו־R² וקו בסיס לפי התבנית; CV לרגרסיה אחרי שנלמד 28.
**המחשה חזותית מומלצת:** וקטור מאפיינים מספריים וקטגוריה→הכנה→רגרסיה→תחזיתמספרית. המחישוMAE ביחידות גרם,השוואהלבסיס ו־R² חסר יחידות. קוActual=Predicted אינו קו־הרגרסיה.
**זיקה להמשך:** רגרסיה ופרספטרון הם גשר ל־DL; אינם אלגוריתמי חובה ביחידה 5. SVM נשאר בגלל מפרט יחידה 3. אין להמציא חפיפה בין שלוש התכניות.

## הוראות למניעת ערבוב דוגמה ותרגול
חלק א הוא דוגמה פתורה שאפשר להסביר ולפתור בשקפים. חלק ב הוא תרגול עצמאי: מציגים את הדרישה, מפרקים לשלבים ונותנים רמזים; אין מייצרים פתרון מלא,קוד מלא או תוצאות סופיות של המשימות הנבחרות. אין בקובץ פתרוןמתועד לתרגול. חומר עודף במחברות מיועד לחזרה; גבולותהליבה לעיל גוברים על שאיפה לכסותכל תא.
דוגמאות מומצאות אינן מאגר אמיתי. קישורים הם ייחוס; אין להניח שתוכנם נכלל אוטומטית במקור שהועלה. לא להמציא פלט,דיוק או גרף מאומת כשהם אינם מופיעים בטקסט.

## חלק א — הסבר ודוגמה פתורה
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 39 — גשר לפרויקט: רגרסיה משולבת,MAE ו־CV
המחברת משלימה את שיעור27 ואת גשר ההכנה בשיעור37.

**הקשר:** דודו בודק אם כמה מדידות יחד עם אי הדגימה מסייעות להעריך מסה. המסה יעד מספרי והאי קטגוריה;אין להמיר אי לסולם מרחק שרירותי.
עוגן: [מבוא הרגרסיה](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/04-Introduction-to-ML/Linear-Regression-Intro/Didactic-Summary.md),[מפגש9 והמעבדות](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/11-ML-Project-Workflow/Meeting-09-Project-Labs.md). זו התאמה חדשה למשימת רגרסיה עם נתונים מעורבים,על Penguins המוכר במקום להניח שקובץ מכוניות חיצוני כבר אומת. המקורות נשמרו.


## למה לומדים את זה עכשיו?
הערכת מחיר מחשב מכמה תכונות: משלבים מספרים וקטגוריה ובודקים גם גודל טעות ביחידות המקור.
**בתהליך הפרויקט:** מודל רגרסיה ואימות.
**מסגרת פעילה:** 2 שעות לימוד — 90 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.

## מה מתווסף למודל בעל מאפיין אחד?
לאחר הכנה מתקבל וקטור תכונות,והמודל מחשב ŷ=b+w₁z₁+...+wₚzₚ. אלה תכונות לאחר השלמה,תקנון וקידוד;אין לקרוא כל מקדם כאילו הוא שיפוע ביחידות הגלם.
לא מלמדים כאן גזירה מטריציונית. One-Hot מלא יחד עם חיתוך עשוי ליצור יתירות;התחזיות עדיין מוגדרות באמצעות התאמת ריבועים פחותים,אך פירוש מקדמים יחידים דורש זהירות.
$$MAE=\frac{1}{N}\sum_i|y_i-\hat y_i|$$
MAE בגרמים,וככל שהוא קטן יותר הטעות המוחלטת הממוצעת קטנה יותר. R² חסר יחידות ויכול להיות שלילי. אין מספר יחיד שמתאר את כל הסיכון.
בדוגמה מומצאת:אמת[100,200,300],תחזית[110,180,330] נותנות שאריות[−10,20,−30],ולכן MAE=20. הממוצע החתום אינו MAE.


Penguins:344 שורות ו־7 עמודות לפני בחירת מסה ידועה,342 לאחריה. המקור Gorman ו־Palmer Station LTER;[תיעוד](https://github.com/allisonhorst/palmerpenguins),Horst,Hill & Gorman (2020),DOI:10.5281/zenodo.3960218.
אי הדגימה צריך להיות ידוע בזמן החיזוי ורלוונטי לשימוש;מודל שלומד ממנו אינו מבטיח הצלחה באי אחר. Penguins כבר נראה בשיעורים קודמים ולכן זו הדגמת תהליך,לא מבחן בלתי תלוי חדש ולא מאגר גמר מאושר.
אין stratify לפי יעד רציף. משתמשים ב־KFold,ולא ב־StratifiedKFold לפי המסה. כל הכנה בתוך Pipeline בקיפולים;יעד חסר אינו מושלם.
התקנון נכלל כאן לשמירת מתכון מוכר וללמידת ייצוג;הוא אינו הכרחי לרגרסיה ליניארית רגילה ללא רגולריזציה.


### תא קוד 5
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split,KFold,cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import r2_score,mean_absolute_error
url="https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
raw=pd.read_csv(url)
data=raw.dropna(subset=["body_mass_g"]).copy()
numeric=["bill_length_mm","flipper_length_mm"]
categorical=["island"]
X=data[numeric+categorical].copy()
y=data["body_mass_g"].copy()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42)
print("Eligible:",len(data),"Train:",len(X_train),"Test:",len(X_test))

```

## הכנה ואימות
המספריים מושלמים בחציון אימון,האי בשכיח ומקודד One-Hot. לכל קיפול התאמות משלו. ממוצע CV אינו Test חיצוני ואינו חייב להיות זהה לציון הסופי.

### תא קוד 7
```python
prepare=ColumnTransformer([
 ("numeric",Pipeline([("fill",SimpleImputer(strategy="median")),("scale",StandardScaler())]),numeric),
 ("categorical",Pipeline([
  ("fill",SimpleImputer(strategy="most_frequent")),
  ("encode",OneHotEncoder(handle_unknown="ignore",sparse_output=False))
 ]),categorical)
])
model=Pipeline([("prepare",prepare),("regression",LinearRegression())])
cv=KFold(n_splits=5,shuffle=True,random_state=42)
cv_scores=cross_val_score(model,X_train,y_train,cv=cv,scoring="r2")
print("CV R² mean:",cv_scores.mean(),"Descriptive std:",cv_scores.std(ddof=0))

```

## התאמה מחדש והערכה
נשתמש בנתוני Test רק לאחר שהמתכון נקבע. baseline לומד ממוצע מ־y_train;התאמה לממוצע Test אינה קו בסיס מעשי.

### תא קוד 9
```python
model.fit(X_train,y_train)
predictions=model.predict(X_test)
comparison=pd.DataFrame({"actual_g":y_test,"predicted_g":predictions},index=y_test.index)
comparison["residual_g"]=comparison["actual_g"]-comparison["predicted_g"]
mae_manual=comparison["residual_g"].abs().mean()
mae=mean_absolute_error(y_test,predictions)
r2=r2_score(y_test,predictions)
baseline=DummyRegressor(strategy="mean")
baseline.fit(X_train,y_train)
baseline_predictions=baseline.predict(X_test)
baseline_mae=mean_absolute_error(y_test,baseline_predictions)
baseline_r2=r2_score(y_test,baseline_predictions)
display(comparison.head(8))
print("Test R²:",r2,"MAE (g):",mae,"Manual MAE:",mae_manual)
print("Training-mean baseline R²:",baseline_r2,"MAE (g):",baseline_mae)

```

## תרשים תחזיות
הקו y=x מציין התאמה מושלמת בין אמת לחיזוי,ולא קו הרגרסיה בין מאפיין ליעד. לכל ציר יחידות גרם.

### תא קוד 11
```python
plt.figure()
plt.scatter(y_test,predictions,alpha=.65)
limits=[min(y_test.min(),predictions.min()),max(y_test.max(),predictions.max())]
plt.plot(limits,limits,color="black",label="Perfect agreement line")
plt.xlabel("Actual mass (g)");plt.ylabel("Predicted mass (g)")
plt.title("Test predictions — multiple features");plt.legend()
plt.tight_layout();plt.show()

```

## העברה לשלוש התכניות
יחידה 3:פרויקט רגרסיה עם כמה סוגי מאפיינים וניתוח טעות. יחידה 5:חיבור מקדים ליחסים בין משתנים ולפרשנות הערכה;רגרסיה אינה מסומנת במפה כיעד חובה של יחידה 5. DL:וקטור קלט,סכום משוקלל ורעיון שגיאה/Loss;אין צורך ללמד כעת Backpropagation.
לפרויקט המכוניות מעבירים את אותו מתכון לאחר אימות מקור,סכמה,יחידות ונתונים;אין טענה שהורדת Kaggle או הפרויקט עצמו אומתו כאן.


---

## חלק ב — תרגול תלמיד ללא פתרון
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 39 — תרגול עצמאי: רגרסיה משולבת,MAE ו־CV
המחברת משלימה את שיעור27 ואת גשר ההכנה בשיעור37.

**הקשר:** דודו בודק אם כמה מדידות יחד עם אי הדגימה מסייעות להעריך מסה. המסה יעד מספרי והאי קטגוריה;אין להמיר אי לסולם מרחק שרירותי.
עוגן: [מבוא הרגרסיה](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/04-Introduction-to-ML/Linear-Regression-Intro/Didactic-Summary.md),[מפגש9 והמעבדות](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/11-ML-Project-Workflow/Meeting-09-Project-Labs.md). זו התאמה חדשה למשימת רגרסיה עם נתונים מעורבים,על Penguins המוכר במקום להניח שקובץ מכוניות חיצוני כבר אומת. המקורות נשמרו.


## למה לומדים את זה עכשיו?
הערכת מחיר מחשב מכמה תכונות: משלבים מספרים וקטגוריה ובודקים גם גודל טעות ביחידות המקור.
**בתהליך הפרויקט:** מודל רגרסיה ואימות.
**מסגרת פעילה:** 2 שעות לימוד — 90 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.
**התרגול הנבחר למסגרת זו:** רגרסיה משולבת, MAE ו־R² וקו בסיס לפי התבנית; CV לרגרסיה אחרי שנלמד 28.

תאי המשימות ריקים בכוונה. קוד טעינה וחלוקה ניתן;יש להסביר כל קוד שתכללו בפרויקט.

### תא קוד 4
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split,KFold,cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import r2_score,mean_absolute_error
url="https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
raw=pd.read_csv(url)
data=raw.dropna(subset=["body_mass_g"]).copy()
numeric=["bill_depth_mm","flipper_length_mm"]
categorical=["island"]
X=data[numeric+categorical].copy()
y=data["body_mass_g"].copy()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=17)
print("Eligible:",len(data),"Train:",len(X_train),"Test:",len(X_test))

```

## משימה 1
נחזה מסה מ־bill_depth_mm,flipper_length_mm ו־island לפי הקוד הנתון. הגדירו יעד,יחידות וזמינות המאפיינים בזמן השימוש.

### תא קוד 6
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## משימה 2
בנו ColumnTransformer מספרי/קטגוריאלי והוסיפו LinearRegression ל־Pipeline. הסבירו מה משתנה במספר התכונות לאחר קידוד.

### תא קוד 9
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## משימה 3
בצעו חמישה קיפולי KFold על אימון בלבד עם scoring='r2'. מדוע אין להשתמש ב־stratify לפי המסה,ומדוע ההכנה חייבת להיות בתוך CV?

### תא קוד 12
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## משימה 4
אמנו מחדש על כל Train,הפיקו תחזיות Test והשוו R² ו־MAE לקו בסיס של ממוצע אימון. חשבו MAE גם ידנית מתוך השאריות.

### תא קוד 15
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## משימה 5
הציגו Actual מול Predicted,פרשו שתי שגיאות וכתבו מסקנה ומגבלה. הסבירו מה יעבור בהמשך ל־Loss ברשת,ומדוע אין טענה לסיבתיות או להכללה.

### תא קוד 18
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר ומסקנה:** כתבו כאן.

