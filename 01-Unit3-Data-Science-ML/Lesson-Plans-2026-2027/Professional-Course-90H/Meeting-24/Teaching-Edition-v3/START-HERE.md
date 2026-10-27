# מפגש 24 — רגרסיה ליניארית ו־R² | Teaching Edition v3
**כיתה י׳ · 90 דקות הוראה ותרגול + 45 דקות פרויקט · Candidate עד CI**

| רכיב | פתיחה |
|---|---|
| ספר תלמיד — סיפור, יחידות, נוסחאות ודוגמה | [Student-Book.md](Student-Book.md) |
| מדריך מורה לפי דקות | [Teacher-Guide.md](Teacher-Guide.md) |
| חישוב ידני למורה | [Teacher-Worked-Example.md](Teacher-Worked-Example.md) |
| הדגמה מבוקרת (סנפיר → מסה), 30 תאים | [Guided-Audited.ipynb](Guided-Audited.ipynb) |
| מעבדה עצמאית (מקור → מסה), 17 תאים ו־29 חוסרים בקוד | [Student-Fill-Blanks-Audited.ipynb](Student-Fill-Blanks-Audited.ipynb) |
| פתרון מורה מבוקר, 25 תאים | [Teacher-Solution-Audited.ipynb](Teacher-Solution-Audited.ipynb) |
| מקור NotebookLM | [NotebookLM-Source.md](NotebookLM-Source.md) |
| פרומפט למצגת | [NotebookLM-Prompt.md](NotebookLM-Prompt.md) |
| בקרת איכות | [Quality-Check.md](Quality-Check.md) |

**שלוש מחברות המקור אינן משתנות**: [Guided](../Guided-Lesson.ipynb) · [Student](../Student-Lab.ipynb) · [Teacher Solution](../Teacher-Solution.ipynb).

## דגשים
המורה מדגים `flipper_length_mm`, seed42; התלמיד מיישם `bill_length_mm`, seed17. היעד המספרי בשני המקרים: `body_mass_g` בגרמים. ה־Test החיצוני 25%. משלימים ערכי מאפיין חסרים על סמך ממוצע Train בלבד. `R²=1−SSE/SST` אינו אחוז דיוק ויכול להיות שלילי; `DummyRegressor` לומד ממוצע Train, ואילו ממוצע Test משמש בנוסחת המדד **לא להתאמת המודל**. תשובות המחברת העצמאית אינן מופיעות כאן.

קוד הבחינה האוטומטי הורחב למפגש 24. **עד שתתקבל תוצאת CI בפועל לא נוכל לטעון שכל המחברות עברו Run All.** גם מצגות NotebookLM ופיילוט כיתה נשארו לבסוף בהתאם להחלטה.
