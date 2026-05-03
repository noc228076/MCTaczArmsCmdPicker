"""MC TACZ 枪械指令生成器主入口。"""

from data.gun_id import original_gun_id
from data.cmd_list import at_cmd_list
from utils import get_valid_int, print_menu

FIRE_MODES = ["AUTO", "SEMI", "BURST"]
MAX_AMMO = 2147483647


def choose_head_command() -> int | None:
    return print_menu(
        "请选择命令模式：",
        ["give（直接给予玩家）", "item（装备到指定槽位）"],
    )


def choose_target_selector() -> str | None:
    choice = print_menu(
        "请选择命令作用对象：",
        ["@a(所有玩家)", "@p(最近的玩家)", "@s(指令执行者自身)", "@r(随机玩家)", "@e(所有实体)"],
    )
    if choice is None:
        return None
    return at_cmd_list[choice - 1]


def choose_slot() -> int | None:
    while True:
        slot = get_valid_int("请输入武器放置的位置（1~9 为快捷栏，10~54 为背包）：")
        if slot is None:
            return None
        if 1 <= slot <= 54:
            return slot
        print("请输入区间为 1~54 的数字。")


def choose_weapon() -> str | None:
    names = list(original_gun_id.keys())
    while True:
        options = [f"{name}（{original_gun_id[name]}）" for name in names]
        choice = print_menu("请选择您要获取的武器：", options, columns=2)
        if choice is None:
            return None
        if 1 <= choice <= len(names):
            return original_gun_id[names[choice - 1]]
        print("请输入正确的数字。")


def choose_fire_mode() -> str | None:
    choice = print_menu("请选择开火模式：", ["全自动", "单发", "二连发"])
    if choice is None:
        return None
    return FIRE_MODES[choice - 1]


def choose_ammo_count() -> int | None:
    while True:
        ammo = get_valid_int(f"请输入初始备弹数（0~{MAX_AMMO}）：")
        if ammo is None:
            return None
        if 0 <= ammo <= MAX_AMMO:
            return ammo
        print("请输入正确的数字。")


def build_command(mode: int, selector: str, slot: int | None, gun_id: str, fire_mode: str, ammo: int) -> str:
    base_nbt = (
        f'tacz:modern_kinetic_gun{{GunId:"{gun_id}",'
        f'GunFireMode:"{fire_mode}",GunCurrentAmmoCount:{ammo}}}'
    )
    if mode == 1:
        return f"give {selector} {base_nbt}"
    return f"item replace entity {selector} container.{slot} with {base_nbt}"


def main() -> None:
    while True:
        mode = choose_head_command()
        if mode is None:
            break

        selector = choose_target_selector()
        if selector is None:
            break

        slot = choose_slot() if mode == 2 else None
        if mode == 2 and slot is None:
            break

        gun_id = choose_weapon()
        if gun_id is None:
            break

        fire_mode = choose_fire_mode()
        if fire_mode is None:
            break

        ammo = choose_ammo_count()
        if ammo is None:
            break

        print("\n" + "|" * 88)
        print(build_command(mode, selector, slot, gun_id, fire_mode, ammo))
        print("|" * 88 + "\n")


if __name__ == "__main__":
    main()
