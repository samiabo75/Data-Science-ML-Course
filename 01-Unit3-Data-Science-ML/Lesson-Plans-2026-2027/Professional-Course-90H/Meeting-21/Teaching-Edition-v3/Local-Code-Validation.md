# בדיקת קוד מקומית מייצגת — מפגש 21
**PASS לבדיקות מייצגות; Run All notebook/Colab NOT DONE.**

## מה נבדק בפועל
הורץ Python מקומי עם pandas ומימוש `train_test_split` של scikit-learn:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
s = pd.DataFrame({"candidate": ["A","B","C"],
                  "train": [1.00,0.88,0.60],
                  "validation": [0.65,0.84,0.58]})
s["gap"] = s["train"] - s["validation"]
assert [round(x,2) for x in s.gap] == [0.35,0.04,0.02]
assert s.loc[s.validation.idxmax(),"candidate"]=="B"
assert s.loc[s.train.idxmax(),"candidate"]=="A"
assert (s.gap>=0).all()
assert len(s)==3
a,b=train_test_split(list(range(20)),test_size=.25,random_state=42)
assert len(a)==15 and len(b)==5
assert not set(a)&set(b)
```
תוצאה: `PASS source math + illustrative split checks (7 checks)`.

## ערכות מתוקנות
- מחברת הדגמה: 16 תאים / 33 פקודות `assert`.
- מחברת תלמיד: 17 תאים / 25 מקומות `???` / 12 פקודות `assert` שחלקן תלויות במילוי.
- פתרון מורה: 12 תאים / 36 פקודות `assert`.

לא מתייחסים לשבעת התנאים המקומיים כאילו אישרו 81 בדיקות בתוך המחברות. נתוני הסקירה **מומצאים**, ולא הושג ציון Test או תוצאת מודל בפועל. נדרשים Run All והגהה בכיתה.
