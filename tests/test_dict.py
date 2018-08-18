import ar_cmudict


# def test_dict():
#     if (ar_cmudict.dict() is None):
#         raise AssertionError('Not there')


def test_dict2():
    print(ar_cmudict.dict_stream())
    if (ar_cmudict.dict() is None):
        raise AssertionError('Not there')
