"""
תרגיל 2 - אלגוריתמים מתקדמים
קורס 96505.1.1 - סמסטר א' תשפ"ו

מכיל את הפתרונות לכל השאלות (1-5)
"""

import random
import string
import itertools


# ============================================================================
# פונקציית עזר: create_random_tuples
# מקור: https://github.com/NadavAharoni/AlgorithmsCourse/blob/main/python/random_tuples.py
# ============================================================================

def create_random_tuples(n, k, types=None):
    """
    Create a list of n tuples, each containing k random elements of specified types.

    Parameters:
    n (int): Number of tuples to create.
    k (int): Number of elements in each tuple.
    types (list): List of types for each element in the tuple. Length must be k.

    Returns:
    list: A list of n tuples with random elements.
    """
    if types is None:
        types = [int] * k  # Default to int if no types provided

    if len(types) != k:
        raise ValueError("Length of types must be equal to k")

    def random_element(t):
        if t == int:
            return random.randint(0, 1000)
        elif t == float:
            return random.uniform(0.0, 1000.0)
        elif t == str:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        else:
            raise ValueError(f"Unsupported type: {t}")

    result = []
    for _ in range(n):
        tuple_elements = tuple(random_element(t) for t in types)
        result.append(tuple_elements)

    return result


# ============================================================================
# שאלה 1: שימוש בפונקציה sorted עם tuples
# ============================================================================

def question_1():
    """
    שאלה 1: תוכנית שמייצרת רשימה של tuples (שלשות מהטיפוסים [int, float, str])
    וממיינת אותה 3 פעמים, כל פעם לפי אחד מהרכיבים.
    """
    print("=" * 70)
    print("שאלה 1: מיון רשימת tuples לפי רכיבים שונים")
    print("=" * 70)
    
    # יצירת רשימה של 5 שלשות
    tuples_list = create_random_tuples(5, 3, [int, float, str])
    
    print("\nרשימת ה-tuples המקורית:")
    for t in tuples_list:
        print(f"  {t}")
    
    # מיון לפי הרכיב הראשון (int)
    sorted_by_first = sorted(tuples_list, key=lambda x: x[0])
    print("\nממוין לפי הרכיב הראשון (int):")
    for t in sorted_by_first:
        print(f"  {t}")
    
    # מיון לפי הרכיב השני (float)
    sorted_by_second = sorted(tuples_list, key=lambda x: x[1])
    print("\nממוין לפי הרכיב השני (float):")
    for t in sorted_by_second:
        print(f"  {t}")
    
    # מיון לפי הרכיב השלישי (str)
    sorted_by_third = sorted(tuples_list, key=lambda x: x[2])
    print("\nממוין לפי הרכיב השלישי (str):")
    for t in sorted_by_third:
        print(f"  {t}")
    
    print()


# ============================================================================
# שאלה 2: פונקציות merge ו-is_sorted
# ============================================================================

def is_sorted(a, key=lambda x: x):
    """
    שאלה 2ב: בדיקה האם רשימה מסודרת בסדר עולה.
    
    Parameters:
    a (list): הרשימה לבדיקה
    key (function): פונקציה שמחזירה את המפתח של כל פריט
    
    Returns:
    bool: True אם הרשימה מסודרת, False אחרת
    
    הפונקציה משתמשת ב-itertools.pairwise לבדוק כל זוג רכיבים עוקבים
    ומוודאת שכל רכיב קטן או שווה לרכיב הבא.
    """
    # רשימה ריקה או עם פריט אחד נחשבת מסודרת
    if len(a) <= 1:
        return True
    
    # בדיקה שכל זוג עוקב מסודר כראוי
    return all(key(first) <= key(second) for first, second in itertools.pairwise(a))


