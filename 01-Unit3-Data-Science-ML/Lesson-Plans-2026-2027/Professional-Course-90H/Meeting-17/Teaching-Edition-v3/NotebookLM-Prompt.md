צור מצגת **בת 9–10 שקפים בלבד**, מקצועית ובהירה לתלמידי כיתה י׳, יחידה 3, **מפגש 17 — KNN בספריית Scikit-learn: אימון, חיזוי והערכה**. מקור מרכזי: NotebookLM-Source.md ו־Student-Book.md בתיקיית Meeting-17/Teaching-Edition-v3. אם מצורפות מצגות ההשתלמות, התמקד ב־5.2 KNN with Sklearn.pptx שקפים 5–11 וב־Data preparation.pptx שקפים 24–29. **אל תכלול קובצי פתרון המורה במקורות מצגת התלמידים.**

עיצוב: רקע בהיר, עברית תקינה RTL, קוד ונוסחאות LTR, כתב גדול, גרפים עם תוויות קריאות, ובלי טעויות כתיב או חישוב. כל שקף רעיון אחד, שאלה סוקרטית והסבר תוצאה.

רצף השקפים:
1. סיפור פינגווין חדש וההבדל בין לחזות לבין לדעת אם צדקנו.
2. טבלת ארבע תוויות אמת [1,0,0,1] מול חיזוי [1,0,1,1] — המחשה מומצאת בלבד.
3. חישוב Accuracy=3/4=0.75=75%, פירוש מונה/מכנה והגדרת שגיאה אחת (השתמש ב־accuracy-four-observations.svg).
4. Penguins האמיתי: 344 רשומות, 7 עמודות, 3 מינים; מטרה y=species ו־X של הדגמת המורה בלבד flipper_length_mm ו־body_mass_g, יחידות וסוגי חסרים.
5. פיצול משותף Train/Test (258/86, seed42, stratify=y); diagram knn-train-test-evaluation.svg.
6. Train-only filling of missing values, StandardScaler.fit על Train בלבד ו־transform לשניהם; Test אינה משמשת ללמידת פרמטרים.
7. KNeighborsClassifier עם K3, weights uniform, metric euclidean; משמעות fit(X_train_scaled,y_train) ו־predict(X_test_scaled) בלי y_test.
8. comparison עם actual/predicted/correct ושמירת אינדקסים; accuracy_score על אמת מול תחזית.
9. טעויות, איך מוצאים עד 3 שורות בדיקה שגויות, והבדל בין זיהוי טעות לבין הסבר סיבתה. error-inspection-table.svg מסומנת סכמטית **לא תוצאת Penguins**.
10. שאלות הגנה ופתיחת מעבדת התלמיד על זוג מדידות **אחר**, ללא פתרונות, והכנה ל־45 דקות פרויקט.

**אסור להציג את הציון או את תוצאות המחברת העצמאית**: bill_length_mm/bill_depth_mm, seed17. הצג רק הנחיה לבניית הקוד. אין לבחור K לפי Test, אין להקדים מטריצת בלבול/Precision/Recall/בדיקת GridSearch. לא לטעון ש־Accuracy על חלוקה יחידה מוכיח דיוק עתידי. לא להשוות את שתי המחברות כבדיקת עדיפות מאפיינים, משום שגם התכונות וגם seed שונים.

הפקה אינה אישור: הגה כל שקף ידנית, תקן עברית/RTL/סמלי משוואה, וודא מספרים, אזהרות זליגה, יחידות ושמות עמודות.