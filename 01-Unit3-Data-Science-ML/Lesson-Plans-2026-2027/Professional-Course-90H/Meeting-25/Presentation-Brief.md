# מקור מקצועי למצגת — מפגש 25 — רגרסיה משולבת וניתוח גודל הטעות
**קהל:** כיתה י׳, תלמידים חדשים בנושא. **מכסה:** 2 שעות הוראה ותרגול ושעת פרויקט אחת; יחד 135 דקות.
המסמך מרכז את הסיפור, ההסבר, דוגמה פתורה וקוד, מטרות המעבדה והוראות ההמחשה. הוא מעבד את מצגות ההשתלמות המצורפות, ואינו מצגת שנוצרה או נבדקה ב־ NotebookLM.

## מצגות מקור שנבדקו
- [4.1 Intro to linear regression.pptx](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/4.1%20Intro%20to%20linear%20regression.pptx) — שקפים 7–11.
- [4.2 Linear regression with sklearn.pptx](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/4.2%20Linear%20regression%20with%20sklearn.pptx) — שקפים 7–12.
- [Data Preparation2.pptx](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/Data%20Preparation2.pptx) — שקפים 22.

## גבולות התוכן
כ־ 85% מזמן ההוראה המושגית בתכנון נשען על מושגי ההשתלמות, וכ־ 15% מוקדשים לפיגום, מניעת טעויות וגשרים להמשך. זהו יעד תכנון בקירוב, לא מדידת אחוזי העתקה. המקורות אינם מועתקים מילה במילה. הדוגמאות החדשות וההעברות מסומנות כדידקטיות. פירוש נכון ומניעת זליגה קודמים להעתקת טעות או API ישן.

# מפגש 25 — רגרסיה משולבת וניתוח גודל הטעות
## סיפור המסגרת ושאלת הלמידה
מחיר מחשב תלוי בכמה מדידות ולעיתים בקטגוריה. נחבר הכנה משולבת לרגרסיה ונמדוד טעות ביחידות השימוש.

## מה נלמד ומדוע
אחרי הכנה, רגרסיה משתמשת בייצוג התכונות המעובד. MAE הוא ממוצע טעויות מוחלטות וביחידות של y. ברגרסיה לא מבצעים stratify לפי ערכי יעד רציף בודדים. משווים לקו בסיס באותו פרוטוקול. תקנון אינו הכרחי לרגרסיה ליניארית רגילה ללא רגולריזציה.

## דוגמה פתורה קטנה
אמת [100,200,300] ותחזית [110,180,330] נותנות טעויות מוחלטות 10,20,30. ה־ MAE הוא 20. ממוצע שאריות חתומות אינו המדד הזה.

```python
import numpy as np
actual = np.array([100, 200, 300])
predicted = np.array([110, 180, 330])
mae = np.mean(np.abs(actual - predicted))
print(mae)
```

**פלט צפוי ופירוש:** 20.0. זוהי דוגמה קטנה ומוצהרת; היא אינה ציון ביצוע של פרויקט אמיתי.

## הדרך לתרגול העצמאי
מאפיינים אחרים, הכנה משולבת, KFold, MAE ו־ R² מול קו בסיס. זוהי משימת העברה של תהליך הרגרסיה.
עבדו לפי הסדר: נסחו את השאלה, זהו נתונים ויחידות, בחרו כלי שכבר נלמד, כתבו ציפייה, הריצו והסבירו תוצאה ומגבלה. במשימה שאינה מובנת חוזרים למושג או לדוגמה, ולא מחפשים שורת קוד להעתקה.

## תוצר לפרויקט
בפרויקט רגרסיה מוסיפים ניתוח טעות ביחידות היעד. בסיווג ממשיכים בניתוח מחיר טעויות ובהשוואה הרלוונטית.

## קשר ללימודי ההמשך
סכום משוקלל, שגיאה ועדכון משקולות מכינים ל־ DL. רגרסיה ופרספטרון אינם מוצגים כאלגוריתמי חובה ביחידה 5.

