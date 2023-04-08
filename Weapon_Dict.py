class Weapon:
    def __init__(self, Name_cn:str, Group:str, Auto=False, MaxAmmoDigits=2, Bps=1):
        self.Auto = Auto#全自动
        self.MaxAmmoDigits=MaxAmmoDigits#最大弹药位数
        self.Name = Name_cn#名称
        self.Group = Group#族: r, sh, p, sn, lmg, smg, m
        self.Bps = Bps#Bullets per shoot
wp_3030 = Weapon('30-30', 'm', False, 2)
wp_car = Weapon('CAR', 'smg', True, 2)
wp_eva8 = Weapon('EVA-8', 'sh', True, 1)
wp_g7 = Weapon('G7侦查枪', 'm', False, 2)
wp_lstar = Weapon('L-STAR能量机枪', 'lmg', True, 3)
wp_p2020 = Weapon('P2020手枪', 'p', False, 2)
wp_r99 = Weapon('R-99冲锋枪', 'smg', True, 2)
wp_r301 = Weapon('R-301卡宾枪', 'r', True, 2)
wp_mastiff = Weapon('敖犬霰弹枪', 'sh', False, 1)
wp_rampage = Weapon('暴走', 'lmg', True, 2)
wp_bocek = Weapon('波塞克', 'm', False, 2)
wp_chargerifle = Weapon('充能步枪', 'sn', False, 1, 2)
wp_volt = Weapon('电能冲锋枪', 'smg', True, 2)
wp_wingman = Weapon('辅助手枪', 'p', False, 2)
wp_havoc = Weapon('哈沃克步枪', 'r', True, 2)
wp_peacekeeper = Weapon('和平捍卫者霰弹枪', 'sh', False, 1)
wp_hemlock = Weapon('赫姆洛克突击步枪', 'r', False, 2)
wp_vantagesniper = Weapon('狙击目标', None, False, 1)
wp_kraber = Weapon('克雷贝尔狙击枪', 'sn', False, 1)
wp_prowler = Weapon('猎兽冲锋枪', 'smg', False, 2)
wp_mozambique = Weapon('莫桑比克', 'sh', False, 1)
wp_spitfire = Weapon('喷火轻机枪', 'lmg', True, 2)
wp_flatline = Weapon('平行步枪', 'r', True, 2)
wp_tripletake = Weapon('三重式狙击枪', 'm', False, 2, 3)
wp_sentinel = Weapon('哨兵狙击步枪', 'sn', False, 1)
wp_longbow = Weapon('长弓', 'sn', False, 2)
wp_devotion = Weapon('专注轻机枪', 'lmg', True, 2)
wp_alternator = Weapon('转换者冲锋枪', 'smg', True, 2)
wp_sheila = Weapon('转轮机枪', None, True, 3)
wp_nemesis = Weapon('复仇女神', 'r', True, 2)
wp_re45 = Weapon('RE-45自动手枪', 'p', True, 2)
Dict_Weapon = {
    '30-30':wp_3030,
    'CAR':wp_car,
    'EVA-8':wp_eva8,
    'G7侦查枪':wp_g7,
    'L-STAR能量机枪':wp_lstar,
    'P2020手枪':wp_p2020,
    'RE-45自动手枪':wp_re45,
    'R-99冲锋枪':wp_r99,
    'R-301卡宾枪':wp_r301,
    '敖犬霰弹枪':wp_mastiff,
    '暴走':wp_rampage,
    '波塞克':wp_bocek,
    '充能步枪':wp_chargerifle,
    '电能冲锋枪':wp_volt,
    '辅助手枪':wp_wingman,
    '哈沃克步枪':wp_havoc,
    '和平捍卫者霰弹枪':wp_peacekeeper,
    '赫姆洛克突击步枪':wp_hemlock,
    '狙击目标':wp_vantagesniper,
    '克雷贝尔狙击枪':wp_kraber,
    '猎兽冲锋枪':wp_prowler,
    '莫桑比克':wp_mozambique,
    '喷火轻机枪':wp_spitfire,
    '平行步枪':wp_flatline,
    '三重式狙击枪':wp_tripletake,
    '哨兵狙击步枪':wp_sentinel,
    '长弓':wp_longbow,
    '专注轻机枪':wp_devotion,
    '转换者冲锋枪':wp_alternator,
    '转轮机枪':wp_sheila,
    '复仇女神':wp_nemesis
}
