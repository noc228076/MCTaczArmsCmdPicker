#获取游戏内得到[tacz]永恒枪械工坊：零的枪械的命令
#give命令示例：/give @p tacz:modern_kinetic_gun{GunId:"lrl:m4a1_zero",GunFireMode:"AUTO",GunCurrentAmmoCount:30,AttachmentMUZZLE:{id:"tacz:attachment",Count:1b,tag:{AttachmentId:"tacz:muzzle_silencer_knight_qd"}}}
#item命令示例：item replace entity @p container.1 with tacz:modern_kinetic_gun{GunId:"tacz:ak47",GunFireMode:"AUTO",GunCurrentAmmoCount:30}
from data.gun_id import original_gun_id
from data.cmd_list import at_cmd_list
from utils import get_valuable_num

head_command = ""
at_command = ""
gun_position = ""
gun_class_command = ""
gun_fire_mode = ""
gun_current_ammo_count = ""
gun_accessories = ""

#获取命令头
while True:
    print("请选择命令模式：\n" \
    "1.give（直接给予玩家）     2.item（装备到指定槽位）")
    head_cmd = get_valuable_num("请输入您的选择：")
    if head_cmd == 1:
        head_command = "give"
    elif head_cmd == 2:
        head_command = "item replace entity"
    elif head_cmd is None:
        break

    #获取命令作用对象
    while True:
        print("""请选择命令作用对象：
1.@a(所有玩家)   2.@p(最近的玩家)   3.@s(指令执行者自身)   4.@r(随机玩家)   5.@e(所有实体)""")
        at_cmd = get_valuable_num("请输入您的选择")
        if at_cmd is None:
            break
        elif at_cmd in range(1,6):
            at_command = at_cmd_list[at_cmd-1]
            break
        else:
            print("请输入区间为1~5的数字。")
            continue
    if at_cmd is None:
        break

    #item命令需获得武器放置位置
    if head_cmd == 2:
        while True:
            print("请输入武器放置的位置，1~9为快捷栏，10~54为背包内。")
            weapon_position = get_valuable_num("请输入放置的位置：")
            if weapon_position is None:
                break
            elif 0 <= weapon_position <= 54:
                gun_position = weapon_position
                break
            else:
                 print("请输入区间为1~54的数字。")
            continue
        if weapon_position is None:
            break

    #获取武器
    while True:
        print("请选择您要获取的武器：")
        weapon_list = ""
        i = 1
        for weapon in original_gun_id.keys():
            if i % 10 == 0:
                gun_list = f"{i}. {weapon}\n"
            else:
                gun_list = f"{i}. {weapon}   "
            weapon_list += gun_list
            i += 1
        print(weapon_list)
        gun_class_cmd = get_valuable_num("请输入您的选择：")
        if gun_class_cmd is None:
            break
        elif gun_class_cmd in range(1,len(original_gun_id) + 1):
            gun_class_command = list(original_gun_id.values())[gun_class_cmd - 1]
            break
        else:
            print("请输入正确的数字。")
            continue
    if gun_class_cmd is None:
        break

    #获取开火模式
    gun_fire_mode_list = ['AUTO','SEMI','BURST']
    while True:
        print("""请选择开火模式：
1.全自动   2.单发   3.二连发""")
        gun_fire_mode_cmd = get_valuable_num("请输入您的选择：")
        if gun_fire_mode_cmd is None:
            break
        elif gun_fire_mode_cmd in range(1,4):
            gun_fire_mode = gun_fire_mode_list[gun_fire_mode_cmd - 1]
            break
        else:
            print("请输入正确的数字。")
            continue
    if gun_fire_mode_cmd is None:
        break

    #获取初始备弹数
    while True:
        print("请选择武器初始备弹数（可设置的子弹数量最大值为2147483647）:")
        ammo_count = get_valuable_num("请输入初始备弹数：")
        if ammo_count is None:
            break
        elif 0 <= ammo_count <= 2147483647:
            gun_current_ammo_count = ammo_count
            break
        else:
            print("请输入正确的数字。")
            continue
    if ammo_count is None:
        break

    #获取配件信息


    #组装NBT命令
    if head_cmd == 1:   #获取give命令
        nbt_cmd = f'{head_command} {at_command} tacz:modern_kinetic_gun{{GunId:"{gun_class_command}",GunFireMode:"{gun_fire_mode}",GunCurrentAmmoCount:{gun_current_ammo_count}}}'
    elif head_cmd == 2:   #获取item命令
        nbt_cmd = f'{head_command} {at_command} container.{gun_position} with tacz:modern_kinetic_gun{{GunId:"{gun_class_command}",GunFireMode:"{gun_fire_mode}",GunCurrentAmmoCount:{gun_current_ammo_count}}}'
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    print(nbt_cmd,"\n")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")