## בדיקה עצמית
האם MAE=20 פירושו 20 אחוזים?
כתבו תשובה במילים שלכם והצביעו על תא או נתון שתומך בה. אין פתרון לתרגול העצמאי במסמך התלמיד.


## יישום מודרך מלא וקוד לדוגמה
# מפגש 25 — רגרסיה משולבת וניתוח גודל הטעות
2 שעות הוראה ותרגול ושעת פרויקט אחת; יחד 135 דקות.

## סיפור המסגרת
מחיר מחשב תלוי בכמה מדידות ולעיתים בקטגוריה. נחבר הכנה משולבת לרגרסיה ונמדוד טעות ביחידות השימוש.

## מטרות
- לשלב סוגי מאפיינים.
- לחשב MAE.
- להשוות מדדי רגרסיה לבסיס.

## המושגים הנחוצים
אחרי הכנה, רגרסיה משתמשת בייצוג התכונות המעובד. MAE הוא ממוצע טעויות מוחלטות וביחידות של y. ברגרסיה לא מבצעים stratify לפי ערכי יעד רציף בודדים. משווים לקו בסיס באותו פרוטוקול. תקנון אינו הכרחי לרגרסיה ליניארית רגילה ללא רגולריזציה.

## דוגמה פתורה לפני קוד
אמת [100,200,300] ותחזית [110,180,330] נותנות טעויות מוחלטות 10,20,30. ה־ MAE הוא 20. ממוצע שאריות חתומות אינו המדד הזה.

```python
import numpy as np
actual = np.array([100, 200, 300])
predicted = np.array([110, 180, 330])
mae = np.mean(np.abs(actual - predicted))
print(mae)
```

**פלט צפוי:** 20.0

## מדוע זה חשוב?
סכום משוקלל, שגיאה ועדכון משקולות מכינים ל־ DL. רגרסיה ופרספטרון אינם מוצגים כאלגוריתמי חובה ביחידה 5.

## יישום מודרך — חלק 1
מקור הקוד: ערכה 39 הקיימת. בהמשך עוברים לתרגול עצמאי באותו נושא.

### תשתית הנתונים והחלוקה
קראו תחילה את היעד ואת שמות המאפיינים. החלוקה שומרת התאמה בין שורות X ל־ y. הפרמטר random_state מאפשר שחזור ואינו משפר דיוק בפני עצמו.

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

### אימות בתוך הפיתוח
ההכנה נמצאת בתוך Pipeline. כל קיפול לומד את פרמטריו מתת־האימון שלו. נקרא את ממוצע האימות לפני שנחליט על מודל.

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

### התאמה ויישום
זהו מה לומד פרמטרים ובאילו שורות נעשה fit. ודאו שכל הכנה שנלמדת מנתונים משתמשת באימון המתאים. לאחר מכן פירשו את הפלט במילים.

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

### המחשה חזותית
לפני הרצה הגדירו שאלה, סוגי משתנים ויחידות. אחרי הרצה פרשו את הצירים ואת הממצא. אין להסיק סיבתיות או למחוק קצה רק מן הציור.

```python
plt.figure()
plt.scatter(y_test,predictions,alpha=.65)
limits=[min(y_test.min(),predictions.min()),max(y_test.max(),predictions.max())]
plt.plot(limits,limits,color="black",label="Perfect agreement line")
plt.xlabel("Actual mass (g)");plt.ylabel("Predicted mass (g)")
plt.title("Test predictions — multiple features");plt.legend()
plt.tight_layout();plt.show()
```

## עצירה לפני המעבדה
האם MAE=20 פירושו 20 אחוזים?

**התוצר הנדרש:** מאפיינים אחרים, הכנה משולבת, KFold, MAE ו־ R² מול קו בסיס. זוהי משימת העברה של תהליך הרגרסיה.

