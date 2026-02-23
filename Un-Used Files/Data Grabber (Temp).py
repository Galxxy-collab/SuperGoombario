from Player_Data_Grabber import save_data
from Player_Data_Grabber import read_data
from Player_Data_Grabber import get_data

save_data("MyUsername", "SuperSercetPass", 10, 24004)


print(read_data("SuperSercetPass")) #Need the key
print(get_data()) #Outputs all user data

