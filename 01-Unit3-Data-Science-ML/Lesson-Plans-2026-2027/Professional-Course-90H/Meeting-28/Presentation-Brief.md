# מקור מקצועי למצגת — מפגש 28 — חקר מלא והערכת סוף
**קהל: ** כיתה י׳, תלמידים חדשים בנושא. **מכסה: ** 2 שעות הוראה ותרגול ו־ 1 שעות פרויקט; יחד 135 דקות.
המסמך מרכז את הסיפור, ההסבר, דוגמה פתורה וקוד, מטרות המעבדה והוראות ההמחשה. הוא מעבד את מצגות ההשתלמות המצורפות, ואינו מצגת שנוצרה או נבדקה ב־ NotebookLM.

## מצגות מקור שנבדקו
- [Data Preparation2.pptx](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/Data%20Preparation2.pptx) — שקפים 21–22.
- [יישום מכונה לומדת.pptx](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/%D7%99%D7%99%D7%A9%D7%95%D7%9D%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94%20%D7%9C%D7%95%D7%9E%D7%93%D7%AA.pptx) — שקפים 12–18,24,29.
- [Performance Indicators updated.pptx](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/Performance%20Indicators%20updated.pptx) — שקפים 21–22.

## גבולות התוכן
כ־ 85% מזמן ההוראה המושגית בתכנון נשען על מושגי ההשתלמות, וכ־ 15% מוקדשים לפיגום, מניעת טעויות וגשרים להמשך. זהו יעד תכנון בקירוב, לא מדידת אחוזי העתקה. המקורות אינם מועתקים מילה במילה. הדוגמאות החדשות וההעברות מסומנות כדידקטיות. פירוש נכון ומניעת זליגה קודמים להעתקת טעות או API ישן.

# מפגש 28 — חקר מלא והערכת סוף
## סיפור המסגרת ושאלת הלמידה
נחבר את כל החלקים לחקר Titanic: שאלה, נתונים, בחירות בפיתוח, מודל נבחר ותוצאה סופית שאפשר להסביר.

## מה נלמד ומדוע
חקר מלא כולל מקור, שאלה, חלוקה, EDA, הכנה, אימון, אימות, בחירה והערכת סוף. המודל נבחר לפני חשיפת Test. לאחר מכן מתאימים את המתכון לכל Train. טעויות ומגבלות הן חלק מהתוצר. חלוקה אקראית לנוסעים אינה מבטיחה הכללה למשפחות חדשות.

## דוגמה פתורה קטנה
לאחר בחירת מועמד באמצעות CV מפיקים פעם אחת תחזיות Test. אפשר לחשב מהן כמה מדדים, אך אין לשנות את המתכון לפי התוצאה ולדווח כאילו לא נחשפה.

```python
from sklearn.metrics import f1_score
y_true = [0, 0, 1, 1]
y_pred = [0, 1, 1, 1]
print(f1_score(y_true, y_pred))
```

**פלט צפוי ופירוש: ** 0.8. זוהי דוגמה קטנה ומוצהרת; היא אינה ציון ביצוע של פרויקט אמיתי.

## הדרך לתרגול העצמאי
במחברת החקר המלא משלימים רק מקטעים שטרם בוצעו. אין חובה לפרויקט Titanic נוסף לצד הפרויקט האישי.
עבדו לפי הסדר: נסחו את השאלה, זהו נתונים ויחידות, בחרו כלי שכבר נלמד, כתבו ציפייה, הריצו והסבירו תוצאה ומגבלה. במשימה שאינה מובנת חוזרים למושג או לדוגמה, ולא מחפשים שורת קוד להעתקה.

## תוצר לפרויקט
מבצעים הערכת סוף לפרויקט לאחר נעילת כל בחירות הפיתוח, ומצרפים תוצאות וניתוח טעויות.

## קשר ללימודי ההמשך
תהליך חקר, תיעוד והערכה עוברים לשתי תכניות ההמשך. מאגר שכבר הכרנו אינו הופך למבחן עצמאי חדש בשנה הבאה.

## בדיקה עצמית
האם כמה מדדים מאותה בדיקת סוף הם בעיה?
כתבו תשובה במילים שלכם והצביעו על תא או נתון שתומך בה. אין פתרון לתרגול העצמאי במסמך התלמיד.


## יישום מודרך מלא וקוד לדוגמה
# מפגש 28 — חקר מלא והערכת סוף
2 שעות הוראה ותרגול ו־ 1 שעות פרויקט; יחד 135 דקות.

## סיפור המסגרת
נחבר את כל החלקים לחקר Titanic: שאלה, נתונים, בחירות בפיתוח, מודל נבחר ותוצאה סופית שאפשר להסביר.

