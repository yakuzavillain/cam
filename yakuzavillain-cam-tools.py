#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests,re,os
import time
import sys

print("""

\033[1;31m\033[1;37m  

                              
 _______ ___ _  ____/ /____  ___  / /__
/ __/ _ `/  ' \/___/ __/ _ \/ _ \/ (_-<
\__/\_,_/_/_/_/    \__/\___/\___/_/___/
                                       

                             
                              
                              

\033[1;31m1)\033[1;37mUnited States                \033[1;31m31)\033[1;37mMexico           
\033[1;31m2)\033[1;37mJapan                        \033[1;31m32)\033[1;37mFinland           
\033[1;31m3)\033[1;37mItaly                        \033[1;31m33)\033[1;37mChina              
\033[1;31m4)\033[1;37mKorea                        \033[1;31m34)\033[1;37mChile            
\033[1;31m5)\033[1;37mFrance                       \033[1;31m35)\033[1;37mSouth Africa       
\033[1;31m6)\033[1;37mGermany                      \033[1;31m36)\033[1;37mSlovakia      
\033[1;31m7)\033[1;37mTaiwan                       \033[1;31m37)\033[1;37mHungary           
\033[1;31m8)\033[1;37mRussian Federation           \033[1;31m38)\033[1;37mIreland               
\033[1;31m9)\033[1;37mUnited Kingdom               \033[1;31m39)\033[1;37mEgypt             
\033[1;31m10)\033[1;37mNetherlands                 \033[1;31m40)\033[1;37mThailand            
\033[1;31m11)\033[1;37mCzech Republic              \033[1;31m41)\033[1;37mUkraine           
\033[1;31m12)\033[1;37mTurkey                      \033[1;31m42)\033[1;37mSerbia              
\033[1;31m13)\033[1;37mAustria                     \033[1;31m43)\033[1;37mHong Kong         
\033[1;31m14)\033[1;37mSwitzerland                 \033[1;31m44)\033[1;37mGreece      
\033[1;31m15)\033[1;37mSpain                       \033[1;31m45)\033[1;37mPortugal          
\033[1;31m16)\033[1;37mCanada                      \033[1;31m46)\033[1;37mLatvia      
\033[1;31m17)\033[1;37mSweden                      \033[1;31m47)\033[1;37mSingapore         
\033[1;31m18)\033[1;37mIsrael                      \033[1;31m48)\033[1;37mIceland         
\033[1;31m19)\033[1;37mIran                        \033[1;31m49)\033[1;37mMalaysia        
\033[1;31m20)\033[1;37mPoland                      \033[1;31m50)\033[1;37mColombia    
\033[1;31m21)\033[1;37mIndia                       
\033[1;31m22)\033[1;37mNorway                      
\033[1;31m23)\033[1;37mRomania                     
\033[1;31m24)\033[1;37mViet Nam                    
\033[1;31m25)\033[1;37mBelgium                     
\033[1;31m26)\033[1;37mBrazil                      \033[1;31m56)\033[1;37mLithuania         
\033[1;31m27)\033[1;37mBulgaria                    
\033[1;31m28)\033[1;37mIndonesia                   \033[1;31m58)\033[1;37mNew Zealand          
\033[1;31m29)\033[1;37mDenmark                     
\033[1;31m30)\033[1;37mArgentina                   
""")



 
try:                                                               
    num = int(input("OPTIONS : "))


    if num == 1:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,720):
			
                url = ("https://www.insecam.org/en/bycountry/US/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ")
    elif num == 2:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,232):
			
                url = ("https://www.insecam.org/en/bycountry/JP/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ")
            
    elif num == 3:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,159):
			
                url = ("https://www.insecam.org/en/bycountry/IT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ")

    elif num == 4:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,141):
			
                url = ("https://www.insecam.org/en/bycountry/KR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ")            
            
    elif num == 5:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,120):
			
                url = ("https://www.insecam.org/en/bycountry/FR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ")
    elif num == 6:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,107):
			
                url = ("https://www.insecam.org/en/bycountry/DE/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ")

    elif num == 7:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,92):
			
                url = ("https://www.insecam.org/en/bycountry/TW/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 8:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,82):
			
                url = ("https://www.insecam.org/en/bycountry/RU/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 9:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,81):
			
                url = ("https://www.insecam.org/en/bycountry/GB/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 10:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,66):
			
                url = ("https://www.insecam.org/en/bycountry/NL/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 11:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,58):
			
                url = ("https://www.insecam.org/en/bycountry/CZ/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 12:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,54):
			
                url = ("https://www.insecam.org/en/bycountry/TR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 13:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,48):
			
                url = ("https://www.insecam.org/en/bycountry/AT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 14:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,44):
			
                url = ("https://www.insecam.org/en/bycountry/CH/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 15:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,39):
			
                url = ("https://www.insecam.org/en/bycountry/ES/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 

    elif num == 16:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,38):
			
                url = ("https://www.insecam.org/en/bycountry/CA/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 17:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,35):
			
                url = ("https://www.insecam.org/en/bycountry/SE/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 18:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,31):
			
                url = ("https://www.insecam.org/en/bycountry/IL/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 20:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,30):
			
                url = ("https://www.insecam.org/en/bycountry/PL/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 19:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,22):
			
                url = ("https://www.insecam.org/en/bycountry/IR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 22:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,29):
			
                url = ("https://www.insecam.org/en/bycountry/NO/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 23:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,28):
			
                url = ("https://www.insecam.org/en/bycountry/RO/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 21:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,26):
			
                url = ("https://www.insecam.org/en/bycountry/IN/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 24:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,23):
			
                url = ("https://www.insecam.org/en/bycountry/VN/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 25:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,23):
			
                url = ("https://www.insecam.org/en/bycountry/BE/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 26:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,23):
			
                url = ("https://www.insecam.org/en/bycountry/BR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 27:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,21):
			
                url = ("https://www.insecam.org/en/bycountry/BG/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 28:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,16):
			
                url = ("https://www.insecam.org/en/bycountry/ID/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 29:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,16):
			
                url = ("https://www.insecam.org/en/bycountry/DK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 30:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,13):
			
                url = ("https://www.insecam.org/en/bycountry/AR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 31:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,13):
			
                url = ("https://www.insecam.org/en/bycountry/MX/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 32:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,23):
			
                url = ("https://www.insecam.org/en/bycountry/FI/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 33:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,13):
			
                url = ("https://www.insecam.org/en/bycountry/CN/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 34:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,13):
			
                url = ("https://www.insecam.org/en/bycountry/CL/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 35:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,11):
			
                url = ("https://www.insecam.org/en/bycountry/ZA/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 36:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,11):
			
                url = ("https://www.insecam.org/en/bycountry/SK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 37:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,11):
			
                url = ("https://www.insecam.org/en/bycountry/HU/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 38:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,11):
			
                url = ("https://www.insecam.org/en/bycountry/IE/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 39:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,10):
			
                url = ("https://www.insecam.org/en/bycountry/EG/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 40:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,11):
			
                url = ("https://www.insecam.org/en/bycountry/TH/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 41:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,10):
			
                url = ("https://www.insecam.org/en/bycountry/UA/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 42:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,10):
			
                url = ("https://www.insecam.org/en/bycountry/RS/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 43:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/HK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 44:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,8):
			
                url = ("https://www.insecam.org/en/bycountry/GR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 45:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/PT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 46:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,6):
			
                url = ("https://www.insecam.org/en/bycountry/LV/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 47:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/SG/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 48:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/IS/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 49:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,6):
			
                url = ("https://www.insecam.org/en/bycountry/MY/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
    elif num == 50:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,6):
			
                url = ("https://www.insecam.org/en/bycountry/CO/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                 
                     count += 1
        except:
            print (" ") 
  


except KeyboardInterrupt:
        print (" ")
