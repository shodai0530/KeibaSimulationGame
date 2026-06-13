#応用課題２ 競馬シミュレーションゲーム
#2023-01-06 02220795　鈴木頌大
import tkinter as tk
import random
import numpy as np
from tkinter import messagebox

rw = tk.Tk()
rw.title("競馬Simulation Game 「大破産」")
rw.geometry("400x350")

cw = tk.Canvas(rw,
               width = 400,
               height = 400,
               bg = "green")
cw.place(x = 0, y = 0)
dw = tk.Canvas(rw,
               width = 400,
               height = 33,
               bg = "darkblue")
dw.place(x = 0, y = 190)

ew = tk.Canvas(rw,
               width = 400,
               height = 200,
               bg = "black")
ew.place(x = 0, y = 222)

horse_num = []
for i in range(9):
    horse_num.append(tk.Label(rw,
    relief = 'raised'))
    
racehorse = []
for i in range(9):
    racehorse.append(tk.Label(rw,
    relief = 'sunken'))
    
horse_odds_win = []
for i in range(9):
    horse_odds_win.append(tk.Label(rw,
    relief = 'sunken'))
    
horse_odds_show = []
for i in range(9):
    horse_odds_show.append(tk.Label(rw,
    relief = 'sunken'))
    
racecourse = ['東京','中山','阪神','京都','札幌','函館','福島','新潟','小倉']
color = ['white','black','red','blue','yellow','green','orange','magenta']
color_c = ['black','white','white','white','black','white','white','white']
       

jra = ['ナランフレグ','ポタジェ','スターズオンアース','ジオグリフ','タイトルホルダー','ダノンスコーピオン','ソダシ','ドウデュース',
'ソングライン','スタニングローズ','アスクビクターモア','イクイノックス','ジェラルディーナ','セリフォス','ヴェラアズール','リバティアイランド',
'ドルチェモア','ドゥラエレーデ','レッドガラン','ザダル','マテンロウオリオン','ライラック','ルビーカサブランカ','オニャンコポン','ヨーホーレイク','キングオブコージ','メイケイエール',
'イルーシヴパンサー','マテンロウレオ','プレサージュリフト','ダノンベルーガ','アフリカンゴールド','テーオーロイヤル','ロータスランド','アリーヴォ','パンサラッサ','ダイアトニック',
'ジャンダルム','クリノプレミアム','サブライムアンセム','ジャックドール','プルパレイ','ビーアストニッシド','ディープボンド','ピースオブエイト','タイムトゥヘヴン','ジャングロ',
'メイショウミモザ','アナザーリリック','エリカヴィータ','ソウルラッシュ','プラダリア','アスクワイルドモア','テーオーケインズ','ウインマーベル','ボッケリーニ','ヴェルトライゼンデ',
'ソングライン','ノースブリッジ','ナムラクレア','ウインマイティ―','フェーングロッテン','テイエムスパーダ','エヒト','ブトンドール','ハヤヤッコ','ベレヌス','ビリーバー','テルツェット',
'ウインカーネリアン','マリアエレーナ','ボンボヤージ','キタウイング','ヴェントヴォーチェ','ドゥーラ','カラテ','ロンドンプラン','ファルコニア','アートハウス','ガイアフォース',
'ジャスティンパレス','サリオス','イズジョーノキセキ','ラヴェル','オオバンブルマイ','リバーラ','ブレークアップ','オールパルフェ','ユニコーンライオン','ガストリック','グリューネグリーン',
'トウシンマカオ','シルヴァーソニック','ソーヴァリアント','キラーアビリティ','リメイク','ミスニューヨーク']

