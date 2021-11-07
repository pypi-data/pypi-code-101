# def test_convert_fx():
#    assert convert_fx() ==

def test_bcb_data():
    assert bcb_data(12, from_date="2021-11-01",
                    to_date="2021-11-02", data_type="quote") == 0.029256
