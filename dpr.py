import numpy as np
import matplotlib.pyplot as plt

target_ac = [13, 13, 13, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 19]
pb_array =  [2,  2,  2,  2,  3,  3,  3,  3,  4,  4,  4,  4,  5,  5,  5,  5,  6,  6,  6,  6]

def attack_dpr(ac, weapon_dmg, atk_mod, dmg_mod, adv=1, crit_range=1, once_per_turn_chances=1):
    rolls_array = np.arange(1, 21, 1)
    n_hit = 0
    n_crit = 0
    n_miss = 1
    for i in range(1, 20): 
        if rolls_array[i] > 20 - crit_range:
            n_crit +=1
        elif rolls_array[i]+atk_mod >= ac:
            n_hit += 1
        else:
            n_miss += 1
    if adv == np.ceil(adv):
        hit_chance = 1 - (1 - n_hit/20.0)**adv
        crit_chance = 1 - (1 - n_crit/20.0)**adv
        miss_chance = 1 - crit_chance - hit_chance
    else:
        hit_chance = (1 - (1 - n_hit/20.0)**np.floor(adv)) * (np.ceil(adv)-adv) + (1 - (1 - n_hit/20.0)**np.ceil(adv)) * (adv-np.floor(adv))
        crit_chance = (1 - (1 - n_crit/20.0)**np.floor(adv)) * (np.ceil(adv)-adv) + (1 - (1 - n_crit/20.0)**np.ceil(adv)) * (adv-np.floor(adv))
        miss_chance = 1 - crit_chance - hit_chance
    if once_per_turn_chances == 1:
        dpr_avg = (weapon_dmg*2 + dmg_mod)*crit_chance + (weapon_dmg + dmg_mod)*hit_chance
    elif once_per_turn_chances == np.ceil(once_per_turn_chances):
        crit_chance_eff = crit_chance + np.sum(miss_chance**np.arange(1,once_per_turn_chances) * crit_chance)
        hit_chance_eff = hit_chance + np.sum(miss_chance**np.arange(1,once_per_turn_chances) * hit_chance)
        dpr_avg = (weapon_dmg*2 + dmg_mod)*crit_chance_eff + (weapon_dmg + dmg_mod)*hit_chance_eff
    else:
        crit_chance_eff_1 = crit_chance + np.sum(miss_chance**np.arange(1,np.floor(once_per_turn_chances)) * crit_chance)
        hit_chance_eff_1 = hit_chance + np.sum(miss_chance**np.arange(1,np.floor(once_per_turn_chances)) * hit_chance)
        dpr_avg_1 = (weapon_dmg*2 + dmg_mod)*crit_chance_eff_1 + (weapon_dmg + dmg_mod)*hit_chance_eff_1
        crit_chance_eff_2 = crit_chance + np.sum(miss_chance**np.arange(1,np.ceil(once_per_turn_chances)) * crit_chance)
        hit_chance_eff_2 = hit_chance + np.sum(miss_chance**np.arange(1,np.ceil(once_per_turn_chances)) * hit_chance)
        dpr_avg_2 = (weapon_dmg*2 + dmg_mod)*crit_chance_eff_2 + (weapon_dmg + dmg_mod)*hit_chance_eff_2
        dpr_avg = (np.ceil(once_per_turn_chances)-once_per_turn_chances) * dpr_avg_1 + -(np.floor(once_per_turn_chances)-once_per_turn_chances) * dpr_avg_2
    return(dpr_avg)

def weapon_attack(level,AS,die,bonus=[0,0],adv=1,crit_range=1,extra_dice=0,dueling=0):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(attack_dpr(AC,die+extra_dice,PB+AS+bonus[0],AS+bonus[1]+dueling*2,adv=adv,crit_range=crit_range))

def spell_attack(level,AS,die,bonus=[0,0],adv=1,crit_range=1,extra_dice=0):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(attack_dpr(AC,die+extra_dice,PB+AS+bonus[0],bonus[1],adv=adv,crit_range=crit_range))

def nick_attack(level,AS,die=3.5,twf=0,bonus=[0,0],adv=1,crit_range=1,extra_dice=0):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(attack_dpr(AC,die+extra_dice,PB+AS+bonus[0],twf*AS+bonus[1],adv=adv,crit_range=crit_range))

def shillelagh_attack(level,AS,die=4.5,mainhand=1,twf=0,bonus=[0,0],adv=1,crit_range=1,extra_dice=0,agonizing=0,dueling=0):
    if level > 4:
        die = 5.5
    if level > 10:
        die = 6.5
    if level > 16:
        die = 7
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(attack_dpr(AC,die+extra_dice,PB+AS+bonus[0],max([mainhand,twf])*AS+bonus[1]+agonizing*AS+dueling*2,adv=adv,crit_range=crit_range))

