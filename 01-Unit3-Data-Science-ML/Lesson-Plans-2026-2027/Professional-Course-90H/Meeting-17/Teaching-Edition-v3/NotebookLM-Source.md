# מקור NotebookLM — מפגש 17: KNN בספרייה, אימון, חיזוי והערכה
**יחידה 3 · כיתה י׳ · 9–10 שקפים בהירים · 90 דקות הוראה ו־45 דקות פרויקט**

## מה אומת ומהו מקור
מקורות העוגן: Guided-Lesson.ipynb ו־Student-Lab.ipynb של Meeting-17, Student-Book.md המשודרג ו־Penguins CSV בקורס. בדיקה ישירה של קובץ GitHub (blob b5093336d83d99d8835c606b455d00065ab7cdcf): 344 רשומות, 7 עמודות, שלושה מינים — Adelie ‏152, Gentoo ‏124, Chinstrap ‏68; 0 חסרים ב־species, שני חסרים בכל אחת מארבע המדידות המספריות, ו־11 חסרים ב־sex. מצגות ההשתלמות ממופות: 5.2 KNN with Sklearn.pptx שקפים 5–11; Data preparation.pptx שקפים 24–29. **מיפוי אינו בדיקה חזותית של השקפים** ויש לבצע אותה לפני הקרנה.

## פתיחה: מודל חוזה, אבל האם צדק?
במפגש 16 התלמיד בנה אלגוריתם עצמאי. במפגש 17 הוא עובר לבדיקת מודל בספרייה מול תוויות אמת של דוגמאות שלא שימשו לאימון. מהי ההבחנה בין predict לבין evaluation? מדוע בלי y_test אי אפשר לחשב הצלחה? השיעור אינו שיעור מדדי Precision/Recall של מפגש 19 או בחירת K מתקדמת של מפגש 23.

## חישוב ידני מדורג — לפני מודל
**דוגמה מומצאת בלבד:** y_true=[1,0,0,1], y_pred=[1,0,1,1]. השוואה לפי אינדקס: שורה 1 נכון, שורה 2 נכון, שורה 3 שגוי, שורה 4 נכון. מתקבל correct_count=3, total=4, Accuracy=3/4=0.75=75%.
\[
Accuracy=\frac{\text{predictions with }y_{\rm pred}=y_{\rm true}}{N_{\rm test}}.
\]
המונה סופר התאמות אמת/חיזוי; המכנה סופר תצפיות בדיקה. ציון 0.75 אינו 0.75%; והוא **לא** תוצאת Penguins. השתמשו ב־accuracy-four-observations.svg ובחישוב ידני עם תוויות כל שורה.

## תהליך אמיתי על Penguins
דוגמת המורה: X=[flipper_length_mm,body_mass_g], y=species, test_size=.25, random_state=42, stratify=y, K=3, uniform, euclidean. **מטלת התלמיד שונה ומחייבת** X=[bill_length_mm,bill_depth_mm], seed17 עם אותם תנאי split/K. אל תציגו במצגת את ציון המודל של התלמיד.

רצף ההכנה:
1. קוראים קובץ Raw CSV ומוודאים עמודות, חסרים ומדידות.
2. מגדירים X רק משתי התכונות ואת y=species בנפרד.
3. מפצלים X/y יחד באמצעות train_test_split, כך שנשמר אינדקס תואם. 344 הרשומות נותנות 258 Train ו־86 Test.
4. מחשבים training_means=X_train.mean(), משתמשים בהם להשלמת חסרים בשתי קבוצות X. **לא לומדים ממוצעים מתוך X_test**.
5. מתאימים StandardScaler רק ל־Train שהושלם; transform על שתי הקבוצות. זה חיוני כי למשל body_mass_g ו־flipper_length_mm נמדדים ביחידות ובסולמות שונים.
6. מפעילים KNeighborsClassifier(n_neighbors=3,weights="uniform",metric="euclidean").fit(X_train_scaled,y_train).
7. יוצרים predictions=model.predict(X_test_scaled) **ללא y_test**.
8. **רק עכשיו** משווים y_test (אמת) ל־predictions, מחשבים נכונות וטעויות.

איור knn-train-test-evaluation.svg מציג שני מסלולים נפרדים — Training מעצב את הסרגל והמודל; Test מועברת דרך סרגל האימון והמודל, והתוויות שלה נשמרות עד ההערכה. אין חץ fit מ־Test ואין שימוש בתוצאות Test לבחירת K.

