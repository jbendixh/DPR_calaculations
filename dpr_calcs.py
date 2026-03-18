import numpy as np
import matplotlib.pyplot as plt

if 1:
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6,25.8,27.1,28.3,29.6,33.3]
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2,51.7,54.2,56.7,59.2,66.7]
    index = [0,1,2,3,4,5, 6, 7, 8, 9,10,11,12,13,14,15,16]
    level = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    AS_1 =  [3,3,4,4,4,4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5] # Ranger 2 / Spores 4 / Ranger 5 / Spores X
    AS_2 =  [4,4,4,4,5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # GWM PAM Champion Fighter
    AS_3 =  [4,4,4,4,5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Magic Stone Spores Druid
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    cantrip_chance = 0.8
    for i in range(1):
        dpr_1[i]=weapon_attack(level[i],AS_1[i],7,adv=1.5) + weapon_attack(level[i],AS_1[i],7) # vex+nick+HM
        dpr_2[i]=weapon_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
        dpr_3[i]=weapon_attack(level[i],AS_3[i],3.5)
    for i in range(1,2):
        dpr_1[i]=weapon_attack(level[i],AS_1[i],7,adv=1.5) + weapon_attack(level[i],AS_1[i],7) # vex+nick+Spores
        dpr_2[i]=(2*weapon_attack(level[i],AS_2[i],5.5,crit_range=2) + 
                  weapon_attack(level[i],AS_2[i],2.5,crit_range=2))
        dpr_3[i]=(3*weapon_attack(level[i],AS_3[i],3.5) + 
                  attack_cantrip(level[i],AS_3[i],4.5)) # 3 skellies/zombies magic stone + starry wisp
    for i in range(2,3):
        dpr_1[i]=weapon_attack(level[i],AS_1[i],7,adv=1.5) + weapon_attack(level[i],AS_1[i],7) + 3/4*weapon_attack(level[i],AS_1[i],3.5+4.5,adv=1.5) # vex+nick+DW+Spores
        dpr_2[i]=2*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
        dpr_3[i]=(3*weapon_attack(level[i],AS_3[i],3.5) + 
                  attack_cantrip(level[i],AS_3[i],4.5)) # 3 skellies/zombies magic stone + starry wisp
    for i in range(3,5):
        dpr_1[i]=(weapon_attack(level[i],AS_1[i],7,adv=1.5) + 
                  weapon_attack(level[i],AS_1[i],7) + 
                  3/4*weapon_attack(level[i],AS_1[i],3.5+4.5,adv=1.5) +
                  once_per_turn_rider(level[i],AS_1[i],2.5,chances=2.75))# vex+nick+DW+Spores
        dpr_2[i]=2*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
        dpr_3[i]=(3*weapon_attack(level[i],AS_3[i],3.5,bonus=[0,AS_3[i]]) + 
                  attack_cantrip(level[i],AS_3[i],4.5,bonus=[0,AS_3[i]])) # 3 skellies/zombies magic stone + starry wisp (both with fury)
    for i in range(5,7):
        dpr_1[i]=(weapon_attack(level[i],AS_1[i],7,adv=1.5) + 
                  weapon_attack(level[i],AS_1[i],7) + 
                  (1+3/4)*weapon_attack(level[i],AS_1[i],3.5+4.5,adv=1.5) +
                  once_per_turn_rider(level[i],AS_1[i],2.5,chances=3.75))# vex+nick+DW+Spores
        dpr_2[i]=2*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
        dpr_3[i]=(3*weapon_attack(level[i],AS_3[i],3.5,bonus=[0,AS_3[i]]) + 
                  attack_cantrip(level[i],AS_3[i],4.5,bonus=[0,AS_3[i]])) # 3 skellies/zombies magic stone + starry wisp (both with fury)
    for i in range(7,8):
        dpr_1[i]=weapon_attack(level[i],AS_1[i],7,adv=1.5) + weapon_attack(level[i],AS_1[i],7) + (1+3/4)*weapon_attack(level[i],AS_1[i],3.5+4.5,adv=1.5) # EA+vex+nick+DW+Spores
        dpr_2[i]=3*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
        dpr_3[i]=(3*weapon_attack(level[i],AS_3[i],3.5,bonus=[0,AS_3[i]]) + 
                  attack_cantrip(level[i],AS_3[i],4.5,bonus=[0,AS_3[i]])) # 3 skellies/zombies magic stone + starry wisp (both with fury)
    for i in range(8,11):
        dpr_1[i]=(weapon_attack(level[i],AS_1[i],7,adv=1.5) + 
                  weapon_attack(level[i],AS_1[i],7) + 
                  (1+3/4)*weapon_attack(level[i],AS_1[i],3.5+4.5,adv=1.5) +
                  once_per_turn_rider(level[i],AS_1[i],2.5,chances=3.75))# vex+nick+DW+Spores
        dpr_2[i]=3*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
        dpr_3[i]=(3*weapon_attack(level[i],AS_3[i],3.5,bonus=[0,AS_3[i]]) + 
                  attack_cantrip(level[i],AS_3[i],4.5,bonus=[0,AS_3[i]])) # 3 skellies/zombies magic stone + starry wisp (both with fury)
    for i in range(11,16):
        dpr_1[i]=(weapon_attack(level[i],AS_1[i],7,adv=1.5) + 
                  weapon_attack(level[i],AS_1[i],7) + 
                  (1+3/4)*weapon_attack(level[i],AS_1[i],3.5+4.5,adv=1.5) +
                  once_per_turn_rider(level[i],AS_1[i],4.5+2.5,chances=3.75))# vex+nick+DW+Spores
        dpr_2[i]=3*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
        dpr_3[i]=(3*weapon_attack(level[i],AS_3[i],3.5,bonus=[0,AS_3[i]]) + 
                  attack_cantrip(level[i],AS_3[i],4.5,bonus=[0,AS_3[i]])) # 3 skellies/zombies magic stone + starry wisp (both with fury)
    for i in range(16,17):
        dpr_1[i]=(weapon_attack(level[i],AS_1[i],7,adv=1.5) + 
                  weapon_attack(level[i],AS_1[i],7) + 
                  (1+3/4)*weapon_attack(level[i],AS_1[i],3.5+4.5,adv=1.5) +
                  once_per_turn_rider(level[i],AS_1[i],2*4,5+2.5,chances=3.75))# vex+nick+DW+Spores
        dpr_2[i]=3*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
        dpr_3[i]=(3*weapon_attack(level[i],AS_3[i],3.5,bonus=[0,AS_3[i]]) + 
                  attack_cantrip(level[i],AS_3[i],4.5,bonus=[0,AS_3[i]])) # 3 skellies/zombies magic stone + starry wisp (both with fury)

    plt.plot(level,dpr_1,'o-', label='SporesRangerDW')
    plt.plot(level,dpr_2,'o-', label='PAM+GWM Champ')
    plt.plot(level,dpr_3,'o-', label='Spore Magic Stone Summoner')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 1:
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6,25.8,27.1,28.3,29.6,33.3]
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2,51.7,54.2,56.7,59.2,66.7]
    index = [0,1,2,3,4,5, 6, 7, 8, 9,10,11,12,13,14,15,16]
    level = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    AS_1 =  [3,3,4,4,4,4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Lightning Lure EK
    AS_2 =  [4,4,4,4,5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # GWM PAM Champion Fighter
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    cantrip_chance = 0.8
    for i in range(1):
        dpr_1[i]=shillelagh_attack(level[i],AS_1[i]) + weapon_attack(level[i],AS_2[i],2.5,adv=1.5)
        dpr_2[i]=weapon_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(1,2):
        dpr_1[i]=shillelagh_attack(level[i],AS_1[i]) + weapon_attack(level[i],AS_2[i],2.5,adv=1.5) + cantrip_chance*(2*4.5 + shillelagh_attack(level[i],AS_1[i]))
        dpr_2[i]=2*weapon_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(2,5):
        dpr_1[i]=shillelagh_attack(level[i],AS_1[i]) + weapon_attack(level[i],AS_2[i],2.5,adv=1.5) + cantrip_chance*(2*4.5 + shillelagh_attack(level[i],AS_1[i]))
        dpr_2[i]=2*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(5,7):
        dpr_1[i]=2*shillelagh_attack(level[i],AS_1[i]) + weapon_attack(level[i],AS_2[i],2.5,adv=2) + bb_attack(level[i],AS_2[i],5.5,shillelagh=1,adv=2,move_chance=0.5) + 3.5
        dpr_2[i]=2*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(7,11):
        dpr_1[i]=3*shillelagh_attack(level[i],AS_1[i]) + weapon_attack(level[i],AS_2[i],2.5,adv=2) + bb_attack(level[i],AS_2[i],5.5,shillelagh=1,adv=2,move_chance=0.5) + 3.5
        dpr_2[i]=3*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(11,16):
        dpr_1[i]=3*shillelagh_attack(level[i],AS_1[i]) + weapon_attack(level[i],AS_2[i],2.5,adv=2) + bb_attack(level[i],AS_2[i],5.5,shillelagh=1,adv=2,move_chance=0.5) + 3.5
        dpr_2[i]=3*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(16,17):
        dpr_1[i]=4*shillelagh_attack(level[i],AS_1[i]) + weapon_attack(level[i],AS_2[i],2.5,adv=2) + bb_attack(level[i],AS_2[i],5.5,shillelagh=1,adv=2,move_chance=0.5) + 3.5
        dpr_2[i]=4*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)

    plt.plot(level,dpr_1,'o-', label='Shill LL EK')
    plt.plot(level,dpr_2,'o-', label='PAM+GWM Champ')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 1:
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6,25.8,27.1,28.3,29.6,33.3]
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2,51.7,54.2,56.7,59.2,66.7]
    index = [0,1,2,3,4,5, 6, 7, 8, 9,10,11,12,13,14,15,16]
    level = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    AS_1 =  [3,3,4,4,4,4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Warlock 2 Draconic Sorcerer X
    AS_2 =  [4,4,4,4,5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # GWM PAM Champion Fighter
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))

    for i in range(1):
        dpr_1[i]=(1+2/3)*bb_attack(level[i],AS_1[i],4.5,move_chance=0,agonizing=1,adv=2)
        dpr_2[i]=weapon_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(1,2):
        dpr_1[i]=(1+2/3)*bb_attack(level[i],AS_1[i],4.5,move_chance=0,agonizing=1,adv=2)
        dpr_2[i]=2*weapon_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(2,4):
        dpr_1[i]=(1+2/3)*bb_attack(level[i],AS_1[i],4.5,move_chance=0,agonizing=1,adv=2)
        dpr_2[i]=2*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(4,7):
        dpr_1[i]=(1+2/3)*bb_attack(level[i],AS_1[i],4.5,move_chance=0,agonizing=1,adv=2,bonus=[0,AS_1[i]])
        dpr_2[i]=2*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(7,11):
        dpr_1[i]=(1+2/3)*bb_attack(level[i],AS_1[i],4.5,move_chance=0,agonizing=1,adv=2,bonus=[0,AS_1[i]])
        dpr_2[i]=3*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(11,16):
        dpr_1[i]=(1+2/3)*bb_attack(level[i],AS_1[i],4.5,move_chance=0,agonizing=1,adv=2,bonus=[0,AS_1[i]])
        dpr_2[i]=3*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)
    for i in range(16,17):
        dpr_1[i]=(1+2/3)*bb_attack(level[i],AS_1[i],4.5,move_chance=0,agonizing=1,adv=2,bonus=[0,AS_1[i]])
        dpr_2[i]=4*gwm_attack(level[i],AS_2[i],5.5,crit_range=2) + weapon_attack(level[i],AS_2[i],2.5,crit_range=2)

    plt.plot(level,dpr_1,'o-', label='Sorc Gish')
    plt.plot(level,dpr_2,'o-', label='PAM+GWM Champ')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 1:
    # Soul Knife Barb
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6,25.8,27.1,28.3,29.6,33.3]
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2,51.7,54.2,56.7,59.2,66.7]
    index = [0,1,2,3,4,5, 6, 7, 8, 9,10,11,12,13,14,15,16]
    level = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    AS_1 =  [3,3,3,4,4,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Soulknife 3 / AG 5 / Soulknife X
    AS_2 =  [3,3,3,4,4,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Soulknife 3 / Berserker 5 / Soulknife X
    AS_2b = [3,3,3,4,4,4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Soulknife 3 / Berserker 5 / Fighter 1 / Soulknife X
    AS_3 =  [3,3,3,4,4,4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Soulknife 3 / Berserker 3 / Soulknife X
    AS_3b = [4,4,4,4,4,4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Soulknife 4 / Berserker 3 / Soulknife X
    AS_4 =  [3,3,3,3,3,4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5] # Giant 6 / Fighter 1 / Giant 12 / Fighter 2 / Giant X
    AS_5 =  [3,3,3,4,4,4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Soulknife 3 / Giant 6 / Soulknife X
    AS_6 =  [3,3,3,4,4,4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_2b = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    dpr_3b = np.zeros(np.size(level))
    dpr_5 = np.zeros(np.size(level))
    dpr_6 = np.zeros(np.size(level))
    dpr_4 = np.zeros(np.size(level))
    dpr_3max = np.zeros(np.size(level))
    dpr_2max = np.zeros(np.size(level))
    b = [0,2]
    b2 = [0,4]
    for i in range(1):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,bonus=b) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b) + sneak_attack(level[i],AS_1[i],chances=1.75,rogue_lvl=3)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5,bonus=b) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b) + sneak_attack(level[i],AS_2[i],chances=1.75,rogue_lvl=3)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b) + sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=3)
        dpr_3b[i] = weapon_attack(level[i],AS_3b[i],3.5) + 3/4*weapon_attack(level[i],AS_3b[i],2.5) + sneak_attack(level[i],AS_3b[i],chances=1.5,rogue_lvl=4)
        dpr_4[i] = weapon_attack(level[i],AS_4[i],2.5,bonus=[0,2],adv=2)
        dpr_3max[i] = 3.5+AS_3[i]+2 + 3/4*(2.5+AS_3[i]+2) + 2*3.5
        dpr_2max[i] = 3.5+AS_2[i]+2 + 3/4*(2.5+AS_2[i]+2) + 2*3.5
        dpr_5[i] = weapon_attack(level[i],AS_5[i],3.5,bonus=b) + 3/4*weapon_attack(level[i],AS_5[i],2.5,bonus=b) + sneak_attack(level[i],AS_5[i],chances=1.75,rogue_lvl=3)
        dpr_6[i] = weapon_attack(level[i],AS_6[i],3.5,bonus=b) + weapon_attack(level[i],AS_6[i],2.5,bonus=b) + sneak_attack(level[i],AS_5[i],chances=1.5,rogue_lvl=3)
        # print(0.95*7+0.05*14,sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=3))
    for i in range(1,2):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=1.75,rogue_lvl=3,adv=2)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=1.75,rogue_lvl=3,adv=2)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=3,adv=2)
        dpr_3b[i] = weapon_attack(level[i],AS_3b[i],3.5,bonus=b,adv=1.5) + 3/4*weapon_attack(level[i],AS_3b[i],2.5,bonus=b,adv=1.5) + sneak_attack(level[i],AS_3b[i],chances=1.5,rogue_lvl=4,adv=1.5)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],2.5,bonus=[0,2],adv=2)
        dpr_3max[i] = 3.5+AS_3[i]+2 + 3/4*(2.5+AS_3[i]+2) + 2*3.5
        dpr_2max[i] = 3.5+AS_2[i]+2 + 3/4*(2.5+AS_2[i]+2) + 2*3.5
        dpr_5[i] = weapon_attack(level[i],AS_5[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_5[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_5[i],chances=1.75,rogue_lvl=3,adv=2)
        dpr_6[i] = weapon_attack(level[i],AS_6[i],3.5,bonus=b) + weapon_attack(level[i],AS_6[i],2.5,bonus=b) + sneak_attack(level[i],AS_5[i],chances=1.5,rogue_lvl=3)
        # print(0.9025*7+0.09755*14,sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=3,adv=2))
    for i in range(2,3):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=1.75,rogue_lvl=3,adv=2)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=1.75,rogue_lvl=3,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=1.75,adv=2)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3[i],7,chances=1.75,adv=2)
        dpr_3b[i] = weapon_attack(level[i],AS_3b[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3b[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3b[i],chances=1.75,rogue_lvl=level[i]-3,adv=2)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],2.5+3.5,bonus=[0,2],adv=2)
        dpr_3max[i] = 3.5+AS_3[i]+2 + 3/4*(2.5+AS_3[i]+2) + 2*3.5 + np.ceil((level[i]-3)/2)*3.5
        dpr_2max[i] = 3.5+AS_2[i]+2 + 3/4*(2.5+AS_2[i]+2)+ 2*3.5 + 2*3.5
        dpr_5[i] = weapon_attack(level[i],AS_5[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_5[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_5[i],chances=1.75,rogue_lvl=3,adv=2)
        dpr_6[i] = weapon_attack(level[i],AS_6[i],3.5,bonus=b,adv=2) + weapon_attack(level[i],AS_6[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_5[i],chances=2,rogue_lvl=3,adv=2)
        # print(0.9025*np.ceil((level[i]-3)/2)*3.5+0.09755*np.ceil((level[i]-3)/2)*3.5*2,sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=level[i]-3,adv=2))
    for i in range(3,4):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=1.75,rogue_lvl=3,adv=2)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=1.75,rogue_lvl=3,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=1.75,adv=2)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3[i],7,chances=1.75,adv=2)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],2.5+3.5,bonus=[2,2],adv=2)
        dpr_3max[i] = 3.5+AS_3[i]+2 + 3/4*(2.5+AS_3[i]+2) + 2*3.5 + np.ceil((level[i]-3)/2)*3.5
        dpr_2max[i] = 3.5+AS_2[i]+2 + 3/4*(2.5+AS_2[i]+2)+ 2*3.5 + 2*3.5
        dpr_5[i] = weapon_attack(level[i],AS_5[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_5[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_5[i],chances=1.75,rogue_lvl=3,adv=2)
        dpr_6[i] = weapon_attack(level[i],AS_6[i],3.5,bonus=b,adv=2) + weapon_attack(level[i],AS_6[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_5[i],chances=2,rogue_lvl=3,adv=2)
        # print(0.9025*np.ceil((level[i]-3)/2)*3.5+0.09755*np.ceil((level[i]-3)/2)*3.5*2,sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=level[i]-3,adv=2))
    for i in range(4,5):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=2.75,rogue_lvl=level[i]-5,adv=2)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=2.75,rogue_lvl=level[i]-5,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=2.75,adv=2)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3[i],7,chances=1.75,adv=2)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],2.5+3.5,bonus=[2,2],adv=2)
        dpr_3max[i] = 3.5+AS_3[i]+2 + 3/4*(2.5+AS_3[i]+2) + 2*3.5 + np.ceil((level[i]-3)/2)*3.5
        dpr_2max[i] = 2*(3.5+AS_2[i]+2) + 3/4*(2.5+AS_2[i]+2)+ 2*3.5 + np.ceil((level[i]-5)/2)*3.5
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_5[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_5[i],chances=2.75,rogue_lvl=3,adv=2)
        dpr_6[i] = 2*weapon_attack(level[i],AS_6[i],3.5,bonus=b,adv=2) + weapon_attack(level[i],AS_6[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_5[i],chances=3,rogue_lvl=3,adv=2)
        # print(0.9025*np.ceil((level[i]-3)/2)*3.5+0.09755*np.ceil((level[i]-3)/2)*3.5*2,sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=level[i]-3,adv=2))
    dpr_2b[:5] = dpr_2[:5]
    for i in range(5,6):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=2.75,rogue_lvl=level[i]-5,adv=2)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=2.75,rogue_lvl=level[i]-5,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=2.75,adv=2)
        dpr_2b[i] = 2*weapon_attack(level[i],AS_2b[i],3.5,bonus=b2,adv=2) + 3/4*weapon_attack(level[i],AS_2b[i],2.5,bonus=b2,adv=2) + sneak_attack(level[i],AS_2[i],chances=2.75,rogue_lvl=level[i]-6,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=2.75,adv=2)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3[i],7,chances=1.75,adv=2)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],2.5+3.5,bonus=[2,2],adv=2)
        dpr_3max[i] = 3.5+AS_3[i]+2 + 3/4*(2.5+AS_3[i]+2) + 2*3.5 + np.ceil((level[i]-3)/2)*3.5
        dpr_2max[i] = 2*(3.5+AS_2[i]+2) + 3/4*(2.5+AS_2[i]+2)+ 2*3.5 + np.ceil((level[i]-5)/2)*3.5
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i],3.5+3.5,bonus=b2,adv=2) + 3/4*weapon_attack(level[i],AS_5[i],2.5+3.5,bonus=b2,adv=2) + sneak_attack(level[i],AS_5[i],chances=2.75,rogue_lvl=3,adv=2)
        dpr_6[i] = 2*weapon_attack(level[i],AS_6[i],3.5,bonus=b,adv=2) + weapon_attack(level[i],AS_6[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_5[i],chances=3,rogue_lvl=3,adv=2)
        print(0.9025*np.ceil((level[i]-3)/2)*3.5+0.09755*np.ceil((level[i]-3)/2)*3.5*2,sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=level[i]-3,adv=2))
    for i in range(5,17):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=2.75,rogue_lvl=level[i]-5,adv=2)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=2.75,rogue_lvl=level[i]-5,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=2.75,adv=2)
        dpr_2b[i] = 2*weapon_attack(level[i],AS_2b[i],3.5,bonus=b2,adv=2) + 3/4*weapon_attack(level[i],AS_2b[i],2.5,bonus=b2,adv=2) + sneak_attack(level[i],AS_2[i],chances=2.75,rogue_lvl=level[i]-6,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=2.75,adv=2)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=2.75,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3[i],7,chances=1.75,adv=2)
        dpr_3max[i] = 3.5+AS_3[i]+2 + 3/4*(2.5+AS_3[i]+2) + 2*3.5 + np.ceil((level[i]-3)/2)*3.5
        dpr_2max[i] = 2*(3.5+AS_2[i]+2) + 3/4*(2.5+AS_2[i]+2)+ 2*3.5 + np.ceil((level[i]-5)/2)*3.5
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i],3.5+3.5,bonus=b2,adv=2) + 3/4*weapon_attack(level[i],AS_5[i],2.5+3.5,bonus=b2,adv=2) + sneak_attack(level[i],AS_5[i],chances=1.75,rogue_lvl=level[i]-7,adv=2)
        dpr_6[i] = 2*weapon_attack(level[i],AS_6[i],3.5,bonus=b,adv=2) + weapon_attack(level[i],AS_6[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_5[i],chances=3,rogue_lvl=3,adv=2)
        # print(0.9025*np.ceil((level[i]-3)/2)*3.5+0.09755*np.ceil((level[i]-3)/2)*3.5*2,sneak_attack(level[i],AS_3[i],chances=1.75,rogue_lvl=level[i]-3,adv=2))
    for i in range (10,17):
        dpr_6[i] = 2*weapon_attack(level[i],AS_6[i],3.5+4.5,bonus=b,adv=2) + weapon_attack(level[i],AS_6[i],2.5+4.5,bonus=b,adv=2) + sneak_attack(level[i],AS_5[i],chances=3,rogue_lvl=level[i]-11,adv=2)
    for i in range(6,13):
        dpr_4[i] = weapon_attack(level[i],AS_4[i],2.5+2*3.5,bonus=[2,3],adv=2) + weapon_attack(level[i],AS_4[i],2.5+2*3.5+5.5,bonus=[2,3])
    for i in range(13,14):
        dpr_4[i] = weapon_attack(level[i],AS_4[i],2.5+2*3.5,bonus=[2,4],adv=2) + weapon_attack(level[i],AS_4[i],2.5+2*3.5+5.5,bonus=[2,4])
    for i in range(14,17):
        dpr_4[i] = weapon_attack(level[i],AS_4[i],2.5+2*3.5,bonus=[2,4],adv=2) + weapon_attack(level[i],AS_4[i],2.5+2*3.5+2*5.5,bonus=[2,4])
    dpr_3b[3:] = dpr_3[3:]
    # plt.plot(level,dpr_1,'o-', label='Soulknife 3 / AG 5 / Soulknife X')
    plt.plot(level,dpr_2,'o-', label='Soulknife 3 / Zerker 5 / Soulknife X')
    plt.plot(level,dpr_2b,'o-', label='Soulknife 3 / Zerker 5 / Fighter 1 / Soulknife X')
    # plt.plot(level,dpr_3,'o-', label='Soulknife 3 / Zerker 3 / Soulknife X')
    # plt.plot(level,dpr_3max*(0.9025 + 0.0975*2),'d-', label='Soulknife 3 / Zerker 3 / Soulknife X all hits')
    # plt.plot(level,dpr_2max*(0.9025 + 0.0975*2),'d-', label='Soulknife 3 / Zerker 5 / Soulknife X all hits')
    # plt.plot(level,dpr_3b,'o-', label='Soulknife 4 / Zerker 3 / Soulknife X')
    # plt.plot(level,dpr_4,'o-', label='Giant 6 / Fighter 1 / Giant X')
    plt.plot(level,dpr_5,'o-', label='Soulknife 3 / Giant 6 / Fighter 1 / Soulknife X')
    plt.plot(level,dpr_6,'o-', label='Soulknife 3 / Vengeance 11 / Soulknife X')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Martial Baselines
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [4,4,4,4,5,5, 5, 5, 5, 5] # Champion Fighter DW
    AS_2 =  [4,4,4,4,5,5, 5, 5, 5, 5] # Berserker Barbarian DW
    rage =  [2,2,2,2,2,3, 3, 3, 3, 3]
    AS_3 =  [4,4,4,4,5,5, 5, 5, 5, 5] # Assassin Rogue
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    for i in range(1):
        dpr_1[i] = 3*weapon_attack(level[i],AS_1[i],3.5,adv=2,crit_range=2)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + (1+2/3)*nick_attack(level[i],AS_2[i],adv=2,bonus=[0,rage[i]]) + once_per_turn_rider(level[i],AS_2[i],3.5*rage[i],adv=2,chances=3)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5) + 2*nick_attack(level[i],AS_3[i],adv=2) + sneak_attack(level[i],AS_3[i],chances=3) + 1/3*once_per_turn_rider(level[i],AS_3[i],0,adv=2,chances=3,bonus=[0,level[i]])
    for i in range(1,5):
        dpr_1[i] = 4*weapon_attack(level[i],AS_1[i],3.5,adv=2,crit_range=2)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + (1+2/3)*nick_attack(level[i],AS_2[i],adv=2,bonus=[0,rage[i]]) + once_per_turn_rider(level[i],AS_2[i],3.5*rage[i],adv=2,chances=4)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5) + 2*nick_attack(level[i],AS_3[i],adv=2) + sneak_attack(level[i],AS_3[i],chances=3) + 1/3*once_per_turn_rider(level[i],AS_3[i],0,adv=2,chances=3,bonus=[0,level[i]])
    for i in range(5,6):
        dpr_1[i] = 4*weapon_attack(level[i],AS_1[i],3.5,adv=2,crit_range=2)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5+5.5,bonus=[0,rage[i]]) + weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + (1+2/3)*nick_attack(level[i],AS_2[i],adv=2,bonus=[0,rage[i]]) + once_per_turn_rider(level[i],AS_2[i],3.5*rage[i],adv=2,chances=4)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5) + 2*nick_attack(level[i],AS_3[i],adv=2) + sneak_attack(level[i],AS_3[i],chances=3) + 1/3*once_per_turn_rider(level[i],AS_3[i],0,adv=2,chances=3,bonus=[0,level[i]])
    for i in range(6,7):
        dpr_1[i] = 4*weapon_attack(level[i],AS_1[i],3.5,adv=2,crit_range=2)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5+5.5,bonus=[0,rage[i]]) + weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + (1+2/3)*nick_attack(level[i],AS_2[i],adv=2,bonus=[0,rage[i]]) + 0.5*weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + once_per_turn_rider(level[i],AS_2[i],3.5*rage[i],adv=2,chances=4) 
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,adv=2) + 2*nick_attack(level[i],AS_3[i],adv=2) + sneak_attack(level[i],AS_3[i],chances=3) + 1/3*once_per_turn_rider(level[i],AS_3[i],0,adv=2,chances=3,bonus=[0,level[i]])
    for i in range(7,10):
        dpr_1[i] = 4*weapon_attack(level[i],AS_1[i],3.5,adv=2,crit_range=2) + weapon_attack(level[i],AS_1[i],3.5,crit_range=2)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5+5.5,bonus=[0,rage[i]]) + weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + (1+2/3)*nick_attack(level[i],AS_2[i],adv=2,bonus=[0,rage[i]]) + 0.5*weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + once_per_turn_rider(level[i],AS_2[i],3.5*rage[i],adv=2,chances=4)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,adv=2) + 2*nick_attack(level[i],AS_3[i],adv=2) + sneak_attack(level[i],AS_3[i],chances=3) + 1/3*once_per_turn_rider(level[i],AS_3[i],0,adv=2,chances=3,bonus=[0,level[i]])
    plt.plot(level,dpr_1,'ro-', label='Champion DW')
    plt.plot(level,dpr_2,'bo-', label='Berserker DW')
    plt.plot(level,dpr_3,'go-', label='Assassin DW')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Echo Knight
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6,25.8,27.1]
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2,51.7,54.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9,10,11,12,13]
    level = [4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    AS_1 =  [4,4,4,4,5,5, 5, 5, 5, 5, 5, 5, 5, 5] # PAM / GWM Ping Pong
    AS_2 =  [4,4,5,5,5,5, 5, 5, 5, 5, 5, 5, 5, 5] # EK 6 / AG Barb 3 / EK X
    AS_3 =  [3,3,3,3,3,4, 4, 4, 4, 5, 5, 5, 5, 5] # AG Barb 17 / EK 3
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    for i in range(1):
        dpr_1[i] = (1 + (1-0.35**1))*weapon_attack(level[i],AS_1[i],5.5) + weapon_attack(level[i],AS_1[i],2.5)
        dpr_2[i] = gwm_attack(level[i],AS_2[i],7) + 0.2*weapon_attack(level[i],AS_2[i],7)
    for i in range(1,2):
        dpr_1[i] = (2 + (1-0.35**2))*weapon_attack(level[i],AS_1[i],5.5) + weapon_attack(level[i],AS_1[i],2.5)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i],7) + 0.2*weapon_attack(level[i],AS_2[i],7)
    for i in range(2,3):
        dpr_1[i] = (2 + (1-0.35**2))*gwm_attack(level[i],AS_1[i],5.5) + weapon_attack(level[i],AS_1[i],2.5)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i],7) + 0.2*weapon_attack(level[i],AS_2[i],7)
    for i in range(3,4):
        dpr_1[i] = (2 + (1-0.35**2))*gwm_attack(level[i],AS_1[i],5.5) + weapon_attack(level[i],AS_1[i],2.5)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i],7,bonus=[0,2]) + 0.17*weapon_attack(level[i],AS_2[i],7,bonus=[0,2])
    for i in range(4,7):
        dpr_1[i] = (2 + (1-0.35**2))*gwm_attack(level[i],AS_1[i],5.5) + weapon_attack(level[i],AS_1[i],2.5)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i],7,bonus=[0,2],adv=1) + 0.17*weapon_attack(level[i],AS_2[i],7,bonus=[0,2],adv=1)
    for i in range(7,10):
        dpr_1[i] = (3 + (1-0.35**3))*gwm_attack(level[i],AS_1[i],5.5) + weapon_attack(level[i],AS_1[i],2.5)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i],7,bonus=[0,2],adv=1) + 0.17*weapon_attack(level[i],AS_2[i],7,bonus=[0,2],adv=1)
    for i in range(10,14):
        dpr_1[i] = (3 + (1-0.35**3))*gwm_attack(level[i],AS_1[i],5.5) + weapon_attack(level[i],AS_1[i],2.5)
        dpr_2[i] = 3*gwm_attack(level[i],AS_2[i],7,bonus=[0,2],adv=1) + 0.17*weapon_attack(level[i],AS_2[i],7,bonus=[0,2],adv=1)
    plt.plot(level,dpr_1,'ro-', label='Ping Pong EK')
    plt.plot(level,dpr_2,'bo-', label='AG 3 / EK 14')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 1:
    # Soul Knife Barb
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6,25.8,27.1,28.3,29.6,33.3]
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2,51.7,54.2,56.7,59.2,66.7]
    index = [0,1,2,3,4,5, 6, 7, 8, 9,10,11,12,13,14,15,16]
    level = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    AS_1 =  [3,3,3,4,4,4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Soulknife 3 / Zealot 6 / Soulknife X
    AS_2 =  [3,3,3,4,4,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Soulknife 3 / Berserker 5 / Soulknife X
    AS_3 =  [3,3,3,4,4,4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Soulknife 3 / Berserker 3 / Soulknife X
    AS_3b = [4,4,4,4,4,4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # Soulknife 4 / Berserker 3 / Soulknife X
    AS_4 =  [3,3,3,3,3,4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5] # Giant 6 / Fighter 1 / Giant 12 / Fighter 2 / Giant X
    AS_5 =  [3,3,3,3,3,4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5] # Giant 6 / Fighter 1 / Giant X
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    dpr_3b = np.zeros(np.size(level))
    dpr_4 = np.zeros(np.size(level))
    b = [0,2]
    for i in range(1):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,bonus=b) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b) + sneak_attack(level[i],AS_1[i],chances=2,rogue_lvl=3)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5,bonus=b) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b) + sneak_attack(level[i],AS_2[i],chances=2,rogue_lvl=3)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b) + sneak_attack(level[i],AS_3[i],chances=2,rogue_lvl=3)
        dpr_3b[i] = weapon_attack(level[i],AS_3b[i],3.5,bonus=b) + 3/4*weapon_attack(level[i],AS_3b[i],2.5,bonus=b) + sneak_attack(level[i],AS_3b[i],chances=2,rogue_lvl=3)
        dpr_4[i] = weapon_attack(level[i],AS_4[i],2.5,bonus=[0,2],adv=2)
    for i in range(1,2):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=2,rogue_lvl=3,adv=2)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=2,rogue_lvl=3,adv=2)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=2,rogue_lvl=3,adv=2)
        dpr_3b[i] = weapon_attack(level[i],AS_3b[i],3.5,bonus=b,adv=1.5) + 3/4*weapon_attack(level[i],AS_3b[i],2.5,bonus=b,adv=1.5) + sneak_attack(level[i],AS_3b[i],chances=2,rogue_lvl=3,adv=1.5)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],2.5,bonus=[0,2],adv=2)
    for i in range(2,3):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=2,rogue_lvl=3,adv=2) + once_per_turn_rider(level[i],AS_1[i],3.5,bonus=[0,1],chances=2,adv=2)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=2,rogue_lvl=3,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=2,adv=2)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=2,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3[i],7,chances=2,adv=2)
        dpr_3b[i] = weapon_attack(level[i],AS_3b[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3b[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3b[i],chances=2,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3b[i],7,chances=2,adv=2)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],2.5+3.5,bonus=[0,2],adv=2)
    for i in range(3,4):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=2,rogue_lvl=3,adv=2) + once_per_turn_rider(level[i],AS_1[i],3.5,bonus=[0,2],chances=2,adv=2)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=2,rogue_lvl=3,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=2,adv=2)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=2,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3[i],7,chances=2,adv=2)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],2.5+3.5,bonus=[2,2],adv=2)
    for i in range(4,5):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=3,rogue_lvl=3,adv=2) + once_per_turn_rider(level[i],AS_1[i],3.5,bonus=[0,2],chances=3,adv=2)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=3,rogue_lvl=level[i]-5,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=3,adv=2)
        dpr_3[i] = 2*weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=3,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3[i],7,chances=3,adv=2)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],2.5+3.5,bonus=[2,2],adv=2)
    for i in range(5,6):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=3,rogue_lvl=level[i]-6,adv=2) + once_per_turn_rider(level[i],AS_1[i],3.5,bonus=[0,3],chances=3,adv=2)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=3,rogue_lvl=level[i]-5,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=3,adv=2)
        dpr_3[i] = 2*weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=3,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3[i],7,chances=3,adv=2)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],2.5+3.5,bonus=[2,2],adv=2)
    for i in range(5,17):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_1[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_1[i],chances=3,rogue_lvl=level[i]-6,adv=2) + once_per_turn_rider(level[i],AS_1[i],3.5,bonus=[0,3],chances=3,adv=2)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_2[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_2[i],chances=3,rogue_lvl=level[i]-5,adv=2) + once_per_turn_rider(level[i],AS_2[i],7,chances=3,adv=2)
        dpr_3[i] = 2*weapon_attack(level[i],AS_3[i],3.5,bonus=b,adv=2) + 3/4*weapon_attack(level[i],AS_3[i],2.5,bonus=b,adv=2) + sneak_attack(level[i],AS_3[i],chances=3,rogue_lvl=level[i]-3,adv=2) + once_per_turn_rider(level[i],AS_3[i],7,chances=3,adv=2)
    for i in range(6,13):
        dpr_4[i] = weapon_attack(level[i],AS_4[i],2.5+2*3.5,bonus=[2,3],adv=2) + weapon_attack(level[i],AS_4[i],2.5+2*3.5+5.5,bonus=[2,3])
    for i in range(13,14):
        dpr_4[i] = weapon_attack(level[i],AS_4[i],2.5+2*3.5,bonus=[2,4],adv=2) + weapon_attack(level[i],AS_4[i],2.5+2*3.5+5.5,bonus=[2,4])
    for i in range(14,17):
        dpr_4[i] = weapon_attack(level[i],AS_4[i],2.5+2*3.5,bonus=[2,4],adv=2) + weapon_attack(level[i],AS_4[i],2.5+2*3.5+2*5.5,bonus=[2,4])
    dpr_3b[3:] = dpr_3[3:]
    # plt.plot(level,dpr_1,'o-', label='Soulknife 3 / Zealot 6 / Soulknife X')
    # plt.plot(level,dpr_2,'o-', label='Soulknife 3 / Zerker 5 / Soulknife X')
    plt.plot(level,dpr_3,'o-', label='Soulknife 3 / Zerker 3 / Soulknife X')
    plt.plot(level,dpr_3b,'o-', label='Soulknife 4 / Zerker 3 / Soulknife X')
    plt.plot(level,dpr_4,'o-', label='Giant 6 / Fighter 1 / Giant X')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Bladesinger Builds
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6]
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9,10,11]
    level = [4,5,6,7,8,9,10,11,12,13,14,15]
    AS_1 =  [4,4,4,4,5,5, 5, 5, 5, 5, 5, 5] # Pure Bladesinger (shillelagh staff)
    AS_2 =  [3,4,4,4,4,5, 5, 5, 5, 5, 5, 5] # Fighter 1 -> Bladesinger 10 - Fighter 2 (shillelagh dw)
    AS_3 =  [3,3,4,4,5,5, 5, 5, 5, 5, 5, 5] # PAM -> WC -> ASI (shillelagh staff duelling)
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    for i in range(2):
        dpr_1[i] = bb_attack(level[i],AS_1[i],4.5,shillelagh=1,move_chance=0.2)
        dpr_2[i] = ts_attack(level[i],AS_2[i],die=3.5) + shillelagh_attack(level[i],AS_2[i])
    for i in range(2,3):
        dpr_1[i] = bb_attack(level[i],AS_1[i],4.5,shillelagh=1,move_chance=0.2) + shillelagh_attack(level[i],AS_1[i])
        dpr_2[i] = ts_attack(level[i],AS_2[i],die=3.5) + shillelagh_attack(level[i],AS_2[i])
    for i in range(3,4):
        dpr_1[i] = 2/3*(bb_attack(level[i],AS_1[i],4.5,shillelagh=1,move_chance=0.2,extra_dice=9) + shillelagh_attack(level[i],AS_1[i],extra_dice=9))
        dpr_2[i] = ts_attack(level[i],AS_2[i],die=3.5) + 2*shillelagh_attack(level[i],AS_2[i])
    for i in range(4,5):
        dpr_1[i] = 2/3*(bb_attack(level[i],AS_1[i],4.5,shillelagh=1,move_chance=0.2,extra_dice=9) + shillelagh_attack(level[i],AS_1[i],extra_dice=9))
        dpr_2[i] = 2/3*(ts_attack(level[i],AS_2[i],die=3.5,extra_dice=9) + 2*shillelagh_attack(level[i],AS_2[i],extra_dice=9))
    for i in range(5,6):
        dpr_1[i] = 2/3*(bb_attack(level[i],AS_1[i],4.5,shillelagh=1,move_chance=0.2,extra_dice=18) + shillelagh_attack(level[i],AS_1[i],extra_dice=18))
        dpr_2[i] = 2/3*(ts_attack(level[i],AS_2[i],die=3.5,extra_dice=9) + 2*shillelagh_attack(level[i],AS_2[i],extra_dice=9))
    for i in range(6,7):
        dpr_1[i] = 2/3*(bb_attack(level[i],AS_1[i],4.5,shillelagh=1,move_chance=0.2,extra_dice=18) + shillelagh_attack(level[i],AS_1[i],extra_dice=18))
        dpr_2[i] = 2/3*(ts_attack(level[i],AS_2[i],die=3.5,extra_dice=18) + 2*shillelagh_attack(level[i],AS_2[i],extra_dice=18))
    for i in range(7,10):
        dpr_1[i] = 2/3*(bb_attack(level[i],AS_1[i],4.5,shillelagh=1,move_chance=0.2,extra_dice=18) + shillelagh_attack(level[i],AS_1[i],extra_dice=18))
        dpr_2[i] = 2/3*(ts_attack(level[i],AS_2[i],die=3.5,extra_dice=18) + 2*shillelagh_attack(level[i],AS_2[i],extra_dice=18))
    for i in range(10,11):
        dpr_1[i] = 2/3*(bb_attack(level[i],AS_1[i],4.5,bonus=[0,AS_1[i]],shillelagh=1,move_chance=0.2,extra_dice=18) + shillelagh_attack(level[i],AS_1[i],bonus=[0,AS_1[i]],extra_dice=18))
        dpr_2[i] = 2/3*(ts_attack(level[i],AS_2[i],die=3.5,extra_dice=18) + 2*shillelagh_attack(level[i],AS_2[i],extra_dice=18))
    for i in range(11,12):
        dpr_1[i] = 2/3*(bb_attack(level[i],AS_1[i],4.5,bonus=[0,AS_1[i]],shillelagh=1,move_chance=0.2,extra_dice=18) + shillelagh_attack(level[i],AS_1[i],bonus=[0,AS_1[i]],extra_dice=18))
        dpr_2[i] = 2/3*(ts_attack(level[i],AS_2[i],bonus=[0,AS_1[i]],die=3.5,extra_dice=18) + 2*shillelagh_attack(level[i],AS_2[i],bonus=[0,AS_1[i]],extra_dice=18))
    plt.plot(level,dpr_1,'ro-', label='Shill Staff')
    plt.plot(level,dpr_2,'bo-', label='Shill DW + TS')
    # plt.plot(level,dpr_3,'go-', label='Shill Duelling')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()


