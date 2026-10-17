# קטלוג מאגרי הנתונים — Data-Science-ML-Course

**מטרת הדף:** ריכוז קישור למקור המאגר, קישור להורדת CSV, והשימוש בהוראה. לחיצה על קישור **CSV להורדה** פותחת קובץ Raw שאפשר לשמור במחשב באמצעות Save As. נתונים מאוחסנים אצל גורם חיצוני עשויים להשתנות.

| מאגר | מקור / הסבר | CSV ישיר (הורדה) | שימוש בשיעורים | מתאים לקריטריוני פרויקט ההשתלמות? |
|---|---|---|---|---|
| Penguins | [Palmer Penguins](https://github.com/allisonhorst/palmerpenguins) | [הורדת penguins.csv](https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv) | Pandas, EDA, KNN, הכנת נתונים, CV | **לא** — 344 רשומות |
| Iris | [מקור המחברת בהשתלמות](https://github.com/arielb30/datasets) | [הורדת Iris.csv](https://raw.githubusercontent.com/arielb30/datasets/main/Iris.csv) | רגרסיה, KNN | **לא** — 150 רשומות |
| Titanic | [Kaggle Titanic](https://www.kaggle.com/datasets/yasserh/titanic-dataset) | [הורדת titanic_data.csv](https://raw.githubusercontent.com/arielb30/datasets/main/titanic_data.csv) | Pandas, Visualization, Feature Engineering, סיווג | **לבדיקה** — הגרסה הלימודית עשויה להכיל פחות מ־1,000 רשומות |
| Diamonds | [Kaggle Diamonds](https://www.kaggle.com/datasets/shivam2503/diamonds) | [הורדת diamonds.csv](https://raw.githubusercontent.com/arielb30/datasets/main/diamonds.csv) | קורלציה, ניקוי, רגרסיה, הנדסת מאפיינים | **מועמד**, בכפוף לבדיקת עמודות ומקור |
| Stroke Prediction | [Kaggle Stroke](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) | [הורדת healthcare-dataset-stroke-data.csv](https://raw.githubusercontent.com/arielb30/datasets/main/healthcare-dataset-stroke-data.csv) | מפגש 10 — חוסר איזון וסיווג | **מועמד**, עם התייחסות לחוסר איזון |
| KC House | [קובץ נתוני בתים ממקורות ההשתלמות](https://github.com/arielb30/datasets) | [הורדת kc_house_data.csv](https://raw.githubusercontent.com/arielb30/datasets/main/kc_house_data.csv) | רגרסיה במסלול Deep Learning | **מועמד**, יש לבדוק מקור ומאפיינים |
| TED | [מחברת ההשתלמות / דוגמת תאריכים](https://www.kaggle.com/datasets) | אין כרגע CSV ישיר מאומת אחד | חילוץ תאריך ותכונות זמן | תלוי בגרסת המאגר |

## קריטריונים לבחירת מאגר לפרויקט לפי המסמך שהועלה
- **1,000 רשומות לפחות**.
- **7 תכונות לפחות** לשערוך או לסיווג.
- **שני משתנים רציפים לפחות** ו־**שני משתנים קטגוריאליים/בדידים לפחות** (כולל טקסט); אם אין בדידים, נדרש לפי המסמך להפיק שניים מתוך הרציפים.
- בסיווג: **שתי מחלקות לפחות** ובדיקת פיזור המחלקות; בחוסר איזון ניתן לשקול Sampling.
- יעד רציף כגון מחיר מאפשר רגרסיה, ולפי המסמך אפשר גם ליצור קבוצות יעד בדידות.

**הבהרה:** אלה הקריטריונים במסמך ההשתלמות שסופק, ולא קביעה שהם כל דרישות המחוון הרשמי. יש לבדוק שכל מאגר מתאים גם למחוון ולרישוי.

## אתרי חיפוש
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [data.gov.il](https://data.gov.il/)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/)

## בדיקת טעינה ב־Colab
```python
import pandas as pd
url = "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/Datasets/penguins.csv"
df = pd.read_csv(url)
print(df.shape)
display(df.head())
```

**הורדת קובץ מתוך Colab:**
```python
from google.colab import files
df.to_csv("my_dataset.csv", index=False)
files.download("my_dataset.csv")
```

## שימוש הוגן ובטוח
לא להעלות מידע פרטי של תלמידים או מטופלים למאגר הציבורי; לבדוק רישוי, מהימנות המקור, השלמות הנתונים ומשמעות המשתנים. מאגרי בריאות הם ללמידה בלבד, לא לאבחון רפואי.
