import tkinter
import pymysql
import random
import tkinter.messagebox
from PIL import Image,ImageTk
import hashlib
from os import startfile

# 播放电脑现有的视频
class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        # Python标准库os中的方法startfile（)可以用来打开外部程序或文件，系统会自动关联相应的程序来打开
        startfile(self.path)

class Movie_MP4(Video):
    type = 'MP4'

def summarize():
    # res=random.randint(1,6)
    movie = Movie_MP4('自己本机视频')
    movie.play()

# 下面有重复代码,tk_Label的
def repetition_Label_code(name,windown,text,width_num,x_mes,y_mes):
    name = tkinter.Label(windown, text=text, bg='orange', fg='green', width=width_num, font=('', '20', ''))
    name.place(x=x_mes, y=y_mes)

# 下面有重复代码,tk_Button的
def repetition_Button_code(name,windown,text,width_num,font_num,def_command,x_mes,y_mes):
    name = tkinter.Button(windown, text=text, bg='orange', fg='green', width=width_num, font=('', font_num, ''),command=def_command)
    name.place(x=x_mes, y=y_mes)

# 号码和验证码
j = 5
res = []
res = ''.join(str(i) for i in random.sample(range(0, 9), j))   #sample(res,n) 从序列res中选择n个随机且独立的元素

# 使看不懂 md5
def encryption(args):
    md5=hashlib.md5()
    md5.update(args.encode('utf8'))
    strmd5=md5.hexdigest()
    return strmd5

conn=pymysql.connect(host='ip地址',port='端口号',user='用户名',password='密码',db='数据库名')
cursor=conn.cursor()
# -----------------------------------------------------------------------------------------------------
# 充钱类
class Prepaid:
    def __init__(self,name,tele,balance,wind):
        self.name=name
        self.tele=tele
        self.balance=balance
        self.wind=wind
    # 充值界面
    def prepaid_phone_interface(self):
        self.wind = tkinter.Tk()
        self.wind.title('充值')
        self.wind.geometry('600x800')
        path2 = Image.open(r'D:\practice.jpg')
        phone2 = ImageTk.PhotoImage(path2)
        labe16 = tkinter.Label(self.wind, image=phone2, height=0, width=0, compound='left')
        labe16.place(relx=0, rely=0)
        repetition_Label_code('label7',self.wind,'name',5,150,200)
        self.name = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=8, font=('', '20', ''))
        self.name.place(x=230, y=200)
        repetition_Label_code('label11',self.wind,'password',10,90,260)
        self.tele = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=8, font=('', '20', ''),show='*')
        self.tele.place(x=230, y=260)
        repetition_Label_code('label21',self.wind,'balance',10,83,320)
        self.balance = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=8, font=('', '20', ''))
        self.balance.place(x=230, y=320)
        repetition_Button_code('entery21',self.wind,'确定',8,20,self.recharge,190,370)
        repetition_Label_code('label0',self.wind,'十元一个月',12,170,430)
        self.wind.mainloop()

    # 充值功能
    def recharge(self):
        a=self.balance.get()
        b=self.name.get()
        c=self.tele.get()
        x=encryption(b)
        n=encryption(c)
        sql = "update watch_register set balance=%s where name=%s and passwor=%s ;"
        val = (a,x,n)
        rres=cursor.execute(sql, val)
        conn.commit()
        if rres:
            label3 = tkinter.Label(self.wind, text='充入成功', bg='red', fg='black')
            label3.place(x=350, y=325)
        else:
            label3 = tkinter.Label(self.wind, text='充入失败', bg='red', fg='black')
            label3.place(x=350, y=325)
# -----------------------------------------------------------------------------------------
class Watch:
    def __init__(self,inner,watch_what,name,balance,wind,mess):
        self.inner=inner
        self.watch_what=watch_what
        self.name=name
        self.balance=balance
        self.wind=wind
        self.mess=mess
