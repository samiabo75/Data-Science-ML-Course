# מדריך מורה — מפגש 17: אימון והערכת KNN בספרייה
**יחידה 3 · כיתה י׳ · 90 דקות הוראה ותרגול + 45 דקות פרויקט**

## עיגון מחייב במקור
נבדקו 3 מחברות המקור. Guided משתמשת ב־flipper_length_mm ו־body_mass_g, seed=42. Student-Lab ופתרון המקור משתמשים ב־bill_length_mm וב־bill_depth_mm, seed=17. בשתיהן: Penguins, יעד species, פיצול משותף test_size=.25, stratify=y, מילוי חסרים בממוצעי Train, StandardScaler.fit על Train בלבד, KNeighborsClassifier עם K3/weights=uniform/metric=euclidean, fit/predict, Accuracy וניתוח טעויות. מפת שקפים: 5.2 KNN with Sklearn.pptx שקפים 5–11 ו־Data preparation.pptx שקפים 24–29; טרם נצפו שוב חזותית. אין לשנות קובצי מקור.

## מטרות ביצוע
התלמיד מזהה X ו־y ומשמר הפרדה; מחלק יחד X/y; מחיל השלמה ותקנון ללא דליפה; מפעיל fit ו־predict עם K קבוע; מחשב 3/4=0.75 באופן ידני, ומשחזר זאת באמצעות accuracy_score; מוצא שורות שגיאה ומזהה מגבלות; אינו בוחר K באמצעות Test.

## תכנון מדויק של 135 דקות
| דקות | פעילות | תוצר |
|---|---|---|
| 0–10 | סיפור פינגווין חדש וחיזוי בלי אמת | הבחנה predict/accuracy |
| 10–30 | טבלת אמת מול חיזוי 4 שורות; נוסחה, שבר ואחוז | Accuracy=0.75, שגיאה בשורה 3 |
| 30–50 | X/y, Split, השלמה/סקיילינג, fit/predict | תרשים תהליך ללא דליפה |
| 50–80 | Guided של מורה ואז Student-Lab על מדדי מקור | חיזוי, טבלת השוואה |
| 80–90 | טעות, אינדקס מקור, איסור בחירת K ב־Test | כרטיס יציאה |
| 90–135 | פרויקט: כרטיס מודל ראשון | מודל/תכנון/מגבלות |

## דף הלוח
אמת [1,0,0,1], חיזוי [1,0,1,1]. השוואה [True,True,False,True]. מונה 3, מכנה 4, Accuracy=0.75=75%. דוגמה *מומצאת*, אין לבלבל עם נתוני Penguins. מציגים קודם מסלול: Raw CSV → X/y → Split → Train mean fill → Train scaler fit → transform Train/Test → KNN.fit(Train,y_train) → predict(Test) → comparison(Test אמת מול חיזוי) → Accuracy → errors. העמודות species/labels אינן שדות X.

## דגשי נתונים, אינדקסים ודיוק
Penguins בקורס 344×7, שלושה מינים, 258 Train ו־86 Test אם אין חסרי יעד. random_state מאפשר שחזור; אינו מתקן הטיה. StandardScaler חיוני להבנה כשהמדדים ביחידות שונות (mm/g). אם predictions הוא NumPy array בסדר X_test, בניית DataFrame עם index=y_test.index שומרת התאמה ל־y_test; יצירת Series עצמאית בעלת RangeIndex והשוואתה מול y_test עלולה להיכשל בגלל יישור אינדקסים.

Accuracy מדווח **מהפלט**, ולא ממספר משוער. שורות השגיאה הן המדידות שנחזתה להן תווית שונה; אין להמציא סיבות או להבטיח שקיימות לפחות שלוש. Display של errors.head(3) מציג עד שלוש שגיאות.

## שתי נקודות ביקורת עקרוניות
- נתוני Test אינם מקורות לפרמטרי fill/scale **וגם אינם מקור לבחירת K או מאפיינים**. התאמת K לפי Test חוזרת היא זליגת מידע של תהליך הפיתוח, אף אם לא ביצענו scaler.fit(X_test).
- מחברת המורה והמעבדה שינו בו־זמנית מאפיינים ו־random_state, לכן **אין** להסיק איזה זוג מאפיינים טוב יותר מתוך הפרש Accuracy בין שתי המחברות. השוואה הוגנת תדרוש פיצול זהה, Validation ובחירה מסודרת בהמשך.

## שאלות סוקרטיות
מדוע species אינה ב־X? מה בדיוק מקבל predict? האם 0.75 = 0.75%? מה משמעות שתי תצפיות שגויות אם יש 86 שורות? מדוע צריך אינדקס מקור? מהו ההבדל בין "נחזה Chinstrap במקום Adelie" לבין "המודל טעה כי שני המינים דומים"? כיצד נשמור Test סופית מבלי לבחון עוד K?

## שגיאות שכיחות
predict(X_test,y_test) אינו שימוש תקין; מילוי חסרים מכל המאגר גורם דליפה; scaler.fit(Test) גורם דליפה; incorrect column order משנה תכונות; השוואת Series עם אינדקס שונה מביאה לטבלה לא נכונה; שינוי K בעקבות Accuracy Test מבטל את עצמאות המדידה; טעויות לא מוכיחות סיבתיות.

## פרויקט 45 דקות
אם יש אמת מתויגת, מאמנים מודל ראשון שהוגדר מראש ומחשבים הערכה מדודה, תוך תיעוד מקור/זמינות תכונות. ללא אמת — מכינים כרטיס תכנון, ללא מספר Accuracy מומצא. במפגש 18 תתווסף מטריצת בלבול; במפגש 19 Precision/Recall/F1. אל תוסיפו GridSearch או CV מעשיים כאן.

## כלים מותאמים
Colab https://colab.research.google.com/ לתרגול; NotebookLM https://notebooklm.google.com/ למצגת; תיעוד Sklearn https://scikit-learn.org/stable/modules/neighbors.html למורה; Pandas https://pandas.pydata.org/docs/ לתיעוד אינדקס. חובה בדיקת Run All מלאה, הגהת מצגת, פיילוט כיתה ובקרת מפרט רשמי לפני READY.

## תוספת עומק למורה — תוצאות אמיתיות על Penguins (27.10.2026)
בבדיקה מקומית על CSV הזהה בדיוק לקובץ המאגר (Git blob b5093336d83d99d8835c606b455d00065ab7cdcf) עברו שתי זרימות KNN המשלבות Train-only imputation, StandardScaler ו־K3. בהדגמת flipper_length_mm/body_mass_g עם seed42 נמצאו **60 נכונות מתוך 86, כלומר 69.77%**. בפתרון מטלת bill_length_mm/bill_depth_mm עם seed17 נמצאו **83 נכונות מתוך 86, כלומר 96.51%**. שלוש הטעויות במטלת התלמיד הן באינדקסי מקור 129, 325 ו־335 — כל אחת ניתנת לשליפה באמצעות X_test.loc[errors.index].

**הוראה דידקטית:** אין להציג מספרים אלה מראש במצגת תלמיד, ואין להשוות בין שני המסלולים כדי לבחור "מאפיינים טובים יותר": השתנו גם המאפיינים וגם חלוקת Train/Test. תנו לתלמידים לחזות, להריץ ולנתח שגיאה בפלט שלהם. דוח למורה בלבד וקוד משחזר: [Real-Penguins-Validation-Teacher.md](Real-Penguins-Validation-Teacher.md) · [Verify-Real-Penguins.py](Verify-Real-Penguins.py). עדיין יש לבצע Run All של המחברות עצמן ב־Colab לפני READY.