## מטרות
- לקשור שלבי חקר.
- להפריד בחירה מבדיקת סוף.
- לנתח מגבלה.

## המושגים הנחוצים
חקר מלא כולל מקור, שאלה, חלוקה, EDA, הכנה, אימון, אימות, בחירה והערכת סוף. המודל נבחר לפני חשיפת Test. לאחר מכן מתאימים את המתכון לכל Train. טעויות ומגבלות הן חלק מהתוצר. חלוקה אקראית לנוסעים אינה מבטיחה הכללה למשפחות חדשות.

## דוגמה פתורה לפני קוד
לאחר בחירת מועמד באמצעות CV מפיקים פעם אחת תחזיות Test. אפשר לחשב מהן כמה מדדים, אך אין לשנות את המתכון לפי התוצאה ולדווח כאילו לא נחשפה.

```python
from sklearn.metrics import f1_score
y_true = [0, 0, 1, 1]
y_pred = [0, 1, 1, 1]
print(f1_score(y_true, y_pred))
```

**פלט צפוי: ** 0.8

## מדוע זה חשוב?
תהליך חקר, תיעוד והערכה עוברים לשתי תכניות ההמשך. מאגר שכבר הכרנו אינו הופך למבחן עצמאי חדש בשנה הבאה.

## יישום מודרך — חלק 1
מקור הקוד: ערכה תהליך החקר הקיימת. בהמשך עוברים לתרגול עצמאי באותו נושא.

