row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ") #23

# Convert String to List
position = list(position)
col = int(position[0]) #2
row = int(position[1]) #3

selected_row = map[row - 1]
selected_row[col -1] = "X"

print(f"{row1}\n{row2}\n{row3}")