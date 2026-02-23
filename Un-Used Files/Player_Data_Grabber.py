import os


def save_data(user_key):
    global data_save_table

    folder_path = "User Data"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, f"user_{user_key}")
    with open(file_path, "w") as data_save_table:
        data_save_table.write(str(0) + "\n")  # Key
        data_save_table.write(str(0) + "\n")  # Level
        data_save_table.write(str(0) + "\n")  # XP
        data_save_table.write(str(0) + "\n")  # XP


def read_data(user_key):
    global data_save_table
    global data_list

    folder_path = "User Data"
    file_path = os.path.join(folder_path, f"user_{user_key}")

    try:
        with open(file_path, "r") as data_save_table:
            data_list = data_save_table.readlines()
            return [s.strip('\n') for s in data_list]

    except:
        return "Invalid Key"


def get_data():
    global data_save_table
    global data_list
    global global_player_data
    folder_path = "../User Data"

    global_player_data = []
    global_player_name = []

    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.startswith("user_"):
                file_path = os.path.join(folder_path, file)
                with open(file_path, "r") as data_save_table:
                    data_list = data_save_table.readlines()
                    user_information = [s.strip('\n') for s in data_list]

                    global_player_data.append(user_information[1])
                    global_player_name.append(user_information[0])

    return global_player_data, global_player_name