def merge(a, b, key=lambda x: x):
    """
    שאלה 2א: מיזוג בין שני מערכים מסודרים בסדר עולה.
    
    Parameters:
    a (list): רשימה מסודרת ראשונה
    b (list): רשימה מסודרת שנייה
    key (function): פונקציה שמחזירה את המפתח של כל פריט
    
    Returns:
    list: רשימה חדשה ממוזגת ומסודרת, או None אם אחד מהמערכים לא מסודר
    
    הפונקציה בודקת תחילה שהמערכים הקלט מסודרים כראוי.
    אם כן, היא ממזגת אותם לרשימה אחת מסודרת.
    """
    # בדיקה ששני המערכים מסודרים
    if not is_sorted(a, key):
        return None
    if not is_sorted(b, key):
        return None
    
    # מיזוג המערכים
    result = []
    i, j = 0, 0
    
    # העתקת הפריטים לפי סדר עולה
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    # העתקת יתרת הפריטים מ-a (אם יש)
    while i < len(a):
        result.append(a[i])
        i += 1
    
    # העתקת יתרת הפריטים מ-b (אם יש)
    while j < len(b):
        result.append(b[j])
        j += 1
    
    return result


def question_2():
    """
    הדגמת השימוש בפונקציות merge ו-is_sorted
    """
    print("=" * 70)
    print("שאלה 2: פונקציות merge ו-is_sorted")
    print("=" * 70)
    
    # בדיקה 1: מיזוג שני מערכים מסודרים
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8]
    print(f"\nמערך a: {a}")
    print(f"מערך b: {b}")
    print(f"a מסודר? {is_sorted(a)}")
    print(f"b מסודר? {is_sorted(b)}")
    
    merged = merge(a, b)
    print(f"מיזוג: {merged}")
    
    # בדיקה 2: ניסיון למזג מערך לא מסודר
    c = [5, 2, 8, 1]
    print(f"\nמערך c (לא מסודר): {c}")
    print(f"c מסודר? {is_sorted(c)}")
    
    result = merge(a, c)
    print(f"ניסיון למזג a ו-c: {result}")
    
    # בדיקה 3: מיזוג עם key function
    tuples_a = [(1, 'z'), (3, 'x'), (5, 'v')]
    tuples_b = [(2, 'y'), (4, 'w'), (6, 'u')]
    print(f"\nמערך tuples_a: {tuples_a}")
    print(f"מערך tuples_b: {tuples_b}")
    
    merged_tuples = merge(tuples_a, tuples_b, key=lambda x: x[0])
    print(f"מיזוג לפי הרכיב הראשון: {merged_tuples}")
    
    print()


# ============================================================================
# שאלה 3: מיזוג מספר רשימות מסודרות
# ============================================================================

def merge_sorted_lists(lists, key=lambda x: x):
    """
    שאלה 3א: מיזוג בין כמה רשימות מסודרות.
    
    Parameters:
    lists (list of lists): רשימה של רשימות מסודרות
    key (function): פונקציה שמחזירה את המפתח של כל פריט
    
    Returns:
    list: רשימה חדשה ממוזגת ומסודרת
    
    האסטרטגיה: מיזוג זוגי - ממזגים את הרשימות זוג-זוג עד שנשארת רשימה אחת.
    
    שאלה 3ב - ניתוח סיבוכיות:
    אם יש k רשימות ובכל אחת n פריטים:
    - בכל שלב של המיזוג הזוגי, אנו ממזגים k רשימות לתוך k/2 רשימות
    - יש log(k) שלבים של מיזוג
    - בכל שלב, אנו עוברים על כל n*k הפריטים
    - סיבוכיות: O(n*k*log(k))
    
    הסבר מפורט:
    - שלב 1: k רשימות -> k/2 רשימות (כל אחת בגודל 2n) - זמן: O(n*k)
    - שלב 2: k/2 רשימות -> k/4 רשימות (כל אחת בגודל 4n) - זמן: O(n*k)
    - ...
    - שלב log(k): 1 רשימה (בגודל n*k) - זמן: O(n*k)
    - סה"כ: O(n*k) * log(k) = O(n*k*log(k))
    """
    if not lists:
        return []
    
    if len(lists) == 1:
        return lists[0]
    
    # מיזוג זוגי - ממזגים זוגות של רשימות עד שנשארת רשימה אחת
    while len(lists) > 1:
        merged_lists = []
        
        # מיזוג רשימות בזוגות
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                # יש זוג - ממזגים
                merged = merge(lists[i], lists[i + 1], key)
                merged_lists.append(merged)
            else:
                # רשימה בודדת - מעתיקים אותה כמות שהיא
                merged_lists.append(lists[i])
        
        lists = merged_lists
    
    return lists[0]