## מה קורה ב־fit, predict, accuracy_score?
fit מקבל X_train_scaled וגם y_train ומשמר את המידע הדרוש לקביעת שכנים עתידיים. predict מקבל **רק** X_test_scaled ומחזיר מערך תוויות באורך len(X_test). accuracy_score מקבל **רק לאחר החיזוי** את אמת y_test ואת predictions ומחשב חלק נכון.

~~~python
model = KNeighborsClassifier(n_neighbors=3,
                             weights="uniform", metric="euclidean")
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)
~~~

## למה אינדקסים חשובים?
Pandas Series של y_test שומרת אינדקסי המקור, אך predictions היא מערך NumPy מסודר לפי שורות X_test. בונים comparison עם index=y_test.index ועם העמודות actual/predicted. לאחר מכן comparison["correct"] הוא המבחן שורה־שורה. יצירת Series תחזיות חדש עם RangeIndex והשוואתו ל־y_test בדרך נאיבית עלולה ליצור יישור שגוי. **אינדקסי המקור חשובים גם לשחזור מדידות השגיאה.**

## בדיקת שגיאות ומגבלות
מציגים errors.head(3), ובודקים actual/predicted ומדידות המקור לפי אינדקס. אם אין שלוש טעויות, אין להמציא. גם אם Accuracy גבוה, **אין זו הוכחת דיוק בעתיד בטבע**; זו הערכה על חלוקה יחידה, על שני מאפיינים. איור error-inspection-table.svg הוא דוגמה *סכמטית בלבד* ואסור להציג את שורותיו כמקרים אמיתיים של Penguins. במפגש 18 התלמיד ילמד מטריצת בלבול; במפגש 19 מדדים נוספים.

## 10 שקפים מדורגים
1. סיפור: חיזוי פינגווין חדש מול אמת שמורה; דיוק אינו ניחוש מוצלח אחד.
2. דוגמת 4 תצפיות מומצאת וטבלת אמת/חיזוי.
3. נוסחת Accuracy והצבה 3/4=0.75=75%; שאלה "מהו המכנה?".
4. Penguins האמיתי: שדות, מינים, חסרים, יחידות ומטרת סיווג.
5. X/y ו־Train/Test; פיצול משותף, 258/86 ו־stratify; תרשים זרימה.
6. Train-only mean imputation ו־StandardScaler, והסכנה בלמידת פרמטרים מ־Test.
7. KNeighborsClassifier(K=3), משמעות fit והקלט של predict; קוד קצר.
8. טבלת comparison עם אינדקס מקור ו־correct, Accuracy ידני מול accuracy_score.
9. הצגת errors וחיבור למדידות; סיבה לטעות אינה ידועה רק מן הטבלה.
10. שאלות יציאה ומטלת התלמיד העצמאית **ללא פתרונות**, עם 45 דקות פרויקט/כרטיס מודל.

## שגיאות שאסור למצגת להכניס
- predict מקבל y_test — שגוי.
- ממוצע/Scaling על כל הקובץ לפני Split — דליפה.
- שינוי K לפי Test ואז דיווח אותו Test — הערכה שאינה עצמאית.
- הפרש Accuracy בין הדגמה למעבדה הוא הוכחה למאפיינים טובים — שגוי כי seed וגם תכונות שונים.
- השגיאות הסכמטיות או 75% במצגת הן פלט מודל Penguins — שגוי.
- פירוש אפס טעויות ב־Test כערובה לדיוק מוחלט בטבע — שגוי.

## הנחיות הגהה וכלים
עד 10 שקפים, רקע בהיר, עברית RTL תקינה, שמות שדות/קוד/נוסחאות LTR, הגבלת עומס ויזואלי. קודם חישוב ידני, אחר כך פלט, אחר כך פירוש ולבסוף מגבלה. העלו ל־NotebookLM את קובץ המקור ואת המצגות המוגדרות בלבד, **ללא פתרון המורה**. לאחר הפקה נדרשת הגהה שקף־שקף; פרומפט אינו מצגת.

קישורי כלי עזר: Google Colab https://colab.research.google.com/; NotebookLM https://notebooklm.google.com/; Scikit-learn neighbors https://scikit-learn.org/stable/modules/neighbors.html; metrics https://scikit-learn.org/stable/modules/model_evaluation.html.