### טעינה ובדיקת קלט
טוענים את מקור הנתונים שהופיע בתרגול. בודקים שדות וממדים לפני שימוש. כתובת Raw שונה מדף התצוגה של GitHub.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split,StratifiedKFold,GridSearchCV,cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.dummy import DummyClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,f1_score
url="https://raw.githubusercontent.com/arielb30/datasets/main/titanic_data.csv"
raw=pd.read_csv(url)
print("Source shape:",raw.shape)
print("Columns:",raw.columns.tolist())
```

### תשתית הנתונים והחלוקה
קראו תחילה את היעד ואת שמות המאפיינים. החלוקה שומרת התאמה בין שורות X ל־ y. הפרמטר random_state מאפשר שחזור ואינו משפר דיוק בפני עצמו.

```python
numeric=['Age', 'Fare']
categorical=['Sex', 'Pclass']
features=numeric+categorical
required=features+["Survived","PassengerId"]
assert set(required).issubset(raw.columns),"Check the supplied schema"
assert raw["PassengerId"].notna().all()
assert raw["PassengerId"].is_unique,"Resolve repeated people before splitting"
assert set(raw["Survived"].dropna().unique()).issubset({0,1})
data=raw.dropna(subset=["Survived"]).copy()
assert data["Age"].dropna().ge(0).all()
assert data["Fare"].dropna().ge(0).all()
X=data[features].copy()
y=data["Survived"].astype(int).copy()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
assert set(X_train.index).isdisjoint(X_test.index)
print("Eligible / train / test:",len(data),len(X_train),len(X_test))
```

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

```python
development=X_train.copy()
development["Survived"]=y_train
development.info()
display(development.describe())
print("Missing:")
print(development.isna().sum())
display(development.groupby("Pclass")["Survived"].agg(["count","sum","mean"]))
```

### המחשה חזותית
לפני הרצה הגדירו שאלה, סוגי משתנים ויחידות. אחרי הרצה פרשו את הצירים ואת הממצא. אין להסיק סיבתיות או למחוק קצה רק מן הציור.

```python
fig,axes=plt.subplots(1,2,figsize=(10,4))
sns.histplot(data=development,x="Age",bins=12,ax=axes[0])
axes[0].set_title("Training ages (known values)")
axes[0].set_xlabel("Age (years)")
sns.countplot(data=development,x="Survived",ax=axes[1])
axes[1].set_title("Training labels")
axes[1].set_ylabel("Number of records")
plt.tight_layout();plt.show()
```

### חיפוש מועמדים
קראו את שמות השלבים, רשימת המועמדים ומדד הבחירה. החיפוש מקבל נתוני אימון בלבד; נתוני האימות הפנימיים אינם Test חיצוני.

```python
prepare=ColumnTransformer([
 ("numeric",Pipeline([("fill",SimpleImputer(strategy="median")),("scale",StandardScaler())]),numeric),
 ("categorical",Pipeline([("fill",SimpleImputer(strategy="most_frequent")),("encode",OneHotEncoder(handle_unknown="ignore",sparse_output=False))]),categorical)
])
knn=Pipeline([("prepare",prepare),("model",KNeighborsClassifier())])
cv=StratifiedKFold(n_splits=5,shuffle=True,random_state=42)
param_grid={"model__n_neighbors":[3,5,9]}
clf=GridSearchCV(knn,param_grid=param_grid,cv=cv,scoring="f1",refit=True,return_train_score=True,error_score="raise")
clf.fit(X_train,y_train)
results=pd.DataFrame(clf.cv_results_)
display(results[["param_model__n_neighbors","mean_train_score","mean_test_score","rank_test_score"]])
print("Best KNN:",clf.best_params_,clf.best_score_)
```

### אימות בתוך הפיתוח
ההכנה נמצאת בתוך Pipeline. כל קיפול לומד את פרמטריו מתת־האימון שלו. נקרא את ממוצע האימות לפני שנחליט על מודל.

```python
svm=Pipeline([("prepare",prepare),("model",SVC(kernel="linear",C=1.0))])
baseline=DummyClassifier(strategy="most_frequent")
svm_scores=cross_val_score(svm,X_train,y_train,cv=cv,scoring="f1",error_score="raise")
baseline_scores=cross_val_score(baseline,X_train,y_train,cv=cv,scoring="f1",error_score="raise")
cv_table=pd.DataFrame({"model":["KNN","Linear SVM","Baseline"],"mean_cv_f1":[clf.best_score_,svm_scores.mean(),baseline_scores.mean()]})
display(cv_table)
# Tie policy: first row in the predefined order wins. Test is not read here.
chosen_name=cv_table.sort_values("mean_cv_f1",ascending=False,kind="stable").iloc[0]["model"]
chosen={"KNN":clf.best_estimator_,"Linear SVM":svm,"Baseline":baseline}[chosen_name]
chosen.fit(X_train,y_train)
baseline.fit(X_train,y_train)
print("Chosen before Test:",chosen_name)
```

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

```python
predictions=chosen.predict(X_test)
baseline_predictions=baseline.predict(X_test)
matrix=confusion_matrix(y_test,predictions,labels=[0,1])
display(pd.DataFrame(matrix,index=["Actual 0","Actual 1"],columns=["Predicted 0","Predicted 1"]))
tn,fp,fn,tp=matrix.ravel()
precision_manual=tp/(tp+fp) if tp+fp else 0.0
recall_manual=tp/(tp+fn) if tp+fn else 0.0
f1_manual=2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else 0.0
print("Accuracy:",accuracy_score(y_test,predictions))
print("Precision:",precision_score(y_test,predictions,zero_division=0),precision_manual)
print("Recall:",recall_score(y_test,predictions,zero_division=0),recall_manual)
print("F1:",f1_score(y_test,predictions,zero_division=0),f1_manual)
print("Baseline F1:",f1_score(y_test,baseline_predictions,zero_division=0))
comparison=X_test.copy()
comparison["actual"]=y_test
comparison["predicted"]=predictions
display(comparison[comparison["actual"]!=comparison["predicted"]].head(5))
```

### חישוב ופירוש
קראו את השמות והיחידות, כתבו ציפייה לפני הרצה ובדקו אותה בפלט. הסבירו מה השתנה ומה נשאר קבוע. אין צורך לשנן פקודה בלי להבין את פעולתה.

```python
new_example=pd.DataFrame([{feature:(1 if feature=="SibSp" else 25 if feature=="Age" else 20 if feature=="Fare" else "female" if feature=="Sex" else 3) for feature in features}])
print("Teaching example prediction:",chosen.predict(new_example))
```

## עצירה לפני המעבדה
האם כמה מדדים מאותה בדיקת סוף הם בעיה?

**התוצר הנדרש: ** במחברת החקר המלא משלימים רק מקטעים שטרם בוצעו. אין חובה לפרויקט Titanic נוסף לצד הפרויקט האישי.

## המשימות שהמצגת חייבת להכין לקראתן
במחברת החקר המלא משלימים רק מקטעים שטרם בוצעו. אין חובה לפרויקט Titanic נוסף לצד הפרויקט האישי.
**מבחן התאמה: ** כל פקודה או רעיון במשימת ליבה צריכים להיות מוסברים קודם בדוגמה, או להופיע כקוד תשתית נתון. בהכנה לתרגול הציגו נתונים, תוצר וצעדי חשיבה; אין לפתור את משימת התלמיד. המעבדה המדויקת היא Student-Lab.ipynb, ופתרונה אינו מקור למצגת התלמיד.

## הוראות חזותיות
רקע לבן או בהיר מאוד, טקסט כהה, ניגודיות גבוהה וגופן גדול. רעיון מרכזי אחד בשקף. המושג יופיע לצד דוגמה קטנה, חישוב או תרשים מדויק. משתמשים בסיפור כדי להסביר את הצורך; אין להציג את נתוני הסיפור המומצאים כאילו נאספו בפועל. לתרשים נתונים אמיתי מצרפים פלט מאומת או מסמנים שהוא סכמטי. אין להמציא ציון מודל או לקרוא ציון החלטה כהסתברות.

## מקורות משלימים מוגבלים
מניעת זליגה והכנה בתוך אימות: [תיעוד scikit-learn](https://scikit-learn.org/stable/common_pitfalls.html). פירוש R²: [תיעוד המדד](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html). משתמשים רק בקטע הרלוונטי לנושא, ללא הוספת יחידת לימוד או ספרייה חדשה.


## נספח — נוסח המעבדה העצמאית ללא פתרון
הנספח מאפשר לבדוק שהמצגת מכינה למשימה בפועל. בחרו רק את משימות הליבה שהוגדרו במדריך. אין להפוך את הנספח לפתרון בשקפים.

# מפגש 28 — חקר מלא והערכת סוף
2 שעות הוראה ותרגול ו־1 שעות פרויקט; יחד 135 דקות.

## סיפור המסגרת
נחבר את כל החלקים לחקר Titanic: שאלה, נתונים, בחירות בפיתוח, מודל נבחר ותוצאה סופית שאפשר להסביר.

## מטרות
- לקשור שלבי חקר.
- להפריד בחירה מבדיקת סוף.
- לנתח מגבלה.

## תרגול עצמאי
במחברת החקר המלא משלימים רק מקטעים שטרם בוצעו. אין חובה לפרויקט Titanic נוסף לצד הפרויקט האישי.

תאי משימות ריקים בכוונה. תשתית טעינה או מודל נתון, אם קיימים, אינם פתרון לחישוב ולפירוש שלכם. הפעילו רק את משימות הליבה שהוגדרו למפגש. שאר משימות המקור הן מאגר חזרה, ללא חובת בית נוספת.

## חלק 1 — תרגול העברה
הנתונים וההוראות מופיעים להלן. עובדים על משימות הליבה של המפגש.

## שאלה ומקור
נסחו שאלה, יעד, חיובי ויחידת תצפית. טענו את CSV של מפגש 9, בדקו schema ואת ייחוד PassengerId. בדקו מקור ורישוי לפני בחירת מאגר גמר.

```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה: ** כתבו כאן.

