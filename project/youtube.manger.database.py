import sqlite3


conn = sqlite3.connect("youtube_manager.db")

cursor = conn.cursor()

cursor.execute(""" 
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
               """)


def list_all_video():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name , time) VALUES(? , ? )", (name, time))
    conn.commit()


def update_video(videoId, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name = ? , time = ? where id = ?",
        (new_name, new_time, videoId),
    )
    conn.commit()


def delete_video(videoId):
    cursor.execute("DELETE FROM videos where id = ?", (videoId,))
    conn.commit()


def main():
    while True:
        print("Choose an option")
        print("1, List all video")
        print("2, Add video")
        print("3, Update video")
        print("4, Delete video")
        print("5, Close the program")
        choose = input("Enter video option ")
        if choose == "1":
            list_all_video()
        elif choose == "2":
            name = input("Enter Video Name ")
            time = input("Enter Video Time ")
            add_video(name, time)
        elif choose == "3":
            videoId = int(input("Enter Video Id to update "))
            new_name = input("Enter new video name ")
            new_time = input("Enter new video time ")
            update_video(videoId, new_name, new_time)
        elif choose == "4":
            videoId = int(input("Enter Video Id "))
            delete_video(videoId)
            conn.commit()
        elif choose == "5":
            break
        else:
            print("Invalid Number")


if __name__ == "__main__":
    main()
