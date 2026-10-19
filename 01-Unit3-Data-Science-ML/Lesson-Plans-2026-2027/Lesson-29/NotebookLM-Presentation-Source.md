# מקור למצגת — שיעור 29 — כרטיס מאגר, קורלציה ובחירת גרפים
**קהל:** תלמידי כיתה י׳ מתחילים. **מכסה:** 2.5 שעות לימוד (112.5 דקות), כולל תרגול; המצגת מחליפה חלק מההסבר ואינה מוסיפה זמן.
**שלב בתהליך החקר:** שאלה וסקירה.
**פתיחה מוכרת:** לפני מחקר על הרגלי נסיעה בודקים מי השתתף והאם קשר כולל מסתיר קבוצות שונות.
**גבולות הליבה במצגת ובתרגול:** שעה לשאלה וכרטיס מקור; 1.5 שעות info/describe וקורלציה. תרגול על זוג משתנים אחר.
**המחשה חזותית מומלצת:** כרטיס מקור וקטעinfo/describe קריא. זוגותמדידה→Scatterplot→קורלציה; דוגמה קצרה מראה שקשר לא ליניארי יכול להתקיים גם כשr≈0.
**זיקה להמשך:** הזיקה המרכזית היא לבסיס וקטורי, סטטיסטי או להערכת מודלים; השתמשו רק בזיקה המפורשת בחומר, כקדימות להמשך ולא כהוראת יחידה 5 מלאה.

## הוראות למניעת ערבוב דוגמה ותרגול
חלק א הוא דוגמה פתורה שאפשר להסביר ולפתור בשקפים. חלק ב הוא תרגול עצמאי: מציגים את הדרישה, מפרקים לשלבים ונותנים רמזים; אין מייצרים פתרון מלא,קוד מלא או תוצאות סופיות של המשימות הנבחרות. אין בקובץ פתרוןמתועד לתרגול. חומר עודף במחברות מיועד לחזרה; גבולותהליבה לעיל גוברים על שאיפה לכסותכל תא.
דוגמאות מומצאות אינן מאגר אמיתי. קישורים הם ייחוס; אין להניח שתוכנם נכלל אוטומטית במקור שהועלה. לא להמציא פלט,דיוק או גרף מאומת כשהם אינם מופיעים בטקסט.

## חלק א — הסבר ודוגמה פתורה
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 29 — כרטיס מאגר, קורלציה ובחירת גרפים

**הקשר ללמידת מכונה:** דודו בוחר מאגר לחיזוי מסה: לפני מודל, מה בדיוק נמדד, מי חסר, ואילו קשרים נראים במדגם?

**עוגן:** [סיכום מפגש 3](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/06-Exploratory-Data-Analysis/Meeting-03-Didactic-Summary.md) ו[סיכום מפגש 9](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/10-Data-Preparation/Meeting-09-Didactic-Summary.md). הרחבה מסומנת המשלימה כלים שלא קיבלו שיעור עצמאי.

המחברת היא התאמה דידקטית חדשה. אין קובץ מקור חדש מהמרצה ולכן אין Exact-Original מלאכותי. אין לייחס לה אישור כיסוי מחוון עדכני.

## למה לומדים את זה עכשיו?
לפני מחקר על הרגלי נסיעה בודקים מי השתתף והאם קשר כולל מסתיר קבוצות שונות.
**בתהליך הפרויקט:** שאלה וסקירה.
**מסגרת פעילה:** 2.5 שעות לימוד — 112.5 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.

## מושגים וידע קודם
סקירת סוגי למידה: supervised מקבל יעדים ידועים; unsupervised מחפש מבנה ללא יעד; reinforcement לומד מהיזון של תגמולים באינטראקציה, לא מעמודת תווית רגילה. בקורס מתנסים בעיקר בלמידה מפוקחת. כרטיס מאגר כולל יחידת תצפית, מקור, תקופה, אוכלוסייה, שדות, יחידות, חסרים ורישוי. info מדפיס ואינו מחזיר טבלה; אין לכתוב display(df.info()) ולצפות לדוח חדש. describe אינו מסביר את משמעות השדות. nunique אינו ספירת רשומות.

## הסבר מתמטי
מתאם Pearson הוא r=Σ((x−x̄)(y−ȳ))/√(Σ(x−x̄)²Σ(y−ȳ)²), בין −1 ל־1 כששתי השונויות חיוביות. הוא מתאר קשר ליניארי, אינו הוכחת סיבתיות, וקרוב לאפס אינו שולל קשר לא ליניארי. Pandas מחשב לכל זוג לפי שורות שבהן שני הערכים ידועים, ולכן יש לדווח גם מספר זוגות. מזהה מספרי אינו מאפיין כמותי בעל משמעות. בחירת מאפיינים בעזרת יעד נעשית רק בנתוני הפיתוח, לא על Test.

## כרטיס מאגר על נתוני פיתוח
קוראים נתונים, מגדירים מראש עמודות, ושומרים בדיקה בצד. קורלציות עם יעד הן ניתוח מונחה ולכן נעשות בפיתוח בלבד.

### תא קוד 6
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
url = "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df = pd.read_csv(url)
development, heldout = train_test_split(df, test_size=0.25, random_state=42)
development.info()
display(development.describe())
display(development.describe(include="object"))
print("Species:", development["species"].unique())
print("Unique species:", development["species"].nunique(dropna=True))
display(development.isna().sum())
```

## מתאם ופיזור
מדדים אינם מחליפים גרף. סכמו מה הכיוון, העוצמה וההקשר. דווחו כמה זוגות ידועים נכללו.

### תא קוד 8
```python
numeric = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
corr = development[numeric].corr()
pair_counts = development[numeric].notna().astype(int).T.dot(
    development[numeric].notna().astype(int))
