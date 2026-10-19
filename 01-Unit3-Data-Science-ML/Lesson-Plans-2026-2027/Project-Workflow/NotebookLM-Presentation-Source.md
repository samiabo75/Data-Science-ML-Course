# מקור למצגת — תהליך חקר מלא
דוגמה ותרגול שלמעבדתTitanic בהשתלמות. כלי תומך בתוך 30שעות הפרויקט; לאשיעור 40. רק הדוגמה הפתורה מותרת לפתרון במצגת; לתרגול נותנים רמזים בלבד.

## חלק א — חקר פתור
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# משאלת חקר למודל חיזוי — דוגמה מלאה על Titanic
**עיבוד שלנו למעבדת מפגש 9 בהשתלמות**, עם השלמה לתהליך תקין: מקור → שאלה → הפרדה → EDA → הכנה → אימון → אימות ובחירה → הערכת סוף → מסקנות ותיעוד.
זו דוגמת הוראה בתוך שעות ההוראה/הפרויקט שכבר הוקצו, ולא פרויקט חדש או שעות נוספות. כל הנתונים היסטוריים; אין לפרש תחזית כהחלטה על חיי אדם או קשר סיבתי. אין פריסה למוצר.
[עוגן ההשתלמות](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/11-ML-Project-Workflow/Meeting-09-Project-Labs.md). אין טענה שמצגת המקור עצמה נפתחה כאן מחדש. הקובץ נקרא כפי שקושר בהשתלמות; המקור הראשוני/רישוי העותק דורשים בדיקה לפני בחירה לפרויקט אישי.

## 1. השאלה והשימוש
האם מאפיינים מתועדים של נוסע מסייעים לחזות Survived בתוך המדגם ההיסטורי? כל שורה נוסע. Survived=1 היא המחלקה החיובית. בוחרים מראש F1 של המחלקה 1 כמדד בחירה, ומדווחים גם Accuracy, Precision ו־Recall. הבחירה במדד היא החלטה דידקטית מקומית, לא מחוון רשמי.

### תא קוד 3
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

## 2. סכמה ואיכות לפני בחירה
בוחרים מראש מאפיינים ידועים לפני התוצאה: Age בשנים, Fare ביחידות המטבע המתועדות בקובץ, Sex קטגוריה מתועדת ו־Pclass מחלקת נסיעה קטגוריאלית. Pclass מקודדת כאן One-Hot כדי לא לכפות מרווחים. אין Name/PassengerId כמספרי חיזוי ואין תכונה הנגזרת מהישרדות. Sex הוא שדה היסטורי רגיש: שימושו דורש דיון בהטיה; אין המלצה לשימוש עכשווי בהחלטות על אנשים.
בודקים מזהה כדי למנוע עותק של אותו נוסע בשני צדי חלוקה. כללי סבירות נקבעים מתחום המשמעות, לא על סמך הצלחת Test.

### תא קוד 5
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

## 3. חקר בפיתוח בלבד
שומרים Test לפני החקר שמשפיע על בחירת מאפיינים. קוראים info/describe, בודקים חסרים, מסכמים קבוצות ומציירים גרפים לשאלות. הקוד הבא עובד על Train בלבד; לא משלימים חסרים לפני הסקירה. כאן השאלה והמאפיינים קבועים מראש. אם קובץ הוצג כבר בכיתה, זו הדגמת פרוטוקול ולא מבחן בלתי תלוי חדש.

### תא קוד 7
```python
development=X_train.copy()
development["Survived"]=y_train
development.info()
display(development.describe())
print("Missing:")
print(development.isna().sum())
display(development.groupby("Pclass")["Survived"].agg(["count","sum","mean"]))
```

## 4. גרפים וקריאת פלט
היסטוגרמה: כיצד הגיל מתפלג בין הערכים הידועים? Countplot: כמה דוגמאות מכל מחלקת יעד באימון? ממוצע Survived לכל מחלקת נסיעה הוא שיעור במדגם, ולא אפקט סיבתי.

### תא קוד 9
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

## 5. הכנה כחלק מהמודל
מספריים: השלמת חציון ואז StandardScaler. קטגוריות: השלמת שכיח ואז One-Hot. כל fit מתרחש באימון הפנימי של הקיפול; לכן ColumnTransformer נמצא בתוך Pipeline. לא מבצעים fit להכנה על כל הנתונים לפני CV.

### תא קוד 11
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

## 6. קו בסיס ומודל השוואה
לפני חשיפת Test משווים ב־CV על אותן חלוקות: KNN שנבחר, SVM ליניארי עם C=1 שנקבע מראש, ו־Dummy שמנבא את המחלקה הנפוצה באימון. כאן משווים שני אלגוריתמים תואמי סיווג; לא משווים R² של רגרסיה ל־F1 של סיווג. ציון CV לאחר בחירה אינו אומדן חסר הטיה; Test נשמר להערכת סוף.

### תא קוד 13
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

## 7. הערכת סוף — אחרי סגירת כל הבחירות
מפיקים פעם אחת תחזיות סופיות; כמה מדדים מאותן תחזיות אינם כמה ניסיונות בחירה. מפרשים את חיובי=1, ומכנים בדיוק את FP/FN. אין משנים K או מאפיינים אחרי התוצאה. ניתוח הטעויות הוא דיווח; רעיון לשיפור עתידי מחייב סבב הערכה חדש.

### תא קוד 15
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

