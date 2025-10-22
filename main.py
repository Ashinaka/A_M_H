import random

hand      = {1:"グー", 2:"チョキ", 3:"パー"} 
judge     = {0:"負け", 1:"あいこ", 2:"勝ち"} 
direction = {1:"↑", 2:"→", 3:"↓", 4:"←"} 


# じゃんけん関数
def r_p_s(player_hand):
    cp_hand = random.randint(1,3)
    print("コンピュータの手 " + hand[cp_hand])
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
    print("コンピュータの選択 " + direction[cp_choice])
    if player_choice == cp_choice:  
        return 1
    else:
        return 0
    return


print("あっち向いてホイ開始")
while True:
    player_hand = int(input("プレイヤーの手を入力 グー:1 チョキ:2 パー:3 やめる:4\n"))
    if player_hand == 4:
        break
    else:
        while True:
            r_p_s_result = r_p_s(player_hand)
            print()
            if r_p_s_result == 2:
                print("じゃんけんに勝利")
                player_choice = int(input("指の方向を入力 ↑:1 →:2 ↓:3 ←:4 \n"))
                a_m_h_result = a_m_h(player_choice)
                if a_m_h_result == 1:
                    print("プレイヤーの勝利")
                    break
                else: 
                    print("ハズレ")
                    break
            elif r_p_s_result == 1: 
                print("あいこ")
            elif r_p_s_result == 0:
                print("じゃんけんに敗北")
                player_choice = int(input("頭の方向を入力 ↑:1 →:2 ↓:3 ←:4 \n"))
                a_m_h_result = a_m_h(player_choice)
                if a_m_h_result == 1:
                    print("プレイヤーの敗北")
                    break
                else: 
                    print("セーフ")
                    break
    print("")