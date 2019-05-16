def test_dict():
    d = {}
    print("1", d)
    d.update({"test": 1})
    print("2", d)
    assert d == {"test": 1}
    d.update({"test": {"test2": 1}})
    print("3", d)
    assert d == {'test': {'test2': 1}}


def test_list():
    l = [5, 4, 3, 2, 1]
    l.sort()
    assert l == [1, 2, 3, 4, 5]
    print(l)
    l.append(4)
    assert l == [1, 2, 3, 4, 5, 4]
    print(l)

def test_2019_05_20():
    # today is study python class
    class A:
        pass
    print(A())