if 0:
    # EK Builds
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6]
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9,10,11]
    level = [4,5,6,7,8,9,10,11,12,13,14,15]
    AS_1 =  [4,4,4,4,4,4, 4, 4, 5, 5, 5, 5] # PAM -> WC -> GWM -> MS (GWM PAM)
    AS_2 =  [3,3,4,4,5,5, 5, 5, 5, 5, 5, 5] # DW -> WC -> ASI (shillelagh club+scimitar ts)
    AS_3 =  [3,3,4,4,5,5, 5, 5, 5, 5, 5, 5] # PAM -> WC -> ASI (shillelagh staff duelling)
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    for i in range(1):
        dpr_1[i] = bb_attack(level[i],AS_1[i],5.5,move_chance=0.4) + weapon_attack(level[i],AS_1[i],2.5)
        dpr_2[i] = (1+2/3)*shillelagh_attack(level[i],AS_2[i]) + weapon_attack(level[i],3,3.5)
        dpr_3[i] = shillelagh_attack(level[i],AS_3[i],bonus=[0,2]) + 2/3*weapon_attack(level[i],AS_3[i],2.5,bonus=[0,2])
    for i in range(1,4):
        dpr_1[i] = bb_attack(level[i],AS_1[i],5.5,move_chance=0.4) + weapon_attack(level[i],AS_1[i],5.5) + weapon_attack(level[i],AS_1[i],2.5)
        dpr_2[i] = (2+2/3)*shillelagh_attack(level[i],AS_2[i]) + ts_attack(level[i],AS_2[i],3.5)
        dpr_3[i] = bb_attack(level[i],AS_3[i],5.5,move_chance=0.4,shillelagh=1,bonus=[0,2]) + shillelagh_attack(level[i],AS_3[i],bonus=[0,2]) + 2/3*weapon_attack(level[i],AS_3[i],2.5,bonus=[0,2])
    for i in range(4,7):
        dpr_1[i] = bb_attack(level[i],AS_1[i],5.5,move_chance=0.4,gwm=1) + gwm_attack(level[i],AS_1[i],die=5.5) + (19/20)**2*gwm_attack(level[i],AS_1[i],die=2.5) + (1-(19/20)**2)*gwm_attack(level[i],AS_1[i],die=5.5)
        dpr_2[i] = (2+2/3)*shillelagh_attack(level[i],AS_2[i]) + ts_attack(level[i],AS_2[i],3.5)
        dpr_3[i] = bb_attack(level[i],AS_3[i],5.5,move_chance=0.4,shillelagh=1,bonus=[0,2]) + shillelagh_attack(level[i],AS_3[i],bonus=[0,2]) + 2/3*weapon_attack(level[i],AS_3[i],2.5,bonus=[0,2])
    for i in range(7,12):
        dpr_1[i] = bb_attack(level[i],AS_1[i],5.5,move_chance=0.4,gwm=1) + 2*gwm_attack(level[i],AS_1[i],die=5.5) + (19/20)**3*gwm_attack(level[i],AS_1[i],die=2.5) + (1-(19/20)**3)*gwm_attack(level[i],AS_1[i],die=5.5)
        dpr_2[i] = (3+2/3)*shillelagh_attack(level[i],AS_2[i]) + ts_attack(level[i],AS_2[i],3.5)
        dpr_3[i] = bb_attack(level[i],AS_3[i],5.5,move_chance=0.4,shillelagh=1,bonus=[0,2]) + 2*shillelagh_attack(level[i],AS_3[i],bonus=[0,2]) + 2/3*weapon_attack(level[i],AS_3[i],2.5,bonus=[0,2])
    plt.plot(level,dpr_1,'ro-', label='PAM GWM')
    plt.plot(level,dpr_2,'bo-', label='Shill DW + TS')
    plt.plot(level,dpr_3,'go-', label='Shill Duelling')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Dao Padlock
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6,25.8,27.1]
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2,51.7,54.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9,10,11,12,13]
    level = [4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    AS_2 =  [3,4,4,4,4,5, 5, 5, 5, 5, 5, 5, 5, 5] # Fighter 1  / Warlock X (Shill AB)
    AS_3 =  [4,4,4,4,5,5, 5, 5, 5, 5, 5, 5, 5, 5] # Pure Warlock (EB+AB)
    AS_4 =  [3,3,3,3,3,4, 4, 4, 4, 5, 5, 5, 5, 5] # Paladin 1  / Warlock X / Paladin 3 / Warlock X (GWM -> WC)
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    dpr_4 = np.zeros(np.size(level))
    for i in range(2):
        dpr_2[i] = bb_attack(level[i],AS_2[i],4.5,bonus=[0,2*AS_2[i]+2],shillelagh=1,move_chance=0.2)
        dpr_3[i] = eb_attack(level[i],AS_3[i],agonizing=1) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=1)
        dpr_4[i] = bb_attack(level[i],AS_4[i],5.5,bonus=[0,2*AS_4[i]],move_chance=0.2)
    for i in range(2,6):
        dpr_2[i] = 2*shillelagh_attack(level[i],AS_2[i],4.5,agonizing=1,dueling=1) + once_per_turn_rider(level[i],AS_2[i],0,bonus=[0,AS_2[i]],chances=2)
        dpr_3[i] = eb_attack(level[i],AS_3[i],agonizing=1) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=2)
        dpr_4[i] = 2*gwm_attack(level[i],AS_4[i],5.5) + (1-(19/20)**2)*weapon_attack(level[i],AS_4[i],5.5) + once_per_turn_rider(level[i],AS_4[i],0,bonus=[0,AS_4[i]],chances=2)
    for i in range(6,9):
        dpr_2[i] = 2*shillelagh_attack(level[i],AS_2[i],4.5,agonizing=1,dueling=1) + once_per_turn_rider(level[i],AS_2[i],3.5,bonus=[0,AS_2[i]],chances=2)
        dpr_3[i] = eb_attack(level[i],AS_3[i],agonizing=1) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=3)
        dpr_4[i] = 2*gwm_attack(level[i],AS_4[i],5.5) + (1-(19/20)**2)*weapon_attack(level[i],AS_4[i],5.5) + once_per_turn_rider(level[i],AS_4[i],3.5,bonus=[0,AS_4[i]],chances=2)
    for i in range(9,14):
        dpr_2[i] = 3*shillelagh_attack(level[i],AS_2[i],4.5,agonizing=1,dueling=1) + once_per_turn_rider(level[i],AS_2[i],3.5,bonus=[0,AS_2[i]],chances=3)
        dpr_3[i] = eb_attack(level[i],AS_3[i],agonizing=1) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=3)
        dpr_4[i] = 3*gwm_attack(level[i],AS_4[i],5.5) + (1-(19/20)**2)*weapon_attack(level[i],AS_4[i],5.5) + once_per_turn_rider(level[i],AS_4[i],3.5,bonus=[0,AS_4[i]],chances=3)
    for i in range(13,14):
        dpr_3[i] = eb_attack(level[i],AS_3[i],agonizing=1) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=4)
    plt.plot(level,dpr_2,'ro-', label='Shill Pact')
    plt.plot(level,dpr_3,'bo-', label='EB+AB')
    plt.plot(level,dpr_4,'go-', label='GWM')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()



