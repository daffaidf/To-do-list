tasks = []

def show_task():
    print("\n=== Daftar Task ===")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Task: {task['task']}, Assignee: {task['assignee']}, Status: {task['status']}")

def add_task():
    print("\n--- Tambah Task Baru ---")
    nama_task = input("Masukkan nama task: ")
    assignee = input("Masukkan nama assignee: ")
    
    task_baru = {
        "task": nama_task,
        "assignee": assignee,
        "status": "Belum Selesai"
    }
    tasks.append(task_baru)
    print("Data task sukses tersimpan!")

def update_status():
    print("\nFitur Update Status (Nanti dikerjain anggota tim lain)")

def delete_task():
    print("\nFitur Delete Task (Nanti dikerjain anggota tim lain)")

def search_task():
    print("\nFitur Search Task (Nanti dikerjain anggota tim lain)")

def main():
    while True:
        print("\n=== Aplikasi To-Do List Kelompok ===")
        print("1. Show Task")
        print("2. Add Task")
        print("3. Update Status")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            show_task()
        elif pilihan == '2':
            add_task()
        elif pilihan == '3':
            update_status()
        elif pilihan == '4':
            delete_task()
        elif pilihan == '5':
            search_task()
        elif pilihan == '6':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == '__main__':
    main()