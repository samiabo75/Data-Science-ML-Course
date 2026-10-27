# בקרת איכות — מפגש 12 (27.10.2026)
**מעמד: Content Checked + Verified Source CSV + Representative Local Code Test; NOT READY.**

## מקור ומיפוי
נבדקו שלוש מחברות המקור. מטלת התלמיד נשמרה במלואה: טעינה ודוח חסרים, יעד species, תכונות flipper_length_mm/body_mass_g, פיצול משותף עם test_size=.25 ו־seed=17 ו־stratify=y, השלמה מממוצעי Train, בדיקת שמירת מקור וניתוח שלוש שגיאות; חציון אימון כרשות. הדגמת המקור היא על bill_length_mm/bill_depth_mm ו־seed=42.

## מה מאומת מספרית
- מקור Penguins via GitHub, SHA b5093336d83d99d8835c606b455d00065ab7cdcf: 344 שורות, 7 עמודות; species=0 חסרים; sex=11 חסרים; ארבע מדידות מספריות=2 חסרים כל אחת; Adelie=152, Chinstrap=68, Gentoo=124.
- פיצול 25% של 344: 258 Train ו־86 Test (בהנחת הזכאות המלאה בקובץ).
- דוגמה מומצאת: Train=[10,20,NaN] ⇒ mean_train=15, Test=[1000,NaN] ⇒ לאחר יישום [1000,15]; חישוב פסול על כל הידועים 1030/3≈343.333.
- Pandas 2.2.3 ו־Scikit-learn 1.8.0 בסביבה המקומית: בדיקות דוגמת ההשלמה וחלוקה מייצגת על דאטה זעיר עברו. **לא מדובר בהרצת המחברת המלאה עם Penguins.**

## מה נבנה
ספר תלמיד ומדריך מורה מעמיקים; דף פתרון ידני; שלושה SVG ממקור מספרי מאומת; שלוש מחברות v4 Audited (Guided, Student Fill Blanks, Teacher Solution); מקור מצגת/פרומפט NotebookLM ותיעוד בקרה.

## שערים פתוחים לפני READY
1. בדיקת מבנה שלוש המחברות, שלושת קובצי SVG וקישורי GitHub אחרי פרסום.
2. Run All אמיתי ב־Colab של Guided-Audited ושל Teacher-Solution-Audited כולל טעינת קובץ Raw ומדידת החסרים בכל קבוצת פיצול.
3. יצירת מצגת NotebookLM, הגהת כל שקף ועיון במצגות המקור הממופות.
4. פיילוט כיתה והצלבה למפרט הערכה רשמי תקף.

## כשלים שצריך לזהות
- Target leakage: species בתוך X או המצאת species חסר.
- Test leakage: מילוי לפני split או למידת ממוצע X_test.
- Index mismatch: חלוקת X ו־y בנפרד.
- Misleading claim: הכרזה על Accuracy למרות שלא אומן מודל.
- Strategy risk: חלוקה אקראית כאשר יש זמן/קבוצות חופפות.

**אין לאשר READY על סמך קיום קבצים או מספר בדיקות assert בלבד.**