if 0:
    # Celestial Warlock / Paladin Build
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1,23.3,24.6]
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2,46.7,49.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9,10,11]
    level = [4,5,6,7,8,9,10,11,12,13,14,15]
    AS_2 =  [4,4,4,4,5,5, 5, 5, 5, 5, 5, 5] # Warlock 1 Valor Bard X (EB + Melee)
    AS_3 =  [3,4,4,4,4,4, 4, 4, 4, 5, 5, 5] # Paladin 1  / Warlock 12 / Paladin 3 / Warlock X (WC -> GWM)
    AS_4 =  [3,3,3,3,3,4, 4, 4, 4, 5, 5, 5] # Paladin 1  / Warlock 12 / Paladin 3 / Warlock X (GWM -> WC)
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    dpr_4 = np.zeros(np.size(level))
    for i in range(1):
        dpr_2[i] = bb_attack(level[i],AS_2[i],4.5,extra_dice=3.5,move_chance=0.2)
        dpr_3[i] = bb_attack(level[i],AS_3[i],5.5,extra_dice=2.5,move_chance=0.5)
        dpr_4[i] = bb_attack(level[i],AS_4[i],5.5,extra_dice=2.5,move_chance=0.5)
    for i in range(1,2):
        dpr_2[i] = bb_attack(level[i],AS_2[i],4.5,extra_dice=3.5,move_chance=0.2)
        dpr_3[i] = bb_attack(level[i],AS_3[i],5.5,extra_dice=2.5,move_chance=0.5)
        dpr_4[i] = bb_attack(level[i],AS_4[i],5.5,extra_dice=2.5,move_chance=0.5,gwm=1) + 0.1*weapon_attack(level[i],AS_4[i],5.5,extra_dice=2.5)
    for i in range(2,3):
        dpr_2[i] = weapon_attack(level[i],AS_2[i],4.5,extra_dice=3.5) + eb_attack(level[i],AS_2[i],extra_dice=3.5)
        dpr_3[i] = 2*weapon_attack(level[i],AS_3[i],7,extra_dice=2.5)
        dpr_4[i] = 2*gwm_attack(level[i],AS_4[i],7,extra_dice=2.5) + 0.1*weapon_attack(level[i],AS_3[i],7,extra_dice=2.5)
    for i in range(3,4):
        dpr_2[i] = weapon_attack(level[i],AS_2[i],4.5,extra_dice=3.5) + eb_attack(level[i],AS_2[i],extra_dice=3.5)
        dpr_3[i] = 2*weapon_attack(level[i],AS_3[i],7,extra_dice=2.5) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=2)
        dpr_4[i] = 2*gwm_attack(level[i],AS_4[i],7,extra_dice=2.5) + once_per_turn_rider(level[i],AS_4[i],0,bonus=[0,AS_4[i]],chances=2) + 0.1*weapon_attack(level[i],AS_4[i],7,extra_dice=2.5)
    for i in range(4,5):
        dpr_2[i] = 2/3 * (weapon_attack(level[i],AS_2[i],4.5,extra_dice=2*3.5) + eb_attack(level[i],AS_2[i],extra_dice=2*3.5))
        dpr_3[i] = 2*weapon_attack(level[i],AS_3[i],7,extra_dice=2.5) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=2)
        dpr_4[i] = 2*gwm_attack(level[i],AS_4[i],7,extra_dice=2.5) + once_per_turn_rider(level[i],AS_4[i],0,bonus=[0,AS_4[i]],chances=2) + 0.1*weapon_attack(level[i],AS_4[i],7,extra_dice=2.5)
    for i in range(5,6):
        dpr_2[i] = 2/3 * (weapon_attack(level[i],AS_2[i],4.5,extra_dice=2*3.5) + eb_attack(level[i],AS_2[i],extra_dice=2*3.5))
        dpr_3[i] = 2*gwm_attack(level[i],AS_3[i],bonus=[0,AS_3[i]],extra_dice=2.5) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=2) + 0.1*weapon_attack(level[i],AS_3[i],7,extra_dice=2.5)
        dpr_4[i] = dpr_3[i]
    for i in range(6,8):
        dpr_2[i] = 2/3 * (weapon_attack(level[i],AS_2[i],4.5,extra_dice=4*4.5) + eb_attack(level[i],AS_2[i],extra_dice=4*4.5))
        dpr_3[i] = 2*gwm_attack(level[i],AS_3[i],bonus=[0,AS_3[i]],extra_dice=2.5) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=2) + 0.1*weapon_attack(level[i],AS_3[i],7,extra_dice=2.5)
        dpr_4[i] = dpr_3[i]
    for i in range(8,9):
        dpr_2[i] = 2/3 * (weapon_attack(level[i],AS_2[i],4.5,extra_dice=4*4.5) + eb_attack(level[i],AS_2[i],extra_dice=4*4.5))
        dpr_3[i] = 2*gwm_attack(level[i],AS_3[i],bonus=[0,AS_3[i]],extra_dice=2.5) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=2) + 0.1*weapon_attack(level[i],AS_3[i],7,extra_dice=2.5)
        dpr_4[i] = dpr_3[i]
    for i in range(9,10):
        dpr_2[i] = 2/3 * (weapon_attack(level[i],AS_2[i],4.5,extra_dice=4*4.5) + eb_attack(level[i],AS_2[i],extra_dice=4*4.5))
        dpr_3[i] = 3*gwm_attack(level[i],AS_3[i],bonus=[0,AS_3[i]],extra_dice=2.5) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=3) + 0.1*weapon_attack(level[i],AS_3[i],7,extra_dice=2.5)
        dpr_4[i] = dpr_3[i]
    for i in range(10,11):
        dpr_2[i] = 2/3 * (weapon_attack(level[i],AS_2[i],4.5,extra_dice=4*4.5) + eb_attack(level[i],AS_2[i],extra_dice=4*4.5))
        dpr_3[i] = 3*gwm_attack(level[i],AS_3[i],bonus=[0,AS_3[i]],extra_dice=2.5) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=3) + 0.1*weapon_attack(level[i],AS_3[i],7,extra_dice=2.5)
        dpr_4[i] = dpr_3[i]
    for i in range(11,12):
        dpr_2[i] = 2/3 * (2*weapon_attack(level[i],AS_2[i],4.5,extra_dice=4*4.5) + eb_attack(level[i],AS_2[i],extra_dice=4*4.5)) + 1/3*weapon_attack(level[i],AS_2[i],4.5,extra_dice=4*4.5)
        dpr_3[i] = 3*gwm_attack(level[i],AS_3[i],bonus=[AS_3[i],AS_3[i]],extra_dice=2.5) + once_per_turn_rider(level[i],AS_3[i],0,bonus=[0,AS_3[i]],chances=3) + 0.1*weapon_attack(level[i],AS_3[i],7,extra_dice=2.5)
        dpr_4[i] = dpr_3[i]
    plt.plot(level,dpr_2,'ro-', label='Warlock Valor')
    # plt.plot(level,dpr_3,'bo-', label='WC -> GWM')
    plt.plot(level,dpr_4,'go-', label='GWM -> WC')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Rogue / Battlemaster Builds
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [3,4,4,4,4,5, 5, 5, 5, 5] # Champion Fighter DW
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    for i in range(2):
        dpr_1[i] = 2*nick_attack(level[i],AS_1[i],3.5,adv=2) + weapon_attack(level[i],AS_1[i],3.5) + sneak_attack(level[i],AS_1[i],chances=2,rogue_lvl=1,adv=1.5) + 0.6*(weapon_attack(level[i],AS_1[i],3.5+4.5) + sneak_attack(level[i],AS_1[i],rogue_lvl=1,adv=1.5))
    for i in range(2,10):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5,adv=2) + 2*weapon_attack(level[i],AS_1[i],3.5) + sneak_attack(level[i],AS_1[i],chances=3,rogue_lvl=level[i]-5,adv=1.5) + 0.6*(weapon_attack(level[i],AS_1[i],3.5+4.5) + sneak_attack(level[i],AS_1[i],rogue_lvl=level[i]-5,adv=1.5))
    
    plt.plot(level,dpr_1,'ro-', label='Battlemaster 5 / Swash X')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Artificer Builds
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    pb =    [2,3,3,3,3,4, 4, 4, 4, 5]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [4,4,4,4,5,5, 5, 5, 5, 5] # TS Arcanosmith
    AS_2 =  [4,4,4,4,4,4, 4, 4, 5, 5] # GWM Crossbow Artillerist
    AS_3 =  [4,4,4,4,5,5, 5, 5, 5, 5] # Ranged Armorer + Homunculus
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    for i in range(1):
        dpr_1[i] = ts_attack(level[i],AS_1[i],4.5) + nick_attack(level[i],AS_1[i],die=2*4.5)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],5.5) + nick_attack(level[i],AS_2[i],die=2*4.5)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],2*3.5) + nick_attack(level[i],AS_3[i],die=2.5,bonus=[0,pb[i]])
    for i in range(1,4):
        dpr_1[i] = ts_attack(level[i],AS_1[i],4.5,bonus=[0,AS_1[i]]) + nick_attack(level[i],AS_1[i],die=2*4.5)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],5.5) + nick_attack(level[i],AS_2[i],die=2*4.5)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],2*3.5) + weapon_attack(level[i],AS_3[i],3.5,adv=2) + once_per_turn_rider(level[i],AS_3[i],3.5,chances=2) + nick_attack(level[i],AS_3[i],die=2.5,bonus=[0,pb[i]])
    for i in range(4,5):
        dpr_1[i] = ts_attack(level[i],AS_1[i],4.5,bonus=[0,AS_1[i]]) + nick_attack(level[i],AS_1[i],die=2*4.5)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i],5.5) + nick_attack(level[i],AS_2[i],die=2*4.5)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],2*3.5) + weapon_attack(level[i],AS_3[i],3.5,adv=2) + once_per_turn_rider(level[i],AS_3[i],3.5,chances=2) + nick_attack(level[i],AS_3[i],die=2.5,bonus=[0,pb[i]])
    for i in range(5,6):
        dpr_1[i] = ts_attack(level[i],AS_1[i],4.5,bonus=[2,AS_1[i]]) + nick_attack(level[i],AS_1[i],die=2*4.5)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i],5.5,bonus=[2,0]) + nick_attack(level[i],AS_2[i],die=2*4.5)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],2*3.5) + weapon_attack(level[i],AS_3[i],3.5,adv=2) + once_per_turn_rider(level[i],AS_3[i],3.5,chances=2) + nick_attack(level[i],AS_3[i],die=2.5,bonus=[0,pb[i]])
    for i in range(6,10):
        dpr_1[i] = ts_attack(level[i],AS_1[i],4.5,bonus=[2,AS_1[i]]) + nick_attack(level[i],AS_1[i],die=3*4.5)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i],5.5,bonus=[2,0]) + nick_attack(level[i],AS_2[i],die=3*4.5)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],2*3.5) + weapon_attack(level[i],AS_3[i],3.5,adv=2) + once_per_turn_rider(level[i],AS_3[i],3.5,chances=2) + nick_attack(level[i],AS_3[i],die=2.5,bonus=[0,pb[i]])
    
    plt.plot(level,dpr_1,'ro-', label='TS Arcanosmith Artillerist')
    plt.plot(level,dpr_2,'bo-', label='GWM Weaponsmith Artillerist')
    plt.plot(level,dpr_3,'go-', label='Ranged Armorer + Homunculus')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Monk Builds
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [4,4,4,4,5,5, 5, 5, 5, 5] # Straight Shadow
    AS_2 =  [3,4,4,4,4,5, 5, 5, 5, 5] # Rogue 1 / Shadow Monk X
    AS_3 =  [3,4,4,4,4,5, 5, 5, 5, 5] # Fighter 1 / Shadow Monk X
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    for i in range(1):
        dpr_1[i] = 2*ma_attack(level[i],AS_1[i],adv=3)
        dpr_2[i] = 2*ma_attack(level[i],AS_2[i],adv=2,monk_level=level[i]-1) + ma_attack(level[i],AS_2[i],adv=2,nick=1,monk_level=level[i]-1) + sneak_attack(level[i],AS_2[i],chances=2,rogue_lvl=1,adv=2)
        dpr_3[i] = 3*ma_attack(level[i],AS_3[i],adv=2,monk_level=level[i]-1)
    for i in range(1,2):
        dpr_1[i] = 3*ma_attack(level[i],AS_1[i],adv=3)
        dpr_2[i] = 2*ma_attack(level[i],AS_2[i],adv=3,monk_level=level[i]-1) + ma_attack(level[i],AS_2[i],adv=3,nick=1,monk_level=level[i]-1) + sneak_attack(level[i],AS_2[i],chances=3,rogue_lvl=1,adv=3)
        dpr_3[i] = 3*ma_attack(level[i],AS_3[i],adv=3,monk_level=level[i]-1)
    for i in range(2,6):
        dpr_1[i] = 3*ma_attack(level[i],AS_1[i],adv=3)
        dpr_2[i] = 3*ma_attack(level[i],AS_2[i],adv=3,monk_level=level[i]-1) + ma_attack(level[i],AS_2[i],adv=3,nick=1,monk_level=level[i]-1) + sneak_attack(level[i],AS_2[i],chances=3,rogue_lvl=1,adv=3)
        dpr_3[i] = 4*ma_attack(level[i],AS_3[i],adv=3,monk_level=level[i]-1)
    for i in range(6,7):
        dpr_1[i] = 3*ma_attack(level[i],AS_1[i],adv=3)
        dpr_2[i] = 3*ma_attack(level[i],AS_2[i],adv=3,monk_level=level[i]-1) + ma_attack(level[i],AS_2[i],adv=3,nick=1,monk_level=level[i]-1) + sneak_attack(level[i],AS_2[i],chances=3,rogue_lvl=1,adv=3)
        dpr_3[i] = 4*ma_attack(level[i],AS_3[i],adv=3,monk_level=level[i]-1)
    for i in range(7,10):
        dpr_1[i] = 3*ma_attack(level[i],AS_1[i],adv=3)
        dpr_2[i] = 3*ma_attack(level[i],AS_2[i],adv=3,monk_level=level[i]-1) + ma_attack(level[i],AS_2[i],adv=3,nick=1,monk_level=level[i]-1) + sneak_attack(level[i],AS_2[i],chances=3,rogue_lvl=1,adv=3)
        dpr_3[i] = 4*ma_attack(level[i],AS_3[i],adv=3,monk_level=level[i]-1)
    plt.plot(level,dpr_1,'ro-', label='Straight Shadow')
    plt.plot(level,dpr_2,'bo-', label='Rogue 1 / Shadow')
    plt.plot(level,dpr_3,'go-', label='Fighter 1 / Shadow')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Barb Builds
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [4,4,4,4,5,5, 5, 5, 5, 5] # Beast Centaur Grappler
    AS_2 =  [4,4,4,4,5,5, 5, 5, 5, 5] # Berserker DW
    rage =  [2,2,2,2,2,3, 3, 3, 3, 3]
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    for i in range(1):
        dpr_1[i] = (2+2/3)*weapon_attack(level[i],AS_1[i],3.5,adv=2,bonus=[0,rage[i]])
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + (1+2/3)*nick_attack(level[i],AS_2[i],adv=2,bonus=[0,rage[i]]) + once_per_turn_rider(level[i],AS_2[i],3.5*rage[i],adv=2,chances=3)
    for i in range(1,5):
        dpr_1[i] = (3+2/3)*weapon_attack(level[i],AS_1[i],3.5,adv=2,bonus=[0,rage[i]]) + nick_attack(level[i],AS_1[i],adv=2,bonus=[0,rage[i]])
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + (1+2/3)*nick_attack(level[i],AS_2[i],adv=2,bonus=[0,rage[i]]) + once_per_turn_rider(level[i],AS_2[i],3.5*rage[i],adv=2,chances=4)
    for i in range(5,6):
        dpr_1[i] = (3+2/3)*weapon_attack(level[i],AS_1[i],3.5,adv=2,bonus=[0,rage[i]]) + nick_attack(level[i],AS_1[i],3.5+5.5,bonus=[0,rage[i]])
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5+5.5,bonus=[0,rage[i]]) + weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + (1+2/3)*nick_attack(level[i],AS_2[i],adv=2,bonus=[0,rage[i]]) + once_per_turn_rider(level[i],AS_2[i],3.5*rage[i],adv=2,chances=4)
    for i in range(6,7):
        dpr_1[i] = (3+2/3)*weapon_attack(level[i],AS_1[i],3.5,adv=2,bonus=[0,rage[i]]) + nick_attack(level[i],AS_1[i],3.5+5.5,bonus=[0,rage[i]])
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5+5.5,bonus=[0,rage[i]]) + weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + (1+2/3)*nick_attack(level[i],AS_2[i],adv=2,bonus=[0,rage[i]]) + 0.5*weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + once_per_turn_rider(level[i],AS_2[i],3.5*rage[i],adv=2,chances=4) 
    for i in range(7,10):
        dpr_1[i] = (3+2/3)*weapon_attack(level[i],AS_1[i],3.5,adv=2,bonus=[0,rage[i]]) + nick_attack(level[i],AS_1[i],3.5+5.5,bonus=[0,rage[i]])
        dpr_2[i] = weapon_attack(level[i],AS_2[i],3.5+5.5,bonus=[0,rage[i]]) + weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + (1+2/3)*nick_attack(level[i],AS_2[i],adv=2,bonus=[0,rage[i]]) + 0.5*weapon_attack(level[i],AS_2[i],3.5,adv=2,bonus=[0,rage[i]]) + once_per_turn_rider(level[i],AS_2[i],3.5*rage[i],adv=2,chances=4)
    plt.plot(level,dpr_1,'ro-', label='Beast Grappler')
    plt.plot(level,dpr_2,'bo-', label='Berserker DW')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Necro Builds
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [3,3,4,4,4,4, 5, 5, 5, 5] # Warlock 2 / Lore Bard X Animate Dead + Magic Stone
    AS_2 =  [4,4,4,4,5,5, 5, 5, 5, 5] # Spores Druid Animate Dead + Magic Stone
    AS_3 =  [4,4,4,4,5,5, 5, 5, 5, 5] # Necromancy Wizard X Animate Dead + Magic Stone
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    for i in range(1):
        dpr_1[i] = ts_attack(level[i],AS_1[i],4.5)
        dpr_2[i] = 2/3*shillelagh_attack(level[i],AS_2[i]) + summon_beast(level[i],AS_2[i],adv=2)
        dpr_3[i] = ts_attack(level[i],AS_3[i],4.5)
    for i in range(1,2):
        dpr_1[i] = eb_attack(level[i],AS_1[i],agonize=1,extra_dice=3.5)
        dpr_2[i] = 2/3*attack_cantrip(level[i],AS_2[i],4.5) + summon_fey(level[i],AS_2[i]) + 3*weapon_attack(level[i],AS_2[i],3.5)
        dpr_3[i] = 2/3*ts_attack(level[i],AS_3[i],4.5) + 3*weapon_attack(level[i],AS_3[i],die=3.5) + summon_undead(level[i],AS_3[i])
    for i in range(2,3):
        dpr_1[i] = eb_attack(level[i],AS_1[i],agonize=1,extra_dice=3.5)
        dpr_2[i] = 2/3*attack_cantrip(level[i],AS_2[i],4.5) + summon_fey(level[i],AS_2[i]) + 3*weapon_attack(level[i],AS_2[i],3.5)
        dpr_3[i] = 2/3*ts_attack(level[i],AS_3[i],4.5) + 3*gwm_attack(level[i],AS_3[i],die=3.5) + gwm_attack(level[i],AS_3[i],die=4.5,bonus=[0,3+3])
    for i in range(3,4):
        dpr_1[i] = eb_attack(level[i],AS_1[i],agonize=1,extra_dice=3.5)
        dpr_2[i] = 2/3*attack_cantrip(level[i],AS_2[i],4.5,bonus=[0,AS_2[i]]) + summon_fey(level[i],AS_2[i],slot_level=4) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_2[i]])
        dpr_3[i] = 2/3*ts_attack(level[i],AS_3[i],4.5) + 3*gwm_attack(level[i],AS_3[i],die=3.5) + 2*gwm_attack(level[i],AS_3[i],die=4.5,bonus=[0,3+4])
    for i in range(4,5):
        dpr_1[i] = 2/3*eb_attack(level[i],AS_1[i],agonize=1) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_1[i]]) + summon_fey(level[i],AS_1[i])
        dpr_2[i] = 2/3*attack_cantrip(level[i],AS_2[i],4.5,bonus=[0,AS_2[i]]) + summon_fey(level[i],AS_2[i],slot_level=4) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_2[i]])
        dpr_3[i] = 2/3*ts_attack(level[i],AS_3[i],4.5) + 3*gwm_attack(level[i],AS_3[i],die=3.5) + 2*gwm_attack(level[i],AS_3[i],die=4.5,bonus=[0,3+4])
    for i in range(5,6):
        dpr_1[i] = 2/3*eb_attack(level[i],AS_1[i],agonize=1) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_1[i]]) + summon_fey(level[i],AS_1[i],slot_level=4)
        dpr_2[i] = 2/3*weapon_attack(level[i],AS_2[i],die=4.5) + summon_fey(level[i],AS_2[i],slot_level=5) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_2[i]])
        dpr_3[i] = 2/3*ts_attack(level[i],AS_3[i],4.5) + 3*gwm_attack(level[i],AS_3[i],die=3.5) + 2*gwm_attack(level[i],AS_3[i],die=4.5,bonus=[0,3+5])
    for i in range(6,7):
        dpr_1[i] = 2/3*eb_attack(level[i],AS_1[i],agonize=1) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_1[i]]) + summon_fey(level[i],AS_1[i],slot_level=4)
        dpr_2[i] = 2/3*attack_cantrip(level[i],AS_2[i],4.5,bonus=[0,AS_2[i]]) + summon_fey(level[i],AS_2[i],slot_level=5) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_2[i]])
        dpr_3[i] = 2/3*ts_attack(level[i],AS_3[i],4.5) + 3*gwm_attack(level[i],AS_3[i],die=3.5) + 2*gwm_attack(level[i],AS_3[i],die=4.5,bonus=[0,3+5])
    for i in range(7,8):
        dpr_1[i] = 2/3*eb_attack(level[i],AS_1[i],agonize=1) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_1[i]]) + summon_fey(level[i],AS_1[i],slot_level=5)
        dpr_2[i] = 2/3*attack_cantrip(level[i],AS_2[i],4.5,bonus=[0,AS_2[i]]) + summon_fey(level[i],AS_2[i],slot_level=6) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_2[i]])
        dpr_3[i] = 2/3*ts_attack(level[i],AS_3[i],4.5) + 3*gwm_attack(level[i],AS_3[i],die=3.5) + 3*gwm_attack(level[i],AS_3[i],die=4.5,bonus=[0,3+6])
    for i in range(8,9):
        dpr_1[i] = 2/3*eb_attack(level[i],AS_1[i],agonize=1) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_1[i]]) + summon_fey(level[i],AS_1[i],slot_level=5)
        dpr_2[i] = 2/3*attack_cantrip(level[i],AS_2[i],4.5,bonus=[0,AS_2[i]]) + summon_fey(level[i],AS_2[i],slot_level=6) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_2[i]])
        dpr_3[i] = 2/3*ts_attack(level[i],AS_3[i],4.5) + 3*gwm_attack(level[i],AS_3[i],die=3.5) + 3*gwm_attack(level[i],AS_3[i],die=4.5,bonus=[0,3+6])
    for i in range(9,10):
        dpr_1[i] = 2/3*eb_attack(level[i],AS_1[i],agonize=1) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_1[i]]) + summon_fey(level[i],AS_1[i],slot_level=6)
        dpr_2[i] = 2/3*attack_cantrip(level[i],AS_2[i],4.5,bonus=[0,AS_2[i]]) + summon_fey(level[i],AS_2[i],slot_level=6) + 3*weapon_attack(level[i],AS_2[i],3.5,bonus=[0,AS_2[i]])
        dpr_3[i] = 2/3*ts_attack(level[i],AS_3[i],4.5) + 3*gwm_attack(level[i],AS_3[i],die=3.5) + 3*gwm_attack(level[i],AS_3[i],die=4.5,bonus=[0,3+6])
    plt.plot(level,dpr_1,'go-', label='Warlock Lore Bard')
    plt.plot(level,dpr_2,'bo-', label='Spores Druid')
    plt.plot(level,dpr_3,'ro-', label='Artificer Necro Wizard')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()