def keiba():
    uma_2022 = random.sample(jra, k=8)


    odds_first = 1 #乱数の逆数
    odds_save = 1 #オッズの全体
    odds_place_first = 0
    
    global odds_win #単勝オッズのリストのグローバル関数
    odds_win = [] #リストの生成
    for i in range(8): #8回操作を行う
        odds_first = odds_save / random.randint(1,5) #1~20までの乱数を生成し、割り算をする
        odds_win.append(odds_first) #割り算して得られた数をリストに格納する
        odds_save = 1 - odds_first #全体から乱数で割った数を引き算する
    
    odds_show_1 = []
    for i in range(8):
        odds_place_first= 3 * odds_win[i]
        if 0 < odds_place_first < 1:
            odds_show_1.append(1 / odds_place_first)
        else:
            odds_show_1.append(1.0)
    
    global odds_show
    odds_show = [round(odds_show_1[i], 1) for i in range(len(odds_show_1))]
    
    horse_num[0].grid(column = 0, row = 0)
    horse_num[0].configure(text = '馬番')
    racehorse[0].grid(column = 1, row = 0, sticky = 'ew')
    racehorse[0].configure(text = '競走馬名', relief = 'raised')
    horse_odds_win[0].grid(column = 2, row = 0, sticky = 'ew')
    horse_odds_win[0].configure(text = '単勝オッズ', relief = 'raised')
    horse_odds_show[0].grid(column = 3, row = 0, sticky = 'ew')
    horse_odds_show[0].configure(text = '複勝オッズ', relief = 'raised')

    for i in range(8):
        horse_num[i+1].grid(column = 0, row = i + 1, sticky = 'ew')
        horse_num[i+1].configure(text = i + 1, fg = color_c[i], bg = color[i])
        racehorse[i+1].grid(column = 1, row = i + 1, sticky = 'ew')
        racehorse[i+1].configure(text = uma_2022[i])
        horse_odds_win[i+1].grid(column = 2, row = i + 1, sticky = 'ew')
        horse_odds_win[i+1].configure(text = f'{1 / odds_win[i]:.1f}')
        horse_odds_show[i+1].grid(column = 3, row = i + 1, sticky = 'ew')
        horse_odds_show[i+1].configure(text = f'{odds_show[i]:.1f}')
        #uma = tk.Label(text = uma_2022[i])
        #uma.place(x = 30, y = (i + 1) * 21)
    
    dw = tk.Canvas(rw,
               width = 400,
               height = 33,
               bg = "darkblue")
    dw.place(x = 0, y = 190)
    
    keibajo = tk.Label(text = random.choice(racecourse), font = 'micho 12 bold', bg = 'darkblue', fg = 'white')
    keibajo.place(x=10, y=195)
    
    race_num = tk.Label(text = '{:>3d}R'.format(random.randint(1,12)), font = 'micho 12 bold', bg = 'darkblue', fg = 'white')
    race_num.place(x = 50, y = 195)
    
    haraimodoshi = tk.Label(text = '払戻金', font = 'micho 12 bold', bg = 'darkblue', fg = 'white')
    haraimodoshi.place(x = 330, y = 195)
    
    


keiba()

first_money = 1000 #所持金の初期値
first_bet_money = 1 #ベット額の初期値
pla_min = 0 #収支の初期値

umaban = tk.Label(text='馬番')
umaban.place(x=240, y=10)

shojikin = tk.Label(text='所持金')
shojikin.place(x=240, y=160)

shushi = tk.Label(text='収支')
shushi.place(x=240, y=130)

kakekin = tk.Label(text='BET')
kakekin.place(x=240, y=40)



uma_num = tk.IntVar()
uma_num_box = tk.Spinbox(textvariable=uma_num, from_=1, to=8, increment=1, width=3)
uma_num_box.place(x=290, y=11)
uma_num_box.configure(state='readonly')

uma_money = tk.Entry(width=3)
uma_money.insert(0, first_bet_money)
uma_money.place(x=290, y=40)

uma_money_ex = tk.Entry(width=2)
uma_money_ex.insert(0, '00')
uma_money_ex.place(x=313, y=40)
uma_money_ex.configure(state='readonly')


plamin_money = tk.Entry(width=12)
plamin_money.place(x=300, y=130)
plamin_money.insert(0, pla_min)
plamin_money.configure(state='readonly')


