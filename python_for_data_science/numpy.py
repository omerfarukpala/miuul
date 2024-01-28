#############################################
# NUMPY
#############################################

# Neden NumPy? (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

#############################################
# Neden NumPy?
#############################################

# verimli veri saklar
# vectorel işlemler ( listelerden daha hızlı )

import numpy as np
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# aynı işlemi numpy da yap
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b




#############################################
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
#############################################
import numpy as np

# bir liste üzerinden numpy array i oluştur.
np.array([1, 2, 3, 4, 5])

# ndarray yani numpy arrayi
type(np.array([1, 2, 3, 4, 5]))

# 10 tane integer 0 oluşturdu
np.zeros(10, dtype=int)

# 0 ile 10 arasında rastgele 10 tane int değer oluştur.
np.random.randint(0, 10, size=10)

# ortalaması 10 standart sapması 4 olan 3e 4 lük bir array oluştur.
np.random.normal(10, 4, (3, 4))

######################################################################
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
######################################################################
import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)

a.ndim              # tek boyutlu "1"
a.shape             # (5, )
a.size              # 5
a.dtype             # int64

######################################################################
# Yeniden Şekillendirme (Reshaping)
######################################################################
import numpy as np

np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)


######################################################################
# Index Seçimi (Index Selection)
######################################################################
import numpy as np
a = np.random.randint(10, size=10)
a[0]
a[0:5]              # soldaki dahil sağdaki hariç
a[0] = 999

m = np.random.randint(10, size=(3, 5))          # 3 satırlı 5 sütunlu array

m[0, 0]
m[1, 1]
m[2, 3]

m[2, 3] = 999

m[2, 3] = 2.9

m[:, 0]             # bütün satırları seç ve 0. sütunu seç
m[1, :]
m[0:2, 0:3]         # 0,1 satırları ve 0,1,2 sütunları

######################################################################
# Fancy Index
######################################################################
import numpy as np

v = np.arange(0, 30, 3)
v[1]
v[4]

# indexler için bir liste oluşturup
catch = [1, 2, 3]

v[catch]

######################################################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
######################################################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

#######################
# Klasik döngü ile
#######################
ab = []
for i in v:
    if i < 3:
        ab.append(i)

#######################
# Numpy ile
#######################
v < 3           # true false değerleri ile gösterir

v[v < 3]        # array([1, 2])
v[v > 3]
v[v != 3]
v[v == 3]
v[v >= 3]

#############################################
# Matematiksel İşlemler (Mathematical Operations)
#############################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)
v = np.subtract(v, 1)

#######################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
#######################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

np.linalg.solve(a, b)