from pathlib import Path

# module doc https://docs.python.org/3/library/pathlib.html#module-pathlib

TARGET_FOLDER = r'' # type path to your folder

#create Path object

path = Path(TARGET_FOLDER)

#iterate over folder items, use str pattern https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob

for item in path.glob('**/*'):
    print(item) # every item - is a Path object


#create folders with name "NewFolder"

try:
    path.joinpath('NewFolder').mkdir()
except FileExistsError as e:
    print(e)

# new path can also be created with the help of /

new_path = path / 'NewFolder2'

# check if path exist

if not new_path.exists():
    new_path.mkdir()


# create empty file in folder
file_name = 'my_text.txt'

with open(new_path / file_name, 'w') as fd:
    pass


# rename file 
file_path = new_path / file_name
new_file_name = 'my_new_text.txt'

new_file_path = file_path.rename(new_path / new_file_name)

# move file

file_in_target = new_file_path.replace(path / new_file_path.name)

#get file parts

print(file_in_target.name)
print(file_in_target.suffix)
print(file_in_target.stem)