total_money = tk.Entry(width=12)
total_money.place(x=300, y=160)
total_money.insert(0, first_money)
total_money.configure(state='readonly')









win = tk.Label(text ='単勝', relief = 'raised', fg='white', bg='blue')
win.place(x=10, y=230)
show = tk.Label(text ='複勝', relief = 'raised', fg='white', bg='red')
show.place(x=10, y=260)
quinella= tk.Label(text ='馬連', relief = 'raised', fg='white', bg='magenta')
quinella.place(x=10, y=290)
exacta= tk.Label(text ='馬単', relief = 'raised', fg='black', bg='yellow')
exacta.place(x=10, y=320)
trio= tk.Label(text ='三連複', relief = 'raised', fg='white', bg='mediumblue')
trio.place(x=150, y=290)
trifecta= tk.Label(text ='三連単', relief = 'raised', fg='black', bg='orange')
trifecta.place(x=150, y=320)




win_num = tk.Entry(width=3)
win_num.place(x=50, y=230)
win_num.configure(state='readonly')

win_name = tk.Entry(width=10)
win_name.place(x=80, y=230)
win_name.configure(state='readonly')



show_1_num = tk.Entry(width=3)
show_1_num.place(x=50, y=260)
show_1_num.configure(state='readonly')

show_1_name = tk.Entry(width=10)
show_1_name.place(x=80, y=260)
show_1_name.configure(state='readonly')

show_2_num = tk.Entry(width=3)
show_2_num.place(x=160, y=260)
show_2_num.configure(state='readonly')

show_2_name = tk.Entry(width=10)
show_2_name.place(x=190, y=260)
show_2_name.configure(state='readonly')

show_3_num = tk.Entry(width=3)
show_3_num.place(x=270, y=260)
show_3_num.configure(state='readonly')

show_3_name = tk.Entry(width=10)
show_3_name.place(x=300, y=260)
show_3_name.configure(state='readonly')



quinella_num_1 = tk.Entry(width=3)
quinella_num_1.place(x=50, y=290)
quinella_num_1.configure(state='readonly')

quinella_num_2 = tk.Entry(width=3)
quinella_num_2.place(x=100, y=290)
quinella_num_2.configure(state='readonly')

label_q = tk.Label(text='―', fg='white', bg='black')
label_q.place(x=78, y=290)



exacta_num_1 = tk.Entry(width=3)
exacta_num_1.place(x=50, y=320)
exacta_num_1.configure(state='readonly')

exacta_num_2 = tk.Entry(width=3)
exacta_num_2.place(x=100, y=320)
exacta_num_2.configure(state='readonly')

label_e = tk.Label(text='＞', fg='white', bg='black')
label_e.place(x=78, y=320)



trio_num_1 = tk.Entry(width=3)
trio_num_1.place(x=200, y=290)
trio_num_1.configure(state='readonly')

trio_num_2 = tk.Entry(width=3)
trio_num_2.place(x=250, y=290)
trio_num_2.configure(state='readonly')

trio_num_3 = tk.Entry(width=3)
trio_num_3.place(x=300, y=290)
trio_num_3.configure(state='readonly')

label_trio_1 = tk.Label(text='―', fg='white', bg='black')
label_trio_1.place(x=228, y=290)

label_trio_2 = tk.Label(text='―', fg='white', bg='black')
label_trio_2.place(x=278, y=290)



trifecta_num_1 = tk.Entry(width=3)
trifecta_num_1.place(x=200, y=320)
trifecta_num_1.configure(state='readonly')

trifecta_num_2 = tk.Entry(width=3)
trifecta_num_2.place(x=250, y=320)
trifecta_num_2.configure(state='readonly')

trifecta_num_3 = tk.Entry(width=3)
trifecta_num_3.place(x=300, y=320)
trifecta_num_3.configure(state='readonly')

