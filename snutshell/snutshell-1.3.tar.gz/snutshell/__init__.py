import pickle
import xlsxwriter
import numpy as np
import os

def load(filename):
    loaded_dict = pickle.load(open(filename, 'rb'))
    return loaded_dict


def np_2darray_converter(matrix):

    if(type(matrix) == type({})):             # making dictionary suitable for excel
        keys = list(matrix.keys())
        values = list(matrix.values())
        values = [str(value) for value in values]
        matrix = np.array([keys, values]).transpose()

    new_matrix = np.array(matrix, ndmin = 2)
    if (new_matrix.dtype == 'O'):         # should I add more data types, for example dictionaries?
        return -1, -1, -1
    rows = new_matrix.shape[0]
    cols = new_matrix.shape[1]
    return rows, cols, new_matrix

def create_dat(filename, keys, data = None):
    if(data == None):
        pickle.dump(keys, open(filename, 'wb'))
    else:
        data_dict = {}
        for i, key in enumerate(keys):
            data_dict[key] = data[i]
        pickle.dump(data_dict, open(filename, 'wb'))

        


def create_xlsx(filename, keys, data = None, dat = False):
    if(dat == True):
        fname, fext = os.path.splitext(filename)
        create_dat(fname + '.dat', keys, data)

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    title_format = workbook.add_format({ 'font_size':16, 'font_color':'#02172C',
                                            'bold':True, 'bg_color':'#7FF000'})  #A9E063
    separator_format = workbook.add_format({'bg_color':'#434446'})  #A72307

    if(data == None):
        try:
            d_keys = list(keys.keys())
            d_data = list(keys.values())
        except:
            print('A dictionary is expected as 2nd positional argument')
            return
    else:
        d_keys = keys
        d_data = data

    current_column = 3
    current_row = 3
    for i in range(len(d_data)):
        worksheet.write(current_row, current_column, d_keys[i], title_format)

        rows, cols, current_data = np_2darray_converter(d_data[i])
        if(rows == -1):
            continue

        if(rows == 1):
            worksheet.write_column(current_row + 2, current_column, current_data[0])
            current_column += 4
            worksheet.set_column(current_column-2, current_column-2, width = 3, cell_format = separator_format)
        else:
            worksheet.conditional_format(current_row, current_column + 1, current_row, current_column + cols - 1, {'type':'blanks',
                                                                                                'format':title_format})
            for j in range(rows):
                worksheet.write_row(current_row + 2 + j, current_column, current_data[j])
            current_column += cols + 3
            worksheet.set_column(current_column-2, current_column-2,width = 3, cell_format = separator_format)

    workbook.close()

    


