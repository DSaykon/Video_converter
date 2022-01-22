import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

root = tk.Tk()

path_output = ''
list_format = ['avi', 'mp4', 'mkv', 'mov', 'mpeg', 'wav', 'mp3', 'aac', 'flac', 'ogg']


def form_inp():
    """
        Диалоговое окно выбора исходных файлов
    """
    global path_output
    fd = tk.filedialog.askopenfilenames(title="Выберите медиафайл",
                                        multiple=True)
    if fd:
        txt.config(state='normal')
        txt.delete(1.0, 'end')
        for i in fd:
            txt.insert('end', i + '\n')
            if path_output == '':
                path_output = os.path.dirname(i)
        txt.insert('end', '\n' + 'Конец списка' + '\n')
        txt.config(state='disable')
        bt_run.config(state='normal')


def form_out():
    """
        Диалоговое окно выбора пути сохранения файлов
    """
    global path_output
    path_output = tk.filedialog.askdirectory(
        title='Укажите каталог для сохранения файлов')
    txt.config(state='normal')
    txt.insert('end', 'Результат будут сохранен в: ' + path_output + '\n' + '\n')
    txt.config(state='disable')


def run():
    """
        Команда выполнить конвертацию
    """
    util_path = str(os.path.abspath('ffmpeg.exe'))

    if os.path.isfile(util_path):
        for i in txt.get(1.0, 'end').split('\n'):
            if i:
                output_file = (path_output
                               + '/' + os.path.basename(i).rsplit('.', 1)[0]
                               + '.' + list_format_file.get())
                print(output_file)
                txt.config(state='normal')
                txt.tag_add(i, 1.0, 'end')
                txt.tag_config(i, background='#90ee90', underline=1)

                try:
                    os.system(util_path + ' -i ' + i + ' ' + output_file)
                except:
                    txt.insert('end', '\n' +
                               'Не удается конвертировать файл: ')
                    txt.insert('end', '\n' + i)
            else:
                break
        txt.insert('end', '\n' + 'Конвертация завершена')
        txt.config(state='disable')

    else:
        txt.config(state='normal')
        txt.insert('end', '\n' + 'Не найден файл "ffmpeg.exe"')
        txt.insert('end', '\n' + 'Убедитесь, что он доступен и находится в корне программы.')
        txt.config(state='disable')


lb_info = tk.Label(text='Выберите один или несколько файлов: ')
lb_info.place(y=10, x=10)

bt_input = tk.Button(root, text='  ...  ', command=form_inp)
bt_input.place(y=10, x=255)

txt = tk.Text(width=110, state='normal')
txt.place(y=80, x=10)
txt.insert('end', 'Для начала выберите один или несколько файлов.' + '\n' +
           'Файл не должен иметь в имени пробелов, иначе операция не выполнится.' + '\n' + '\n' +
           'Программа использует для конвертации внешний модуль: ffmpeg.exe' + '\n' +
           'Загрузить его можно здесь: https://ffmpeg.org/download.html' + '\n' +
           'Файл сохраняем в корне папки с данной программой' + '\n' + '\n')

lb_output = tk.Label(text='Выберите каталог для сохранения файлов:')
lb_output.place(y=40, x=10)

bt_output = tk.Button(root, text='  ...  ', command=form_out)
bt_output.place(y=40, x=255)

lb_format_info = tk.Label(text='В какой формат конвертировать файл(ы)?')
lb_format_info.place(y=10, x=500)

list_format_file = ttk.Combobox(root,
                                values=[u'avi', u'mp4', u'mkv', u'mov', u'mpeg',
                                        u'wav', u'mp3', u'aac', u'flac', u'ogg'],
                                height=6, state='readonly')
list_format_file.current(0)
list_format_file.place(y=10, x=745)

bt_run = tk.Button(root, text='Выполнить', command=run, state='disable')
bt_run.place(y=470, x=420)

root.geometry('900x500')
root.title('Audio-Video Converter')
root.mainloop()
if __name__ == '__main__':
    pass
