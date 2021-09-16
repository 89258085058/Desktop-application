

def test_add_group(app):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group("my group")
    new_list = app.groups.get_group_list()
    old_list.append("my group")
    assert sorted(old_list) == sorted(new_list)


def test_add_group_with_generator(app, xlsx_groups):
    group = xlsx_groups
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    assert len(old_list) + 1 == len(new_list)
    old_list.append(group)
    assert sorted(old_list) == sorted(new_list)