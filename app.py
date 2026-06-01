import streamlit as st

st.set_page_config(
    page_title="Matematika Geometri",
    page_icon="🔥"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("logo geometri.png")

    st.title("Bangun Datar")

    pilihan = st.selectbox(
        "Pilihan Bangun Datar",
        ["Persegi", "Persegi Panjang", "Lingkaran", "Jajar Genjang", "Trapesium", "Belah Ketupat", "LayangLayang"]
    )

    st.caption("Dibuat dengan 🔥 oleh **Evelyn Pricilia Nurrisky Putri Ahrini**")


match pilihan:

    case "Persegi":
        st.markdown("""
        <h1 style='text-align:center;'>Persegi</h1>
        <p style='text-align:center;'>
        Menghitung <span style='color:#00ff88;'>luas</span> dan 
        <span style='color:#00ff88;'>keliling</span>
        </p>
        """, unsafe_allow_html=True)

        sisi = st.number_input("Masukkan Sisi", min_value=0.0)

        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            st.success(f"Luas = {luas:.2f}")
            st.success(f"Keliling = {keliling:.2f}")
            st.balloons()


    case "Persegi Panjang":
        st.markdown("""
        <h1 style='text-align:center;'>Persegi Panjang</h1>
        """, unsafe_allow_html=True)

        p = st.number_input("Masukkan Panjang")
        l = st.number_input("Masukkan Lebar")

        if st.button("Hitung", type="primary"):
            luas = p * l
            keliling = 2 * (p + l)
            st.success(f"Luas = {luas:.2f}")
            st.success(f"Keliling = {keliling:.2f}")
            st.balloons()


    case "Lingkaran":
        st.markdown("""
        <h1 style='text-align:center;'>Lingkaran</h1>
        """, unsafe_allow_html=True)

        r = st.number_input("Masukkan Jari-jari")

        if st.button("Hitung", type="primary"):
            luas = 3.14 * r * r
            keliling = 2 * 3.14 * r
            st.success(f"Luas = {luas:.2f}")
            st.success(f"Keliling = {keliling:.2f}")
            st.balloons()


    case "Jajar Genjang":
        st.markdown("""
        <h1 style='text-align:center;'>Jajar Genjang</h1>
        """, unsafe_allow_html=True)

        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        sisi = st.number_input("Masukkan Sisi Miring")

        if st.button("Hitung", type="primary"):
            luas = alas * tinggi
            keliling = 2 * (alas + sisi)
            st.success(f"Luas = {luas:.2f}")
            st.success(f"Keliling = {keliling:.2f}")
            st.balloons()


    case "Trapesium":
        st.markdown("""
        <h1 style='text-align:center;'>Trapesium</h1>
        """, unsafe_allow_html=True)

        a = st.number_input("Sisi Atas")
        b = st.number_input("Sisi Bawah")
        t = st.number_input("Tinggi")
        s1 = st.number_input("Sisi Miring 1")
        s2 = st.number_input("Sisi Miring 2")

        if st.button("Hitung", type="primary"):
            luas = 0.5 * (a + b) * t
            keliling = a + b + s1 + s2
            st.success(f"Luas = {luas:.2f}")
            st.success(f"Keliling = {keliling:.2f}")
            st.balloons()


    case "Belah Ketupat":
        st.markdown("""
        <h1 style='text-align:center;'>Belah Ketupat</h1>
        """, unsafe_allow_html=True)

        d1 = st.number_input("Diagonal 1")
        d2 = st.number_input("Diagonal 2")
        sisi = st.number_input("Sisi")

        if st.button("Hitung", type="primary"):
            luas = 0.5 * d1 * d2
            keliling = 4 * sisi
            st.success(f"Luas = {luas:.2f}")
            st.success(f"Keliling = {keliling:.2f}")
            st.balloons()


    case "LayangLayang":
        st.markdown("""
        <h1 style='text-align:center;'>Layang-Layang</h1>
        """, unsafe_allow_html=True)

        d1 = st.number_input("Diagonal 1")
        d2 = st.number_input("Diagonal 2")
        a = st.number_input("Sisi A")
        b = st.number_input("Sisi B")

        if st.button("Hitung", type="primary"):
            luas = 0.5 * d1 * d2
            keliling = 2 * (a + b)
            st.success(f"Luas = {luas:.2f}")
            st.success(f"Keliling = {keliling:.2f}")
            st.balloons()


    case _:
        st.error("Terjadi Kesalahan")