label_trifecta_1 = tk.Label(text='＞', fg='white', bg='black')
label_trifecta_1.place(x=228, y=320)

label_trifecta_2 = tk.Label(text='＞', fg='white', bg='black')
label_trifecta_2.place(x=278, y=320)


def buy_win():
    win_1_horse = np.random.choice(8, 1, odds_win)
    win_1st_horse = win_1_horse[0] + 1
    while True:
        win_2_horse = np.random.choice(8, 1, odds_win)
        if win_2_horse != win_1_horse:
            win_2nd_horse = win_2_horse[0] + 1
            break
    while True:
        win_3_horse = np.random.choice(8, 1, odds_win)
        if win_3_horse != win_1_horse and win_3_horse != win_2_horse:
            win_3rd_horse = win_3_horse[0] + 1
            break
    
    win_num.configure(state='normal')
    win_num.delete(0, tk.END)
    win_num.insert(0, win_1st_horse)
    win_num.configure(state='readonly')
    
    show_1_num.configure(state='normal')
    show_1_num.delete(0, tk.END)
    show_1_num.insert(0, win_1st_horse)
    show_1_num.configure(state='readonly')
    
    show_2_num.configure(state='normal')
    show_2_num.delete(0, tk.END)
    show_2_num.insert(0, win_2nd_horse)
    show_2_num.configure(state='readonly')
    
    show_3_num.configure(state='normal')
    show_3_num.delete(0, tk.END)
    show_3_num.insert(0, win_3rd_horse)
    show_3_num.configure(state='readonly')
    
    quinella_num_1.configure(state='normal')
    quinella_num_1.delete(0, tk.END)
    quinella_num_1.insert(0, win_1st_horse)
    quinella_num_1.configure(state='readonly')
    
    quinella_num_2.configure(state='normal')
    quinella_num_2.delete(0, tk.END)
    quinella_num_2.insert(0, win_2nd_horse)
    quinella_num_2.configure(state='readonly')
    
    exacta_num_1.configure(state='normal')
    exacta_num_1.delete(0, tk.END)
    exacta_num_1.insert(0, win_1st_horse)
    exacta_num_1.configure(state='readonly')
    
    exacta_num_2.configure(state='normal')
    exacta_num_2.delete(0, tk.END)
    exacta_num_2.insert(0, win_2nd_horse)
    exacta_num_2.configure(state='readonly')
    
    trio_num_1.configure(state='normal')
    trio_num_1.delete(0, tk.END)
    trio_num_1.insert(0, win_1st_horse)
    trio_num_1.configure(state='readonly')
    
    trio_num_2.configure(state='normal')
    trio_num_2.delete(0, tk.END)
    trio_num_2.insert(0, win_2nd_horse)
    trio_num_2.configure(state='readonly')
    
    trio_num_3.configure(state='normal')
    trio_num_3.delete(0, tk.END)
    trio_num_3.insert(0, win_3rd_horse)
    trio_num_3.configure(state='readonly')
    
    trifecta_num_1.configure(state='normal')
    trifecta_num_1.delete(0, tk.END)
    trifecta_num_1.insert(0, win_1st_horse)
    trifecta_num_1.configure(state='readonly')
    
    trifecta_num_2.configure(state='normal')
    trifecta_num_2.delete(0, tk.END)
    trifecta_num_2.insert(0, win_2nd_horse)
    trifecta_num_2.configure(state='readonly')
    
    trifecta_num_3.configure(state='normal')
    trifecta_num_3.delete(0, tk.END)
    trifecta_num_3.insert(0, win_3rd_horse)
    trifecta_num_3.configure(state='readonly')
    
    money = int(total_money.get())
    havemoney = int(uma_money.get()) * 100
    set_money = money - havemoney
    uma_bangou = int(uma_num.get())
    
    win_name.configure(state='normal')
    win_name.delete(0, tk.END)
    win_name.insert(0, '{s}円'.format(s =int(100 * (1 / odds_win[win_1st_horse - 1]))))
    win_name.configure(state='readonly')
    
    show_1_name.configure(state='normal')
    show_1_name.delete(0, tk.END)
    show_1_name.insert(0, '{s}円'.format(s =int(100 * odds_show[win_1st_horse - 1])))
    show_1_name.configure(state='readonly')
    
    show_2_name.configure(state='normal')
    show_2_name.delete(0, tk.END)
    show_2_name.insert(0, '{s}円'.format(s =int(100 * odds_show[win_2nd_horse - 1])))
    show_2_name.configure(state='readonly')
    
    show_3_name.configure(state='normal')
    show_3_name.delete(0, tk.END)
    show_3_name.insert(0, '{s}円'.format(s =int(100 * odds_show[win_3rd_horse - 1])))
    show_3_name.configure(state='readonly')
    
    if win_1st_horse == uma_bangou:
        return_money = havemoney * round((1 / odds_win[win_1st_horse - 1]),1)
        total_money.configure(state='normal')
        total_money.delete(0, tk.END)
        total_money.insert(0, int(set_money) + int(return_money))
        total_money.configure(state='readonly')
        
        
        plamin_money.configure(state='normal')
        plamin_money.delete(0, tk.END)
        plamin_money.insert(0, int(return_money))
        plamin_money.configure(state='readonly')
        

    else:
        return_money = havemoney * round((1 / odds_win[win_1st_horse - 1]),1)
        total_money.configure(state='normal')
        total_money.delete(0, tk.END)
        total_money.insert(0, int(set_money))
        total_money.configure(state='readonly')
        
        plamin_money.configure(state='normal')
        plamin_money.delete(0, tk.END)
        plamin_money.insert(0, 0)
        plamin_money.configure(state='readonly')
    
    money_checker()

    


