# מקור למצגת — שיעור 34 — SVM: קו הפרדה, שוליים ומימוש בספרייה
**קהל:** תלמידי כיתה י׳ מתחילים. **מכסה:** 1.5 שעות לימוד (67.5 דקות), כולל תרגול; המצגת מחליפה חלק מההסבר ואינה מוסיפה זמן.
**שלב בתהליך החקר:** מודל השוואה.
**פתיחה מוכרת:** שני קווים יכולים להפריד בין סוגי מוצרים: SVM מחפש פשרה בין שוליים לטעויות.
**גבולות הליבה במצגת ובתרגול:** רעיון שוליים, SVC ליניארי כתבנית מוכרת, החלטה חתומה ומטריצה. ללא חיפוש kernels.
**המחשה חזותית מומלצת:** כמהקווים מפרידיםואז מרווחיםלנקודות קרובות. הסבירו פשרהבין שולייםוטעויות, והבדילוdecision_function מהסתברות; ללאגזירתאופטימיזציה.
**זיקה להמשך:** רגרסיה ופרספטרון הם גשר ל־DL; אינם אלגוריתמי חובה ביחידה 5. SVM נשאר בגלל מפרט יחידה 3. אין להמציא חפיפה בין שלוש התכניות.

## הוראות למניעת ערבוב דוגמה ותרגול
חלק א הוא דוגמה פתורה שאפשר להסביר ולפתור בשקפים. חלק ב הוא תרגול עצמאי: מציגים את הדרישה, מפרקים לשלבים ונותנים רמזים; אין מייצרים פתרון מלא,קוד מלא או תוצאות סופיות של המשימות הנבחרות. אין בקובץ פתרוןמתועד לתרגול. חומר עודף במחברות מיועד לחזרה; גבולותהליבה לעיל גוברים על שאיפה לכסותכל תא.
דוגמאות מומצאות אינן מאגר אמיתי. קישורים הם ייחוס; אין להניח שתוכנם נכלל אוטומטית במקור שהועלה. לא להמציא פלט,דיוק או גרף מאומת כשהם אינם מופיעים בטקסט.

## חלק א — הסבר ודוגמה פתורה
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 34 — SVM: קו הפרדה, שוליים ומימוש בספרייה

**הקשר ללמידת מכונה:** פרספטרון יכול למצוא קו מפריד,אך ייתכנו כמה קווים. דודו רוצה להבין את הרעיון של העדפת שוליים ושל איזון בין הפרות למורכבות.

**עוגן:** [סיכום מפגש 11](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/13-Perceptron-SVM/Meeting-11-Didactic-Summary.md) ו[סיכום מפגש 12](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/13-Perceptron-SVM/Meeting-12-Didactic-Summary.md). יעד sex נשמר מעוגן מפגש 12. GridSearchCV נדחה; C ו־kernel קבועים מראש.

המחברת היא התאמה דידקטית חדשה. אין קובץ מקור חדש מהמרצה ולכן אין Exact-Original מלאכותי. אין לייחס לה אישור כיסוי מחוון עדכני.

## למה לומדים את זה עכשיו?
שני קווים יכולים להפריד בין סוגי מוצרים: SVM מחפש פשרה בין שוליים לטעויות.
**בתהליך הפרויקט:** מודל השוואה.
**מסגרת פעילה:** 1.5 שעות לימוד — 67.5 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.

## מושגים וידע קודם
Support vectors הן דוגמאות המשפיעות על הגבול. כשיש חפיפה עשויות להיות הפרות; אין טענה שכל הנתונים נפרדים. kernel מאפשר לייצג קשר לא ליניארי; מתחילים בליניארי ולא משווים גרסאות לפי Test. עבור ארבעה מאפיינים הגבול הוא על־מישור ולא קו בשרטוט דו־ממדי. אלגוריתם האימון של SVM שונה מעדכון פרספטרון.

## הסבר מתמטי
SVM ליניארי משתמש ב־w·x+b. במודל בר־הפרדה בתצורה הקנונית רוחב השוליים הוא 2/||w||. בפרשנות soft-margin,אובייקטיב ½||w||²+CΣξᵢ משלב קו ושגיאות/הפרות. C גדול מעניש הפרות יותר ביחס לרכיב המשקולות,לא מבטיח ציון Test טוב יותר. decision_function הוא ציון חתום,לא הסתברות. הרחבה זו מתארת רעיון; לא נדרשת אופטימיזציה ידנית.

## הכנה ויעד
sex כאן מתאר תיוג ביולוגי של פינגווינים במאגר,לא ניתוח אנשים. לא מסיקים מכך מודל אוניברסלי. Penguins כבר מוכר; זו הדגמה ולא מבחן בלתי תלוי חדש.

### תא קוד 6
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
url="https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df=pd.read_csv(url)
model_df=df.dropna(subset=["sex"]).copy()
features=["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]
X=model_df[features].copy();y=model_df["sex"].copy()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)

