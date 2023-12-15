import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Model fonksiyonu
def model_function(price):
    return 286.92 - 2.38 * price

# Streamlit uygulaması başlığı
st.title("Price & Quantity Relationship")

# Slider oluştur
price = st.slider("Select the Price (P)", min_value=0, max_value=120, value=50)

# Modelden miktarı hesapla
quantity = model_function(price)

# Grafik çiz
fig, ax = plt.subplots()
prices = np.arange(0, 120, 1)
quantities = model_function(prices)
ax.plot(prices, quantities, label="Q = 286.92 - 2.38P")
ax.scatter([price], [quantity], color='red')  # Kullanıcının seçtiği nokta

# Nokta üzerinde P ve Q değerlerini yazdır
ax.text(price, quantity, f"P={price}, Q={quantity:.2f}", color='blue', ha='left', va='bottom')

ax.set_xlabel("Price (P)")
ax.set_ylabel("Quantity (Q)")
ax.legend()
st.pyplot(fig)
