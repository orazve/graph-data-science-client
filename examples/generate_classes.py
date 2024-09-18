import shutil

SEEDS = [42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
class_name = "NCLRCoraFRPZeroHops"
src = f"{class_name}.java"
for seed in SEEDS:
    filename = f"{class_name}{seed}.java"
    shutil.copy(src, filename)
    with open(filename, "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(f'{class_name}', f'{class_name}{seed}')
    filedata = filedata.replace('42', f'{seed}')

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)