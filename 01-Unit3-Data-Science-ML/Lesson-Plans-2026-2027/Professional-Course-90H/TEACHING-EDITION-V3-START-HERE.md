# יחידה 3 — ספריית הוראה משודרגת (Teaching Edition v3)
**כיתה י׳ • 30 מפגשים • 90 שעות לימוד בתכנון הקיים • מהדורה מועמדת לבדיקה, 26.10.2026**

הספרייה נבנתה מתוך [מסלול 30 המפגשים המקורי](./Course-Plan-90H.md), חומרי ההשתלמות והתוצרים הקיימים. אין למחוק/לשנות שום מחברת, מצגת או תרגיל מקור. **כל 30 המפגשים כוללים 7 מסמכי הוראה חדשים אישיים לנושא; המחברות המודרכות, תרגול התלמיד והפתרון נשארו נגישים בתיקיית המפגש המקורית.**

**משמעות סטטוס:** Candidate = חומר מורחב שנוצר והועלה, אך לא נבדקה עדיין כל מצגת, כל מחברת מחדש ב־Colab, התאמה פרטנית למחוון התקף או תפקוד בכיתה. אין לקרוא לכך גרסת 'בגרות סופית מאושרת'.

## הוראות למורה: סדר עבודה בכל מפגש
1. פתחו את START-HERE באותה תיקיית Teaching-Edition-v3.
2. קראו ספר תלמיד ומדריך מורה, זהו ידע קודם, עוגן השתלמות ומשימת הליבה מתוך המקור.
3. פתחו את קובץ החישוב המודרך וההמחשה, הראו הצבות מספריות צעד אחר צעד.
4. עבור NotebookLM העלו NotebookLM-Source.md יחד עם שקפי ההשתלמות הרלוונטיים, והשתמשו בפרומפט; אין להעלות פתרון מורה.
5. בצעו יחד מחברת Guided-Lesson.ipynb המקורית; אחריה תנו Student-Lab.ipynb כעותק לכל תלמיד ב־Classroom.
6. המורה משתמש ב־Teacher-Solution.ipynb המקורי. יש להבחין שהמאגר ציבורי ולכן פתרונות עשויים להיות נגישים גם לתלמידים.
7. סיימו בכרטיס חוקר: שאלה, נתונים, נוסחה/בחירה, חישוב או פלט, מסקנה ומגבלה.
8. קראו Quality-Check.md לסימון מה בוצע ומה עדיין דורש אימות.

## מפת המפגשים לפי הסדר המחייב

### מבוא, Python ונתונים

| מפגש | נושא | חבילת v3 | מעבדת תלמיד מקורית |
|---|---|---|---|
| 1 | שאלת חקר, Colab ונתונים ראשונים | [פתיחת חבילת ההוראה](./Meeting-01/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-01/Student-Lab.ipynb) |
| 2 | רשימות ולולאה על תצפיות | [פתיחת חבילת ההוראה](./Meeting-02/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-02/Student-Lab.ipynb) |
| 3 | תנאי פשוט וטבלת הנתונים הראשונה | [פתיחת חבילת ההוראה](./Meeting-03/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-03/Student-Lab.ipynb) |
| 4 | מקור הנתונים, CSV וסקירה ראשונית | [פתיחת חבילת ההוראה](./Meeting-04/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-04/Student-Lab.ipynb) |
| 5 | בחירת מאפיינים וסינון שורות | [פתיחת חבילת ההוראה](./Meeting-05/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-05/Student-Lab.ipynb) |
| 6 | מיון, תנאים משולבים ומשימת העברה | [פתיחת חבילת ההוראה](./Meeting-06/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-06/Student-Lab.ipynb) |

### חקר נתונים, סטטיסטיקה ו־EDA

| מפגש | נושא | חבילת v3 | מעבדת תלמיד מקורית |
|---|---|---|---|
| 7 | סוגי משתנים, ספירה והתפלגות | [פתיחת חבילת ההוראה](./Meeting-07/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-07/Student-Lab.ipynb) |
| 8 | מרכז, פיזור והיכרות עם נורמלית | [פתיחת חבילת ההוראה](./Meeting-08/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-08/Student-Lab.ipynb) |
| 9 | קשר בין משתנים וקורלציה | [פתיחת חבילת ההוראה](./Meeting-09/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-09/Student-Lab.ipynb) |
| 10 | Groupby, אגרגציות וגרף סיכום | [פתיחת חבילת ההוראה](./Meeting-10/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-10/Student-Lab.ipynb) |
| 11 | Boxplot ואיכות נתונים | [פתיחת חבילת ההוראה](./Meeting-11/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-11/Student-Lab.ipynb) |

### הכנת נתונים והימנעות מזליגה

| מפגש | נושא | חבילת v3 | מעבדת תלמיד מקורית |
|---|---|---|---|
| 12 | יעד, חלוקה והשלמת חסרים | [פתיחת חבילת ההוראה](./Meeting-12/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-12/Student-Lab.ipynb) |
| 13 | StandardScaler ו־MinMaxScaler | [פתיחת חבילת ההוראה](./Meeting-13/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-13/Student-Lab.ipynb) |
| 14 | קידוד קטגוריות והכנה משולבת | [פתיחת חבילת ההוראה](./Meeting-14/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-14/Student-Lab.ipynb) |

### KNN וסיווג

