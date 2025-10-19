import random
hand      = {0:"グー", 1:"チョキ", 2:"パー"} 
judge     = {0:"負け", 1:"あいこ", 2:"勝ち"} 
direction = {0:"↑", 1:"→", 2:"↓", 3:"←"} 

# じゃんけんをする
# 勝ち   2
# あいこ 1
# 負け   0
def rock_paper_scissors(player_hand):
    cp_hand = random.randint(0,2)
    print("コンピュータの手 " + hand[cp_hand])
    if player_hand == 0: # プレイヤーがグー出してたら
        if cp_hand == 0: # コンピュータ グー 
            return 1
        if cp_hand == 1: # コンピュータ チョキ
            return 2
        if cp_hand == 2: # コンピュータ パー
            return 0
    elif player_hand == 1: # プレイヤーがチョキ出してたら
        if cp_hand == 0: # コンピュータ グー 
            return 0
        if cp_hand == 1: # コンピュータ チョキ
            return 1
        if cp_hand == 2: # コンピュータ パー
            return 2
    elif player_hand == 2: # プレイヤーがパー出してたら
        if cp_hand == 0: # コンピュータ グー 
            return 2
        if cp_hand == 1: # コンピュータ チョキ
            return 0
        if cp_hand == 2: # コンピュータ パー
            return 1

# あっちむいてほいをする
# 同じ向き 1
# 違う向き 0
def look_that_way(player_choice):
    cp_choice = random.randint(0,3)
    print("コンピュータの選択 " + direction[cp_choice])
    if player_choice == cp_choice:  
        return 1
    else:
        return 0
    return

# 勝ち あなたの勝ちです と表示
# あいこ もう一回じゃんけんする
# 負け あなたの負けです と表示
print("あっちむいてほいをしましょう！")
while True:
    player_hand = int(input("あなたの手を入力してください グー:0 チョキ:1 パー:2 \n"))
    rock_paper_scissors_result = rock_paper_scissors(player_hand)
    print() # 見やすくするために改行
    if rock_paper_scissors_result == 2: # 勝ってたら
        print("じゃんけんに勝ちました！")
        player_choice = int(input("指をどっちに向けますか？ ↑:0 →:1 ↓:2 ←:3 \n"))
        look_that_way_result = look_that_way(player_choice)
        if look_that_way_result == 1: # あっちむいてほい勝った
            print("あなたの勝ちです！")
            break
        else: 
            print("ハズレです ><")
    elif rock_paper_scissors_result == 1: # あいこ
        print("あいこです！")
    elif rock_paper_scissors_result == 0: # 負け
        print("じゃんけんに負けました ><")
        player_choice = int(input("頭をどっちに向けますか？ ↑:0 →:1 ↓:2 ←:3 \n"))
        look_that_way_result = look_that_way(player_choice)
        if look_that_way_result == 1: # あっちむいてほい負け
            print("あなたの負けです！")
            break
        else: 
            print("セーフ！ ")
    print("") # 見やすくするために改行