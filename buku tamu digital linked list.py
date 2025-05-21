import os

class Node:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        self.next = None

class GuestBookLinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, message):
        new_node = Node(name, message)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_all_entries(self):
        entries = []
        current = self.head
        while current:
            entries.append((current.name, current.message))
            current = current.next
        return entries

    def load_from_file(self, filepath):
        if not os.path.exists(filepath):
            return
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    if '|' in line:
                        name, message = line.split('|', 1)
                        self.append(name, message)

    def save_to_file(self, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            current = self.head
            while current:
                line = f"{current.name}|{current.message}\n"
                f.write(line)
                current = current.next

def print_welcome():
    print("="*50)
    print("  SELAMAT DATANG DI BUKU TAMU DIGITAL by jonathan   ")
    print(" Ketik 'sign <nama> <pesan>' untuk menandatangani")
    print("       Ketik 'show' untuk menampilkan tamu    ")
    print("             Ketik 'exit' untuk keluar          ")
    print("="*50)

def main():
    guestbook_file = "guestbook.txt"
    guestbook = GuestBookLinkedList()
    guestbook.load_from_file(guestbook_file)

    print_welcome()

    while True:
        try:
            user_input = input(">> ").strip()
            if not user_input:
                continue
            tokens = user_input.split(' ', 2)  
            command = tokens[0].lower()

            if command == 'sign':
        
                if len(tokens) < 3 or not tokens[1].strip() or not tokens[2].strip():
                    print("Format salah. Gunakan: sign <nama> <pesan>")
                    continue
                name = tokens[1].strip()
                message = tokens[2].strip()
                guestbook.append(name, message)
                guestbook.save_to_file(guestbook_file)
                print(f"Terima kasih, {name}, atas pesan Anda!")
            elif command == 'show':
                entries = guestbook.get_all_entries()
                if not entries:
                    print("Belum ada tamu yang menandatangani buku tamu.")
                else:
                    print("-"*50)
                    print("Daftar Tamu:")
                    for idx, (name, msg) in enumerate(entries, start=1):
                        print(f"{idx}. {name}: {msg}")
                    print("-"*50)
            elif command == 'exit':
                print("Terima kasih sudah menggunakan Buku Tamu Digital. Sampai jumpa!")
                break
            else:
                print("Perintah tidak dikenali. Gunakan 'sign', 'show' atau 'exit'.")
        except KeyboardInterrupt:
            print("\nDitetapkan keluar program.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()

