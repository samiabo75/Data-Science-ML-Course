# מפגש 5 — יומן איכות פרטני

**סטטוס:** Content-Checked / CSV-Verified / Code checks pending full Colab. *לא READY סופי.*

## התאמה למקור
- מדריך ומעבדה מקוריים נבדקו. נשמרו שני חלקי התרגול: בחירת עמודה/שתי עמודות + X/y; מסכות וסינונים Gentoo, Dream, flipper>=220 ותצוגת שתי עמודות.
- מיפוי ההשתלמות הקיים: 2.1 Python for DS.pptx שקפים 11–15. נדרש אימות חזותי.
- קובץ Datasets/penguins.csv נבדק דרך GitHub: 344×7, Gentoo=124, Dream=124, flipper>=220=43, flipper>220=35, flipper=220=8, flipper חסר=2.

## חישובים ידניים ונוסחאות
- A–D הדגמה מומצאת: מסכה True,False,False,True בתנאי price<=2500; שיעור 2/4×100=50%.
- מקור 4×4, עמודות year/memory_gb נותן 4×2; מסכה בוחרת A,D ומחזירה 2×4; בחירת שתי עמודות לאחריה נותנת 2×2.
- חשיבת AI: לא להצמיד X ו־y בסדר שונה, לא לתת את היעד כאחד המאפיינים; לא לטעון ש־NaN פירושו מתחת לסף.

## רכיבי הערכה
Student-Book.md; Teacher-Guide.md; Teacher-Worked-Example.md; column-row-selection.svg; mask-trace.svg; 3 מחברות Audited; NotebookLM-Source/PROMPT; START-HERE.

## שערי השלמה
1. בדיקת מבנה קובצי ipynb ו־SVG ב־GitHub.
2. הרצת קוד הדגמה ומבחני teacher עם CSV בסביבה מקומית, אם ניתן — תיעוד תוצאה ולא רק קיום assert.
3. Run All מלא לשתי מחברות המורה ב־Google Colab, כולל קריאת URL Raw ובדיקת תצוגת עברית.
4. יצירת והגהת מצגת NotebookLM שקף־שקף, ובדיקת שקפי השתלמות מקוריים.
5. פיילוט בכיתה ומיפוי ברור למחוון/מפרט משרד החינוך העדכניים.

**אין להציג מעבדת תרגול כמוכנה להרצה לפני שהתלמיד מחליף את סימני ? בקוד ממשי. מחברות המורה פומביות ב־GitHub, ולכן אינן פתרונות חסויים.**
