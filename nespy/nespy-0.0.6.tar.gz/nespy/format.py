import struct

import nespy.grpc.SerializableDataType_pb2 as dt


def _write_header(buf, col):
    """
    Writes head of table and add the column name.

    Parameters
    ----------
    buf : stringio
          Buffer we want to write the header into.
    col : str
          Column name as a string.

    Returns
    -------

    """
    col_string = '<th>{}</th>'.format(col)
    buf.write(col_string)


def _write_data(buf, line, index):
    """
    Writes a line into a buffer in HTML.

    Parameters
    ----------
    buf : stringio
          Stringio buffer to write into.
    line : list
           The actual data received from NebulaStream. Each index is for a column in the table.
    index : int
            Index for the table.

    Returns
    -------

    """
    s = ""
    buf.write('<tr>')
    buf.write('<th>{}</th>'.format(index) + ' ')

    for i in line:
        s += '<td>{}</td>'.format(i) + ' '
    buf.write(s)
    buf.write('</tr>')


def _types_details(data_type, value):
    """
    For each message there exist a nested message for the specific data type. This requires a different decoding.
    This function basically decodes the nested message according to the given data type.

    Parameters
    ----------
    data_type : str
                Data type of the first decoding (the message is nested. Therefore, the inner message is another Protocol
                Buffer schema).
    value : protobuf schema
            Nested message, which requires a different schema.

    Returns
    -------
    data_type : str
                same data_type as the parameter
    decoded_value : str
                    Decoded message.

    """
    decoded_value = ''
    if 'ArrayDetails' in data_type:
        decoded_value = dt.SerializableDataType.ArrayDetails()
        decoded_value.ParseFromString(value)
    elif 'IntegerDetails' in data_type:
        decoded_value = dt.SerializableDataType.IntegerDetails()
        decoded_value.ParseFromString(value)
    elif 'FloatDetails' in data_type:
        decoded_value = dt.SerializableDataType.FloatDetails()
        decoded_value.ParseFromString(value)
    elif 'CharDetails' in data_type:
        decoded_value = dt.SerializableDataType.CharDetails()
        decoded_value.ParseFromString(value)
    return data_type, decoded_value


def _how_many_bytes_per_row(details):
    """
    Counts how many bytes we need for one row.

    Parameters
    ----------
    details : dict_items
              List of dict_items. Each dict_items consist of the data type and therefore, we can calculate how many
              bytes a row consists of.

    Returns
    -------
    summed_bytes : int
                   Length of a single row.

    """
    summed_bytes = 0
    for i in details:
        if 'Integer' in i[1][0] or 'Float' in i[1][0]:
            summed_bytes += i[1][1].bits // 8
        elif 'Char' in i[1][0] or 'Array' in i[1][0]:
            summed_bytes += i[1][1].dimensions
    return summed_bytes


def _byte_row_to_string(details, one_row_byte, keys):
    """
    Translates one row of bytes into string.

    Parameters
    ----------
    details : list
             schema details from first message, know the data type
    one_row_byte : bytearray
                   One row of data but it is still in bytes. We call bytes to type to decode a specific length of byte
                   into a string.
    keys : list
           The column names.

    Returns
    -------
    s : str
        One line of the result as a list. Each index is a value for the result table.
    di : dict
         One line as a dict. This is for the process function.

    """
    s = list()
    di = dict()
    for d in range(len(details)):
        if 'IntegerDetails' in details[d][0]:
            byte_length = details[d][1].bits // 8
            i = one_row_byte[0:byte_length]
            if byte_length == 4:
                s.append(_bytes_to_type(1, i))
                di[keys[d]] = int(_bytes_to_type(1, i))
            elif byte_length == 8:
                s.append(_bytes_to_type(4, i))
                di[keys[d]] = int(_bytes_to_type(4, i))
            one_row_byte = one_row_byte[byte_length:]
        elif 'FloatDetails' in details[d][0]:
            byte_length = details[d][1].bits // 8
            i = one_row_byte[0:byte_length]
            s.append(_bytes_to_type(2, i))
            di[keys[d]] = float(_bytes_to_type(2, i))
            one_row_byte = one_row_byte[byte_length:]
        elif 'ArrayDetails' in details[d][0]:
            data_type = details[d][1].componentType.type
            if data_type == dt.SerializableDataType.Type.CHAR:
                i = one_row_byte[0:details[d][1].dimensions]
                s.append(_bytes_to_type(3, i))
                di[keys[d]] = _bytes_to_type(3, i)
                one_row_byte = one_row_byte[details[d][1].dimensions:]
    return s, di


def _bytes_to_type(data_type, byte_pieces):
    """
    Converts bytes to a certain type.

    Parameters
    ----------
    data_type : int
                Type we want to translate to.
    byte_pieces : bytearray
                  The byte piece we want to translate to the data type.

    Returns
    -------

    Notes
    -------
    NebulaStream should only support :
    UNDEFINED = 0;
    INTEGER = 1;
    FLOAT = 2;
    CHAR = 3;
    LONG = 4;
    ARRAY = 5;
    BOOLEAN = 6;
    FIXEDCHAR = 7;
    byteorder = 'little', signed = True

    """
    # upper und lower bound sagt, ob die signed oder unsigned sind, je nachdem in welchem bereich die sich befinden
    if data_type == 0:
        return "UNDEFINED DATA TYPE"
    elif data_type == 1:
        return str(struct.unpack('<i', byte_pieces)[0])
    elif data_type == 2:
        if len(byte_pieces) == 8:
            return str(struct.unpack('<d', byte_pieces)[0])
        return str(struct.unpack('<f', byte_pieces)[0])
    elif data_type == 3:
        s = ''
        for i in range(len(byte_pieces)):
            if byte_pieces[i:i + 1] == b'\x00':
                break
            c = struct.unpack('<c', byte_pieces[i:i + 1])[0]
            s += str(c)[2]
        return s
    elif data_type == 4:
        return str(struct.unpack('<q', byte_pieces)[0])
    # elif data_type == 5:
    # elif data_type == 6:
    # elif data_type == 7:
    else:
        return "Error"