#
    # 电视剧
    def tv_mes(self,swind):
        text = tkinter.Text(swind, width=30, height=15, bg='white', font=('', '15', ''))
        text.pack()
        self.inner = {}
        self.inner['  <<免费电视剧>>  '] = ['三生三世十里桃花', '因为遇见你', '快把我哥带走', '最好的我们', '家有儿女', '香蜜沉沉烬如霜', '少年派']
        self.inner['   <<VIP电视剧>>  '] = ['花千骨', '青云志', '青云志2', '西游记', '三国演义', '水浒传', '红楼梦', '马卡龙少女', '橘生淮南']
        self.inner['   <<免费电影>>   '] = ['天长地久', '夏洛特烦恼', '一见倾情', '何以为家', '前任3', '双生', '下一任：前任', '宋慈洗冤录']
        self.inner['    <<VIP电影>>    '] = ['大话西游', '李茶的姑妈', '羞羞哒铁拳', '三打白骨精', '洗罪', '反贪风暴4', '反贪风暴3']
        str = self.inner
        text.insert(tkinter.INSERT, str)

    #看界面
    def watch_tv(self):
        wind = tkinter.Tk()
        wind.title('看')
        wind.geometry('600x800')
        path2 = Image.open(r'D:\practice.jpg')
        phone2 = ImageTk.PhotoImage(path2)
        labe16 = tkinter.Label(wind, image=phone2, height=0, width=0, compound='left')
        labe16.place(relx=0, rely=0)
        self.tv_mes(wind)
        repetition_Label_code('label7', wind, '请输入你要观看的', 15, 83, 330)
        self.watch_what = tkinter.Entry(wind, text='', bg='orange', fg='green', width=15, font=('', '20', ''))
        self.watch_what.place(x=300, y=332)
        repetition_Label_code('label7', wind, '输入一句话', 15, 83, 390)
        self.mess = tkinter.Entry(wind, text='', bg='orange', fg='green', width=20, font=('', '20', ''))
        self.mess.place(x=300, y=390)
        repetition_Button_code('entery21', wind, '确定', 8, 20, self.judge_whether_charge, 240, 440)
        wind.mainloop()

    # 判断是否充过钱
    def judge_whether_charge(self):
        res=self.mess.get()
        rres=cursor.execute('select * from watch_register where mes=%s',(res))
        if (res=='') or (not rres):
            tkinter.messagebox.showinfo('提示','输入不规范!!!')
        else:
            res=self.watch_what
            if res.get() in self.inner['  <<免费电视剧>>  ']or res.get() in self.inner['   <<免费电影>>   ']:
                self.show_free()
            elif res.get() in self.inner['   <<VIP电视剧>>  '] or res.get() in self.inner['    <<VIP电影>>    ']:
                self.show_VIP()
            else:
                tkinter.messagebox.showinfo('提示', '小哥,暂无此影片!')

    # 免费电视剧,电影界面
    def show_free(self):
        summarize()

    #VIP电视剧,电影界面
    def show_VIP(self):
        win2=tkinter.Toplevel()
        win2.title('界面')
        win2.geometry('600x800')
        path2 = Image.open(r'D:\practice.jpg')
        phone2 = ImageTk.PhotoImage(path2)
        labe16 = tkinter.Label(win2, image=phone2, height=0, width=0, compound='left')
        labe16.place(relx=0, rely=0)
        mees=self.mess.get()
        res=cursor.execute('select * from watch_register where mes=%s and balance/10>0', (mees))
        if res:
            summarize()
        else:
            repetition_Label_code('label7', win2, self.watch_what.get(), 20, 150, 200)
            repetition_Label_code('label8', win2, '试看5分钟', 20, 200, 280)
            repetition_Label_code('label9', win2, '充值请按确定', 15, 95, 365)
            repetition_Button_code('button2',win2,'确定',8,20,self.coordinate_charge,295,360)
            win2.mainloop()

    #充钱界面
    def coordinate_charge(self):
        self.wind = tkinter.Toplevel()
        self.wind.title('充值')
        self.wind.geometry('600x800')
        path2 = Image.open(r'D:\practice.jpg')
        phone2 = ImageTk.PhotoImage(path2)
        labe16 = tkinter.Label(self.wind, image=phone2, height=0, width=0, compound='left')
        labe16.place(relx=0, rely=0)
        repetition_Label_code('label7',self.wind,'name',5,150,200)
        self.name = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=8, font=('', '20', ''))
        self.name.place(x=230, y=200)
        repetition_Label_code('label21',self.wind,'balance',10,83,320)
        self.balance = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=8, font=('', '20', ''))
        self.balance.place(x=230, y=320)
        repetition_Button_code('entery21',self.wind,'确定',8,20,self.recharge_money,190,370)
        repetition_Label_code('label0',self.wind,'十元一个月',12,170,430)
        self.wind.mainloop()

    def recharge_money(self):
            a = self.balance.get()
            b = self.name.get()
            n = encryption(b)
            sql = "update watch_register set balance=%s where name=%s;"
            val = (a, n)
            rres = cursor.execute(sql, val)
            conn.commit()
            if rres:
                label3 = tkinter.Label(self.wind, text='充入成功', bg='red', fg='black')
                label3.place(x=350, y=325)
                summarize()
            else:
                label3 = tkinter.Label(self.wind, text='充入失败', bg='red', fg='black')
                label3.place(x=350, y=325)
