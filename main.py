

with open("./input/names/invited_names.txt") as names:
    list_names = names.readlines()


with open("./input/letters/starting_letter.docx") as file:
    lines = file.read()


    for replac in list_names:
        strip_name = replac.strip()
        replace_datas = lines.replace("[name]", strip_name)
        print(replace_datas)
        with open(f"./output/readytosend/letter_for_{strip_name}.docx", mode="w") as completed_letter:
            completed_letter.write(replace_datas)


