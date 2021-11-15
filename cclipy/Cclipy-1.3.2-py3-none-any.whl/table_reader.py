import numpy as np
import xlrd


class TableReader:
    def __init__(self, target_path, sheet_idx):
        self.path = target_path
        self.data = xlrd.open_workbook(self.path)
        self.table = self.data.sheets()[sheet_idx]
        self.attrs = []
        self.instance_idx = 0
        self.rows = self.table.nrows

        # The idx where the instances start
        self.offset = 0

        self.table_list = []

    def excel2list(self):
        ret = self.get_instance(0)
        while ret is not None:
            self.table_list.append(ret)
            ret = self.get_next_instance()

    def load_attr_in_table(self, row):
        self.attrs = self.table.row_values(row)
        self.offset = row + 1

    def get_instance(self, idx):
        idx_offset = idx + self.offset
        if not self._is_valid_idx(idx_offset):
            print('The given idx is invalid')
            return None
        self.instance_idx = idx_offset
        return self.table.row_values(self.instance_idx)

    def get_next_instance(self):
        if not self._is_valid_idx(self.instance_idx+1):
            print('Reached end of the table')
            return None
        self.instance_idx += 1
        return self.table.row_values(self.instance_idx)

    def get_attr(self):
        return self.attrs

    def get_instance_array(self):
        pass

    def _is_valid_idx(self, idx):
        if idx >= self.rows:
            return False
        return True


if __name__ == '__main__':
    m_table = TableReader('data/sample.xlsx', 4)
    m_table.load_attr_in_table(3)
    print(m_table.get_attr())
    print(m_table.get_instance(0))
    m_table.excel2list()
    
    print(m_table.table_list)
    
    table_array = np.array(m_table.table_list)
    table_array = np.delete(table_array, [0, 1], axis=1)    # remove the first two columns, which are irrelevant
    
    table_array = table_array.astype(np.float16)
    
    score_arr = np.sum(table_array, axis=1)
    score_arr = score_arr.reshape(len(score_arr), 1)
    print(score_arr)
    print(len(score_arr))
    
    print(np.shape(score_arr), np.shape(table_array))
    
    #res = np.column_stack((table_array, score_arr))
    res = np.hstack((table_array, score_arr))
    print(res)