## המשימות שהמצגת חייבת להכין לקראתן
מאפיינים אחרים, הכנה משולבת, KFold, MAE ו־ R² מול קו בסיס. זוהי משימת העברה של תהליך הרגרסיה.
**מבחן התאמה:** כל פקודה או רעיון במשימת ליבה צריכים להיות מוסברים קודם בדוגמה, או להופיע כקוד תשתית נתון. בהכנה לתרגול הציגו נתונים, תוצר וצעדי חשיבה; אין לפתור את משימת התלמיד. המעבדה המדויקת היא Student-Lab.ipynb, ופתרונה אינו מקור למצגת התלמיד.

## הוראות חזותיות
רקע לבן או בהיר מאוד, טקסט כהה, ניגודיות גבוהה וגופן גדול. רעיון מרכזי אחד בשקף. המושג יופיע לצד דוגמה קטנה, חישוב או תרשים מדויק. משתמשים בסיפור כדי להסביר את הצורך; אין להציג את נתוני הסיפור המומצאים כאילו נאספו בפועל. לתרשים נתונים אמיתי מצרפים פלט מאומת או מסמנים שהוא סכמטי. אין להמציא ציון מודל או לקרוא ציון החלטה כהסתברות.

## מקורות משלימים מוגבלים
מניעת זליגה והכנה בתוך אימות: [תיעוד scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html). פירוש R²: [תיעוד המדד](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html). משתמשים רק בקטע הרלוונטי לנושא, ללא הוספת יחידת לימוד או ספרייה חדשה.


## נספח — נוסח המעבדה העצמאית ללא פתרון
הנספח מאפשר לבדוק שהמצגת מכינה למשימה בפועל. בחרו רק את משימות הליבה שהוגדרו במדריך. אין להפוך את הנספח לפתרון בשקפים.

# מפגש 25 — רגרסיה משולבת וניתוח גודל הטעות
2 שעות הוראה ותרגול ושעת פרויקט אחת; יחד 135 דקות.

## סיפור המסגרת
מחיר מחשב תלוי בכמה מדידות ולעיתים בקטגוריה. נחבר הכנה משולבת לרגרסיה ונמדוד טעות ביחידות השימוש.

## מטרות
- לשלב סוגי מאפיינים.
- לחשב MAE.
- להשוות מדדי רגרסיה לבסיס.

## תרגול עצמאי
מאפיינים אחרים, הכנה משולבת, KFold, MAE ו־R² מול קו בסיס. זוהי משימת העברה של תהליך הרגרסיה.

תאי משימות ריקים בכוונה. תשתית טעינה או מודל נתון, אם קיימים, אינם פתרון לחישוב ולפירוש שלכם. הפעילו רק את משימות הליבה שהוגדרו למפגש. שאר משימות המקור הן מאגר חזרה, ללא חובת בית נוספת.

## חלק 1 — תרגול העברה
הנתונים וההוראות מופיעים להלן. עובדים על משימות הליבה של המפגש.

תאי המשימות ריקים בכוונה. קוד טעינה וחלוקה ניתן; יש להסביר כל קוד שתכללו בפרויקט.

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
נחזה מסה מ־ bill_depth_mm, flipper_length_mm ו־ island לפי הקוד הנתון. הגדירו יעד, יחידות וזמינות המאפיינים בזמן השימוש.

```python
# כתבו כאן את הפתרון שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## משימה 2
בנו ColumnTransformer מספרי/קטגוריאלי והוסיפו LinearRegression ל־ Pipeline. הסבירו מה משתנה במספר התכונות לאחר קידוד.

```python
# כתבו כאן את הפתרון שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## משימה 3
בצעו חמישה קיפולי KFold על אימון בלבד עם scoring='r2'. מדוע אין להשתמש ב־ stratify לפי המסה, ומדוע ההכנה חייבת להיות בתוך CV?