def question_3():
    """
    הדגמת השימוש בפונקציה merge_sorted_lists
    """
    print("=" * 70)
    print("שאלה 3: מיזוג מספר רשימות מסודרות")
    print("=" * 70)
    
    # יצירת מספר רשימות מסודרות
    list1 = [1, 4, 7, 10]
    list2 = [2, 5, 8, 11]
    list3 = [3, 6, 9, 12]
    list4 = [0, 13, 14, 15]
    
    lists = [list1, list2, list3, list4]
    
    print("\nרשימות הקלט:")
    for i, lst in enumerate(lists, 1):
        print(f"  רשימה {i}: {lst}")
    
    merged = merge_sorted_lists(lists)
    print(f"\nרשימה ממוזגת: {merged}")
    
    print("\nניתוח סיבוכיות:")
    print("אם יש k רשימות ובכל אחת n פריטים:")
    print("- הסיבוכיות היא O(n*k*log(k))")
    print("- הסבר: בכל שלב של מיזוג זוגי עוברים על n*k פריטים")
    print("- יש log(k) שלבים כאלה (כל פעם מחצית מספר הרשימות)")
    print()


# ============================================================================
# שאלה 4: פונקציות partition - Lomuto ו-Hoare
# ============================================================================

def partition_lomuto(a, key=lambda x: x):
    """
    שאלה 4א: מימוש partition בשיטת Lomuto.
    
    Parameters:
    a (list): רשימה לא מסודרת (תשונה במקום)
    key (function): פונקציה שמחזירה את המפתח של כל פריט
    
    Returns:
    int: האינדקס הסופי של ה-pivot
    
    השיטה:
    - בוחרים את הפריט האחרון בתור pivot
    - מחלקים את המערך כך שכל הפריטים הקטנים או שווים ל-pivot יהיו משמאלו
    - כל הפריטים הגדולים מ-pivot יהיו מימינו
    - ה-pivot נמצא במיקומו הסופי הנכון
    """
    if len(a) <= 1:
        return 0
    
    # בחירת הפריט האחרון בתור pivot
    pivot_value = key(a[-1])
    i = -1  # מצביע על הגבול בין הקטנים לגדולים
    
    # מעבר על כל הפריטים (מלבד ה-pivot עצמו)
    for j in range(len(a) - 1):
        if key(a[j]) <= pivot_value:
            i += 1
            a[i], a[j] = a[j], a[i]  # החלפה
    
    # הצבת ה-pivot במקומו הנכון
    i += 1
    a[i], a[-1] = a[-1], a[i]
    
    return i


def partition_hoare(a, key=lambda x: x):
    """
    שאלה 4ב: מימוש partition בשיטת Hoare.
    
    Parameters:
    a (list): רשימה לא מסודרת (תשונה במקום)
    key (function): פונקציה שמחזירה את המפתח של כל פריט
    
    Returns:
    int: האינדקס שבו מסתיים החלק השמאלי
    
    השיטה:
    - בוחרים את הפריט הראשון בתור pivot
    - משתמשים בשני מצביעים שנעים זה כלפי זה
    - המצביע השמאלי מחפש פריט גדול מ-pivot
    - המצביע הימני מחפש פריט קטן מ-pivot
    - מחליפים ביניהם עד שהמצביעים נפגשים
    """
    if len(a) <= 1:
        return 0
    
    pivot_value = key(a[0])
    i = -1  # מצביע שמאלי
    j = len(a)  # מצביע ימני
    
    while True:
        # הזז את i ימינה עד שמוצאים פריט >= pivot
        i += 1
        while i < len(a) and key(a[i]) < pivot_value:
            i += 1
        
        # הזז את j שמאלה עד שמוצאים פריט <= pivot
        j -= 1
        while j >= 0 and key(a[j]) > pivot_value:
            j -= 1
        
        # אם המצביעים נפגשו או חצו - סיימנו
        if i >= j:
            return j
        
        # החלף בין הפריטים
        a[i], a[j] = a[j], a[i]


