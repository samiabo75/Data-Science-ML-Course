# מקור למצגת — שיעור 36 — StandardScaler מול MinMaxScaler — חישוב והסבר
**קהל:** תלמידי כיתה י׳ מתחילים. **מכסה:** 1 שעות לימוד (45 דקות), כולל תרגול; המצגת מחליפה חלק מההסבר ואינה מוסיפה זמן.
**שלב בתהליך החקר:** הכנה.
**פתיחה מוכרת:** איך משווים מחיר וזיכרון של מחשבים על סולמות שונים בלי ללמוד את הסרגל מנתוני הבחינה?
**גבולות הליבה במצגת ובתרגול:** השוואה ידנית Standard/MinMax עם נתוני אימון ובדיקה אחרים ואז אימות בקוד.
**המחשה חזותית מומלצת:** אותם ערכיTrain/Test עלשניסרגלים: z=(x−mean_train)/std_train מול(x−min_train)/(max_train−min_train). ערךTest עשוילצאתמטווח0–1.
**זיקה להמשך:** הזיקה המרכזית היא לבסיס וקטורי, סטטיסטי או להערכת מודלים; השתמשו רק בזיקה המפורשת בחומר, כקדימות להמשך ולא כהוראת יחידה 5 מלאה.

## הוראות למניעת ערבוב דוגמה ותרגול
חלק א הוא דוגמה פתורה שאפשר להסביר ולפתור בשקפים. חלק ב הוא תרגול עצמאי: מציגים את הדרישה, מפרקים לשלבים ונותנים רמזים; אין מייצרים פתרון מלא,קוד מלא או תוצאות סופיות של המשימות הנבחרות. אין בקובץ פתרוןמתועד לתרגול. חומר עודף במחברות מיועד לחזרה; גבולותהליבה לעיל גוברים על שאיפה לכסותכל תא.
דוגמאות מומצאות אינן מאגר אמיתי. קישורים הם ייחוס; אין להניח שתוכנם נכלל אוטומטית במקור שהועלה. לא להמציא פלט,דיוק או גרף מאומת כשהם אינם מופיעים בטקסט.

## חלק א — הסבר ודוגמה פתורה
מקור: `Guided-Lesson.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 36 — StandardScaler מול MinMaxScaler — חישוב והסבר
**פתיחה:** דודו יודע שמרחק מושפע מיחידות המדידה. כעת עליו להסביר מה בדיוק מחושב בשתי שיטות שינוי קנה מידה,ואילו פרמטרים נשמרים מאימון.

**עוגן:** [סיכום מפגש 7](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/10-Data-Preparation/Meeting-07-Didactic-Summary.md),שיעור 21 ומפרט הבחינה שמסר המורה. MinMaxScaler נדרש במפורש ברשימה,ולכן אינו עוד רשות בתכנון שלנו.
אלה חומרים מותאמים חדשים,לא שחזור תרגיל מקור. חומרי ההשתלמות לא שונו.


## למה לומדים את זה עכשיו?
איך משווים מחיר וזיכרון של מחשבים על סולמות שונים בלי ללמוד את הסרגל מנתוני הבחינה?
**בתהליך הפרויקט:** הכנה.
**מסגרת פעילה:** 1 שעות לימוד — 45 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.

## משמעות מתמטית ומושגים
StandardScaler מחשב z=(x−μ_train)/σ_train עם ddof=0. MinMaxScaler בטווח ברירת המחדל מחשב u=(x−min_train)/(max_train−min_train). שתיהן נלמדות מאימון. MinMax אינו מבטיח שכל Test ייפול בין 0 ל־1 כאשר clip=False,וברירת המחדל היא False. תקנון אינו הופך התפלגות לנורמלית. הנוסחאות הידניות כאן מניחות שונות וטווח שאינם אפס;בעמודה קבועה יש לספרייה טיפול מוגדר נפרד.

## דוגמה ידנית ואז ספרייה
באימון 10,20,30:ממוצע 20,מינימום 10,מקסימום 30. חשבו את התקנון ואת MinMax של 20 ושל 40 לפני הרצה.

### תא קוד 5
```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
train=pd.DataFrame({"measurement":[10.,20.,30.]})
test=pd.DataFrame({"measurement":[40.]})
mean_train=train["measurement"].mean()
std_train=train["measurement"].std(ddof=0)
min_train=train["measurement"].min()
max_train=train["measurement"].max()
manual_standard=(test["measurement"]-mean_train)/std_train
manual_minmax=(test["measurement"]-min_train)/(max_train-min_train)
standard=StandardScaler().set_output(transform="pandas")
minmax=MinMaxScaler().set_output(transform="pandas")
standard.fit(train);minmax.fit(train)
standard_train=standard.transform(train)
standard_test=standard.transform(test)
minmax_train=minmax.transform(train)
minmax_test=minmax.transform(test)
display(standard_train);display(minmax_train)
display(standard_test);display(minmax_test)
print("Manual Test:",manual_standard.to_list(),manual_minmax.to_list())
```

## מה נלמד באימון?
mean_,scale_ ו־data_min_,data_max_ הם תוצאות fit. אין לבצע fit שני על Test. קליפת ערכים לא משנה את העובדה שיש חריגה מהטווח;כאן לא מפעילים clip.

### תא קוד 7
```python
print("Standard mean and scale:",standard.mean_,standard.scale_)
print("MinMax training limits:",minmax.data_min_,minmax.data_max_)
print("Standard train mean:",standard_train.mean().to_dict())
print("Standard train std ddof=0:",standard_train.std(ddof=0).to_dict())
print("MinMax test outside [0,1]:",minmax_test.iloc[0,0])