## 8. דוגמת חיזוי חדשה וגבולותיה
נוסע דמיוני עם קלט תקין מדגים predict בלבד. אין אמת ידועה ולכן אין לו ציון Accuracy, ואין מייחסים לו הסתברות מן התווית.

### תא קוד 17
```python
new_example=pd.DataFrame([{feature:(1 if feature=="SibSp" else 25 if feature=="Age" else 20 if feature=="Fare" else "female" if feature=="Sex" else 3) for feature in features}])
print("Teaching example prediction:",chosen.predict(new_example))
```

## 9. מסקנה, מגבלות ורפלקציה
**דוגמת ניסוח:** בתנאי המדגם והחלוקה המתועדים, CV בחר את המודל שמודפס לעיל. תוצאת Test היא המדדים שהתקבלו בפועל; אין להחליף אותם במספר צפוי. מפרשים לפחות טעות אחת. המדגם ההיסטורי אינו מייצג נוסעים בני ימינו, אין להסיק סיבתיות מתכונה, וחלוקה אקראית אינה מבטיחה הפרדת בני אותה משפחה. מחקר על העברה למשפחות חדשות ידרוש מזהה קבוצה ותכנון חלוקה אחר.
**להגשה:** הוסיפו שער, מקור ותאריך/גרסה, מילון נתונים, פירוש לכל גרף, יומן החלטות, טבלת ניסויים, תוצאות, מגבלות ורפלקציה אישית. הריצו מחדש מתחילת המחברת והסבירו כל תא. סכמת תיעוד זו נשענת על פרק14 בתכנית יחידה 3; אין כאן אישור למחוון תשפ״ז מלא.
**להמשך:** בי״א מעמיקים במרחקים, סטטיסטיקה והכללה; ב־DL משנים את המודל ושומרים על שיטת החקר וההערכה. אין צורך ברשת בכיתה י׳.

---
## חלק ב — תרגול עצמאי
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# משאלת חקר למודל חיזוי — תרגול עצמאי ללא פתרון על Titanic
**עיבוד שלנו למעבדת מפגש 9 בהשתלמות**, עם השלמה לתהליך תקין: מקור → שאלה → הפרדה → EDA → הכנה → אימון → אימות ובחירה → הערכת סוף → מסקנות ותיעוד.
זו דוגמת הוראה בתוך שעות ההוראה/הפרויקט שכבר הוקצו, ולא פרויקט חדש או שעות נוספות. כל הנתונים היסטוריים; אין לפרש תחזית כהחלטה על חיי אדם או קשר סיבתי. אין פריסה למוצר.
[עוגן ההשתלמות](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/11-ML-Project-Workflow/Meeting-09-Project-Labs.md). אין טענה שמצגת המקור עצמה נפתחה כאן מחדש. הקובץ נקרא כפי שקושר בהשתלמות; המקור הראשוני/רישוי העותק דורשים בדיקה לפני בחירה לפרויקט אישי.

הקשר והנתונים מוכרים; המשימה היא לבצע את כל השלבים בעצמכם עם קבוצת מאפיינים אחרת. אין חובה לבצע בנוסף פרויקט אישי שני.

## שאלה ומקור
נסחו שאלה, יעד, חיובי ויחידת תצפית. טענו את CSV של מפגש9, בדקו schema ואת ייחוד PassengerId. בדקו מקור ורישוי לפני בחירת מאגר גמר.

### תא קוד 4
```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה:** כתבו כאן.

## הפרדה
הגדירו numeric=[Age,Fare,SibSp], categorical=[Sex,Pclass], y=Survived. חלקו 25% Test עם random_state=17 ו־stratify=y לפני EDA מכוון מודל. אל תשלימו יעד חסר.

### תא קוד 7
```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה:** כתבו כאן.

## למידת הנתונים
על Train בלבד: info,describe,חסרים, groupby ל־Pclass ושני גרפים עם שאלה, צירים, ממצא ומגבלה. מה אומר ממוצע יעד 0/1?

### תא קוד 10
```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה:** כתבו כאן.

## הכנה ואימון
בנו שני מסלולי הכנה בתוך Pipeline. בחרו מראש K=[3,5,9], חמישה קיפולים ו־F1 לחיובי1. הסבירו היכן fit מופעל ומה נשמר.

### תא קוד 13
```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה:** כתבו כאן.

## אימות והשוואה
הציגו cv_results_,best_params_ והשוו גם SVM ליניארי C=1 וקו בסיס. בחרו לפי ממוצע CV בלבד, לפי סדר KNN,SVM,Baseline בהכרעת שוויון.

### תא קוד 16
```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה:** כתבו כאן.

## הערכת סוף
אמנו את המתכון הנבחר על כל Train. הפיקו תחזיות Test, מטריצה, Accuracy,P/R/F1 וקו בסיס. בדקו P/R/F1 ביד מהמטריצה. אל תשנו מודל לפי Test.

### תא קוד 19
```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה:** כתבו כאן.

## תחזית, מסקנה והגנה
הציגו תחזית לקלט דמיוני תקין, נתחו שתי טעויות וכתבו מסקנה, מגבלה, רפלקציה והוראות שחזור. מה נשאר אותו דבר אם בהמשך מחליפים את המודל ברשת?

### תא קוד 22
```python
# כתבו כאן את הקוד
```

**הסבר ומסקנה:** כתבו כאן.