def buy_show():
    win_1_horse = np.random.choice(8, 1, odds_win)
    win_1st_horse = win_1_horse[0] + 1
    while True:
        win_2_horse = np.random.choice(8, 1, odds_win)
        if win_2_horse != win_1_horse:
            win_2nd_horse = win_2_horse[0] + 1
            break
    while True:
        win_3_horse = np.random.choice(8, 1, odds_win)
        if win_3_horse != win_1_horse and win_3_horse != win_2_horse:
            win_3rd_horse = win_3_horse[0] + 1
            break
        

    win_num.configure(state='normal')
    win_num.delete(0, tk.END)
    win_num.insert(0, win_1st_horse)
    win_num.configure(state='readonly')
    
    show_1_num.configure(state='normal')
    show_1_num.delete(0, tk.END)
    show_1_num.insert(0, win_1st_horse)
    show_1_num.configure(state='readonly')
    
    show_2_num.configure(state='normal')
    show_2_num.delete(0, tk.END)
    show_2_num.insert(0, win_2nd_horse)
    show_2_num.configure(state='readonly')
    
    show_3_num.configure(state='normal')
    show_3_num.delete(0, tk.END)
    show_3_num.insert(0, win_3rd_horse)
    show_3_num.configure(state='readonly')
    
    quinella_num_1.configure(state='normal')
    quinella_num_1.delete(0, tk.END)
    quinella_num_1.insert(0, win_1st_horse)
    quinella_num_1.configure(state='readonly')
    
    quinella_num_2.configure(state='normal')
    quinella_num_2.delete(0, tk.END)
    quinella_num_2.insert(0, win_2nd_horse)
    quinella_num_2.configure(state='readonly')
    
    exacta_num_1.configure(state='normal')
    exacta_num_1.delete(0, tk.END)
    exacta_num_1.insert(0, win_1st_horse)
    exacta_num_1.configure(state='readonly')
    
    exacta_num_2.configure(state='normal')
    exacta_num_2.delete(0, tk.END)
    exacta_num_2.insert(0, win_2nd_horse)
    exacta_num_2.configure(state='readonly')
    
    trio_num_1.configure(state='normal')
    trio_num_1.delete(0, tk.END)
    trio_num_1.insert(0, win_1st_horse)
    trio_num_1.configure(state='readonly')
    
    trio_num_2.configure(state='normal')
    trio_num_2.delete(0, tk.END)
    trio_num_2.insert(0, win_2nd_horse)
    trio_num_2.configure(state='readonly')
    
    trio_num_3.configure(state='normal')
    trio_num_3.delete(0, tk.END)
    trio_num_3.insert(0, win_3rd_horse)
    trio_num_3.configure(state='readonly')
    
    trifecta_num_1.configure(state='normal')
    trifecta_num_1.delete(0, tk.END)
    trifecta_num_1.insert(0, win_1st_horse)
    trifecta_num_1.configure(state='readonly')
    
    trifecta_num_2.configure(state='normal')
    trifecta_num_2.delete(0, tk.END)
    trifecta_num_2.insert(0, win_2nd_horse)
    trifecta_num_2.configure(state='readonly')
    
    trifecta_num_3.configure(state='normal')
    trifecta_num_3.delete(0, tk.END)
    trifecta_num_3.insert(0, win_3rd_horse)
    trifecta_num_3.configure(state='readonly')
    
    money = int(total_money.get())
    havemoney = int(uma_money.get()) * 100
    set_money = money - havemoney
    uma_bangou = int(uma_num.get())
    
    win_name.configure(state='normal')
    win_name.delete(0, tk.END)
    win_name.insert(0, '{s}円'.format(s =int(100 * round((1 / odds_win[win_1st_horse - 1]),1))))
    win_name.configure(state='readonly')
    
    show_1_name.configure(state='normal')
    show_1_name.delete(0, tk.END)
    show_1_name.insert(0, '{s}円'.format(s =int(100 * odds_show[win_1st_horse - 1])))
    show_1_name.configure(state='readonly')
    
    show_2_name.configure(state='normal')
    show_2_name.delete(0, tk.END)
    show_2_name.insert(0, '{s}円'.format(s =int(100 * odds_show[win_2nd_horse - 1])))
    show_2_name.configure(state='readonly')
    
    show_3_name.configure(state='normal')
    show_3_name.delete(0, tk.END)
    show_3_name.insert(0, '{s}円'.format(s =int(100 * odds_show[win_3rd_horse - 1])))
    show_3_name.configure(state='readonly')
    
    if uma_bangou == win_1st_horse:
        return_money = havemoney * (odds_show[win_1st_horse - 1])
        total_money.configure(state='normal')
        total_money.delete(0, tk.END)
        total_money.insert(0, int(set_money) + int(return_money))
        total_money.configure(state='readonly')
        
        
        plamin_money.configure(state='normal')
        plamin_money.delete(0, tk.END)
        plamin_money.insert(0, int(return_money))
        plamin_money.configure(state='readonly')
        

        
    elif uma_bangou == win_2nd_horse:
        return_money = havemoney * (odds_show[win_2nd_horse - 1])
        total_money.configure(state='normal')
        total_money.delete(0, tk.END)
        total_money.insert(0, int(set_money) + int(return_money))
        total_money.configure(state='readonly')
        
        
        plamin_money.configure(state='normal')
        plamin_money.delete(0, tk.END)
        plamin_money.insert(0, int(return_money))
        plamin_money.configure(state='readonly')
        

    
    elif uma_bangou == win_3rd_horse:
        return_money = havemoney * (odds_show[win_3rd_horse - 1])
        total_money.configure(state='normal')
        total_money.delete(0, tk.END)
        total_money.insert(0, int(set_money) + int(return_money))
        total_money.configure(state='readonly')
        
        
        plamin_money.configure(state='normal')
        plamin_money.delete(0, tk.END)
        plamin_money.insert(0, int(return_money))
        plamin_money.configure(state='readonly')
        

    else:    
        return_money = havemoney * (1 / odds_win[win_1st_horse - 1])
        total_money.configure(state='normal')
        total_money.delete(0, tk.END)
        total_money.insert(0, int(set_money))
        total_money.configure(state='readonly')
        
        plamin_money.configure(state='normal')
        plamin_money.delete(0, tk.END)
        plamin_money.insert(0, 0)
        plamin_money.configure(state='readonly')
    
    money_checker() 
        
        