## הפרדה
הגדירו numeric=[Age, Fare, SibSp], categorical=[Sex, Pclass], y=Survived. חלקו 25% Test עם random_state=17 ו־ stratify=y לפני EDA מכוון מודל. אל תשלימו יעד חסר.

```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה: ** כתבו כאן.

## למידת הנתונים
על Train בלבד: info, describe, חסרים, groupby ל־ Pclass ושני גרפים עם שאלה, צירים, ממצא ומגבלה. מה אומר ממוצע יעד 0/1?

```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה: ** כתבו כאן.

## הכנה ואימון
בנו שני מסלולי הכנה בתוך Pipeline. בחרו מראש K=[3,5,9], חמישה קיפולים ו־ F1 לחיובי 1. הסבירו היכן fit מופעל ומה נשמר.

```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה: ** כתבו כאן.

## אימות והשוואה
הציגו cv_results_, best_params_ והשוו גם SVM ליניארי C=1 וקו בסיס. בחרו לפי ממוצע CV בלבד, לפי סדר KNN, SVM, Baseline בהכרעת שוויון.

```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה: ** כתבו כאן.

## הערכת סוף
אמנו את המתכון הנבחר על כל Train. הפיקו תחזיות Test, מטריצה, Accuracy, P/R/F1 וקו בסיס. בדקו P/R/F1 ביד מהמטריצה. אל תשנו מודל לפי Test.

```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה: ** כתבו כאן.

## תחזית, מסקנה והגנה
הציגו תחזית לקלט דמיוני תקין, נתחו שתי טעויות וכתבו מסקנה, מגבלה, רפלקציה והוראות שחזור. מה נשאר אותו דבר אם בהמשך מחליפים את המודל ברשת?

```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה: ** כתבו כאן.

## יישום בפרויקט
מבצעים הערכת סוף לפרויקט לאחר נעילת כל בחירות הפיתוח, ומצרפים תוצאות וניתוח טעויות.

## לפני הגשה
הריצו לפי הסדר, בדקו פלטים עדכניים, כתבו פירוש ומגבלה והצהירו היכן נעזרתם. פתרונות נמצאים בנפרד למורה אך גלויים במאגר הציבורי.