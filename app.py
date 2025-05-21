
from asyncio import Handle
from operator import add
import streamlit as st  # type: ignore
import pickle
import os



# validasi input
def validasi_input(nama, pesan, show):
    if not nama or not pesan or not show:
        raise ValueError('semua kolom harus diisi, ')

# class tamu
class guest:
    def _init_(self, nama, pesan, show):
        self.nama = nama
        self.pesan = pesan
        self.show = show

# menyimpan tamu
    def save_guests_to_file(guests_list, filename= 'guests.pkl'):
        with open(filename, "wb") as file:
            pickle.dump(guests_list, file)

# memuat tamu
    def load_guests_from_file(filename= 'guests.pkl'):
        if os.path.exists(filename):
            with open(filename= 'rb') as file:
                return pickle.load(file)
            return[]
        
    # muat daftar tamu
    guests_list = load_guests_from_file

# menambah tamu
def display_info(self):
        return f"name: {self.name}, {self.pesan}, {self.show}"
    
def add_guest(nama, pesan, show):
        new_guest = guest(nama, pesan, show)
        guests_list.append(new_guest) # type: ignore
        save_guests_to_file(guests_list)  # type: ignore


# menampilkan tamu
def display_guests():
        global guest
        if guest.list:
            for guest in guest.list:
                st.write(guest.display_info())
        else:
            st.write('belum ada tamu')

        def handle_input(nama, pesan, show):
            try:
                validasi_input(nama, pesan, show)
                add.guest(nama, pesan, show)
                st.success('tamu berhasil ditambahkan')
            except ValueError as e:
                st.error(f'error: {e}')

#web 
st.title('buku tamu digital')
st.subheader('isi daftar tamu')

nama = st.text_input('nama')
pesan = st.text_input('pesan')
show = st.text_input ('show')

if st.button('kirim'):  
    class Handle:
    
     def input(nama, pesan, show):
        print(nama, pesan, show)
        
    st.subheader('daftar tamu')
    st.success("tamu berhasil ditambahkan")
    st.write('sudah ada tamu')
    
    