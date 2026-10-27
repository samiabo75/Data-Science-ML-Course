# בקרת עומק — מפגש 28: חקר Titanic מלא

**Candidate עד ראיית Run All אמיתית.**

## עוגנים שאין לשנות
Guided seed42: Age, Fare, Sex, Pclass. Student + Teacher Solution seed17: Age, Fare, SibSp, Sex, Pclass. בכל המחברות יעד `Survived` חיובי 1, PassengerId ייחודי, פיצול stratify לפני EDA מוכוון החלטות, Pipeline מספרי/קטגוריאלי, K=[3,5,9], CV=StratifiedKFold(5,shuffle,seed42), השוואה ל־SVC(kernel='linear',C=1) ול־DummyClassifier(most_frequent). הכרעת שוויון קבועה KNN → SVM → Baseline; הערכת Test חד־פעמית.

## שדרוגים
שלוש מחברות Audited בתיקייה הקיימת. Guided ו־Teacher עוקבות אחרי המחברות המקוריות ומוסיפות בדיקות נוקשות: סכמה, חלוקה ללא חפיפה, מפתח ייחודי, מדדים ידניים מול ספריית sklearn, בחירת מודל על סמך CV בלבד. Student כוללת מטלות מודרכות־עצמאיות עם 32 השלמות קוד: חישוב F1 ידני, בדיקת נתונים, EDA רק על Train, אימון Pipeline בתוך CV, השוואת מודלים ומבחן Test סופי. פתרונות נבדקים על עותקים בזיכרון ואינם מופיעים במחברת התלמיד.

## מקור נתונים ושחזור
נוסף `Datasets/titanic_data.csv` כתמונת מקור של `https://github.com/arielb30/datasets/blob/main/titanic_data.csv`. בודקי CI מחליפים בעת ההרצה את כתובת Raw של המקור בנתיב המקומי. יש לבדוק זמינות/הרשאות שימוש בעת הפצה מחוץ למאגר.

## מצב בדיקות
Run All דורש מעבר 24/24 מחברות מודרכות/מורה ו־12/12 מחברות תלמיד בתצורת פתרון במפגשים 17–28. לא מאושר ללא ראיית CI. הגהת המצגות והפיילוט נשמרים לסוף.
