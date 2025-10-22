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


print("あっちむいてほいをしましょう！")
while True:
    player_hand = int(input("あなたの手を入力してください グー:1 チョキ:2 パー:3 やめる:4\n"))
    if player_hand == 4:
        break
    else:
        while True:
            r_p_s_result = r_p_s(player_hand)
            print()
            if r_p_s_result == 2:
                print("じゃんけんに勝ちました！")
                player_choice = int(input("指をどっちに向けますか？ ↑:1 →:2 ↓:3 ←:4 \n"))
                a_m_h_result = a_m_h(player_choice)
                if a_m_h_result == 1:
                    print("あなたの勝ちです！")
                    break
                else: 
                    print("ハズレです ><")
                    break
            elif r_p_s_result == 1: 
                print("あいこです！")
            elif r_p_s_result == 0:
                print("じゃんけんに負けました ><")
                player_choice = int(input("頭をどっちに向けますか？ ↑:1 →:2 ↓:3 ←:4 \n"))
                a_m_h_result = a_m_h(player_choice)
                if a_m_h_result == 1:
                    print("あなたの負けです！")
                    break
                else: 
                    print("セーフ！ ")
                    break
    print("")