# # --------------------------------------------------------------------------------------------------------------------------
#点登录界面
# 登录类
class Deng:
    def __init__(self,name,pas,balance,wind):
        self.name=name
        self.pas=pas
        self.balance=balance
        self.wind=wind

    #    登录界面
    def login_interface(self):
        self.wind = tkinter.Toplevel()
        self.wind.title('登录')
        self.wind.geometry('600x800')
        path2 = Image.open(r'D:\practice.jpg')
        phone2 = ImageTk.PhotoImage(path2)
        labe16 = tkinter.Label(self.wind, image=phone2, height=0, width=0, compound='left')
        labe16.place(relx=0, rely=0)
        repetition_Label_code('label7',self.wind,'name',5,150,200)
        self.name = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=8, font=('', '20', ''))
        self.name.place(x=230, y=200)
        repetition_Label_code('label11',self.wind,'password',8,105,260)
        self.pas = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=8, font=('', '20', ''),show='*')
        self.pas.place(x=230, y=260)
        repetition_Button_code('entery21',self.wind,'确定',8,20,self.judge_exist,190,320)
        entery33 = tkinter.Button(self.wind, text='忘记密码', bg='red', fg='black',command=jiehe)
        entery33.place(x=360, y=260)
        self.wind.mainloop()

    # 判断是否有账号
    def judge_exist(self):
        res=self.name.get()
        rres=self.pas.get()
        f=encryption(res)
        d=encryption(rres)
        cursor.execute('show tables')
        sql='select * from watch_register where name=%s and passwor=%s'
        val=(f,d)
        hhh=cursor.execute(sql,val)
        if hhh:
            tkinter.messagebox.showinfo('提示', '登陆成功')
            root.destroy()
            p1 = Prepaid('BUT', 'NU', 'DH', 'WW')
            p1.prepaid_phone_interface()
            w1 = Watch('ss', 'saq','ww','dd','rr','tt')
            w1.watch_tv()
        else:
            tkinter.messagebox.showinfo('提示', '密码或账号错误')
#-------------------------------------------------------------------------------------------------------------------------------
    #修改密码
class Update_pass:
    def __init__(self,wind,name,tele,get,ps,pss):
        self.wind=wind
        self.name=name
        self.tele=tele
        self.get=get
        self.ps=ps
        self.pss=pss
    #忘记密码
    def forget_password(self):
        self.wind = tkinter.Toplevel()
        self.wind.title('设置新密码')
        self.wind.geometry('600x800')
        path2 = Image.open(r'D:\practice.jpg')
        phone2 = ImageTk.PhotoImage(path2)
        labe16 = tkinter.Label(self.wind, image=phone2, height=0, width=0, compound='left')
        labe16.place(relx=0, rely=0)
        repetition_Label_code('label12',self.wind,'name',10,110,220)
        self.name = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=10, font=('', '20', ''))
        self.name.place(x=270, y=220)
        label12=tkinter.Label(self.wind,text='输入绑定手机号',bg='orange', fg='green', width=15, font=('', '15', ''))
        label12.place(x=110,y=270)
        self.tele=tkinter.Entry(self.wind,text='',bg='orange', fg='green', width=15, font=('', '15', ''))
        self.tele.place(x=270,y=270)
        repetition_Button_code('button',self.wind,'点击获取验证码',15,15,self.judge_tele_exist,110,310)
        repetition_Label_code('label33',self.wind,'',8,270,310)
        self.get = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=13, font=('', '20', ''))
        self.get.place(x=190, y=350)
        self.get = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=13, font=('', '20', ''))
        self.get.place(x=190, y=350)
        repetition_Button_code('button3',self.wind,'确定',8,15,self.update_password,220,390)
        self.wind.mainloop()

    #判断电话号码是否存在信息里
    def judge_tele_exist(self):
        resss=self.tele.get()
        t=self.name.get()
        rres=encryption(resss)
        tt=encryption(t)
        res1=cursor.execute('select * from watch_register where tele=%s and name=%s',(rres,tt))
        if res1:
            repetition_Label_code('lab7',self.wind,res,8,270,310)
        else:
            self.tele.delete(0,len(resss))
            self.name.delete(0,len(t))

