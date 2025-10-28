import random
import numpy as np
hand      = {1:"グー", 2:"チョキ", 3:"パー"} 
judge     = {0:"負け", 1:"あいこ", 2:"勝ち"} 
direction = {1:"↑", 2:"→", 3:"↓", 4:"←"} 
round = 9

# じゃんけん関数
def r_p_s(player_hand):
    cp_hand = random.randint(1,3)
    print("コンピュータ:" + hand[cp_hand], "VS プレイヤー:" + hand[player_hand], file=f)
    if player_hand == 1: 
        if cp_hand == 1: 
            return 1
        if cp_hand == 2: 
            return 2
        if cp_hand == 3: 
            return 0
    elif player_hand == 2: 
        if cp_hand == 1:  
            return 0
        if cp_hand == 2: 
            return 1
        if cp_hand == 3: 
            return 2
    elif player_hand == 3: 
        if cp_hand == 1:  
            return 2
        if cp_hand == 2: 
            return 0
        if cp_hand == 3: 
            return 1


# あっちむいてほい関数
def a_m_h(player_choice):
    cp_choice = random.randint(1,4)
    print("コンピュータ:" + direction[cp_choice], "VS プレイヤー:" + direction[player_choice], file=f)
    if player_choice == cp_choice:  
        return 1
    else:
        return 0
    return


print("あっち向いてホイ開始")
f = open('AMH_result.txt', 'w', encoding='UTF-8')
pl_hands =np.loadtxt(r'D:\VSCode\Github\A_M_H\handirection.txt', dtype='int64', skiprows=1, usecols=[0])
pl_choices =np.loadtxt(r'D:\VSCode\Github\A_M_H\handirection.txt', dtype='int64', skiprows=1, usecols=[1])
for i in range(round):
    player_hand = pl_hands[i]
    player_choice = pl_choices[i]
    while True:
        r_p_s_result = r_p_s(player_hand)
        if r_p_s_result == 2:
            f.write('アタックフェーズ\n')
            a_m_h_result = a_m_h(player_choice)
            if a_m_h_result == 1:
                f.write('プレイヤーの勝利\n')
                break
            else: 
                f.write('倒しきれなかった\n')
                break
        elif r_p_s_result == 1: 
            f.write('あいこ\n')
        elif r_p_s_result == 0:
            f.write('ガードフェーズ\n')
            a_m_h_result = a_m_h(player_choice)
            if a_m_h_result == 1:
                f.write('プレイヤーの敗北\n')
                break
            else:
                f.write('攻撃を凌いだ\n')
                break
    print("", file=f)
f.close()
print("あっち向いてホイ終了")