display(corr)
display(pair_counts)
plt.figure(figsize=(7, 5))
sns.heatmap(corr, vmin=-1, vmax=1, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Development data — Pearson correlations")
plt.tight_layout()
plt.show()
plt.figure()
sns.scatterplot(data=development, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.title("Development data — relationship and groups")
plt.tight_layout()
plt.show()
```

## דוגמה נגדית ומבחר גרפים
הדוגמה מומצאת: y=x² תלוי ב־x, אך הקורלציה הליניארית אפס. KDE/Violin/Pairplot הם קטלוג קריאה נוסף, לא חובה לצרף כל סוג לפרויקט; KDE הוא אומדן תלוי החלקה ואינו הוכחת נורמליות.

### תא קוד 10
```python
toy_x = pd.Series([-2., -1., 0., 1., 2.])
toy_y = toy_x ** 2
print("Nonlinear toy correlation:", toy_x.corr(toy_y))
plt.figure()
plt.scatter(toy_x, toy_y)
plt.xlabel("x"); plt.ylabel("x squared")
plt.title("Synthetic example — zero Pearson does not mean no relationship")
plt.tight_layout(); plt.show()
# עיון בקטלוג: בוחרים גרף לפי שאלה, אין צורך להפיק את כולם
# sns.kdeplot(data=development, x="body_mass_g")
# sns.violinplot(data=development, x="species", y="body_mass_g")
# sns.pairplot(development, vars=numeric, hue="species")
```

## מסקנה ובדיקת הבנה
תעדו מה נכנס,מה חושב,מה התקבל ומה אי אפשר להסיק. כתבו שני משפטים על הקשר לפרויקט.
לא מתאמים קודים שרירותיים של מינים; לא מציגים r כ־R²; לא מסיקים נורמליות מ־describe; קוראים קבוצות בגרף כדי לזהות ערבוב. לתלמיד מתקשה מספקים רשימת שדות וגרף אחד, למצטיין בודקים הבדל קשר כולל לעומת קשר בתוך קבוצה.

**כרטיס יציאה:** הסבירו פעולה אחת ללא קריאת הקוד ומגבלה אחת של הדוגמה. דוגמאות מומצאות אינן ראיה על אוכלוסייה אמיתית.


---

## חלק ב — תרגול תלמיד ללא פתרון
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 29 — תרגול עצמאי: כרטיס מאגר, קורלציה ובחירת גרפים

**הקשר ללמידת מכונה:** דודו בוחר מאגר לחיזוי מסה: לפני מודל, מה בדיוק נמדד, מי חסר, ואילו קשרים נראים במדגם?

**עוגן:** [סיכום מפגש 3](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/06-Exploratory-Data-Analysis/Meeting-03-Didactic-Summary.md) ו[סיכום מפגש 9](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/10-Data-Preparation/Meeting-09-Didactic-Summary.md). הרחבה מסומנת המשלימה כלים שלא קיבלו שיעור עצמאי.

המחברת היא התאמה דידקטית חדשה. אין קובץ מקור חדש מהמרצה ולכן אין Exact-Original מלאכותי. אין לייחס לה אישור כיסוי מחוון עדכני.

## למה לומדים את זה עכשיו?
לפני מחקר על הרגלי נסיעה בודקים מי השתתף והאם קשר כולל מסתיר קבוצות שונות.
**בתהליך הפרויקט:** שאלה וסקירה.
**מסגרת פעילה:** 2.5 שעות לימוד — 112.5 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.
**התרגול הנבחר למסגרת זו:** שעה לשאלה וכרטיס מקור; 1.5 שעות info/describe וקורלציה. תרגול על זוג משתנים אחר.

תאי המשימות ריקים בכוונה; אפשר להיעזר במחברת המודרכת. לפני כל הרצה כתבו ציפייה ואחריה פרשנות. אין להעתיק פתרון בלי להסביר.

### תא קוד 4
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
url = "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df = pd.read_csv(url)
development, heldout = train_test_split(df, test_size=0.25, random_state=17)
```

## משימה 1
הפיקו info ו־describe מספרי וקטגוריאלי ל־development בלבד; כתבו יחידת תצפית, שני טיפוסים ומגבלת אוכלוסייה.

### תא קוד 6
```python
# כתבו כאן את הפתרון שלכם
```

**תיעוד התלמיד:** כתבו כאן.

## משימה 2
הציגו unique,nunique ו־value_counts ל־island. הסבירו הבדל בין כמות ערכים שונים לכמות רשומות, והתייחסו לחסרים.

### תא קוד 9
```python
# כתבו כאן את הפתרון שלכם
```

**תיעוד התלמיד:** כתבו כאן.

## משימה 3
בחרו מראש bill_length_mm ו־body_mass_g; חשבו מתאם ומספר זוגות ידועים, וציירו Scatterplot עם יחידות.

### תא קוד 12
```python
# כתבו כאן את הפתרון שלכם
```

**תיעוד התלמיד:** כתבו כאן.

## משימה 4
צרו מטריצת מתאמים ו־Heatmap לארבע המדידות. בחרו קשר אחד והסבירו מדוע אינו מוכיח סיבתיות; אל תפתחו heldout לצורך הבחירה.

### תא קוד 15
```python
# כתבו כאן את הפתרון שלכם
```

**תיעוד התלמיד:** כתבו כאן.

## משימה 5
הראו על x=[-3,-2,-1,0,1,2,3] ו־y=x² מדוע r קרוב לאפס אינו מבטל תלות. בחרו שלושה גרפים שונים לשאלות חקר והסבירו את התאמתם.

### תא קוד 18
```python
# כתבו כאן את הפתרון שלכם
```

**תיעוד התלמיד:** כתבו כאן.