# 在输入验证码后 跳出修改密码的界面
    def change_password(self):
        labe16 = tkinter.Label(self.wind, image=phone2, height=0, width=0, compound='left')
        labe16.place(relx=0, rely=0)
        repetition_Label_code('label1',self.wind,'password',8,105,260)
        self.ps = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=8, font=('', '20', ''), show='*')
        self.ps.place(x=230, y=260)
        repetition_Label_code('label2',self.wind,'repassword',10,83,320)
        self.pss = tkinter.Entry(self.wind, text='', bg='orange', fg='green', width=8, font=('', '20', ''), show='*')
        self.pss.place(x=230, y=320)
        repetition_Button_code('button3',self.wind,'确定',8,20,self.Judge_successful_modification,150,380)

    #修改的功能
    def update_password(self):
        ress=res
        rs=self.get.get()
        if ress==rs:
            tkinter.messagebox.showinfo('提示', '认证成功!')
            self.change_password()
        else:
            self.get.delete(0,len(rs))
    # 判断是否修改成功
    def Judge_successful_modification(self):
        one_password = self.ps.get()
        two_password = self.pss.get()
        md5_password = encryption(two_password)
        if one_password == two_password:
            get_name = self.name.get()
            md5_name = encryption(get_name)
            cursor.execute('update watch_register set passwor=%s where name=%s', (md5_password, md5_name))
            conn.commit()
            tkinter.messagebox.showinfo('提示', '修改成功')
        else:
            self.pss.delete(0, len(two_password))
            tkinter.messagebox.showinfo('提示', '修改失败')

def jiehe():
    ww1=Update_pass('ss','dd','ff','ff','ww','hh')
    ww1.forget_password()
# -----------------------------------------------------------------

def cloding():
    d1=Deng('www','ww','ee','dd')
    d1.login_interface()

root=tkinter.Tk()
root.title('电视')
root.geometry('600x800')
# 点注册后
# 判断 名称是否规范 是否重复
def judge_name():
    list_a=['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','`','·','《','》','/,' ';']
    name_get = entery.get()
    md5_name = encryption(name_get)
    select_name = cursor.execute('select * from watch_register where name=%s', (md5_name))
    if select_name:
        label3 = tkinter.Label(root, text='输入昵称重复', bg='red', fg='black')
        label3.place(x=350, y=200)
        entery.delete(0, len(name_get))
    else:
        for i in name_get:
            if i in list_a and name_get=='':
                label3 = tkinter.Label(root, text='输入不合法了', bg='red', fg='black')
                label3.place(x=350, y=200)
                entery.delete(0,len(name_get))
        else:
            label3 = tkinter.Label(root, text='输入很规范了', bg='red', fg='black')
            label3.place(x=350, y=200)

# 判断密码输入是否输入统一或为空
def judge():
    psw_one_get=entery1.get()
    psw_two_get=entery2.get()
    if psw_one_get==psw_two_get:
        label3=tkinter.Label(root,text='两次输入很统一',bg='red',fg='black')
        label3.place(x=350,y=325)
    else:
        label5 = tkinter.Label(root, text='两次输入不统一', bg='red', fg='black')
        label5.place(x=350, y=325)
        entery1.delete(0, len(psw_one_get))
        entery2.delete(0, len(psw_two_get))

def code():
    # 结合两个函数
    judge_name()
    judge()
    tele_get=entery4.get()
    if len(tele_get)==11:
        repetition_Label_code('label3',root,res,8,230,470)
        repetition_Label_code('label5',root,'号码很合格',0,360,420)
    else:
        label5 = tkinter.Label(root, text='号码不合格',  bg='red', fg='black')
        label5.place(x=360, y=420)