if 0:
    # CME Gish
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [3,4,4,4,4,4, 4, 4, 4, 4] # Fighter 2 / Bladesinger X DW+EA
    AS_2 =  [3,4,4,4,4,4, 4, 4, 4, 4] # Fighter 2 / Valor Bard X DW
    AS_3 =  [3,4,4,4,4,4, 4, 4, 4, 4] # Fighter 2 / Bladesinger X Shill
    AS_4 =  [3,4,4,4,4,5, 5, 5, 5, 5] # Fighter 1 / Abjurer X SpikeTank
    AS_5 =  [3,3,4,4,4,4, 5, 5, 5, 5] # Warlock 2 / Valor Bard X Magic Stone + Sling + EB
    AS_6 =  [3,3,4,4,4,4, 4, 4, 4, 4] # Fighter 1 / Warlock 1 / Valor Bard X Shill DW
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    dpr_4 = np.zeros(np.size(level))
    dpr_6 = np.zeros(np.size(level))
    # Dex based DW
    for i in range(1):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,adv=2) + nick_attack(level[i],AS_1[i],twf=1,adv=2)
        dpr_3[i] = ts_attack(level[i],AS_3[i],4.5,shillelagh=1,adv=2)
        dpr_4[i] = ts_attack(level[i],AS_4[i],4.5,adv=2) + 10
        dpr_2[i] = weapon_attack(level[i],AS_1[i],3.5) + nick_attack(level[i],AS_1[i],twf=1,adv=2)
        dpr_6[i] = shillelagh_attack(level[i],AS_6[i]) + nick_attack(level[i],AS_6[i],twf=1)
    for i in range(1,2):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,adv=2) + 2*nick_attack(level[i],AS_1[i],twf=1,adv=2)
        dpr_3[i] = ts_attack(level[i],AS_3[i],4.5,shillelagh=1,adv=2)
        dpr_4[i] = ts_attack(level[i],AS_4[i],4.5,adv=2) + 10
        dpr_2[i] = weapon_attack(level[i],AS_1[i],3.5) + 2*nick_attack(level[i],AS_1[i],twf=1,adv=2)
        dpr_6[i] = shillelagh_attack(level[i],AS_6[i]) + nick_attack(level[i],AS_6[i],twf=1)
    for i in range(2,3):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,adv=2) + (1+3/4)*weapon_attack(level[i],AS_1[i],3.5,adv=2)
        dpr_3[i] = ts_attack(level[i],AS_3[i],4.5,shillelagh=1,adv=2,extra_dice=4.5)
        dpr_4[i] = ts_attack(level[i],AS_4[i],4.5,adv=2) + 15
        dpr_2[i] = weapon_attack(level[i],AS_1[i],3.5) + 2*nick_attack(level[i],AS_1[i],twf=1,adv=2)
        dpr_6[i] = shillelagh_attack(level[i],AS_6[i]) + nick_attack(level[i],AS_6[i],twf=1)
    for i in range(3,4):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,adv=2) + bb_attack(level[i],AS_1[i],3.5,move_chance=0.3,adv=2) + (1+3/4)*weapon_attack(level[i],AS_1[i],3.5,adv=2)
        dpr_3[i] = ts_attack(level[i],AS_3[i],3.5,adv=2) + 2*shillelagh_attack(level[i],AS_3[i],adv=2)
        dpr_4[i] = ts_attack(level[i],AS_4[i],4.5,adv=2) + 15
        dpr_2[i] = 2*weapon_attack(level[i],AS_1[i],3.5) + weapon_attack(level[i],AS_1[i],3.5,adv=2) + bb_attack(level[i],AS_1[i],3.5,move_chance=0.3,adv=2)
        dpr_6[i] = shillelagh_attack(level[i],AS_6[i]) + nick_attack(level[i],AS_6[i],twf=1)
    for i in range(4,5):
        dpr_1[i] = 3/4*(2*weapon_attack(level[i],AS_1[i],3.5+2*4.5,adv=2) + weapon_attack(level[i],AS_1[i],3.5+2*4.5,adv=2) + bb_attack(level[i],AS_1[i],3.5,move_chance=0.3,adv=3,extra_dice=2*4.5))
        dpr_3[i] = 3/4*(ts_attack(level[i],AS_3[i],3.5,adv=2,extra_dice=2*4.5) + 2*shillelagh_attack(level[i],AS_3[i],adv=2,extra_dice=2*4.5))
        dpr_4[i] = ts_attack(level[i],AS_4[i],4.5,adv=2) + 15
        dpr_2[i] = 3/4*(2*weapon_attack(level[i],AS_1[i],3.5+2*3.5) + weapon_attack(level[i],AS_1[i],3.5+2*3.5,adv=2) + bb_attack(level[i],AS_1[i],3.5+2*3.5,move_chance=0.3,adv=2))
        dpr_6[i] = eb_attack(level[i],AS_6[i]) + shillelagh_attack(level[i],AS_6[i]) + nick_attack(level[i],AS_6[i],twf=1)
    for i in range(5,6):
        dpr_1[i] = 3/4*(2*weapon_attack(level[i],AS_1[i],3.5+2*4.5,adv=3) + weapon_attack(level[i],AS_1[i],3.5+2*4.5,adv=3) + bb_attack(level[i],AS_1[i],3.5,move_chance=0.3,adv=3,extra_dice=2*4.5))
        dpr_3[i] = 3/4*(ts_attack(level[i],AS_3[i],3.5,adv=3,extra_dice=2*4.5) + 2*shillelagh_attack(level[i],AS_3[i],adv=3,extra_dice=2*4.5))
        dpr_4[i] = ts_attack(level[i],AS_4[i],4.5,adv=2) + 20
        dpr_2[i] = 3/4*(2*weapon_attack(level[i],AS_1[i],3.5+2*3.5) + weapon_attack(level[i],AS_1[i],3.5+2*3.5,adv=2) + bb_attack(level[i],AS_1[i],3.5+2*3.5,move_chance=0.3,adv=2))
        dpr_6[i] = 3/4*(eb_attack(level[i],AS_6[i],extra_dice=2*3.5) + shillelagh_attack(level[i],AS_6[i],extra_dice=2*3.5) + nick_attack(level[i],AS_6[i],die=3.5+2*3.5,twf=1))
    for i in range(6,7):
        dpr_1[i] = 3/4*(2*weapon_attack(level[i],AS_1[i],3.5+4*4.5,adv=3) + weapon_attack(level[i],AS_1[i],3.5+4*4.5,adv=3) + bb_attack(level[i],AS_1[i],3.5,move_chance=0.3,adv=3,extra_dice=4*4.5))
        dpr_3[i] = 3/4*(ts_attack(level[i],AS_3[i],3.5,adv=3,extra_dice=4*4.5) + 2*shillelagh_attack(level[i],AS_3[i],adv=3,extra_dice=4*4.5))
        dpr_4[i] = ts_attack(level[i],AS_4[i],4.5,adv=2) + 20
        dpr_2[i] = 3/4*(2*weapon_attack(level[i],AS_1[i],3.5+2*3.5) + weapon_attack(level[i],AS_1[i],3.5+2*3.5,adv=2) + bb_attack(level[i],AS_1[i],3.5+2*3.5,move_chance=0.3,adv=2))
        dpr_6[i] = 3/4*(eb_attack(level[i],AS_6[i],extra_dice=2*3.5) + shillelagh_attack(level[i],AS_6[i],extra_dice=2*3.5) + nick_attack(level[i],AS_6[i],die=3.5+2*3.5,twf=1))
    for i in range(7,8):
        dpr_1[i] = (2*weapon_attack(level[i],AS_1[i],3.5+4*4.5,adv=3) + 3/4*weapon_attack(level[i],AS_1[i],3.5+4*4.5,adv=3) + bb_attack(level[i],AS_1[i],3.5,move_chance=0.3,adv=3,extra_dice=4*4.5))
        dpr_3[i] = (ts_attack(level[i],AS_3[i],3.5,adv=3,extra_dice=4*4.5) + 2*shillelagh_attack(level[i],AS_3[i],adv=3,extra_dice=4*4.5))
        dpr_4[i] = ts_attack(level[i],AS_4[i],4.5,adv=2) + 25 + 2*4.5
        dpr_2[i] = 3/4*(2*weapon_attack(level[i],AS_1[i],3.5+4*4.5) + weapon_attack(level[i],AS_1[i],3.5+4*4.5,adv=2) + bb_attack(level[i],AS_1[i],3.5+4*4.5,move_chance=0.3,adv=2))
        dpr_6[i] = 3/4*(eb_attack(level[i],AS_6[i],extra_dice=2*3.5) + shillelagh_attack(level[i],AS_6[i],extra_dice=2*3.5) + nick_attack(level[i],AS_6[i],die=3.5+2*3.5,twf=1))
    for i in range(8,9):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5+4*4.5,adv=3) + 3/4*weapon_attack(level[i],AS_1[i],3.5+4*4.5,adv=3) + bb_attack(level[i],AS_1[i],3.5,move_chance=0.3,adv=3,extra_dice=4*4.5)
        dpr_3[i] = (ts_attack(level[i],AS_3[i],3.5,adv=3,extra_dice=4*4.5) + 2*shillelagh_attack(level[i],AS_3[i],adv=3,extra_dice=4*4.5))
        dpr_4[i] = ts_attack(level[i],AS_4[i],4.5,adv=2) + 25 + 2*4.5
        dpr_2[i] = 2*weapon_attack(level[i],AS_1[i],3.5+4*4.5) + weapon_attack(level[i],AS_1[i],3.5+4*4.5,adv=2) + bb_attack(level[i],AS_1[i],3.5+4*4.5,move_chance=0.3,adv=2)
        dpr_6[i] = 3/4*(eb_attack(level[i],AS_6[i],extra_dice=4*4.5) + shillelagh_attack(level[i],AS_6[i],extra_dice=4*4.5) + nick_attack(level[i],AS_6[i],die=3.5+4*4.5,twf=1))
    for i in range(9,10):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5+4.5*4.5,adv=3) + 3/4*weapon_attack(level[i],AS_1[i],3.5+4.5*4.5,adv=3) + bb_attack(level[i],AS_1[i],3.5,move_chance=0.3,adv=3,extra_dice=4.5*4.5)
        dpr_3[i] = (ts_attack(level[i],AS_3[i],3.5,adv=3,extra_dice=4.5*4.5) + 2*shillelagh_attack(level[i],AS_3[i],adv=3,extra_dice=4.5*4.5))
        dpr_4[i] = ts_attack(level[i],AS_4[i],4.5,adv=2) + 30 + 2*4.5
        dpr_2[i] = 2*weapon_attack(level[i],AS_1[i],3.5+4.5*4.5) + weapon_attack(level[i],AS_1[i],3.5+4.5*4.5,adv=2) + bb_attack(level[i],AS_1[i],3.5+4.5*4.5,move_chance=0.3,adv=2)
        dpr_6[i] = eb_attack(level[i],AS_6[i],extra_dice=4*4.5) + shillelagh_attack(level[i],AS_6[i],extra_dice=4*4.5) + nick_attack(level[i],AS_6[i],die=3.5+4*4.5,twf=1)
    plt.plot(level,dpr_1,'ro-', label='DW Wizard CME Gish (Dex)')
    plt.plot(level,dpr_3,'go-', label='Shill Wizard CME Gish (Int)')
    plt.plot(level,dpr_4,'bo-', label='Spike Tank')
    # plt.plot(level,dpr_2,'bo-', label='DW Valor CME Gish (Dex)')
    # plt.plot(level,dpr_6,'ro-', label='ValorLockFighter CME')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()
    # plt.plot(level,dpr_1/dpr_3,'o-')
    # plt.show()