```

## בדיקת הבנה בעל־פה
1. חשבו ביד ממוצע,סטיית תקן ddof=0,מינימום ומקסימום של האימון הנתון.
2. חשבו ידנית Standard ו־MinMax עבור שתי דוגמאות הבדיקה. כתבו מאיזה חלק נלקח כל פרמטר.
3. התאימו שני Scalers לאימון בלבד והמירו אימון ובדיקה. השוו לתוצאות הידניות.
4. הסבירו מדוע ערך בדיקה עשוי לקבל MinMax שלילי או גדול מ־1,ומדוע ממוצע Test מתוקנן אינו חייב להיות אפס.
5. בהסבר בעל־פה:מתי fit,mתי transform,מדוע יש השפעה על KNN,והאם אחת השיטות תמיד משפרת חיזוי?

אין fit_transform ל־Test;אין חלוקה אוטומטית באפס בנוסחה ידנית;אין פירוש ל־MinMax כהסתברות. למתקשים מספקים טבלת ארבעת הפרמטרים;למצטיינים שואלים מה יקרה אם מוסיפים ערך Test קיצוני בלי fit מחדש.


---

## חלק ב — תרגול תלמיד ללא פתרון
מקור: `Student-Practice.ipynb`. תאי הקוד מובאים כטקסט; פלטים אינם נוצרים על ידי ההמרה.

# שיעור 36 — תרגול תלמיד: StandardScaler מול MinMaxScaler — חישוב והסבר
**פתיחה:** דודו יודע שמרחק מושפע מיחידות המדידה. כעת עליו להסביר מה בדיוק מחושב בשתי שיטות שינוי קנה מידה,ואילו פרמטרים נשמרים מאימון.

**עוגן:** [סיכום מפגש 7](https://github.com/samiabo75/Data-Science-ML-Course/blob/main/01-Unit3-Data-Science-ML/10-Data-Preparation/Meeting-07-Didactic-Summary.md),שיעור 21 ומפרט הבחינה שמסר המורה. MinMaxScaler נדרש במפורש ברשימה,ולכן אינו עוד רשות בתכנון שלנו.
אלה חומרים מותאמים חדשים,לא שחזור תרגיל מקור. חומרי ההשתלמות לא שונו.


## למה לומדים את זה עכשיו?
איך משווים מחיר וזיכרון של מחשבים על סולמות שונים בלי ללמוד את הסרגל מנתוני הבחינה?
**בתהליך הפרויקט:** הכנה.
**מסגרת פעילה:** 1 שעות לימוד — 45 דקות, כולל דוגמה ותרגול עצמאי. המורה בוחר את משימות הליבה שבמדריך; שאר הפעילויות לחזרה או לעיון, ללא תוספת שעות.
**התרגול הנבחר למסגרת זו:** השוואה ידנית Standard/MinMax עם נתוני אימון ובדיקה אחרים ואז אימות בקוד.

התאים ריקים בכוונה. כתבו קודם מה אתם מצפים לקבל,ואחר כך הסבירו את הפלט. השתמשו במודרכת כתבנית אך הסבירו כל קוד שנכנס למחברתכם.

### תא קוד 4
```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# נתונים דידקטיים מומצאים,ללא CSV
train = pd.DataFrame({"measurement":[100.,200.,300.]})
test = pd.DataFrame({"measurement":[50.,400.]})
```

## משימה 1
חשבו ביד ממוצע,סטיית תקן ddof=0,מינימום ומקסימום של האימון הנתון.

### תא קוד 6
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 2
חשבו ידנית Standard ו־MinMax עבור שתי דוגמאות הבדיקה. כתבו מאיזה חלק נלקח כל פרמטר.

### תא קוד 9
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 3
התאימו שני Scalers לאימון בלבד והמירו אימון ובדיקה. השוו לתוצאות הידניות.

### תא קוד 12
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 4
הסבירו מדוע ערך בדיקה עשוי לקבל MinMax שלילי או גדול מ־1,ומדוע ממוצע Test מתוקנן אינו חייב להיות אפס.

### תא קוד 15
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

## משימה 5
בהסבר בעל־פה:מתי fit,mתי transform,מדוע יש השפעה על KNN,והאם אחת השיטות תמיד משפרת חיזוי?

### תא קוד 18
```python
# כתבו כאן את הפתרון שלכם
```

**הסבר התלמיד:** כתבו כאן.

