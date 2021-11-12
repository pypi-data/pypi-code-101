import pandas as pd

class SCADA_data():
    def __init__(self, filepath='', sep=';', name='', data=pd.DataFrame()):
        self.name = name
        self.col_dict = {}
        if data.empty:
            self.set_data(filepath, sep)
        else:
            self.data_raw = data
        self.data_filtered = self.data_raw

    def set_data(self, filepath, sep):
        df = pd.DataFrame()
        ext = filepath.split('.')[-1]
        if ext == 'csv':
            print('CSV wird eingelesen...')
            df = pd.read_csv(filepath, sep=sep)
            pos_sep = [';', ',', '\t', '    ']
            while len(df.columns) < 3 and len(pos_sep) > 0:
                sep = pos_sep.pop(0)
                print(f'Eingelesene Tabelle nicht genug Spalten'
                      ', Seperator "{sep}" wird getestet.')
                
                df = pd.read_csv(filepath, sep=sep)
        elif 'xls' in ext:
            print('xls wird eingelesen...')
            df = pd.read_excel(filepath)
        else:
            print('Dateiformat nicht bekannt: {}'.format(ext))
            print('{} wird als csv gelesen'.format(filepath.split('/')[-1]))
            try:
                df = pd.read_csv(filepath, sep=sep)
                pos_sep = [';', ',', '\t', '    ']
                while len(df.columns) < 3 and len(pos_sep) > 0:
                    sep = pos_sep.pop(0)
                    print('Eingelesene Tabelle nicht genug Spalten'
                          ', Seperator "{}" wird getestet.'.format(sep))
                    df = pd.read_csv(filepath, sep=sep)

            except Exception as e:
                print(e)
                print('Einlesen fehlgeschlagen, Datei wird übersprungen.')
        if self.name == '':
            self.name = filepath.split('/')[-1]
        key_cols = [col for col in df.columns if (
                                                  'Zeit' in col or
                                                  'Datum' in col or
                                                  'UTC' in col)]
        if key_cols:
            print('Datumsspalte: {}'.format(key_cols[0]))
            self._datcol = key_cols[0]
        else:
            print('keine Zeitspalte gefunden'
                  ', {} wird verwendet'.format(df.columns[0]))
            self._datcol = df.columns[0]
        self.data_raw = df
        print('{} eingelesen!'.format(filepath.split('/')[-1]))
        print('{}: {}'.format(self.name, len(self.data_raw)))
        return self.name

    def filter(self, filter_abs={}):
        df1 = self.data_raw
        filter_list = pd.Series(len(df1)*[True])
        for key, val in filter_abs.items():
            key = key.split('_')[0]
            col = self.col_dict[key]
            filter_list = filter_list & (df1[col] > val[0])
            filter_list = filter_list & (df1[col] <= val[1])
        self.data_filtered = df1[filter_list]


class SCADA_group():
    def __init__(self, scada_dict):
        self.scada_dict = scada_dict
        sd0 = list(self.scada_dict.values())[0]
        self.data_merged = sd0.data_filtered.rename(
            columns={col: col+'_'+list(scada_dict.keys())[0]
                     for col in sd0.data_filtered.columns
                     }
            )
        for nam, sd in list(self.scada_dict.items())[1:]:
            df = sd.data_filtered
            col_l = sd0.col_dict['Zeit']+'_'+list(self.scada_dict.keys())[0]
            col_r = sd.col_dict['Zeit']+'_'+nam
            self.data_merged = self.data_merged.merge(
                df.rename(columns={col: col+'_'+nam
                                   for col in df.columns}),
                'inner',
                left_on=col_l,
                right_on=col_r,
            )
        self.split()

    def filter(self, filterdict_rel):
        df = self.data_merged
        filter_list = pd.Series(len(df)*[True])
        for key, value in filterdict_rel.items():
            cols = []
            for nam, sd in self.scada_dict.items():
                col = sd.col_dict[key]+'_'+nam
                cols.append(col)
            dk = df[cols].max(axis=1)-df[cols].min(axis=1)
            filter_list = filter_list & (dk < value)
        self.data_merged = df[filter_list]
        self.split()

    def split(self):
        df = self.data_merged
        for nam, sd in self.scada_dict.items():
            cols = [col for col in df.columns if nam in col]
            col_rename = {col: col.replace('_'+nam, '') for col in cols}
            sd.data_filtered = df[cols].rename(columns=col_rename)
            self.scada_dict[nam] = sd
