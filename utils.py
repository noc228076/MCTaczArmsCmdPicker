"""通用输入与展示工具函数。"""


def get_valid_int(prompt: str):
    """读取整数输入；输入 q 可退出当前流程。"""
    while True:
        raw = input(prompt).strip()
        if raw.lower() == "q":
            print("欢迎下次使用本程序。")
            return None
        try:
            return int(raw)
        except ValueError:
            print("请输入正确的数字。")


def print_menu(title: str, options: list[str], columns: int = 1):
    """打印编号菜单并返回用户选择。"""
    print(title)

    if columns <= 1:
        for idx, item in enumerate(options, start=1):
            print(f"{idx}. {item}")
    else:
        rows = []
        for idx, item in enumerate(options, start=1):
            rows.append(f"{idx}. {item}")

        width = max(len(text) for text in rows) + 4
        for row_start in range(0, len(rows), columns):
            row = rows[row_start : row_start + columns]
            print("".join(cell.ljust(width) for cell in row))

    return get_valid_int("请输入您的选择（输入 q 退出）：")
