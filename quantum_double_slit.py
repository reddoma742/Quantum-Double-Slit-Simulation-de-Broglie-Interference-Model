==========================================================
Project: Quantum Double-Slit Simulation: de Broglie Interference Model
Author: [  بالرمضان رضوان]
License: MIT
Description: A rigorous mathematical simulation of the double-slit
experiment using the de Broglie wavelength hypothesis.
This model bridges quantum wave evolution with classical optics.
==========================================================

import numpy as np
import matplotlib.pyplot as plt

1. المعطيات الفيزيائية (Physical Parameters)
L = 50.0 # مسافة الشاشة
d = 6.0 # تباعد الشقين
a = 1.0 # عرض الشق
k0 = 3.0 # العدد الموجي
lambda_dB = 2 * np.pi / k0 # طول موجة دي برولي

2. إنشاء نقاط الشاشة (Screen Grid)
y = np.linspace(-30, 30, 2000)

3. المعادلات الرياضية (Fraunhofer Diffraction Model)
beta: تداخل الشقين
alpha: حيود الشق الواحد
beta = np.pi * d * y / (lambda_dB * L)
alpha = np.pi * a * y / (lambda_dB * L)

شدة التداخل (Probability Density)
I = (np.cos(beta)2) * (np.sinc(alpha/np.pi) 2)

4. الرسم البياني (Visualization)
plt.figure(figsize=(12, 6))

رسم منحنى التداخل (Interference Pattern)
plt.plot(y, I, color='navy', lw=1.5, label='de Broglie Interference Pattern')

رسم تمثيل الشقين (Slit Representation)
plt.axvspan(-d/2-a/2, -d/2+a/2, color='red', alpha=0.3, label='Slit Position')
plt.axvspan(d/2-a/2, d/2+a/2, color='red', alpha=0.3)

تحسينات المظهر (Styling)
plt.title('Quantum Double-Slit Simulation: de Broglie Interference Model')
plt.xlabel('Screen position (y)')
plt.ylabel('Probability Density')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.tight_layout()

عرض النتيجة
plt.show()