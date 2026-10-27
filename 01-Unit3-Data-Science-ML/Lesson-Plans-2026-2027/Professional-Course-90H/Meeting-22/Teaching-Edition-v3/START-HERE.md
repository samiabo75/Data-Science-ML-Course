# מפגש 22 — Pipeline ו־Cross Validation | Teaching Edition v3
**כיתה י׳ · 90 דקות הוראה ותרגול + 45 דקות פרויקט · Candidate**

| תוצר | פתיחה |
|---|---|
| ספר התלמיד, נוסחאות, סיפור ודוגמה | [Student-Book.md](Student-Book.md) |
| מדריך מורה | [Teacher-Guide.md](Teacher-Guide.md) |
| דוגמה ידנית למורה | [Teacher-Worked-Example.md](Teacher-Worked-Example.md) |
| מחברת מודרכת — 16 תאים, 41 פקודות assert | [Guided-Audited.ipynb](Guided-Audited.ipynb) |
| מעבדת תלמיד — 19 תאים, 28 השלמות | [Student-Fill-Blanks-Audited.ipynb](Student-Fill-Blanks-Audited.ipynb) |
| פתרון מורה — 17 תאים, 48 פקודות assert | [Teacher-Solution-Audited.ipynb](Teacher-Solution-Audited.ipynb) |
| NotebookLM | [מסמך מקור](NotebookLM-Source.md) · [פרומפט](NotebookLM-Prompt.md) |
| המחשות | [קיפולי CV](cv-three-folds.svg) · [Pipeline ללא זליגה](pipeline-no-leakage.svg) |
| בקרת איכות | [Quality-Check.md](Quality-Check.md) · [Local-Code-Validation.md](Local-Code-Validation.md) |

## עוגן המקור והפרדה
קובצי המקור נשמרו ללא שינוי: [Guided](../Guided-Lesson.ipynb), [Student Lab](../Student-Lab.ipynb), [Teacher Solution](../Teacher-Solution.ipynb).

מודרכת: `flipper_length_mm`, `body_mass_g`, `random_state=42`. תלמיד: `bill_length_mm`, `bill_depth_mm`, `random_state=17`. CV חמשת הקיפולים `random_state=42`, K=[1,3,5,15,51], `scoring="f1_macro"`, `SimpleImputer → StandardScaler → KNN`; Test 25%. אין לשנות K על סמך Test; בחירה לפי `cv_mean`, ובשוויון מדויק K קטן יותר.

**Candidate:** Run All עם Penguins, בדיקת המחברת הממולאת בכיתה, הגהת NotebookLM ופיילוט עדיין נדרשים.
