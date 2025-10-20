import random
hand      = {1:"グー", 2:"チョキ", 3:"パー"} 
judge     = {0:"負け", 1:"あいこ", 2:"勝ち"} 
direction = {1:"↑", 2:"→", 3:"↓", 4:"←"} 


# じゃんけん関数
def r_p_s(player_hand):
    cp_hand = random.randint(1,3)
    print("コンピュータの手 " + hand[cp_hand])
    if player_hand == 1: # プレイヤーがグー出してたら
        if cp_hand == 1: # コンピュータ グー 
            return 1
        if cp_hand == 2: # コンピュータ チョキ
            return 2
        if cp_hand == 3: # コンピュータ パー
            return 0
    elif player_hand == 2: # プレイヤーがチョキ出してたら
        if cp_hand == 1: # コンピュータ グー 
            return 0
        if cp_hand == 2: # コンピュータ チョキ
            return 1
        if cp_hand == 3: # コンピュータ パー
            return 2
    elif player_hand == 3: # プレイヤーがパー出してたら
        if cp_hand == 1: # コンピュータ グー 
            return 2
        if cp_hand == 2: # コンピュータ チョキ
            return 0
        if cp_hand == 3: # コンピュータ パー
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
    player_hand = int(input("あなたの手を入力してください グー:1 チョキ:2 パー:3 \n"))
    rock_paper_scissors_result = r_p_s(player_hand)
    print() # 見やすくするために改行
    if rock_paper_scissors_result == 2: # 勝ってたら
        print("じゃんけんに勝ちました！")
        player_choice = int(input("指をどっちに向けますか？ ↑:1 →:2 ↓:3 ←:4 \n"))
        look_that_way_result = a_m_h(player_choice)
        if look_that_way_result == 1: # あっちむいてほい勝った
            print("あなたの勝ちです！")
            break
        else: 
            print("ハズレです ><")
    elif rock_paper_scissors_result == 1: # あいこ
        print("あいこです！")
    elif rock_paper_scissors_result == 0: # 負け
        print("じゃんけんに負けました ><")
        player_choice = int(input("頭をどっちに向けますか？ ↑:1 →:2 ↓:3 ←:4 \n"))
        look_that_way_result = a_m_h(player_choice)
        if look_that_way_result == 1: # あっちむいてほい負け
            print("あなたの負けです！")
            break
        else: 
            print("セーフ！ ")
    print("") # 見やすくするために改行