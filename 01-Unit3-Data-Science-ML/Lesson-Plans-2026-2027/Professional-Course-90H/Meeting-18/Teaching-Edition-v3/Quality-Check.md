# בקרת איכות — מפגש 18
**Candidate; content checked and representative binary code checked — NOT READY.**

## אימות מול המקור
- `Guided-Lesson.ipynb`: 8 מוצרים, TN=3, FP=1, FN=2, TP=2; תשתית Penguins קבועה עם flipper_length_mm/body_mass_g, seed42, K=3, Test 25%.
- `Student-Lab.ipynb`: 8 OK ו־2 Defect אמיתיים, כל החיזויים OK; מטריצה ידנית, קוד ופרשנות, ולאחר מכן מטריצת Penguins 3×3.
- `Teacher-Solution.ipynb`: מפתח נפרד למטלת התלמיד, לא להציג כחלק מספר או מצגת תלמיד.
- שמירה על היקף הלמידה: מטריצה, FP/FN ו־Accuracy בלבד. Precision/Recall/F1 נשמרים למפגש 19.

## תוצרים חדשים
שלוש מחברות Audited: מודרכת עם 25 פקודות assert, תלמיד עם 36 השלמות ???, פתרון עם 27 פקודות assert. המקורות נשמרו ללא שינוי. המחברות מחייבות הרצת Run All לפני הכרזה על תקינות תפעולית.

## בדיקות
שתי המטריצות הבינריות ו־Accuracy נבדקו מקומית בפועל. ראו `Local-Code-Validation.md`. אין טענה להרצת Penguins המלאה או כל קטעי ה־Audited.

## פתוח
Run All ב־Colab על המודרכת ופתרון המורה, בדיקות סטטיות למחברת תלמיד לאחר מילוי, בדיקת תרשים SVG, הפקת והגהת NotebookLM, פיילוט כיתה והתאמה לסילבוס הרשמי.
