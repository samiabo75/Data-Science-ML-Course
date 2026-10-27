# פתרון מורה — מפגש 14
**אין לצרף מסמך זה למצגת תלמיד.**

## טבלת One-Hot ידנית
Train=[A,B,A], סדר עמודות group_A/group_B. מקבלים [1,0],[0,1],[1,0]. Test=[B,C] ⇒ [0,1],[0,0], כאשר C לא נלמדה ב־Train. [0,0] אינו קרבה או הסתברות.

## הכנה משולבת של המורה
Train age=[10,20,None], group=[A,B,A]. חציון ידועים = 15. After fill age=[10,20,15]. μ=15, סטיות −5,+5,0 וסכום ריבועים 50. סטיית תקן ddof=0 היא σ=√(50/3)=4.0824829. הגילים לאחר Standard: [−1.224745,+1.224745,0]. בשילוב One-Hot מתקבל:
- train1 [−1.224745,1,0]
- train2 [+1.224745,0,1]
- train3 [0,1,0]
- new=(15,C) → [0,0,0].
סכמת העמודות היא numeric__age,categorical__group_A,categorical__group_B.

## פתרונות מעבדת התלמיד
Penguins: 344×7, X=island, y=species, split seed17 ו־stratify=y → Train258,Test86. שמות עמודות: island_Biscoe,island_Dream,island_Torgersen. Dream מקבלת [0,1,0].

Shapes: circle,square,circle באימון; triangle,square בבדיקה. triangle→[0,0], square→[0,1].

העברה משולבת: age=[5,15,None],group=[C,D,D], new=(10,E). חציון age=10, אחרי השלמה [5,15,10]. μ=10,σ=√(50/3), ולכן z=[−1.224745,+1.224745,0]. קטגוריות C/D: [1,0],[0,1],[0,1].
- train1 [−1.224745,1,0]
- train2 [+1.224745,0,1]
- train3 [0,0,1]
- new=(10,E) → [0,0,0].
סכמה: numeric__age,categorical__group_C,categorical__group_D.

**גבולות:** אין לבצע fit מחדש על New, אין לטעון שהקטגוריה החדשה דומה לכולן, ואין אימון מסווג/Accuracy/חיפוש היפר־פרמטרים במפגש הזה.