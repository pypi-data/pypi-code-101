import pandas as pd
from datetime import datetime


def convert_columns(df, column_dict):
    new_df = df.rename(columns=column_dict)
    new_df = new_df[column_dict.values()]
    return new_df


def get_diff_df(old, new, subset, id_key='ID'):
    def report_diff(x):
        return x[0] if x[0] == x[1] else '{}→{}'.format(*x)

    old.fillna('', inplace=True)  # 去掉excel的空：nan
    new.fillna('', inplace=True)

    # 按key去除重复的行
    old.drop_duplicates(subset=[id_key], keep='last', inplace=True)
    new.drop_duplicates(subset=[id_key], keep='last', inplace=True)

    old['version'] = "old"
    new['version'] = "new"
    old_accts_all = set(old[id_key])
    new_accts_all = set(new[id_key])

    dropped_accts = old_accts_all - new_accts_all
    added_accts = new_accts_all - old_accts_all

    # 合并两个项目列表
    all_data = pd.concat([old, new], ignore_index=True)

    # 去除重复的项目（没有变化的项目）subset里不包含version
    changes = all_data.drop_duplicates(subset=subset, keep='last')

    # 查找duplicated的id 生成一个list
    dupe_accts = changes[changes[id_key].duplicated() == True][id_key].tolist()

    # 检索出所有在id重复列表中的row
    dupes = changes[changes[id_key].isin(dupe_accts)]

    # Pull out the old and new data into separate dataframes
    change_new = dupes[(dupes["version"] == "new")]
    change_old = dupes[(dupes["version"] == "old")]

    # Drop the temp columns - we don't need them now
    change_new = change_new.drop(['version'], axis=1)
    change_old = change_old.drop(['version'], axis=1)

    # Index on the account numbers
    change_new.set_index(id_key, inplace=True)
    change_old.set_index(id_key, inplace=True)

    # return change_old, change_new, changes
    # Combine all the changes together
    df_all_changes = pd.concat([change_old, change_new],
                               axis='columns',
                               keys=['old', 'new'],
                               join='outer')

    df_all_changes = df_all_changes.swaplevel(axis='columns')[change_new.columns[0:]]
    df_changed = df_all_changes.groupby(level=0, axis=1).apply(lambda frame: frame.apply(report_diff, axis=1))
    df_changed = df_changed.reset_index()

    df_removed = changes[changes[id_key].isin(dropped_accts)]
    df_added = changes[changes[id_key].isin(added_accts)]

    return df_changed, df_removed, df_added


# "./data/projects_diff.xlsx"
def save_diff_to_excel(file_name, df_old, df_changed, df_removed, df_added, output_columns):
    # print(df_changed)
    (max_row, max_col) = df_changed.shape
    # print('max_row: {}, max_col:{}'.format(max_row, max_col))
    writer = pd.ExcelWriter(file_name)
    df_old.to_excel(writer, "old", index=False, columns=output_columns)
    if max_row > 0:
        df_changed.to_excel(writer, "changed", index=False, columns=output_columns)
    df_removed.to_excel(writer, "removed", index=False, columns=output_columns)
    df_added.to_excel(writer, "added", index=False, columns=output_columns)

    if max_row > 0:
        workbook = writer.book
        worksheet = writer.sheets['changed']
        worksheet.hide_gridlines(0)
        # define formats
        grey_fmt = workbook.add_format({'font_color': '#E0E0E0'})
        highlight_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color': '#B1B3B3'})
        ## highlight changed cells
        worksheet.conditional_format('A1:ZZ{}'.format(max_row + 1), {'type': 'text',
                                                                     'criteria': 'containing',
                                                                     'value': '→',
                                                                     'format': highlight_fmt})
        ## highlight unchanged cells
        worksheet.conditional_format('A1:ZZ{}'.format(max_row + 1), {'type': 'text',
                                                                     'criteria': 'not containing',
                                                                     'value': '→',
                                                                     'format': grey_fmt})
    writer.save()


def check_two_excel_diff(old_file_name, new_file_name, subset=None, id_key='ID', out_file_name=None, out_dir='./data'):
    old = pd.read_excel(old_file_name, 'Sheet1', na_values=['NA'])
    new = pd.read_excel(new_file_name, 'Sheet1', na_values=['NA'])  # reload from excel
    if not subset:
        subset = old.columns
    print(subset)
    df_changed, df_removed, df_added = get_diff_df(old, new, subset, id_key)

    if len(df_changed) == 0 and len(df_removed) == 0 and len(df_added) == 0:
        print('Nothing differece.')
        return

    if out_file_name is None:
        time_stemp = str(datetime.now())
        time_stemp = time_stemp.replace(':', '_')
        out_file_name = '{}/check_two_excel_diff_{}.xlsx'.format(out_dir, time_stemp)
    save_diff_to_excel(out_file_name, old, df_changed, df_removed, df_added, subset)

    print('Finish: {} changed, {} remvoed, {} added.'.format(len(df_changed), len(df_removed), len(df_added)))
    print('Difference file: ' + out_file_name)
    return df_changed[subset], df_removed[subset], df_added[subset]