| מפגש | נושא | חבילת v3 | מעבדת תלמיד מקורית |
|---|---|---|---|
| 15 | KNN ביד: מרחק, שכנים והצבעה | [פתיחת חבילת ההוראה](./Meeting-15/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-15/Student-Lab.ipynb) |
| 16 | מימוש KNN בפונקציות ו־NumPy | [פתיחת חבילת ההוראה](./Meeting-16/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-16/Student-Lab.ipynb) |
| 17 | KNN בספרייה: אימון וחיזוי | [פתיחת חבילת ההוראה](./Meeting-17/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-17/Student-Lab.ipynb) |

### מדדי הערכה ותכנון ניסויים

| מפגש | נושא | חבילת v3 | מעבדת תלמיד מקורית |
|---|---|---|---|
| 18 | מטריצת בלבול וסוגי טעויות | [פתיחת חבילת ההוראה](./Meeting-18/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-18/Student-Lab.ipynb) |
| 19 | Precision, Recall ו־F1 | [פתיחת חבילת ההוראה](./Meeting-19/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-19/Student-Lab.ipynb) |
| 20 | חוסר איזון וקו בסיס | [פתיחת חבילת ההוראה](./Meeting-20/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-20/Student-Lab.ipynb) |
| 21 | הכללה, התאמת יתר וחלוקת אימות | [פתיחת חבילת ההוראה](./Meeting-21/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-21/Student-Lab.ipynb) |
| 22 | Pipeline ו־Cross Validation | [פתיחת חבילת ההוראה](./Meeting-22/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-22/Student-Lab.ipynb) |
| 23 | GridSearchCV וקריאת תוצאות | [פתיחת חבילת ההוראה](./Meeting-23/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-23/Student-Lab.ipynb) |

### רגרסיה, פרספטרון ו־SVM

| מפגש | נושא | חבילת v3 | מעבדת תלמיד מקורית |
|---|---|---|---|
| 24 | רגרסיה ליניארית ו־R² | [פתיחת חבילת ההוראה](./Meeting-24/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-24/Student-Lab.ipynb) |
| 25 | רגרסיה משולבת וניתוח גודל הטעות | [פתיחת חבילת ההוראה](./Meeting-25/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-25/Student-Lab.ipynb) |
| 26 | פרספטרון: סכום משוקלל ולמידה מטעות | [פתיחת חבילת ההוראה](./Meeting-26/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-26/Student-Lab.ipynb) |
| 27 | SVM והשוואת מודלים | [פתיחת חבילת ההוראה](./Meeting-27/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-27/Student-Lab.ipynb) |

### פרויקט, מחקר והגנה

| מפגש | נושא | חבילת v3 | מעבדת תלמיד מקורית |
|---|---|---|---|
| 28 | חקר מלא והערכת סוף | [פתיחת חבילת ההוראה](./Meeting-28/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-28/Student-Lab.ipynb) |
| 29 | כתיבת דוח, שחזור והכנה להגנה | [פתיחת חבילת ההוראה](./Meeting-29/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-29/Student-Lab.ipynb) |
| 30 | הגנה אישית והעברת ידע להמשך | [פתיחת חבילת ההוראה](./Meeting-30/Teaching-Edition-v3/START-HERE.md) | [מעבדה](./Meeting-30/Student-Lab.ipynb) |

## עקרונות מחייבים
- כל שיעור נפתח בסיפור ומוביל לשאלת חקר, לפי רצף קוגניטיבי: שאלה → נתונים → הסבר → חישוב ידני כשנדרש → גרף/טבלה → Python → תרגול → הגנה על מסקנה.
- האינפוגרפיקות שהועלו הן השראה חזותית בלבד; נוסחאות, מספרים ונתוני דוגמה מאומתים ממקורות ולא מועתקים מהן אוטומטית.
- אין להמציא זמן הוראה נוסף: **מפגשים 1–2: 135 דקות לימוד; מפגשים 3–29: 90 דקות לימוד ו־45 דקות פרויקט; מפגש 30: 135 דקות פרויקט**. יחד 60 שעות הוראה ו־30 שעות פרויקט.
- **לא נכנסים לנתוני Test** לצורך בחירת מאפיינים, התאמת טרנספורמציות או כיוון היפר־פרמטרים. חקר קבוצת הבדיקה מבוצע לאחר נעילת כל הבחירות.
- מסמכי Student-Book.md החדשים הם הרחבה ללימוד, בעוד שתרגילי הקוד המדויקים ופתרונותיהם נמצאים במחברות המקוריות, ללא שינוי.
- אין להציג הרחבות ביחידה 5 וב־DL כחובת יחידה 3 בלי מקור רשמי. Perceptron, SVM, Pipeline, GridSearchCV, cv_results_ ו־best_params_ נשמרים בשל מפרט הבחינה שהמורה מסר.

## מה חסר לשלב READY-to-Teach?
- הרצת שלוש מחברות המקור בכל מפגש ב־Colab לאחר עדכון סביבת Python הנוכחית.
- פתיחה של כל מצגת שנוצרה ב־NotebookLM והגהה שקף־שקף בעברית, מספרים, צירים וקוד.
- אימות מתמטי והצלבה פרטנית של חומרי ההרחבה מול מצגות ההשתלמות ומחוון ההערכה התקף.
- ניסוי בכיתה: קצב, טעויות תלמידים והאם תלמיד מסוגל לבצע העברה עצמאית.

[מסמך חוזה ההוראה הראשי](../../../MASTER-THREE-KITS-TEACHING-CONTRACT.md) · [תוכנית המפגשים](Course-Plan-90H.md) · [מיפוי דרישות הבחינה](Exam-and-Project-Alignment.md) · [מסמך בקרת מהדורה](V3-RELEASE-AND-VALIDATION.md).