def question_4():
    """
    שאלה 4: השוואה בין partition_lomuto ו-partition_hoare
    """
    print("=" * 70)
    print("שאלה 4: פונקציות partition - Lomuto ו-Hoare")
    print("=" * 70)
    
    # יצירת מערך לדוגמה
    original = [3, 7, 8, 5, 2, 1, 9, 5, 4]
    
    # בדיקת Lomuto
    arr_lomuto = original.copy()
    print(f"\nמערך מקורי: {arr_lomuto}")
    print("שימוש ב-partition_lomuto (pivot = הפריט האחרון):")
    pivot_index = partition_lomuto(arr_lomuto)
    print(f"אחרי partition: {arr_lomuto}")
    print(f"מיקום ה-pivot: {pivot_index}, ערך: {arr_lomuto[pivot_index]}")
    
    # בדיקת Hoare
    arr_hoare = original.copy()
    print(f"\nמערך מקורי: {arr_hoare}")
    print("שימוש ב-partition_hoare (pivot = הפריט הראשון):")
    split_index = partition_hoare(arr_hoare)
    print(f"אחרי partition: {arr_hoare}")
    print(f"מיקום הפיצול: {split_index}")
    
    print("\n" + "=" * 70)
    print("שאלה 4ג - ההבדל בין שתי הפונקציות:")
    print("=" * 70)
    print("""
    Lomuto:
    - ה-pivot (הפריט האחרון) נמצא במיקומו הסופי והנכון במערך
    - כל הפריטים משמאל ל-pivot קטנים או שווים לו
    - כל הפריטים מימין ל-pivot גדולים ממנו
    - הפונקציה מחזירה את האינדקס המדויק של ה-pivot
    
    Hoare:
    - ה-pivot (הפריט הראשון) לא בהכרח נמצא במיקומו הסופי
    - המערך מחולק לשני חלקים: שמאל (קטנים או שווים) וימין (גדולים או שווים)
    - הפונקציה מחזירה את נקודת החלוקה בין שני החלקים
    - ה-pivot עצמו יכול להיות בכל מקום בחלק השמאלי
    """)
    
    print("\n" + "=" * 70)
    print("שאלה 4ד - זמן ריצה:")
    print("=" * 70)
    print("""
    זמן הריצה של partition (גם Lomuto וגם Hoare):
    - O(n) כאשר n הוא גודל המערך
    
    הסבר:
    - שתי הפונקציות עוברות על כל פריט במערך פעם אחת (או קבוע קטן של פעמים)
    - בכל איטרציה מבצעים פעולות בזמן קבוע (השוואה, החלפה)
    - לכן הסיבוכיות היא ליניארית: Θ(n)
    """)
    print()


# ============================================================================
# שאלה 5: partition עם שני pivots
# ============================================================================

