from fastapi import APIRouter, HTTPException, status, Response
from ..schemas import MenuCreate, MenuOut
from ..service import create_menu, get_menus, get_menu_by_id

router = APIRouter(prefix="/api/menu", tags=["Menu"])


@router.post("", response_model=MenuOut, status_code=status.HTTP_201_CREATED)
def create(menu: MenuCreate, response: Response):
    new_menu = create_menu(menu)

    response.headers["Location"] = f"/api/menu/{new_menu.id}"

    return new_menu


@router.get("", response_model=list[MenuOut])
def get_all(
    skip: int = 0,
    limit: int = 10,
    search: str | None = None
):
    menus = get_menus()

    if search:
        menus = [
            menu for menu in menus
            if search.lower() in menu.nama.lower()
            or search.lower() in menu.sku.lower()
        ]

    return menus[skip:skip + limit]


@router.get("/{menu_id}", response_model=MenuOut)
def get_by_id(menu_id: int):
    menu = get_menu_by_id(menu_id)

    if menu is None:
        raise HTTPException(
            status_code=404,
            detail="Menu tidak ditemukan"
        )

    return menu