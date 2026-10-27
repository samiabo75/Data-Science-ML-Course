# פתרון מורה — חישוב GridSearchCV ידני
## על הלוח
קובעים מראש `K=[3,5,9]` ובכל מועמד 5 קיפולי אימות.
\[
N_{fits}=3\times5=15.
\]
אם `refit=True`, אחרי בחירת המועמד יש עוד התאמה אחת על כל Train החיצוני. כלומר 16 התאמות מודל במסגרת החיפוש וה־refit (לא מספר נתונים).

לצורך המחשה **מומצאת בלבד**, ציוני מועמד אחד הם 0.80, 0.85, 0.75, 0.90, 0.70:
\[
\bar s=(0.80+0.85+0.75+0.90+0.70)/5=0.80.
\]
```python
import numpy as np
candidate_values = [3,5,9]
assert len(candidate_values)*5==15
scores=np.array([0.80,0.85,0.75,0.90,0.70])
assert np.isclose(scores.mean(),0.80)
```

ב־`GridSearchCV` התלמיד קורא `param_knn__n_neighbors`, `mean_train_score`, `mean_test_score`, `std_test_score`, `rank_test_score`. `best_params_` נבחר מתוך החיפוש; `best_score_` הוא ממוצע CV. `mean_test_score` אינו Test החיצוני.
**אין לצרף תוצאות אמיתיות או בחירת K של מעבדת התלמיד למצגת.**