if 0:
    # Pala Builds
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [4,4,4,4,4,4, 4, 4, 5, 5] # DW EA Dexadin
    AS_2 =  [4,4,4,4,4,4, 4, 4, 5, 5] # Mounted Lance Dueling + GWM
    AS_3 =  [4,4,4,4,5,5, 5, 5, 5, 5] # GWM + GWF Devotion
    AS_4 =  [3,3,3,3,4,4, 4, 4, 5, 5] # Shillelagh Devotion
    AS_5 =  [4,4,4,4,4,4, 4, 4, 5, 5] # DBS GWF RB+EA Dexadin
    AS_6 =  [3,4,4,4,4,4, 4, 4, 4, 5] # GWM Paladin 1 / Celestial Bladelock 12
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    dpr_4 = np.zeros(np.size(level))
    dpr_5 = np.zeros(np.size(level))
    dpr_6 = np.zeros(np.size(level))
    for i in range(1):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5+2.5,adv=3) + nick_attack(level[i],AS_1[i],die=3.5+2.5,twf=1,adv=3)
        dpr_2[i] = weapon_attack(level[i],AS_2[i],5.5+2.5,bonus=[3,2])
        dpr_3[i] = gwm_attack(level[i],AS_3[i],8+3.25,bonus=[3,0]) + 0.25*gwm_attack(level[i],AS_3[i],8+3.25,bonus=[3,0])
        dpr_4[i] = shillelagh_attack(level[i],AS_3[i],extra_dice=2.5,bonus=[AS_4[i],2]) + 2/3*weapon_attack(level[i],AS_3[i],2.5+2.5,bonus=[AS_4[i],2])
        dpr_5[i] = weapon_attack(level[i],AS_5[i],2*3.25+3.25,adv=2) + 2/3*weapon_attack(level[i],AS_5[i],3.25+3.25,adv=2)
        dpr_6[i] = weapon_attack(level[i],AS_6[i],7+2.5)
    for i in range(1,2):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i]+1,3.5+2.5,adv=3) + nick_attack(level[i],AS_1[i],die=3.5+2.5,twf=1,adv=3)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i]+1,5.5+2.5,bonus=[3,2],adv=2)
        dpr_3[i] = gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0]) + gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0],adv=2) + 0.25*gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0])
        dpr_4[i] = shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2]) + shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2],adv=2) + 2/3*weapon_attack(level[i],AS_3[i]+1,2.5+2.5,bonus=[AS_4[i],2])
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i]+1,2*3.25+3.25,adv=2) + 2/3*weapon_attack(level[i],AS_5[i]+1,3.25+3.25,adv=2)
        dpr_6[i] = weapon_attack(level[i],AS_6[i],7+2.5)
    for i in range(2,3):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i]+1,3.5+2.5,adv=3) + nick_attack(level[i],AS_1[i],die=3.5+2.5,twf=1,adv=3)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i]+1,5.5+2.5,bonus=[3,2],adv=2)
        dpr_3[i] = gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0]) + gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0],adv=2) + 0.25*gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0])
        dpr_4[i] = shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2]) + shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2],adv=2) + 2/3*weapon_attack(level[i],AS_3[i]+1,2.5+2.5,bonus=[AS_4[i],2])
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i]+1,2*3.25+3.25,adv=2) + 2/3*weapon_attack(level[i],AS_5[i]+1,3.25+3.25,adv=2)
        dpr_6[i] = 2*weapon_attack(level[i],AS_6[i],7+4.5)
    for i in range(3,4):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i]+1,3.5+2.5,adv=3) + nick_attack(level[i],AS_1[i],die=3.5+2.5,twf=1,adv=3)
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i]+1,5.5+2.5,bonus=[3,2],adv=2)
        dpr_3[i] = gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0]) + gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0],adv=2) + 0.25*gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0])
        dpr_4[i] = shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2]) + shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2],adv=2) + 2/3*weapon_attack(level[i],AS_3[i]+1,2.5+2.5,bonus=[AS_4[i],2])
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i]+1,2*3.25+3.25,adv=2) + 2/3*weapon_attack(level[i],AS_5[i]+1,3.25+3.25,adv=2)
        dpr_6[i] = 2*weapon_attack(level[i],AS_6[i],7+4.5) + once_per_turn_rider(level[i],AS_6[i],0,bonus=[0,AS_6[i]],chances=2)
    for i in range(4,5):
        dpr_1[i] = (2+2/3)*weapon_attack(level[i],AS_1[i]+1,3.5+2.5,adv=3) + nick_attack(level[i],AS_1[i],die=3.5+2.5,twf=1,adv=3)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i]+1,5.5+2.5,bonus=[3,2],adv=2) + 0.25*gwm_attack(level[i],AS_2[i]+1,5.5+2.5,bonus=[3,2],adv=2)
        dpr_3[i] = gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0]) + gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0],adv=2) + 0.25*gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0])
        dpr_4[i] = shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2]) + shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2],adv=2) + 2/3*weapon_attack(level[i],AS_3[i]+1,2.5+2.5,bonus=[AS_4[i],2])
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i]+1,2*3.25+3.25,adv=3) + 2/3*weapon_attack(level[i],AS_5[i]+1,3.25+3.25,adv=3)
        dpr_6[i] = 2*weapon_attack(level[i],AS_6[i],7+4.5) + once_per_turn_rider(level[i],AS_6[i],0,bonus=[0,AS_6[i]],chances=2)
    for i in range(5,6):
        dpr_1[i] = (2+2/3)*weapon_attack(level[i],AS_1[i]+1,3.5+2.5,adv=3) + nick_attack(level[i],AS_1[i],die=3.5+2.5,twf=1,adv=3)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i]+1,5.5+2.5,bonus=[3,2],adv=2) + 0.25*gwm_attack(level[i],AS_2[i]+1,5.5+2.5,bonus=[3,2],adv=2)
        dpr_3[i] = gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0]) + gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0],adv=2) + 0.25*gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0])
        dpr_4[i] = shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2]) + shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2],adv=2) + 2/3*weapon_attack(level[i],AS_3[i]+1,2.5+2.5,bonus=[AS_4[i],2])
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i]+1,2*3.25+3.25,adv=3) + 2/3*weapon_attack(level[i],AS_5[i]+1,3.25+3.25,adv=3)
        dpr_6[i] = 2*gwm_attack(level[i],AS_6[i],7+4.5) + once_per_turn_rider(level[i],AS_6[i],0,bonus=[0,AS_6[i]],chances=2) + 0.25*2/3*weapon_attack(level[i],AS_6[i],7+4.5)
    for i in range(6,7):
        dpr_1[i] = (2+2/3)*weapon_attack(level[i],AS_1[i]+1,3.5+2.5,adv=3) + nick_attack(level[i],AS_1[i],die=3.5+2.5,twf=1,adv=3)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i]+1,5.5+2.5,bonus=[3,2],adv=2) + 0.25*gwm_attack(level[i],AS_2[i]+1,5.5+2.5,bonus=[3,2],adv=2)
        dpr_3[i] = gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0]) + gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0],adv=2) + 0.25*gwm_attack(level[i],AS_3[i]+1,8+3.25,bonus=[3,0])
        dpr_4[i] = shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2]) + shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5,bonus=[AS_4[i],2],adv=2) + 2/3*weapon_attack(level[i],AS_3[i]+1,2.5+2.5,bonus=[AS_4[i],2])
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i]+1,2*3.25+3.25,adv=3) + 2/3*weapon_attack(level[i],AS_5[i]+1,3.25+3.25,adv=3)
        dpr_6[i] = 2*gwm_attack(level[i],AS_6[i],7+2*4.5) + once_per_turn_rider(level[i],AS_6[i],0,bonus=[0,AS_6[i]],chances=2) + 0.25*2/3*weapon_attack(level[i],AS_6[i],7+2*4.5)
    for i in range(7,10):
        dpr_1[i] = (2+2/3)*weapon_attack(level[i],AS_1[i]+1,3.5+2.5+4.5,adv=3) + nick_attack(level[i],AS_1[i],die=3.5+2.5+4.5,twf=1,adv=3)
        dpr_2[i] = 2*gwm_attack(level[i],AS_2[i]+1,5.5+2.5+4.5,bonus=[3,2],adv=2) + 0.25*gwm_attack(level[i],AS_2[i]+1,5.5+2.5+4.5,bonus=[3,2],adv=2)
        dpr_3[i] = gwm_attack(level[i],AS_3[i]+1,8+3.25+4.875,bonus=[3,0]) + gwm_attack(level[i],AS_3[i]+1,8+3.25+4.875,bonus=[3,0],adv=2) + 0.25*gwm_attack(level[i],AS_3[i]+1,8+3.25+4.875,bonus=[3,0])
        dpr_4[i] = shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5+4.5,bonus=[AS_4[i],2]) + shillelagh_attack(level[i],AS_4[i]+1,extra_dice=2.5+4.5,bonus=[AS_4[i],2],adv=2) + 2/3*weapon_attack(level[i],AS_3[i]+1,2.5+2.5+4.5,bonus=[AS_4[i],2])
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i]+1,2*3.25+3.25+4.875,adv=3) + 2/3*weapon_attack(level[i],AS_5[i]+1,3.25+3.25+4.875,adv=3)
        dpr_6[i] = 2*weapon_attack(level[i],AS_6[i],7+2*4.5) + once_per_turn_rider(level[i],AS_6[i],0,bonus=[0,AS_6[i]],chances=2)
        dpr_6[i] = 2*gwm_attack(level[i],AS_6[i],7+4.5) + once_per_turn_rider(level[i],AS_6[i],0,bonus=[0,AS_6[i]],chances=2) + 0.25*2/3*weapon_attack(level[i],AS_6[i],7+4.5)
    dpr_6[-1] = 3*weapon_attack(level[i],AS_6[i],7+2*4.5) + once_per_turn_rider(level[i],AS_6[i],0,bonus=[0,AS_6[i]],chances=3) + 0.25*2/3*weapon_attack(level[i],AS_6[i],7+2*4.5)

    
    plt.plot(level,dpr_1,'ro-', label='DW+EA Vengeance')
    plt.plot(level,dpr_2,'go-', label='Mounted Lance Dueling+GWM Devotion ')
    plt.plot(level,dpr_3,'bo-', label='GWF+GWM Devotion')
    plt.plot(level,dpr_4,'o-', label='Shillelagh Dueling Devotion')
    plt.plot(level,dpr_5,'yo-', label='DBS+GWF+EA Vengeance')
    plt.plot(level,dpr_6,'D-', label='GWM Celsetial')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Barb Builds
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [4,4,4,4,5,5, 5, 5, 5, 5] # Giant Barb Thrower + PAM + GWM
    AS_2 =  [4,4,4,4,4,4, 4, 4, 5, 5] # Giant Barb PAM + GWM
    AS_3 =  [3,4,4,4,4,5, 5, 5, 5, 5] # Ancestral Barb + Soulknife Rogue
    rage =  [2,2,2,2,2,3, 3, 3, 3, 3]
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    i=0
    dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5,adv=2,bonus=[0,2]*rage[i]) + nick_attack(level[i],AS_1[i],die=2.5,adv=2,bonus=[0,2]*rage[i])
    dpr_2[i] = weapon_attack(level[i],AS_2[i],5.5,adv=2,bonus=rage[i]) + weapon_attack(level[i],AS_2[i],2.5,adv=2,bonus=rage[i])
    dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,adv=2,bonus=[0,2]) + nick_attack(level[i],AS_3[i],adv=2,bonus=rage[i]) + sneak_attack(level[i],AS_3[i],adv=2,chances=2,rogue_lvl=1)
    i=1
    dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5,adv=2,bonus=[0,2]) + nick_attack(level[i],AS_3[i],adv=2,bonus=rage[i]) + sneak_attack(level[i],AS_3[i],adv=2,chances=2,rogue_lvl=1)
    i=2
    dpr_3[i] = 2*weapon_attack(level[i],AS_3[i],3.5,adv=2,bonus=[0,2]) + nick_attack(level[i],AS_3[i],adv=2,bonus=rage[i]) + sneak_attack(level[i],AS_3[i],adv=2,chances=3,rogue_lvl=1)
    for i in range(3,4):
        dpr_3[i] = 2*weapon_attack(level[i],AS_3[i],3.5,adv=2,bonus=[0,2]) + nick_attack(level[i],AS_3[i],adv=2,bonus=rage[i]) + sneak_attack(level[i],AS_3[i],adv=2,chances=3,rogue_lvl=level[i]-5)
    for i in range(4,10):
        dpr_3[i] = 2*weapon_attack(level[i],AS_3[i],3.5,adv=2,bonus=[0,2]) + 2/3*weapon_attack(level[i],AS_3[i],2.5,adv=2,bonus=rage[i]) + sneak_attack(level[i],AS_3[i],adv=2,chances=3,rogue_lvl=level[i]-5)
    for i in range(1,2):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5,adv=2,bonus=[0,2]*rage[i]) + nick_attack(level[i],AS_1[i],die=2.5,adv=2,bonus=[0,2]*rage[i])
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],5.5,adv=2,bonus=rage[i]) + weapon_attack(level[i],AS_2[i],2.5,adv=2,bonus=rage[i])
    for i in range(2,4):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5+3.5,adv=2,bonus=[0,2]*rage[i]) + nick_attack(level[i],AS_1[i],die=2.5,adv=2,bonus=[0,2]*rage[i])
        dpr_2[i] = 2*weapon_attack(level[i],AS_2[i],5.5+3.5,adv=2,bonus=[0,2]*rage[i]) + weapon_attack(level[i],AS_2[i],2.5+3.5,adv=2,bonus=[0,2]*rage[i])
    i=4
    dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5+3.5,adv=2,bonus=[0,2]*rage[i]) + weapon_attack(level[i],AS_1[i],2.5+3.5,adv=2,bonus=[0,2]*rage[i])
    dpr_2[i] = 2*gwm_attack(level[i],AS_2[i],5.5+3.5,adv=2,bonus=[0,2]*rage[i]) + weapon_attack(level[i],AS_2[i],2.5+3.5,adv=2,bonus=[0,2]*rage[i])
    for i in range(5,10):
        dpr_1[i] = weapon_attack(level[i],AS_1[i],3.5+3.5,adv=2,bonus=[0,2]*rage[i]) + weapon_attack(level[i],AS_1[i],3.5+3.5+5.5,adv=1,bonus=[0,2]*rage[i]) + weapon_attack(level[i],AS_1[i],2.5+3.5,adv=2,bonus=[0,2]*rage[i])
        dpr_2[i] = gwm_attack(level[i],AS_2[i],5.5+3.5,adv=2,bonus=[0,2]*rage[i]) + gwm_attack(level[i],AS_2[i],5.5+3.5+5.5,adv=1,bonus=[0,2]*rage[i]) + weapon_attack(level[i],AS_2[i],2.5+3.5,adv=2,bonus=[0,2]*rage[i])
    for i in range(8,10):
        dpr_1[i] = gwm_attack(level[i],AS_1[i],5.5+3.5,adv=2,bonus=[0,2]*rage[i]) + gwm_attack(level[i],AS_1[i],5.5+3.5+5.5,adv=1,bonus=[0,2]*rage[i]) + weapon_attack(level[i],AS_1[i],2.5+3.5,adv=2,bonus=[0,2]*rage[i])

    plt.plot(level,dpr_1,'ro-', label='Nick Throw -> PAM + GWM')
    plt.plot(level,dpr_2,'go-', label='PAM + GWM -> Throw')
    plt.plot(level,dpr_3,'yo-', label='Barb Soulknife')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()

