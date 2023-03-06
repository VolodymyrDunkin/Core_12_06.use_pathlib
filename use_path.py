from pathlib import Path


path = Path(r'd:\testfolder')

# print(type(path))

def move_file(target_path:Path, file:Path):
    file.replace(target_path / file.name)


for item in path.glob('**/*.*'):
    move_file(path, item)

for item in path.glob('**/*.*'):
    print(item.suffix, item.stem)

folders_to_del = []

for item in path.glob('**'):
    folders_to_del.append(item)

for item in folders_to_del[::-1]:
    try:
        item.rmdir()
    except Exception as e:
        print(e)
    
# print(folders_to_del[::-1])


CATEGORIES = {'audio': ['.mp3', '.aiff']}