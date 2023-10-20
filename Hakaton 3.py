# Подивіться, будь-ласка на цей кодік. Видає наче правильно, я навіть превіряв все в ручну, але не те що було у вас(

patern = ".,!@#$^&*()_=?/\%^:;<>—»«\"\t"
num_of_lines = [157, 1043, 1107, 759, 153]  # Всі числа на 1 меньше бо в масиві перший елемент 0.
num_of_words = [92, 14, 105, 54, 11]   
urls = ["C:\\Users\ASUS\Downloads\Chorna_rada.txt", "C:\\Users\ASUS\Downloads\Khiba_revut_voly.txt", "C:\\Users\ASUS\Downloads\Misto.txt"]


def norm_text(name_of_file):
    with open(name_of_file, 'r', encoding='utf-8') as file:
        text = file.read()
        for i in patern:
            for j in text:
                if i == j:
                    text = text.replace(i, "")
        text = text.split('\n')
        tex = []
        for line in text:
            tex.append(line.split())
        return tex


def result_words(tex, line_num, word_num):
    if len(tex[line_num]) < word_num:
        print('')
    else:
        print(tex[line_num][word_num])


for adr in urls:
    text = norm_text(adr)
    i = 0
    while i < len(num_of_lines):
        result_words(text, num_of_lines[i], num_of_words[i])
        i += 1   