def partition_two_pivots(a, key=lambda x: x):
    """
    שאלה 5: חלוקת מערך לשלושה קטעים באמצעות שני pivots.
    
    Parameters:
    a (list): רשימה לא מסודרת (תשונה במקום)
    key (function): פונקציה שמחזירה את המפתח של כל פריט
    
    Returns:
    tuple: (p1, p2) כאשר:
        - קטע 1: a[0:p1] - פריטים קטנים מ-pivot1
        - קטע 2: a[p1:p2] - פריטים בין pivot1 ל-pivot2
        - קטע 3: a[p2:] - פריטים גדולים מ-pivot2
    
    האלגוריתם:
    1. בוחרים שני pivots: הקטן מבין הראשון והאחרון, והגדול מביניהם
    2. משתמשים ב-3 מצביעים:
       - i: גבול בין הקטנים לאמצעיים
       - j: הפריט הנוכחי שאנו בודקים
       - k: גבול בין האמצעיים לגדולים
    3. עוברים על המערך ומחלקים לשלושה קטעים
    """
    if len(a) <= 2:
        return (0, len(a))
    
    # בחירת שני pivots - הראשון והאחרון
    first, last = a[0], a[-1]
    
    # ודא ש-pivot1 <= pivot2
    if key(first) > key(last):
        a[0], a[-1] = a[-1], a[0]
        first, last = last, first
    
    pivot1 = key(first)
    pivot2 = key(last)
    
    # אם שני ה-pivots שווים, נשתמש ב-partition רגיל
    if pivot1 == pivot2:
        p = partition_lomuto(a, key)
        return (p, p + 1)
    
    # מצביעים:
    # i - סוף הקטע של פריטים < pivot1
    # j - הפריט הנוכחי
    # k - תחילת הקטע של פריטים > pivot2
    i = 0
    j = 1
    k = len(a) - 1
    
    while j < k:
        if key(a[j]) < pivot1:
            # הפריט קטן מ-pivot1 - העבר לקטע השמאלי
            i += 1
            a[i], a[j] = a[j], a[i]
            j += 1
        elif key(a[j]) > pivot2:
            # הפריט גדול מ-pivot2 - העבר לקטע הימני
            k -= 1
            a[j], a[k] = a[k], a[j]
            # לא מגדילים את j כי צריך לבדוק את הפריט שהגיע מ-k
        else:
            # הפריט בין pivot1 ל-pivot2 - השאר באמצע
            j += 1
    
    # הצב את ה-pivots במקומות הנכונים
    a[0], a[i] = a[i], a[0]  # pivot1 במקומו
    a[len(a) - 1], a[k] = a[k], a[len(a) - 1]  # pivot2 במקומו
    
    return (i, k + 1)


def question_5():
    """
    הדגמת השימוש ב-partition עם שני pivots
    """
    print("=" * 70)
    print("שאלה 5: partition עם שני pivots")
    print("=" * 70)
    
    # יצירת מערך לדוגמה
    arr = [3, 7, 8, 5, 2, 1, 9, 5, 4, 10, 6]
    print(f"\nמערך מקורי: {arr}")
    
    # שימוש ב-partition עם שני pivots
    arr_copy = arr.copy()
    p1, p2 = partition_two_pivots(arr_copy)
    
    print(f"אחרי partition: {arr_copy}")
    print(f"\nחלוקה לשלושה קטעים:")
    print(f"  קטע 1 (קטנים מ-pivot1): {arr_copy[0:p1]} - אינדקסים [0:{p1}]")
    print(f"  קטע 2 (בין ה-pivots): {arr_copy[p1:p2]} - אינדקסים [{p1}:{p2}]")
    print(f"  קטע 3 (גדולים מ-pivot2): {arr_copy[p2:]} - אינדקסים [{p2}:{len(arr_copy)}]")
    
    # בדיקה שהחלוקה נכונה
    if len(arr_copy[0:p1]) > 0 and len(arr_copy[p1:p2]) > 0:
        print(f"\nמקסימום בקטע 1: {max(arr_copy[0:p1])}")
        print(f"מינימום בקטע 2: {min(arr_copy[p1:p2])}")
    if len(arr_copy[p1:p2]) > 0 and len(arr_copy[p2:]) > 0:
        print(f"מקסימום בקטע 2: {max(arr_copy[p1:p2])}")
        print(f"מינימום בקטע 3: {min(arr_copy[p2:])}")
    
    print()


# ============================================================================
# הרצת כל השאלות
# ============================================================================

def main():
    """
    הרצת כל השאלות בתרגיל
    """
    print("\n" + "=" * 70)
    print("תרגיל 2 - אלגוריתמים מתקדמים")
    print("=" * 70 + "\n")
    
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    
    print("=" * 70)
    print("סיום התרגיל")
    print("=" * 70)


if __name__ == "__main__":
    main()
