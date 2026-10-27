# בקרת איכות חוזרת — מפגש 23 (27.10.2026)
**Candidate, NOT READY.**

## נאמנות למקור
נבדקו שוב שלוש מחברות המקור. Guided מלמד bill_length_mm, bill_depth_mm, island, seed42; Student/Teacher Solution עובדים flipper_length_mm, body_mass_g, island, seed17. בשניהם: 25% Test, CV חמישה קיפולים, K=[3,5,9], macro-F1, Pipeline מספרי/קטגוריאלי, refit=True. המחברות המקוריות לא שונו.

## תיקון עומק
שלוש המחברות עודכנו במקומן: Guided עם 18 תאים/35 assert; Student עם 22 תאים/25 השלמות; Teacher עם 13 תאים/39 assert. נוספו: מפת 15 fits+refit, בדיקות קיפולים, הדגמת זליגת StandardScaler, בדיקות cv_results_/best_params_/best_score_, השוואת DummyClassifier, כרטיס יציאה. תוקן שם תחזיות קו הבסיס `dummy_prediction`.

## בדיקות
הורץ ניסוי sklearn מקומי **מייצג על נתונים סינתטיים**, כולל ColumnTransformer, GridSearchCV, cross validation ו־refit, ועבר; ראו `Local-Code-Validation.md`. אין טענה להרצת קובצי Penguins המלאים או ל־Run All של המחברות.

## פתוח
Run All מלא במודרכת ובפתרון המורה ב־Colab/Penguins, מילוי והרצת התלמיד, בדיקה חזותית של SVG ומצגת NotebookLM, ופיילוט כיתה.