if 0:
    # Ranger Builds
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [4,4,4,4,5,5, 5, 5, 5, 5]
    AS_3 =  [3,4,4,4,4,4, 4, 4, 5, 5] # Ranger 1 --> Druid 8 --> Ranger 5 --> Druid X
    AS_6 =  [4,4,4,4,4,5, 5, 5, 5, 5] # Beastmaster 5/Druid X Summoner DW
    dpr_1 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    dpr_6 = np.zeros(np.size(level))
    for i in range(1):
        dpr_6[i] = weapon_attack(level[i],AS_6[i],4.5+3.5,bonus=[0,2]) + shillelagh_attack(level[i],AS_6[i],adv=2)
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5+3.5) + nick_attack(level[i],AS_3[i],die=3.5+3.5,adv=2)
    for i in range(1,4):
        dpr_6[i] = weapon_attack(level[i],AS_6[i],4.5+3.5,bonus=[0,2]) + 2/3*2*shillelagh_attack(level[i],AS_6[i],adv=2) + weapon_attack(level[i],AS_6[i],4.5,adv=2,bonus=[0,4+2+np.floor((level[i]-5)/2)])
        dpr_3[i] = weapon_attack(level[i],AS_3[i],3.5+3.5) + nick_attack(level[i],AS_3[i],die=3.5+3.5,adv=2)
    for i in range(4,5):
        dpr_6[i] = weapon_attack(level[i],AS_6[i],4.5+3.5,bonus=[0,2]) + 2/3*2*shillelagh_attack(level[i],AS_6[i],adv=2) + weapon_attack(level[i],AS_6[i],4.5,adv=2,bonus=[0,4+2+np.floor((level[i]-5)/2)])
        dpr_3[i] = 2/3*(weapon_attack(level[i],AS_3[i],3.5+2*4.5) + nick_attack(level[i],AS_3[i],die=3.5+2*4.5,adv=2))
    for i in range(5,6):
        dpr_6[i] = weapon_attack(level[i],AS_6[i],4.5+3.5,bonus=[0,2]) + 2/3*2*shillelagh_attack(level[i],AS_6[i],adv=2) + weapon_attack(level[i],AS_6[i],4.5,adv=2,bonus=[0,4+2+np.floor((level[i]-5)/2)])
        dpr_3[i] = 2/3*(weapon_attack(level[i],AS_3[i],3.5+2*4.5) + 2*nick_attack(level[i],AS_3[i],die=3.5+2*4.5,adv=2))
    for i in range(6,9):
        dpr_6[i] = weapon_attack(level[i],AS_6[i],4.5+3.5,bonus=[0,2]) + 2/3*2*shillelagh_attack(level[i],AS_6[i],adv=2) + weapon_attack(level[i],AS_6[i],4.5,adv=2,bonus=[0,4+2+np.floor((level[i]-5)/2)])
        dpr_3[i] = 2/3*(weapon_attack(level[i],AS_3[i],3.5+4*4.5) + 2*nick_attack(level[i],AS_3[i],die=3.5+4*4.5,adv=2))
    for i in range(8,9):
        dpr_6[i] = weapon_attack(level[i],AS_6[i],4.5+3.5,bonus=[0,2]) + 2/3*2*shillelagh_attack(level[i],AS_6[i],adv=2,bonus=[0,AS_6[i]]) + 2*weapon_attack(level[i],AS_6[i],7,adv=2,bonus=[0,3+5])
        dpr_3[i] = 2/3*(weapon_attack(level[i],AS_3[i],3.5+4*4.5) + 2*nick_attack(level[i],AS_3[i],die=3.5+4*4.5,adv=2))
    for i in range(9,10):
        dpr_6[i] = weapon_attack(level[i],AS_6[i],4.5+3.5,bonus=[0,2]) + 2/3*2*shillelagh_attack(level[i],AS_6[i],adv=2,bonus=[0,AS_6[i]]) + 2.33*weapon_attack(level[i],AS_6[i],7,adv=2,bonus=[0,3+5.33])
        dpr_3[i] = 2/3*(2*weapon_attack(level[i],AS_3[i],3.5+4*4.5) + 2*nick_attack(level[i],AS_3[i],die=3.5+4*4.5,adv=2))
    

    # plt.plot(level,dpr_1,'ro-', label='Nick Shill Beastmaster')
    # plt.plot(level,dpr_2,'go-', label='Nick Shill Beastmaster 11 / Druid X + Summon')
    plt.plot(level,dpr_6,'ro-', label='Nick Shill Beastmaster 5 / Druid X + Summon')
    plt.plot(level,dpr_3,'go-', label='Nick Dex DW CME')

    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()


