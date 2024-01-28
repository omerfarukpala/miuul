
######################################################################
# COMPREHENSIONS
######################################################################

######################################################################
# List Comprehension
######################################################################

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))


# sonucu liste olan bir dögüyü tek satırda oluşturan yapı
# en sonunda ulaşacağımız yapı
[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

# ilk adım
[salary * 2 for salary in salaries]

# tek bir if varsa döngünün sağına yazılır..
[salary * 2 for salary in salaries if salary < 3000]

# if , else if , else de varsa dögünün soluna yazılır.
[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

# mevcut bir fonsiyonu da bu yapıda kullanablriz.
[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]

######################################################################

# elimizde 2 adet liste var.
# ilk listede tüm öğrenciler, 2. listede istemediğim öğrenciler var.
# istemediklerimi küçük diğerlerini büyük harfle yaz.


students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]


[student.lower() if student in students_no else student.upper() for student in students]
[student.upper() if student not in students_no else student.lower() for student in students]




######################################################################
# Dict Comprehension
######################################################################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

# keyleri görmek istersek
dictionary.keys()
# dict_keys(['a', 'b', 'c', 'd'])

# değerleri görmek istersek
dictionary.values()
# dict_values([1, 2, 3, 4])

# liste formunda ama her bir elemanı tuple olarak görmek istersek.
dictionary.items()
# dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# key değerleri sabit ama valur değerleinin karesini alıyoruz.
{k: v ** 2 for (k, v) in dictionary.items()}

# key değerlerini büyük harf yapıyor. value değerleri sbt
{k.upper(): v for (k, v) in dictionary.items()}

# hem hey hem value değerlerine işlem uyguluyoruz
{k.upper(): v*2 for (k, v) in dictionary.items()}



######################################################################


######################################################################
# List & Dict Comprehension Uygulamalar
######################################################################

######################################################################
# Bir Veri Setindeki Değişken İsimlerini Değiştirmek
######################################################################

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

#  seaborn kütüphanesini ekledik
import seaborn as sns
# dataframe e seaborn kütüphanesinden bir veri seti yükledik.
df = sns.load_dataset("car_crashes")
# dataframe de veri setinin sütunlarını gösterdik
df.columns

for col in df.columns:
    print(col.upper())


A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]




#####################################################################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
#####################################################################

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']
# içinde INS yazanaları getirdik
[col for col in df.columns if "INS" in col]

# içinde ins geçenlerin başına FLAG getirdik
["FLAG_" + col for col in df.columns if "INS" in col]

# yoksa da NO FLAG getirdik
["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

# kalıcı olarak data frame oluşturmak için
df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]




#####################################################################
# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.
#####################################################################

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# sadece sayısal olanları seçmek için
# if df[col].dtype != "O" ## object değildir.
num_cols = [col for col in df.columns if df[col].dtype != "O"]

# boş sözlük oluştur.
soz = {}
# sbt liste // value olarak eklenecek
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

# kısa yol
# col aynı kalsın value ya sabit bir liste ile doldur.
new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()
# sözlüğün value kısmındaki fonksiyon isimlerini anayabilen bir agg fonsiyonu içerisinde kullandık
df[num_cols].agg(new_dict)

# çıktı aşağıda

# df[num_cols].agg(new_dict)
#            total    speeding  ...   ins_premium   ins_losses
# mean   15.790196    4.998196  ...    886.957647   134.493137
# min     5.900000    1.792000  ...    641.960000    82.750000
# max    23.900000    9.450000  ...   1301.520000   194.780000
# sum   805.300000  254.908000  ...  45234.840000  6859.150000