def judge_code():
    # 判断 验证码是否跟输入的统一
    code_judge=entery5.get()
    if res == code_judge:
        tkinter.messagebox.showinfo('注意','亲,记住注册时的那一句话')
        a=mess.get()
        rres=cursor.execute('select * from watch_register where mes=%s ',(a))
        if a=='':
            mess.delete(0,len(a))
            tkinter.messagebox.showinfo('提示', '不能为空')
        else:
            if rres:
                tkinter.messagebox.showinfo('提示', '有人用过')
            else:
                insert_stu()
                tkinter.messagebox.showinfo('提示', '注册成功!')
                root.destroy()
            # 显示充钱界面,不充的话也可以观看只能看看不要钱的,如要看要钱的就需要充值
                p1 = Prepaid('BUT', 'NU', 'DH', 'WW')
                p1.prepaid_phone_interface()
                w1 = Watch('ss', 'saq','ww','dd','ff','ff')
                w1.watch_tv()
    else:
        entery5.delete(0,len(code_judge))

# 数据库插入数据
def insert_stu():
    name_get=entery.get()
    psw_get=entery1.get()
    age_get=entery3.get()
    tel_get=entery4.get()
    md5_name=encryption(name_get)
    md5_psw=encryption(psw_get)
    md5_tel=encryption(tel_get)
    mes_get=mess.get()
    sql='insert into watch_register(name,passwor,age,tele,mes) values(%s,%s,%s,%s,%s)'
    val=(md5_name,md5_psw,age_get,md5_tel,mes_get)
    cursor.execute(sql,val)
    conn.commit()

def the_help():
    help_msg='请按照正常操作来进行,这就是最好的帮助'
    tkinter.messagebox.showinfo(title='帮助文件', message=help_msg)

def the_author_msg():
    msg='''
    联系我请发邮箱,哈哈
    邮箱：2134933571@qq.com
    '''
    tkinter.messagebox.showinfo(title='联系方式', message=msg)

# 插放一张图片
path2 = Image.open(r'D:\practice.jpg')
phone2 = ImageTk.PhotoImage(path2)
labe1 = tkinter.Label(root, image=phone2, height=0, width=0, compound='left')
labe1.place(relx=0, rely=0)
# 有一个菜单
menubar = tkinter.Menu(root)
# tearoff如果=1 上面会有横线   =0则是没有
helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label='帮助文档', command=the_help)
helpmenu.add_command(label='作者信息', command=the_author_msg)
menubar.add_cascade(label='帮助(H)', menu=helpmenu)
root.config(menu=menubar)

repetition_Label_code('label',root,'name',5,150,200)
entery=tkinter.Entry(root,text='',bg='orange',fg='green', width=8,font=('', '20', ''))
entery.place(x=230,y=200)
label3 = tkinter.Label(root, text='昵称不能重复', bg='red', fg='black')
label3.place(x=350, y=200)
repetition_Label_code('label1',root,'password',8,105,260)
entery1=tkinter.Entry(root,text='',bg='orange',fg='green', width=8,font=('', '20', ''),show='*')
entery1.place(x=230,y=260)
repetition_Label_code('label2',root,'repassword',10,83,320)
entery2=tkinter.Entry(root,text='',bg='orange',fg='green' ,width=8,font=('', '20', ''),show='*')
entery2.place(x=230,y=320)
repetition_Label_code('label6',root,'age',5,150,370)
entery3=tkinter.Entry(root,text='',bg='orange',fg='green', width=8,font=('', '20', ''))
entery3.place(x=230,y=370)
repetition_Label_code('label7',root,'tel',5,150,420)
entery4=tkinter.Entry(root,text='',bg='orange',fg='green', width=8,font=('', '20', ''))
entery4.place(x=230,y=420)
repetition_Button_code('button', root, '点击获取验证码', 15,15, code, 68, 470)
repetition_Label_code('label3',root,'',8,230,470)
entery5=tkinter.Entry(root,text='',bg='orange',fg='green', width=13,font=('', '20', ''))
entery5.place(x=150,y=510)
label3 = tkinter.Label(root, text='输入一句话', bg='orange', fg='green',width=10,font=('','15',''))
label3.place(x=55, y=555)
mess = tkinter.Entry(root, text='', bg='orange', fg='green', width=15, font=('', '20', ''))
mess.place(x=140, y=550)
repetition_Button_code('button1', root, '注册', 5,20, judge_code, 120, 600)
repetition_Button_code('button7', root, '登录', 5,20, cloding, 290, 600)
root.mainloop()