if 0:
    # GWM Blade Pact Warlock vs DW+Shill blade Warlock
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [3,3,3,3,3,4, 4, 4, 4, 5]
    AS_2 =  AS_1 #[3,4,4,4,4,4, 4, 4, 4, 5]
    AS_3 =  [4,4,4,4,5,5, 5, 5, 5, 5]
    AS_4 = AS_3
    AS_5 = [3,4,4,4,4,4, 5, 5, 5, 5]
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    dpr_4 = np.zeros(np.size(level))
    dpr_5 = np.zeros(np.size(level))
    for i in range(0,2):
        dpr_1[i] = 2*shillelagh_attack(level[i],AS_1[i]) + nick_attack(level[i],AS_1[i],twf=1)
        dpr_2[i] = dpr_2[i] = 0.5*(gwm_attack(level[i],AS_2[i]) + 0.25*weapon_attack(level[i],AS_2[i],7)) + 0.5*(gwm_attack(level[i],AS_2[i],adv=2,crit_range=20))
        dpr_3[i] = weapon_attack(level[i],AS_3[i],5.5,bonus=3.5)
        dpr_4[i] = 0.5*(shillelagh_attack(level[i],AS_3[i]) + nick_attack(level[i],AS_3[i],twf=1)) + 0.5*(shillelagh_attack(level[i],AS_3[i],adv=2,crit_range=20) + nick_attack(level[i],AS_3[i],twf=1,adv=2,crit_range=20))
        dpr_5[i] = shillelagh_attack(level[i],AS_5[i],bonus=[0,2]+AS_5[i])
    i=1
    dpr_3[i] = 2*weapon_attack(level[i],AS_2[i],5.5,bonus=3.5)
    for i in range(2,np.size(level)-1):
        dpr_1[i] = 2*shillelagh_attack(level[i],AS_1[i]) + 2*nick_attack(level[i],AS_1[i],twf=1)
        dpr_2[i] = dpr_2[i] = 0.5*(2*gwm_attack(level[i],AS_2[i]) + 0.25*weapon_attack(level[i],AS_2[i],7)) + 0.5*(2*gwm_attack(level[i],AS_2[i],adv=2,crit_range=20))
        dpr_3[i] = 2*weapon_attack(level[i],AS_3[i],5.5,bonus=3.5)
        dpr_4[i] = 0.5*(shillelagh_attack(level[i],AS_3[i]) + 2*nick_attack(level[i],AS_3[i],twf=1)) + 0.5*(shillelagh_attack(level[i],AS_3[i],adv=2,crit_range=20) + 2*nick_attack(level[i],AS_3[i],twf=1,adv=2,crit_range=20))
        dpr_5[i] = 2*shillelagh_attack(level[i],AS_5[i],bonus=[0,2]+AS_5[i]) + extra_dice(level[i],AS_5[i],4.5,chances=2)
    for i in range(7,10):
        dpr_3[i] = 3*weapon_attack(level[i],AS_3[i],5.5,bonus=3.5)
    for i in range(6,np.size(level)-1):
        dpr_1[i] += once_per_turn_rider(level[i],AS_1[i],3.5,chances=2)
        dpr_2[i] += once_per_turn_rider(level[i],AS_2[i],3.5,chances=4)
        dpr_4[i] += once_per_turn_rider(level[i],AS_4[i],3.5,chances=3)
        dpr_5[i] += once_per_turn_rider(level[i],AS_5[i],3.5,chances=2) + extra_dice(level[i],AS_5[i],4.5,chances=2)
    i=9
    dpr_1[i] = 2*shillelagh_attack(level[i],AS_1[i]) + 3*nick_attack(level[i],AS_1[i],twf=1)
    dpr_2[i] = 0.5*(3*gwm_attack(level[i],AS_2[i]) + 0.25*weapon_attack(level[i],AS_2[i],7)) + 0.5*(3*gwm_attack(level[i],AS_2[i],adv=2,crit_range=20))
    dpr_4[i] = 0.5*(shillelagh_attack(level[i],AS_3[i]) + 3*nick_attack(level[i],AS_3[i],twf=1)) + 0.5*(shillelagh_attack(level[i],AS_3[i],adv=2,crit_range=20) + 3*nick_attack(level[i],AS_3[i],twf=1,adv=2,crit_range=20))
    dpr_5[i] = 3*shillelagh_attack(level[i],AS_5[i],bonus=[0,2]+AS_5[i]) + extra_dice(level[i],AS_5[i],2*4.5,chances=3)
    dpr_1[i] += once_per_turn_rider(level[i],AS_1[i],3.5,chances=3)
    dpr_2[i] += once_per_turn_rider(level[i],AS_2[i],3.5,chances=5)
    dpr_4[i] += once_per_turn_rider(level[i],AS_4[i],3.5,chances=4)
    dpr_5[i] += once_per_turn_rider(level[i],AS_5[i],3.5,chances=3)

    plt.plot(level,dpr_2,'r-', label='GWM Bladelock')
    # plt.plot(level,dpr_1,'g-', label='DW Bladelock')
    # plt.plot(level,dpr_3,'y-', label='EB+AB Warlock')
    plt.plot(level,dpr_4,'b-', label='Nick+Shill Bladelock')
    plt.plot(level,dpr_5,'g-', label='TomeBladeLock')
    plt.plot(level,target,'b--')
    plt.plot(level,high,'b--')
    plt.legend()
    plt.show()