def money_checker():
    if int(total_money.get()) <= 0:
        messagebox.showwarning('競馬Simulation Game 「大破産」','     ＿人人人人人＿\n      ＞　大破産　＜\n     ￣Y^Y^Y^Y￣\n\nゲームオーバー！\n所持金が0円になりました。Resetで最初からやり直す')
        button_2.place(x=350, y=40)
    elif int(total_money.get()) >= 10000:
        messagebox.showinfo('競馬Simulation Game 「大破産]','   ＿人人人人人人＿\n     ＞　億万長者　＜\n     ￣Y^Y^Y^Y^Y￣\n\nゲームクリア！！！\n所持金が10,000円を超えました！このまま自己ベストを目指そう！')
        keiba()
    else:
        keiba()

def select_buy():
    entryword = uma_money.get()
    if entryword.isalpha() == True:
        if uma_money.get() == 'cheat':
                button_5.place(x=350, y=70)
        elif uma_money.get() == 'supercheat':
                button_3.place(x=350, y=100)
        else:
            messagebox.showerror('競馬Simulation Game 「大破産」','入力エラー！\n半角数字を入力してください')
    else:
        if uma_money.get() > total_money.get():
            messagebox.showerror('競馬Simulation Game 「大破産」','購入金額オーバー！\n入力した金額が所持金を超えています')
        else:
            if radiobtn_status.get() == 0:
                buy_win()
            
            elif radiobtn_status.get() == 1:
                buy_show()


