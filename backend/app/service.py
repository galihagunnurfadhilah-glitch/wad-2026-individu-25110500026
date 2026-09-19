from .schemas import MenuCreate, MenuOut


menus = []
next_id = 1


def create_menu(menu: MenuCreate) -> MenuOut:
    global next_id

    new_menu = MenuOut(
        id=next_id,
        sku=menu.sku,
        nama=menu.nama,
        harga=menu.harga,
        kategori=menu.kategori,
    )

    menus.append(new_menu)
    next_id += 1

    return new_menu


def get_menus() -> list[MenuOut]:
    return menus


def get_menu_by_id(menu_id: int) -> MenuOut | None:
    for menu in menus:
        if menu.id == menu_id:
            return menu

    return None
