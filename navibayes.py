# Soal: Menghitung probabilitas berdasarkan tabel frekuensi

# --- DATA FREKUENSI DARI GAMBAR ---
# Discount
discount = {
    'Yes': {'BuyYes': 19, 'BuyNo': 1},
    'No': {'BuyYes': 5, 'BuyNo': 5}
}

# Free Delivery
delivery = {
    'Yes': {'BuyYes': 21, 'BuyNo': 2},
    'No': {'BuyYes': 3, 'BuyNo': 4}
}

# Day
day = {
    'Weekday': {'BuyYes': 9, 'BuyNo': 2},
    'Weekend': {'BuyYes': 7, 'BuyNo': 1},
    'Holiday': {'BuyYes': 8, 'BuyNo': 3}
}

# Total record
total_records = 30

# Hitung total pembelian Yes dan No
buy_yes = sum([discount[k]['BuyYes'] for k in discount])
buy_no = sum([discount[k]['BuyNo'] for k in discount])

print("Total Buy=Yes:", buy_yes)
print("Total Buy=No:", buy_no)

# --- FUNGSI MENGHITUNG PROBABILITAS ---
def P_Buy(buy_value):
    if buy_value == "Yes":
        return buy_yes / total_records
    else:
        return buy_no / total_records

def P_Discount_given_Buy(discount_value, buy_value):
    return discount[discount_value]['Buy' + buy_value] / buy_yes if buy_value == "Yes" else discount[discount_value]['Buy' + buy_value] / buy_no

def P_Delivery_given_Buy(delivery_value, buy_value):
    return delivery[delivery_value]['Buy' + buy_value] / buy_yes if buy_value == "Yes" else delivery[delivery_value]['Buy' + buy_value] / buy_no

def P_Day_given_Buy(day_value, buy_value):
    return day[day_value]['Buy' + buy_value] / buy_yes if buy_value == "Yes" else day[day_value]['Buy' + buy_value] / buy_no

# --- HITUNG SEMUA PROBABILITAS DIMINTA ---
# Rumus: P(Buy|X) ∝ P(Buy) * P(X|Buy)
# Kita tidak perlu normalisasi karena hanya perbandingan

def calc_prob(buy_value, day_value, delivery_value, discount_value):
    return P_Buy(buy_value) * \
           P_Day_given_Buy(day_value, buy_value) * \
           P_Delivery_given_Buy(delivery_value, buy_value) * \
           P_Discount_given_Buy(discount_value, buy_value)

# a. P(Buy | Day=Weekday, Free Delivery=Yes, Discount=Yes)
a = calc_prob("Yes", "Weekday", "Yes", "Yes")

# b. P(Buy | Day=Weekday, Free Delivery=No, Discount=No)
b = calc_prob("Yes", "Weekday", "No", "No")

# c. P(Not Buy | Day=Weekday, Free Delivery=Yes, Discount=Yes)
c = calc_prob("No", "Weekday", "Yes", "Yes")

# d. P(Not Buy | Day=Weekday, Free Delivery=No, Discount=No)
d = calc_prob("No", "Weekday", "No", "No")

# e. P(Buy | Day=Weekend, Free Delivery=Yes, Discount=Yes)
e = calc_prob("Yes", "Weekend", "Yes", "Yes")

# f. P(Buy | Day=Weekend, Free Delivery=No, Discount=No)
f = calc_prob("Yes", "Weekend", "No", "No")

# g. P(Not Buy | Day=Weekend, Free Delivery=Yes, Discount=Yes)
g = calc_prob("No", "Weekend", "Yes", "Yes")

# h. P(Not Buy | Day=Weekend, Free Delivery=No, Discount=No)
h = calc_prob("No", "Weekend", "No", "No")

# --- OUTPUT HASIL ---
print("\nHASIL PROBABILITAS:")
print("a. P(Buy | Weekday, Yes, Yes) =", a)
print("b. P(Buy | Weekday, No, No) =", b)
print("c. P(Not Buy | Weekday, Yes, Yes) =", c)
print("d. P(Not Buy | Weekday, No, No) =", d)
print("e. P(Buy | Weekend, Yes, Yes) =", e)
print("f. P(Buy | Weekend, No, No) =", f)
print("g. P(Not Buy | Weekend, Yes, Yes) =", g)
print("h. P(Not Buy | Weekend, No, No) =", h)