def gwm_attack(level,AS,die=7,bonus=[0,0],adv=1,crit_range=1,extra_dice=0):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(attack_dpr(AC,die+extra_dice,PB+AS+bonus[0],AS+bonus[1]+PB,adv=adv,crit_range=crit_range))

def sneak_attack(level,AS,adv=1,crit_range=1,chances=1,rogue_lvl=None):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    if rogue_lvl == None:
        rogue_lvl = level
    ndice = np.ceil(rogue_lvl/2)
    return(attack_dpr(AC,ndice*3.5,PB+AS,0,adv=adv,crit_range=crit_range,once_per_turn_chances=chances))

def bb_attack(level,AS,die,mainhand=1,twf=0,bonus=[0,0],adv=1,crit_range=1,shillelagh=None,gwm=0,move_chance=0,extra_dice=0,agonizing=0):
    bb_dmg = 0.0
    if level > 4:
        bb_dmg = 4.5
    if level > 10:
        bb_dmg = 9
    if level > 16:
        bb_dmg = 13.5
    if shillelagh != None:
        die = 4.5
        if level > 4:
            die = 5.5
        if level > 10:
            die = 6.5
        if level > 16:
            die = 7
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(attack_dpr(AC,die+bb_dmg+extra_dice,PB+AS+bonus[0],max([mainhand,twf])*AS+bonus[1]+AS*agonizing+(bb_dmg + 4.5 + AS*agonizing)*move_chance+gwm*PB,adv=adv,crit_range=crit_range))

def ts_attack(level,AS,die,mainhand=1,twf=0,bonus=[0,0],adv=1,crit_range=1,shillelagh=None,gwm=0,extra_dice=0):
    bb_dmg = 0.0
    if level > 4:
        bb_dmg = 3.5
    if level > 10:
        bb_dmg = 7
    if level > 16:
        bb_dmg = 10.5
    if shillelagh != None:
        die = 4.5
        if level > 4:
            die = 5.5
        if level > 10:
            die = 6.5
        if level > 16:
            die = 7
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(attack_dpr(AC,die+bb_dmg+extra_dice,PB+AS+bonus[0],max([mainhand,twf])*AS+bonus[1]+gwm*PB,adv=adv,crit_range=crit_range))

def once_per_turn_rider(level,AS,die,adv=1,crit_range=1,chances=1,bonus=[0,0]):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(attack_dpr(AC,die,PB+AS+bonus[0],bonus[1],adv=adv,crit_range=crit_range,once_per_turn_chances=chances))

def extra_dice(level,AS,die,adv=1,crit_range=1,chances=1):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(chances*attack_dpr(AC,die,PB+AS,0,adv=adv,crit_range=crit_range))

def eb_attack(level,AS,adv=1,crit_range=1,agonizing=0,extra_dice=0.0,bonus=[0,0]):
    beams = 1
    if level > 4:
        beams = 2
    if level > 10:
        beams = 3
    if level > 16:
        beams = 4
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    die = 5.5 + extra_dice
    return(beams*attack_dpr(AC,die,PB+AS+bonus[0],agonizing*AS+bonus[1],adv=adv,crit_range=crit_range))

def attack_cantrip(level,AS,die,adv=1,crit_range=1,bonus=[0,0],extra_dice=0):
    ndice = 1
    if level > 4:
        ndice = 2
    if level > 10:
        ndice = 3
    if level > 16:
        ndice = 4
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    die_eff = ndice*die + extra_dice
    return(attack_dpr(AC,die_eff,PB+AS+bonus[0],bonus[1],adv=adv,crit_range=crit_range))

def summon_beast(level,AS,slot_level=2,adv=1,crit_range=1):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(np.floor(slot_level/2)*attack_dpr(AC,4.5,PB+AS,4+slot_level,adv=adv,crit_range=crit_range))

def summon_fey(level,AS,slot_level=3,adv=1,crit_range=1):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(np.floor(slot_level/2)*attack_dpr(AC,7,PB+AS,3+slot_level,adv=adv,crit_range=crit_range))

def summon_undead(level,AS,slot_level=3,die=4.5,adv=1,crit_range=1):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    return(np.floor(slot_level/2)*attack_dpr(AC,die,PB+AS,3+slot_level,adv=adv,crit_range=crit_range))

def ma_attack(level,AS,monk_level=None,bonus=[0,0],adv=1,crit_range=1,nick=0):
    global target_ac, pb_array
    AC = target_ac[level-1]
    PB = pb_array[level-1]
    if monk_level == None: monk_level = level
    die = 3.5
    if monk_level > 4: die = 4.5
    if monk_level > 10: die = 5.5
    if monk_level > 16: die = 6.5
    dmg = (1-nick)*AS
    return(attack_dpr(AC,die,PB+AS+bonus[0],dmg+bonus[1],adv=adv,crit_range=crit_range))

