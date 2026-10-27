# בדיקות קוד ומקור בפועל — מפגש 10
**27.10.2026 — Representative Local Checks PASSED, Full Notebook Run All NOT TESTED.**

## מה נבדק ישירות
1. קובץ Datasets/penguins.csv נפתח דרך חיבור GitHub ונקראו שורות המקור; SHA ‏b5093336d83d99d8835c606b455d00065ab7cdcf. 344 שורות, 7 עמודות. עבור Biscoe: size=168, count flipper=167, sum flipper=35021 מ״מ, mean≈209.7065868 מ״מ. Dream: size=124,count=124,sum=23941 מ״מ,mean≈193.0725806 מ״מ. Torgersen: size=52,count=51,sum=9751 מ״מ,mean≈191.1960784 מ״מ.
2. Python מקומי עם Pandas 2.2.3, על דוגמת המורה A=[1,NaN], B=[2,4]: size A/B 2/2; count 1/2; sum 1/6; mean 1/3. על שש העסקאות של התלמיד: A size2 count1 sum1 mean1, B size3 count2 sum4 mean2, C size1 count1 sum5 mean5.
3. Python מקומי אישר ממוצע כולל 2.5 וממוצע ממוצעי קבוצות 2.6666666666666665. במקרה קבוצת D שכל ערכיה חסרים: size=2,count=0, sum default=0, sum(min_count=1)=NaN, mean=NaN. נבדקו assert מתוך קטעי התרגול המייצגים.
4. Seaborn 0.13.2 זמין מקומית; הורץ Barplot עם estimator='mean' ו־errorbar=None ללא חריגה. זה מאמת תחביר גרף מייצג, **לא** הרצה של כל תאי המחברות או גרפי Penguins.

## מה לא נבדק
- לא הורץ Run All מלא של שתי מחברות המורה מתוך קובצי GitHub עצמם בממשק Google Colab; קריאת כתובת ה־Raw מ־Python המקומי לא אומתה. הנתונים האמיתיים אומתו דרך GitHub connector.
- קובצי SVG החדשים נשמרו במאגר אך טרם בוצעה בדיקה חזותית מול הקרנה בכיתה.
- NotebookLM קיבל מקור ופרומפט; **לא הופקה מצגת ולא בוצעה הגהה שקף־שקף**.
- המיפוי לשקפי ההשתלמות נשען על המקור המתועד; השקפים לא נבדקו מחדש חזותית. לא נעשה פיילוט ולא אושר מחוון רשמי תקף.

## תנאי השלמה לפני READY
הפעלת Run All של Guided-Audited ו־Teacher-Solution-Audited ב־Colab; קריאת Penguins, מבנה 344×7 ותוצאות קיבוץ; הגהת SVG ו־NotebookLM; נסיון תלמיד בכיתה; הצלבה עם הסילבוס ומפרט הבחינה המעודכנים.

הנוסח "Passed" מתייחס **לבדיקות מקומיות מייצגות בלבד** — לא לאישור מוכן להוראה סופי.