def clear():
    total_money.configure(state='normal')
    total_money.delete(0, tk.END)
    total_money.insert(0, first_money)
    total_money.configure(state='readonly')
        
        
    plamin_money.configure(state='normal')
    plamin_money.delete(0, tk.END)
    plamin_money.insert(0, 0)
    plamin_money.configure(state='readonly')
    button_2.place_forget()
  
def debt():
    calc_money = int(total_money.get())
    total_money.configure(state='normal')
    total_money.delete(0, tk.END)
    total_money.insert(0, calc_money + 1000)
    total_money.configure(state='readonly')  

def help():
    messagebox.showinfo('競馬Simulation Game','競馬Simulation Game 「大破産」\n     Ver.1.1.0 (build.20230127)\
        \n                    ～～～～～～～遊び方～～～～～～～\nどの競走馬が勝つか予想して、所持金を１万円にするとゲームクリア！\nただし、所持金が０円になったらゲームオーバー（破産）です\
        \n目指せ！競馬で億万長者！！！！！\
        \n馬番：競走馬の番号を選択\nBET：賭ける金額\n収支：当レースで獲得した払戻額\n所持金：今持っているお金\
        \n単勝：１着の馬を予想する買い方\n複勝：１～３着の馬を予想する買い方')
button_1 = tk.Button(rw,
                    text='購入',
                    command=select_buy)
button_1.place(x=350, y=10)

button_2 = tk.Button(rw,
                    text='Reset',
                    command=clear)


button_3 = tk.Button(rw,
                    text='Skip',
                    command=keiba)

button_4 = tk.Button(rw,
                    text='?',
                    command=help)
button_4.place(x=300, y=100)

button_5 = tk.Button(rw,
                    text='ATM',
                    command=debt)

radiobtn_status = tk.IntVar()
radiobtn_status.set(0)
radio_button1 = tk.Radiobutton(text='単勝', fg='blue', variable=radiobtn_status,
                               value=0)
radio_button1.place(x= 240, y=70)
radio_button2 = tk.Radiobutton(text='複勝', fg='red', variable=radiobtn_status,
                               value=1)
radio_button2.place(x= 240, y=100)


rw.mainloop()