```python
# כתבו כאן את הפתרון שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## משימה 4
אמנו מחדש על כל Train, הפיקו תחזיות Test והשוו R² ו־ MAE לקו בסיס של ממוצע אימון. חשבו MAE גם ידנית מתוך השאריות.

```python
# כתבו כאן את הפתרון שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## משימה 5
הציגו Actual מול Predicted, פרשו שתי שגיאות וכתבו מסקנה ומגבלה. הסבירו מה יעבור בהמשך ל־ Loss ברשת, ומדוע אין טענה לסיבתיות או להכללה.

```python
# כתבו כאן את הפתרון שלכם
```

**הסבר ומסקנה:** כתבו כאן.

## יישום בפרויקט
בפרויקט רגרסיה מוסיפים ניתוח טעות ביחידות היעד. בסיווג ממשיכים בניתוח מחיר טעויות ובהשוואה הרלוונטית.

## לפני הגשה
הריצו לפי הסדר, בדקו פלטים עדכניים, כתבו פירוש ומגבלה והצהירו היכן נעזרתם. פתרונות נמצאים בנפרד למורה אך גלויים במאגר הציבורי.

## תכנון מדורג למצגת של מפגש 25

**שאלת פתיחה:** מחיר מחשב תלוי בכמה מדידות ולעיתים בקטגוריה. נחבר הכנה משולבת לרגרסיה ונמדוד טעות ביחידות השימוש.

**המחשה מרכזית:** טבלת אמת, תחזית ושגיאה מוחלטת עם יחידות; הצג כיצד MAE שומר על יחידת היעד.

| שלב | מה מציגים לתלמיד | בדיקת הבנה |
|---|---|---|
| צורך ומטרה | הסיפור ומטרה אחת: לשלב סוגי מאפיינים | מה נרצה לדעת בסיום? |
| מושג לפני קוד | אחרי הכנה, רגרסיה משתמשת בייצוג התכונות המעובד. MAE הוא ממוצע טעויות מוחלטות וביחידות של y. ברגרסיה לא מבצעים stratify לפי ערכי יעד רציף בודדים. משווים לקו בסיס באותו פרוטוקול. תקנון אינו הכרחי לרגרסיה ליניארית רגילה ללא רגולריזציה. | התלמיד מסביר את המושג באמצעות הדוגמה. |
| דוגמה פתורה | אמת [100,200,300] ותחזית [110,180,330] נותנות טעויות מוחלטות 10,20,30. ה־MAE הוא 20. ממוצע שאריות חתומות אינו המדד הזה. | עוצרים לפני חישוב או חשיפת פלט ומבקשים ציפייה מנומקת. |
| מעבר לקוד | קטע קצר מתוך הדוגמה הקיימת, עם שמות משתנים ויחידות ללא שינוי | התלמיד מקשר פעולה בקוד לשלב בדוגמה. |
| תרגול בסיוע | בוחרים משימת ליבה מתוך Student-Lab.ipynb ומציגים רק נתון, דרישה ורמז | התלמיד מציע פעולה ומנמק אותה לפני כתיבת קוד. |
| העברה עצמאית | ממשיכים במשימת הליבה עם מאפיין או הקשר השונים מהדוגמה הפתורה | התלמיד מגיש ביצוע ופירוש ללא העתקת הפתרון. |
| סיום | האם MAE=20 פירושו 20 אחוזים? | התלמיד מצביע על ראיה ומציין מגבלה. |

**תוצר בתוך מכסת הזמן:** בפרויקט רגרסיה מוסיפים ניתוח טעות ביחידות היעד. בסיווג ממשיכים בניתוח מחיר טעויות ובהשוואה הרלוונטית.

**הקשר להמשך:** סכום משוקלל, שגיאה ועדכון משקולות מכינים ל־DL. רגרסיה ופרספטרון אינם מוצגים כאלגוריתמי חובה ביחידה 5.

הטבלה מפרטת את חומר המפגש הקיים; אין להפוך כל שורה לשקף נוסף אם היא חורגת ממכסת השקפים. במפגש הגנה משתמשים בה כשאלות ומשוב על הפרויקט האישי, ללא מעבדה נוספת.
