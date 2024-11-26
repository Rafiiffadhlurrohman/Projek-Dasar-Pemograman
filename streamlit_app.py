import streamlit as st
import pandas as pd

# Fungsi untuk memuat data dari file CSV
def load_data():
    try:
        data = pd.read_csv('stok_sembako.csv')
    except FileNotFoundError:
        data = pd.DataFrame({
            'Nama Barang': ['Beras', 'Gula', 'Minyak Goreng', 'Telur', 'Tepung', 'Garam', 'Kopi', 'Asem'],
            'Stok': [200, 100, 300, 400, 500, 700, 800, 600]
        })
    return data

# Fungsi untuk menyimpan data ke file CSV
def save_data(data):
    data.to_csv('stok_sembako.csv', index=False)

# Inisialisasi data stok barang
if 'data' not in st.session_state:
    st.session_state.data = load_data()

# Fungsi untuk menambah stok
def tambah_stok(nama_barang, jumlah):
    st.session_state.data.loc[st.session_state.data['Nama Barang'] == nama_barang, 'Stok'] += jumlah
    save_data(st.session_state.data)

# Fungsi untuk mengurangi stok
def kurangi_stok(nama_barang, jumlah):
    st.session_state.data.loc[st.session_state.data['Nama Barang'] == nama_barang, 'Stok'] -= jumlah
    save_data(st.session_state.data)

st.title('Manajemen Stok Toko Sembako')

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