if 0:
    # DW Paladin
    target =[10.8,12.1,13.3,14.6,15.8,17.1,18.3,19.6,20.8,22.1]	
    high =  [21.7,24.2,26.7,29.2,31.7,34.2,36.7,39.2,41.7,44.2]
    index = [0,1,2,3,4,5, 6, 7, 8, 9]
    level = [4,5,6,7,8,9,10,11,12,13]
    AS_1 =  [4,4,4,4,4,5, 5, 5, 5, 5] # EA Soulknife Pala
    AS_2 =  [3,3,4,4,4,4, 5, 5, 5, 5] # EA Warlock Blade Pact + Tome + AB Shillelagh
    AS_3 =  [4,4,4,4,4,4, 4, 4, 4, 5] # EA+DW feat
    AS_4 =  [4,4,4,4,5,5, 5, 5, 5, 5] # EA feat dex
    AS_5 =  [4,4,4,4,4,5, 5, 5, 5, 5] # EA Soulknife Champion
    AS_6 =  [3,3,3,3,3,4, 4, 4, 4, 5] # PAM Shillelagh Warlock
    dpr_1 = np.zeros(np.size(level))
    dpr_2 = np.zeros(np.size(level))
    dpr_3 = np.zeros(np.size(level))
    dpr_4 = np.zeros(np.size(level))
    dpr_5 = np.zeros(np.size(level))
    dpr_6 = np.zeros(np.size(level))
    i=0
    dpr_1[i] = weapon_attack(level[i],AS_1[i],2.5+2.5,adv=3,bonus=[0,2]) + nick_attack(level[i],AS_1[i],die=2.5+2.5,twf=0,adv=3,bonus=[0,2])
    dpr_3[i] = (1+2/3)*weapon_attack(level[i],AS_3[i],4.5+2.5,adv=2) + nick_attack(level[i],AS_3[i],die=3.5+2.5,twf=1,adv=2)
    dpr_4[i] = weapon_attack(level[i],AS_3[i],4.5+2.5,adv=3) + nick_attack(level[i],AS_3[i],die=3.5+2.5,twf=1,adv=3)
    dpr_2[i] = shillelagh_attack(level[i],AS_2[i],adv=1,bonus=AS_2[i]) + extra_dice(level[i],AS_2[i],2.5,adv=1) + nick_attack(level[i],AS_2[i],die=3.5+2.5,twf=1,adv=1)
    dpr_5[i] = weapon_attack(level[i],AS_5[i],2.5,adv=3,crit_range=2,bonus=[0,2]) + nick_attack(level[i],AS_5[i],die=2.5,twf=0,adv=3,crit_range=2,bonus=[0,2])
    dpr_6[i] = shillelagh_attack(level[i],AS_6[i],adv=1,bonus=AS_6[i]+2) 
    for i in range(1,2):
        dpr_6[i] = shillelagh_attack(level[i],AS_6[i],adv=1,bonus=AS_6[i]+2) + weapon_attack(level[i],AS_6[i],2.5,bonus=AS_6[i]+2)
        dpr_2[i] = shillelagh_attack(level[i],AS_2[i],adv=2,bonus=AS_2[i]) + extra_dice(level[i],AS_2[i],2.5,adv=2) + nick_attack(level[i],AS_2[i],die=3.5+2.5,twf=1,adv=2)
    for i in range(2,9):
        dpr_6[i] = 2*shillelagh_attack(level[i],AS_6[i],adv=1,bonus=AS_6[i]+2) + weapon_attack(level[i],AS_6[i],2.5,bonus=AS_6[i]+2)
    for i in range(2,3):
        dpr_2[i] = shillelagh_attack(level[i],AS_2[i],adv=3,bonus=AS_2[i]) + extra_dice(level[i],AS_2[i],2.5,adv=3) + nick_attack(level[i],AS_2[i],die=3.5+2.5,twf=1,adv=3)
    for i in range(1,4):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],2.5+2.5,adv=3,bonus=[0,2]) + nick_attack(level[i],AS_1[i],die=2.5+2.5,twf=0,adv=3,bonus=[0,2])
        dpr_3[i] = (2+2/3)*weapon_attack(level[i],AS_3[i],4.5+2.5,adv=2) + nick_attack(level[i],AS_3[i],die=3.5+2.5,twf=1,adv=2)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],3.5+2.5,adv=3) + nick_attack(level[i],AS_4[i],die=3.5+2.5,twf=1,adv=3)
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i],2.5,adv=3,crit_range=2,bonus=[0,2]) + nick_attack(level[i],AS_5[i],die=2.5,twf=0,adv=3,crit_range=2,bonus=[0,2])
    for i in range(2,4): 
        dpr_1[i] += sneak_attack(level[i],AS_1[i],np.ceil((level[i]-5)/2),adv=3,chances=3)
        dpr_5[i] += sneak_attack(level[i],AS_5[i],np.ceil((level[i]-5)/2),adv=3,chances=3,crit_range=2)
    for i in range(3,9): 
        dpr_2[i] = 2*shillelagh_attack(level[i],AS_2[i],adv=3,bonus=AS_2[i]) + extra_dice(level[i],AS_2[i],2.5,adv=3,chances=2) + nick_attack(level[i],AS_2[i],die=3.5+2.5,twf=1,adv=3)
    for i in range(4,7):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5+2.5,adv=3,bonus=[0,2]) + weapon_attack(level[i],AS_1[i],2.5+2.5,adv=3,bonus=[0,2]) + sneak_attack(level[i],AS_1[i],np.ceil((level[i]-5)/2),adv=3,chances=3)
        dpr_3[i] = dpr_2[i]
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],3.5+2.5,adv=3) + nick_attack(level[i],AS_4[i],die=3.5+2.5,twf=1,adv=3)
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i],3.5,adv=3,bonus=[0,2],crit_range=2) + weapon_attack(level[i],AS_5[i],2.5,adv=3,bonus=[0,2],crit_range=2) + sneak_attack(level[i],AS_5[i],np.ceil((level[i]-5)/2),adv=3,chances=3,crit_range=2)
    for i in range(7,np.size(level)):
        dpr_1[i] = 2*weapon_attack(level[i],AS_1[i],3.5+2.5,adv=3,bonus=[0,2]) + weapon_attack(level[i],AS_1[i],2.5+2.5,adv=3,bonus=[0,2]) + sneak_attack(level[i],AS_1[i],np.ceil((level[i]-5)/2),adv=3,chances=3)
        dpr_3[i] = (2+2/3)*weapon_attack(level[i],AS_2[i],4.5+2.5+4.5,adv=3) + nick_attack(level[i],AS_2[i],die=3.5+2.5+4.5,twf=1,adv=3)
        dpr_4[i] = 2*weapon_attack(level[i],AS_4[i],3.5+2.5+4.5,adv=3) + nick_attack(level[i],AS_4[i],die=3.5+2.5+4.5,twf=1,adv=3)
        dpr_5[i] = 2*weapon_attack(level[i],AS_5[i],3.5,adv=3,bonus=[0,2],crit_range=2) + weapon_attack(level[i],AS_5[i],2.5,adv=3,bonus=[0,2],crit_range=2) + sneak_attack(level[i],AS_5[i],np.ceil((level[i]-5)/2),adv=3,chances=3,crit_range=2)
    i=9
    dpr_2[i] = 2*shillelagh_attack(level[i],AS_2[i],adv=3,bonus=AS_2[i]) + extra_dice(level[i],AS_2[i],2.5+4.5,adv=3,chances=2) + nick_attack(level[i],AS_2[i],die=3.5+2.5+4.5,twf=1,adv=3)
    dpr_6[i] = 3*shillelagh_attack(level[i],AS_6[i],adv=1,bonus=AS_6[i]+2) + weapon_attack(level[i],AS_6[i],2.5,bonus=AS_6[i]+2)


    # plt.plot(level,dpr_1,'r-', label='Soulknife Pala')
    # plt.plot(level,dpr_2,'g-', label='EA + Warlock 2')
    # plt.plot(level,dpr_3,'b-.', label='DW+TWF -> EA')
    plt.plot(level,dpr_4,'y-.', label='EA only')
    # plt.plot(level,dpr_5,'g--', label='SoulChamp')
    plt.plot(level,dpr_6,'r-.', label='PAM Warlock')
    plt.plot(level,target,'--')
    plt.plot(level,high,'--')
    plt.legend()
    plt.show()