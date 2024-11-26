import streamlit as st
import pandas as pd

# Inisialisasi data stok barang
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({
        'Nama Barang': ['Beras', 'Gula', 'Minyak Goreng', 'Indomie'],
        'Stok': [100, 300, 500, 1000]
    })

# Fungsi untuk menambah stok
def tambah_stok(nama_barang, jumlah):
    st.session_state.data.loc[st.session_state.data['Nama Barang'] == nama_barang, 'Stok'] += jumlah

# Fungsi untuk mengurangi stok
def kurangi_stok(nama_barang, jumlah):
    st.session_state.data.loc[st.session_state.data['Nama Barang'] == nama_barang, 'Stok'] -= jumlah

st.title('Manajemen Stok Barang')

# Form untuk menambah stok
st.header('Tambah Stok')
with st.form('tambah_stok_form'):
    nama_barang_tambah = st.selectbox('Pilih Barang', st.session_state.data['Nama Barang'])
    jumlah_tambah = st.number_input('Jumlah', min_value=1, step=1)
    submit_tambah = st.form_submit_button('Tambah Stok')
    if submit_tambah:
        tambah_stok(nama_barang_tambah, jumlah_tambah)
        st.success(f'Stok {nama_barang_tambah} berhasil ditambah sebanyak {jumlah_tambah}.')

# Form untuk mengurangi stok
st.header('Kurangi Stok')
with st.form('kurangi_stok_form'):
    nama_barang_kurangi = st.selectbox('Pilih Barang', st.session_state.data['Nama Barang'])
    jumlah_kurangi = st.number_input('Jumlah', min_value=1, step=1)
    submit_kurangi = st.form_submit_button('Kurangi Stok')
    if submit_kurangi:
        if st.session_state.data.loc[st.session_state.data['Nama Barang'] == nama_barang_kurangi, 'Stok'].values[0] >= jumlah_kurangi:
            kurangi_stok(nama_barang_kurangi, jumlah_kurangi)
            st.success(f'Stok {nama_barang_kurangi} berhasil dikurangi sebanyak {jumlah_kurangi}.')
        else:
            st.error('Jumlah pengurangan melebihi stok yang tersedia.')

# Tampilkan data stok barang
st.header('Daftar Stok Barang')
st.table(st.session_state.data)
