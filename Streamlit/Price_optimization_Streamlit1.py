import streamlit as st
import pandas as pd
import pickle

# CSS Stillerini Ekleyin
def set_css():
    st.markdown(
        """
        <style>
        .stNumberInput, .stTextInput {
            margin-top: -25px;    /* Kutuların üst etiketlere olan boşluğunu azalt */
            margin-bottom: -5px;  /* Kutuların alt etiketlere olan boşluğunu azalt */
        }
        .stNumberInput > div > div, .stTextInput > div > div {
            padding-top: 0px;    /* Kutu içi üst boşluğu azalt */
            padding-bottom: 0px; /* Kutu içi alt boşluğu azalt */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
st.sidebar.title("Fiyat Optimizasyonu ve Fiyat - Miktar Iliskisi ML Algoritmaları")

# Her sayfa için bir fonksiyon tanımlayın
def teorik():
    st.title('Fiyat Optimizasyonu')
    
    st.markdown("""
    **Not:** Bu analiz her bir ASIN bazında yapılmaktadır.

    **Kar = Satış Fiyatı – Maliyetler**

    **Kar veya Gelir = Revenue: R ile gösterilecek**

    **Satış Fiyatı (Price: P):** Ürünün Canada’da satış fiyatı, US Dolara çevrildi

    **Maliyetler (Cost: C) =** Ürünün US’den Alış Fiyatı + OneAMZ Aradepo Fee + Amazon Fee

    **R = P – C** kullanılarak tarafımızdan hesaplanıyor.

    Alttaki grafikte de görüldüğü üzere, revenue ile price arasında ters U şeklinde bir ilişki söz konusudur.
    """)
    # Resmi göster
    #st.image("/mnt/data/image.png", use_column_width=True)
    st.image("resim.jpg",  width=500)
    # Metni göster
    st.markdown("""
<style>
.red-text { color: red; }
</style>

Şimdi bu ters U şeklindeki ilişkiyi denklem haline getirelim:

<span class="red-text">R = β₀ + β₁P + β₂P² + β₃Q + β₄BSRSub + β₅SellerNumbers + β₆Rating + β₇ReviewNumbers</span><br><br>

Bu modelde fiyat optimizasyonu için asıl önemli olan kısım; <span class="red-text">R = β₀ + β₁P + β₂P²</span> bölümü olup, diğer değişkenler modele ek açıklayıcı değişken olarak dahil edilmektedir.<br><br>

Bu model ML algoritmaları ile tahmin edildikten sonra R’nin P’ye göre kısmi türevi alınıp, sıfıra eşitlenecek. Çünkü ters U şeklindeki fonksiyonda gelirin maksimum olduğu noktada teğetin eğimi (1. türev) sıfıra eşit olacaktır.<br><br>

<span class="red-text">R' = β₁ + 2β₂P = 0</span><br><br>

<span class="red-text">P = -β₁ / (2β₂)</span><br><br>

olacaktır. Böylece geliri maksimize eden fiyat (P), yani optimum fiyat düzeyi bulunmuş olacaktır.
""", unsafe_allow_html=True)
    
# Fiyat Optimizasyon Sayfasını Tanımlayın
def price_optimization_page():
    selected_asin = st.sidebar.selectbox("Bir ASIN Seçin", ["B00FS3VJAO", "B0779LHFMF", "B0811VD9MY"])

    # Ürün Bilgilerini Göster
    if selected_asin == "B00FS3VJAO":
        st.image("B00FS3VJAO.jpg", caption="Ürün Resmi", width=180)
        # Kullanıcı girdilerini al
        input_data = {}
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.markdown("**ABD'den Alış Fiyatı($):**")
            input_data['us_purchase_price'] = st.number_input('', value=39.99 )  
        with col3:
            st.markdown("**Kanada Satış Fiyatı($):**")
            input_data['us_sellin_price'] = st.number_input('', value=56.65)
        with col5:
            st.markdown("**Amazon Ücreti($):**")
            input_data['amazon_fee'] = st.number_input('', value=17.16)
    
        col7, col8, col9, col10, col11, col12 = st.columns(6)
        with col7:
            st.markdown("**OneAMZ Ara Depo Ücreti($):**")
            input_data['oneamz_fee'] = st.number_input('', value=42.78)  
        with col9:
            st.markdown("**Alt Kategori Sales Rank:**")
            input_data['Sub_Sales_Rank'] = st.number_input('', value=4)
        with col11:
            st.markdown("**Günlük Satış Adedi:**")
            input_data['daily_sales'] = st.number_input('', value=48)
        col13, col14, col15, col16,col17,col18 = st.columns(6)
        with col13:
            st.markdown("**Rewiew Sayısı:**")
            input_data['mnumber_of_reviews'] = st.number_input('', value=8904)
        with col15:
            st.markdown("**Seller Sayısı:**")
            input_data['number_of_floods'] = st.number_input('', value=1)
        with col17:
            st.markdown("**Rating:**")
            input_data['rating'] = st.number_input('', value=4.2)
        col19, col20, col21, col22,col23,col24 = st.columns(6)
        with col19:
            st.markdown("**Kanada İçin Hesaplanan Optimum Satış Fiyatı($):**")
            input_data['optimum_price'] = st.number_input('', value=113.18)
        with col21:
            st.markdown("**OneAMZ Satıcısına Kalan Net Kar($):**")
            input_data['Remaining_Profit_to_OneAMZ_Seller'] = st.number_input('', value=21.54)
        with col23:
            st.markdown("**OneAMZ Satıcısına Kalan Net Kar(%):**")
            input_data['Net_Profit_Remaining_for_OneAMZ_Seller'] = st.number_input('', value=23.51)
        
        
       
     # Ürün Bilgilerini Göster
    elif selected_asin == "B0779LHFMF":
        st.image("B0779LHFMF.jpg", caption="Ürün Resmi", width=180)
        # Kullanıcı girdilerini al
        input_data = {}
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.markdown("**ABD'den Alış Fiyatı($):**")
            input_data['us_purchase_price'] = st.number_input('', value=32.99 )  
        with col3:
            st.markdown("**Kanada Satış Fiyatı($):**")
            input_data['us_sellin_price'] = st.number_input('', value=34.62)
        with col5:
            st.markdown("**Amazon Ücreti($):**")
            input_data['amazon_fee'] = st.number_input('', value=10.12)
    
        col7, col8, col9, col10, col11, col12 = st.columns(6)
        with col7:
            st.markdown("**OneAMZ Ara Depo Ücreti($):**")
            input_data['oneamz_fee'] = st.number_input('', value=15.75)  
        with col9:
            st.markdown("**Alt Kategori Sales Rank:**")
            input_data['Sub_Sales_Rank'] = st.number_input('', value=4)
        with col11:
            st.markdown("**Günlük Satış Adedi:**")
            input_data['daily_sales'] = st.number_input('', value=174)
        col13, col14, col15, col16,col17,col18 = st.columns(6)
        with col13:
            st.markdown("**Rewiew Sayısı:**")
            input_data['mnumber_of_reviews'] = st.number_input('', value=42352)
        with col15:
            st.markdown("**Seller Sayısı:**")
            input_data['number_of_floods'] = st.number_input('', value=2)
        with col17:
            st.markdown("**Rating:**")
            input_data['rating'] = st.number_input('', value=4.4)
        col19, col20, col21, col22,col23,col24 = st.columns(6)
        with col19:
            st.markdown("**Kanada İçin Hesaplanan Optimum Satış Fiyatı ($):**")
            input_data['optimum_price'] = st.number_input('', value=67.46)
        with col21:
            st.markdown("**OneAMZ Satıcısına Kalan Net Kar($):**")
            input_data['Remaining_Profit_to_OneAMZ_Seller'] = st.number_input('', value=11.60)
        with col23:
            st.markdown("**OneAMZ Satıcısına Kalan Net Kar(%):**")
            input_data['Net_Profit_Remaining_for_OneAMZ_Seller'] = st.number_input('', value=20.77)
            
        
         # Ürün Bilgilerini Göster
    elif selected_asin == "B0811VD9MY":
        st.image("B0811VD9MY.jpg", caption="Ürün Resmi", width=160)
        # Kullanıcı girdilerini al
        input_data = {}
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.markdown("**ABD'den Alış Fiyatı($):**")
            input_data['us_purchase_price'] = st.number_input('', value=13.39)  
        with col3:
            st.markdown("**Kanada Satış Fiyatı($):**")
            input_data['us_sellin_price'] = st.number_input('', value=10.1)
        with col5:
            st.markdown("**Amazon Ücreti($):**")
            input_data['amazon_fee'] = st.number_input('', value=6.10)
    
        col7, col8, col9, col10, col11, col12 = st.columns(6)
        with col7:
            st.markdown("**OneAMZ Ara Depo Ücreti($):**")
            input_data['oneamz_fee'] = st.number_input('$', value=13.53)  
        with col9:
            st.markdown("**Alt Kategori Sales Rank:**")
            input_data['Sub_Sales_Rank'] = st.number_input('', value=25)
        with col11:
            st.markdown("**Günlük Satış Adedi:**")
            input_data['daily_sales'] = st.number_input('', value=3)
        col13, col14, col15, col16,col17,col18 = st.columns(6)
        with col13:
            st.markdown("**Rewiew Sayısı:**")
            input_data['mnumber_of_reviews'] = st.number_input('', value=69)
        with col15:
            st.markdown("**Seller Sayısı:**")
            input_data['number_of_floods'] = st.number_input('', value=18)
        with col17:
            st.markdown("**Rating:**")
            input_data['rating'] = st.number_input('', value=2.7)
        col19, col20, col21, col22,col23,col24 = st.columns(6)
        with col19:
            st.markdown("**Kanada İçin Hesaplanan Optimum Satış Fiyatı($):**")
            input_data['optimum_price'] = st.number_input('', value=40.02)
        with col21:
            st.markdown("**OneAMZ Satıcısına Kalan Net Kar($):**")
            input_data['Remaining_Profit_to_OneAMZ_Seller'] = st.number_input('', value=4.51)
        with col23:
            st.markdown("**OneAMZ Satıcısına Kalan Net Kar(%):**")
            input_data['Net_Profit_Remaining_for_OneAMZ_Seller'] = st.number_input('', value=12.71)

def Fiyat_Miktar_İlişkisi():
    st.title('Fiyat - Miktar İlişkisi')
    
    st.markdown("""
    **Dataset Hakkında:**

    - Q: Quantity (Miktar)
    - P: Price (Fiyat)

    **Model: P = β₀ + β₁ * Q**
    """)

    # Grafik dosyanızın adını ve yolunu güncelleyin
    st.image("resim3.png", caption="Fiyat - Miktar Grafiği", width=600)
    
    st.markdown("""
    **Ekonomideki Talep Kanunu:** Bir ürünün fiyatı adustukçe, talep edilen miktar artacaktır. 
    
    Bu analizde; temsili olarak B00FS3VJAO ASIN numaralı ürün için bu inceleme yapılmıştır.
    """)

# Sayfa 4 Fonksiyonu
def page4():
    st.title('Fiyat - Miktar')
    
    # Grafik dosyanızın adını ve yolunu güncelleyin
    st.image("B00FS3VJAO.jpg", caption="B00FS3VJAO", width=100)
    st.image("resim4.jpeg", caption="B00FS3VJAO", width=600)
    
    # Denklemi kırmızı ve büyük fontla, ortalanmış şekilde göster
    st.markdown("""
    <h3 style="color:red; text-align:center;">Q = 286.92 - 2.38*P</h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Fiyat($):**")
        price = st.number_input('', value=10.00)
        
    miktar=286.92-2.38*price
        
    with col2:
        st.markdown("**Miktar:**")
        st.info(miktar)  

# Sidebar Menüsü
def sidebar_navigation():
    page = st.sidebar.radio('Sayfa seçiniz:', ('Fiyat Optimizasyonu Teorik Çerçeve', 'Fiyat Optimizasyonu Uygulaması', 'Fiyat Miktar İlişkisi Teorik Çerçeve', 'Fiyat Miktar İlişkisi Uygulaması'))

    if page == 'Fiyat Optimizasyonu Teorik Çerçeve':
        teorik()
    elif page == 'Fiyat Optimizasyonu Uygulaması':
        price_optimization_page()
    elif page == 'Fiyat Miktar İlişkisi Teorik Çerçeve':
        Fiyat_Miktar_İlişkisi()  # Burada uygun fonksiyon çağrısını yapın.
    elif page == 'Fiyat Miktar İlişkisi Uygulaması':
        page4()

# Ana fonksiyon
def main():
    set_css()
    sidebar_navigation()

# Ana fonksiyonu çağırın
if __name__ == "__main__":
    main()