```

## אימון והערכה
הכנה נלמדת מאימון בלבד. בניסוי השוואת C או kernel משתמשים ב־CV עם כל ה־Pipeline בתוכו,כמו בשיעור 28.

### תא קוד 8
```python
# kernel ו-C נקבעו מראש; אין חיפוש על Test
model=make_pipeline(
 SimpleImputer(strategy="mean"),StandardScaler(),
 SVC(kernel="linear",C=1.0)
)
model.fit(X_train,y_train)
predictions=model.predict(X_test)
labels=["female","male"]
matrix=confusion_matrix(y_test,predictions,labels=labels)
display(pd.DataFrame(matrix,index=labels,columns=labels))
print(classification_report(y_test,predictions,labels=labels,zero_division=0))
print("Classes:",model.named_steps["svc"].classes_)
print("Number of support vectors:",model.named_steps["svc"].n_support_)

```

## ציון מול הסתברות
בסיווג בינרי סימן decision_function מתייחס ל־classes_[1] מול classes_[0]. הציון מושפע מהמודל ואינו אחוז ביטחון.

### תא קוד 10
```python
decision_scores=model.decision_function(X_test)
print("First signed decision scores:",decision_scores[:5])
print("Positive score class:",model.named_steps["svc"].classes_[1])

```

## מסקנה ובדיקת הבנה
תעדו מה נכנס,מה חושב,מה התקבל ומה אי אפשר להסיק. כתבו שני משפטים על הקשר לפרויקט.
לא מעתיקים יעד species כשהעוגן הוא sex; לא מפרשים kernel כקידוד קטגוריות; לא מבטיחים שוליים ללא הפרות בכל נתון. למתקשים מקבלים Pipeline נתון ומסבירים שלבים,למצטיינים מציעים תכנית CV כתובה בלבד.

**כרטיס יציאה:** הסבירו פעולה אחת ללא קריאת הקוד ומגבלה אחת של הדוגמה. דוגמאות מומצאות אינן ראיה על אוכלוסייה אמיתית.


---

## חלק ב — תרגול תלמיד ללא פתרון
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 34 — תרגול עצמאי: SVM: קו הפרדה, שוליים ומימוש בספרייה

**הקשר ללמידת מכונה:** פרספטרון יכול למצוא קו מפריד,אך ייתכנו כמה קווים. דודו רוצה להבין את הרעיון של העדפת שוליים ושל איזון בין הפרות למורכבות.

**עוגן:** [סיכום מפגש 11](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/13-Perceptron-SVM/Meeting-11-Didactic-Summary.md) ו[סיכום מפגש 12](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/13-Perceptron-SVM/Meeting-12-Didactic-Summary.md). יעד sex נשמר מעוגן מפגש 12. GridSearchCV נדחה; C ו־kernel קבועים מראש.

המחברת היא התאמה דידקטית חדשה. אין קובץ מקור חדש מהמרצה ולכן אין Exact-Original מלאכותי. אין לייחס לה אישור כיסוי מחוון עדכני.

## למה לומדים את זה עכשיו?
שני קווים יכולים להפריד בין סוגי מוצרים: SVM מחפש פשרה בין שוליים לטעויות.
**בתהליך הפרויקט:** מודל השוואה.
**מסגרת פעילה:** 1.5 שעות לימוד — 67.5 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.
**התרגול הנבחר למסגרת זו:** רעיון שוליים, SVC ליניארי כתבנית מוכרת, החלטה חתומה ומטריצה. ללא חיפוש kernels.

תאי המשימות ריקים בכוונה; אפשר להיעזר במחברת המודרכת. לפני כל הרצה כתבו ציפייה ואחריה פרשנות. אין להעתיק פתרון בלי להסביר.

### תא קוד 4
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
url="https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df=pd.read_csv(url)
model_df=df.dropna(subset=["sex"]).copy()
features=["bill_depth_mm","body_mass_g"]
X=model_df[features].copy();y=model_df["sex"].copy()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=17,stratify=y)

```

## משימה 1
הגדירו את יעד התרגיל ואת שני המאפיינים שבקוד הנתון. דווחו כמה שורות בעלות יעד ידוע,ומה לא נכנס ל־X.

### תא קוד 6
```python
# כתבו כאן את הפתרון שלכם
```

**תיעוד התלמיד:** כתבו כאן.

## משימה 2
בנו Pipeline עם SimpleImputer(mean),StandardScaler ו־SVC(kernel='linear',C=1). אמנו באימון בלבד.

### תא קוד 9
```python
# כתבו כאן את הפתרון שלכם
```

**תיעוד התלמיד:** כתבו כאן.

## משימה 3
הציגו מטריצת בלבול ודוח ב־Test,וציינו כותרות אמת/חיזוי. הסבירו מגבלה של נתונים מוכרים ושל אוכלוסיית המדגם.

### תא קוד 12
```python
# כתבו כאן את הפתרון שלכם
```

**תיעוד התלמיד:** כתבו כאן.

## משימה 4
הציגו decision_function ואת classes_. הסבירו למה הציון החתום אינו הסתברות ומה הקשר לסימן.

### תא קוד 15
```python
# כתבו כאן את הפתרון שלכם
```

**תיעוד התלמיד:** כתבו כאן.

## משימה 5
הסבירו במילים מה מוסיף רעיון השוליים לעומת פרספטרון,מה עשוי להשתנות עם C,ואיך הייתם בוחרים C בלי Test. אין להריץ חיפוש נוסף על הבדיקה.

### תא קוד 18
```python
# כתבו כאן את הפתרון שלכם
```

**תיעוד התלמיד:** כתבו כאן.

