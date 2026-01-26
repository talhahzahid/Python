import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test = json.load(file)
            return test
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def list_all_videos(videos):
    if len(videos) > 0:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']}, Duration: {video['time']} ")
    else:
        print("No Video Found")


def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter video time : ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    index = int(input("Enter the video number to updated "))
    print(index, "index")
    if 1 <= index <= len(videos):
        name = input("Enter video name ")
        time = input("Enter video time ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid video number to selected")


def delete_video(videos):
    index = int(input("Enter video number to deleted "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index")


def main():
    videos = load_data()
    print("Loaded videos:", videos)
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