if 1:
    target =np.array([9.6,10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6,25.8,27.1,28.3,29.6,33.3])
    high =  np.array([19.2,21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2,51.7,54.2,56.7,59.2,66.7])
    index = np.array([0,1,2,3,4,5, 6, 7, 8, 9,10,11,12,13,14,15,16,17])
    level = np.array([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    AS_1 =  np.array([3,4,4,4,4,4,4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5]) # Paladin DW
    AS_2 =  np.array([3,4,4,4,4,5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) # GWM Greataxe Champion
    AS_3 =  np.array([3,4,4,4,4,5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) # Hex EB+AB Warlock
    AS_4 =  np.array([3,4,4,4,4,5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) # Artillerist Arti +1 Weapon
    dpr_1 = np.zeros(np.size(level))
    dpr_1b = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    dpr_4 = np.zeros(np.size(level))
    cantrip_chance = 0.8
    for i in range(1):
        dpr_1[i]=(weapon_attack(level[i],AS_1[i],3.5,extra_dice=2.5) + 
                  weapon_attack(level[i],AS_1[i],2.5,extra_dice=2.5,adv=1.5) )# vex+nick
        dpr_1b[i]=(weapon_attack(level[i],AS_1[i],3.5,) + 
                  weapon_attack(level[i],AS_1[i],2.5,adv=1.5) )# vex+nick
        dpr_2[i]=weapon_attack(level[i],AS_2[i],7.75,crit_range=2) # greataxe with GWF (modified)
        dpr_3[i]=eb_attack(level[i],AS_3[i],extra_dice=3.5,agonizing=1) # EB+Hex
        dpr_4[i]=(weapon_attack(level[i],AS_4[i]+1,5.5) +
                  spell_attack(level[i],AS_4[i],9) )# Musket+1 and force ballista
    for i in range(1,2):
        dpr_1[i]=(weapon_attack(level[i],AS_1[i],4.5,extra_dice=2.5) + 
                  weapon_attack(level[i],AS_1[i],2.5,extra_dice=2.5,adv=1.5) + 
                  2/3*weapon_attack(level[i],AS_1[i],2.5,extra_dice=2.5) ) # vex+nick
        dpr_1b[i]=(weapon_attack(level[i],AS_1[i],4.5) + 
                  weapon_attack(level[i],AS_1[i],2.5,adv=1.5) + 
                  weapon_attack(level[i],AS_1[i],2.5) ) # vex+nick
        dpr_2[i]=(gwm_attack(level[i],AS_2[i],7.75,crit_range=2) + 
                  0.2*weapon_attack(level[i],AS_2[i],7.75,crit_range=2) )# greataxe with GWF + GWM
        dpr_3[i]=eb_attack(level[i],AS_3[i],extra_dice=3.5,agonizing=1) # EB+Hex
        dpr_4[i]=(weapon_attack(level[i],AS_4[i]+1,5.5) +
                  spell_attack(level[i],AS_4[i],9) )# Musket+1 and force ballista
    for i in range(2,3):
        dpr_1[i]=(weapon_attack(level[i],AS_1[i],4.5,extra_dice=2.5) + 
                  weapon_attack(level[i],AS_1[i],4.5,extra_dice=2.5,adv=1.5) + 
                  weapon_attack(level[i],AS_1[i],2.5,extra_dice=2.5,adv=1.5) + 
                  3/4*weapon_attack(level[i],AS_1[i],2.5) ) # vex+nick
        dpr_1b[i]=(weapon_attack(level[i],AS_1[i],4.5) + 
                  weapon_attack(level[i],AS_1[i],4.5,adv=1.5) + 
                  weapon_attack(level[i],AS_1[i],2.5,adv=1.5) + 
                  weapon_attack(level[i],AS_1[i],2.5) ) # vex+nick
        dpr_2[i]=(2*gwm_attack(level[i],AS_2[i],7.75,crit_range=2) + 
                  0.2*weapon_attack(level[i],AS_2[i],7.75,crit_range=2) )# greataxe with GWF + GWM
        dpr_3[i]=eb_attack(level[i],AS_3[i],extra_dice=3.5,agonizing=1) # EB+Hex
        dpr_4[i]=(2*weapon_attack(level[i],AS_4[i]+1,5.5) +
                  spell_attack(level[i],AS_4[i],9) )# Musket+1 and force ballista

    lvl_range = level < 6
    plt.plot(level[lvl_range],dpr_1[lvl_range],'o-', label='DW Paladin Favor')
    plt.plot(level[lvl_range],dpr_1b[lvl_range],'o-', label='DW Paladin no Favor')
    plt.plot(level[lvl_range],dpr_2[lvl_range],'o-', label='GWM+GWF Greataxe Champ')
    plt.plot(level[lvl_range],dpr_3[lvl_range],'o-', label='EB+AB+Hex')
    plt.plot(level[lvl_range],dpr_4[lvl_range],'o-', label='Artillerist')
    plt.plot(level[lvl_range],target[lvl_range],'--')
    plt.plot(level[lvl_range],high[lvl_range],'--')
    plt.legend()
    plt.show()