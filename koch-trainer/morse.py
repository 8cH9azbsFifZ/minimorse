#!/usr/bin/python
# (C) Copyright Gerolf Ziegenhain 2008

# FIXME: include the words from the text generator class
import wave, struct, os, sys, time
from math import *
from random import randint, choice #picker

#########################################################################################
# N0HFF
#########################################################################################
class n0hff:
   longwords=["somewhere","newspaper","wonderful","exchange","household","grandfather","overlooked","depending","movement",
   "handsome","contained","amounting","homestead","workmanship","production","discovered","preventing","misplaced","requested",
   "breakfast","department","investment","throughout","furnishing","regulation","forwarded","friendship","herewith","foundation",
   "deportment","geography","important","lemonade","graduation","federated","educational","handkerchief","conversation","arrangement",
   "nightgown","commercial","exceptional","prosperity","subscription","visionary","federation","heretofore","ingredients","certificate",
   "pneumonia","interview","knowledge","stockholders","property","chaperone","permanently","demonstrated","immediately","responsible",
   "Chautauqua","candidacy","supervisor","independent","strawberry","epidemics","specification","agricultural","catalogues","phosphorus",
   "schedules","rheumatism","temperature","circumstances","convenience","Pullman","trigonometry","bourgeoisie","slenderize","camouflage",
   "broadcast","defamatory","ramshackle","bimonthly","predetermined","clemency","beleaguered","voluptuous","intoxicating","depository",
   "pseudonym","indescribable","hieroglyphics","morphologist","Yugoslavia","cynosure","parallelogram","pleasurable","toxicology","bassoonist",
   "influenza"]
   prefixes=["un","ex","re","de","dis","mis","con","com","for","per","sub","pur","pro","post","anti","para","fore","coun","susp","extr","trans"]
   suffixes=["ly","ing","ify","ally","tial","ful","ure","sume","sult","jure","logy","gram","hood","graph","ment","pose","pute","tain",
   "ture","cient","spect","quire","ulate","ject","ther"]
   words100=["a","an","the","this","these","that","some","all","any","every","who","which","what","such","other","I","me","my","we",
   "us","our","you","your","he","him","his","she","her","it","its","they","them","their","man","men","people","time","work","well","May",
   "will","can","one","two","great","little","first","at","by","on","upon","over","before","to","from","with","in","into","out","for","of",
   "about","up","when","then","now","how","so","like","as","well","very","only","no","not","more","there","than","and","or","if","but","be",
   "am","is","are","was","were","been","has","have","had","may","can","could","will","would","shall","should","must","say","said","like","go",
   "come","do","made","work"]
   words500_3=["did","low","see","yet","act","die","sea","run","age","end","new","set","ago","sun","eye","nor","son","air","way","far","off",
   "ten","big","arm","few","old","too","ask","get","own","try","add","God","pay","use","boy","got","put","war","car","law","red","sir","yes",
   "why","cry","let","sat","cut","lie","saw","Mrs","ill"]
   words500_4=["also","case","even","five","head","less","just","mile","once","seem","talk","wall","bank","fill","want","tell","seen","open",
   "mind","life","keep","hear","four","ever","city","army","back","cost","face","full","held","kept","line","miss","part","ship","thus","week",
   "lady","many","went","told","show","pass","most","live","kind","help","gave","fact","dear","best","bill","does","fall","girl","here","king",
   "long","move","poor","side","took","were","whom","town","soon","read","much","look","knew","high","give","feet","done","body","book","dont",
   "felt","gone","hold","know","lost","name","real","sort","tree","wide","wind","true","step","rest","near","love","land","home","good","till",
   "door","both","call","down","find","half","hope","last","make","need","road","stop","turn","wish","came","drop","fine","hand","hour","late",
   "mark","next","room","sure","wait","word","year","walk","take","same","note","mean","left","idea","hard","fire","each","care"]
   words500_5=["young","watch","thing","speak","right","paper","least","heard","dress","bring","above","often","water","think","stand","river",
   "party","leave","heart","early","built","after","carry","again","fight","horse","light","place","round","start","those","where","alone",
   "cause","force","house","marry","plant","serve","state","three","white","still","today","whole","short","point","might","human","found",
   "child","along","began","color","given","large","month","price","small","story","under","world","whose","tried","stood","since","power",
   "money","labor","front","close","among","begin","court","green","laugh","night","quite","smile","table","until","write","being","cover",
   "happy","learn","order","reach","sound","taken","voice","wrong"]
   words500_6=["chance","across","letter","enough","public","twenty","always","change","family","matter","rather","wonder","answer","coming",
   "father","moment","reason","result","appear","demand","figure","mother","remain","supply","around","doctor","follow","myself","return",
   "system","became","dollar","friend","number","school","second","office","garden","during","become","better","either","happen","person",
   "toward"]
   words500_7=["hundred","against","brought","produce","company","already","husband","receive","country","America","morning","several","another",
   "evening","nothing","suppose","because","herself","perhaps","through","believe","himself","picture","whether","between","however","present",
   "without","national","continue","question","consider","increase","American","interest","possible","anything","children","remember","business",
   "together"]
   words500_8=["important","themselves","Washington","government","something","condition","president"]
   words_qrp=[
  "+","73","88","AA","AB","ABT","ADR","AGN","AM","ANT","AS","B4","BCI",
  "BCL","BK","BN","BUG","C","CFM","CL","CLD","CLG","CQ","CW","DLD","DLVD",
  "DR","DX","ES","FB","FM","GA","GM","GN","GND","GUD","HI","HR","HV","HW",
  "K","LID","MA","MILS","MSG","N","NCS","ND","NIL","NM","NR","NW","OB","OC",
  "OM","OP","OPR","OT","PBL","PSE","PWR","PX","QRG","QRH","QRI","QRJ","QRK",
  "QRL","QRM","QRN","QRO","QRP","QRQ","QRS","QRT","QRU","QRV","QRW","QRX",
  "QRY","QRZ","QSA","QSB","QSD","QSG","QSK","QSL","QSM","QSN","QSO","QSP",
  "QST","QSU","QSW","QSX","QSY","QSZ","QTA","QTB","QTC","QTH","QTR","R",
  "RCD","RCVR","REF","RFI","RIG","RTTY","RX","SASE","SED","SIG","SKED","SRI",
  "SSB","SVC","T","TFC","TKS","TMW","TNX","TT","TU","TVI","TX","TXT","UR",
  "URS","VFO","VY","WA","WB","WD","WDS","WKD","WKG","WL","WUD","WX","XCVR",
  "XMTR","XTAL","XYL","YL","BURO","HPE","CU","SN","TEST","TEMP","MNI","RST",
  "599","5NN","559","CPY","DE","OK","RPT","ANI","BCNU","BD","BLV","CC","CK",
  "CNT","CO","CONDX","CPSE","CRD","CUD","CUAGN","CUL","ELBUG","ENUF","FER",
  "FONE","FREQ","GB","GD","GE","HVY","II","INPT","LSN","PA","PP","RPRT","RPT",
  "SA","STN","SUM","SWL","TRX","WID"]

   def __init__(self,frequency=750.,speed=18.,eff_speed=18.,lesson="all",pause=True):
      self.frequency = frequency
      self.speed = speed
      self.eff_speed = eff_speed
      self.lesson=lesson

      self.album="N0HFF - "+self.lesson
      self.pause=pause
      
      self.words500=self.words500_3+self.words500_4+self.words500_5+self.words500_6+self.words500_7+self.words500_8
      self.fixes=self.prefixes+self.suffixes

      self.SetLesson()
   
   def SetLesson(self):
      if lesson == "all":
         self.words=self.words500+self.fixes+self.longwords+self.words100
      elif lesson == "words100":
         self.words=self.words100
      elif lesson == "fixes":
         self.words=self.fixes
      elif lesson == "longwords":
         self.words = self.longwords
      elif lesson == "words500":
         self.words = self.words500

   def Group(self,length=5,count=10,id=1):
      filename="n0hff."+str(self.lesson)+".groups"+str(length)+"."+str(id)+".wav"
      w=WaveMaker(filename=filename,frequency=self.frequency,speed=self.speed,eff_speed=self.eff_speed,
            bookstable=False,pause=self.pause,
            track=str(id),album=self.album,title=self.lesson+" "+str(id))
      grp=str()
      for j in range(0,count):
         grp+=" "
         for i in range(0,length):
            w.Morse(choice(self.words).lower()+" ")
            #grp+=choice(self.words).lower()+" "
      #w.Morse(grp)


morse_table = {'a':'.-',     'b':'-...',   'c':'-.-.',  'd':'-..',
               'e':'.',      'f':'..-.',   'g':'--.',    'h':'....',
               'i':'..',     'j':'.---',   'k':'-.-',    'l':'.-..',
               'm':'--',     'n':'-.',     'o':'---',    'p':'.--.',
               'q':'--.-',   'r':'.-.',    's':'...',    't':'-',
               'u':'..-',    'v':'...-',   'w':'.--',    'x':'-..-',
               'y':'-.--',   'z':'--..',   '0':'-----',  '1':'.----',
               '2':'..---',  '3':'...--',  '4':'....-',  '5':'.....',
               '6':'-....',  '7':'--...',  '8':'---..',  '9':'----.',
               '.':'.-.-.-', ',':'--..--', '?':'..--..', "'":'.----.',
               '!':'-.-.--', '/':'-..-.',  '(':'-.--.',  ')':'-.--.-',
               '&':'.-...',  ':':'---...', ';':'-.-.-.', '=':'-...-',
               '+':'.-.-.',  '-':'-....-', '_':'..--.-', '"':'.-..-.',
               '$':'...-..-','@':'.--.-.'}

bookstable = { "0": "Zero",  "1": "One",   "2": "Two",   "3":"Three","4":"Four","5":"Five",
               "6": "Six",   "7": "Seven", "8": "Eight", "9": "Nine",
               "A": "Alfa",   "B": "Bravo",
               "C": "Charlie", "D": "Delta",    "E": "Echo",   "F": "Foxtrot","G": "Golf",   "H": "Hotel",
               "I": "India",  "J": "Juliett",   "K": "Kilo",   "L": "Lima",   "M": "Mike",   "N": "November",  "O": "Oscar",  
               "P": "Papa",   "Q": "Quebec",    "R": "Romeo",  "S": "Sierra", "T": "Tango",  "U": "Uniform",   "V": "Victor", 
               "W": "Whiskey",   "X": "X-ray",  "Y": "Yankee", "Z": "Zulu" ,
               ".": "Point",  ",": "Comma",     "/": "Slash",  "?": "Questionmark"
               }

#########################################################################################
# WaveWrite
#########################################################################################
class WaveWriter:
    def __init__(self, filename):
        self.__wav = wave.open(filename, "wb")
        
    def __del__(self):   
        self.__wav.close()
 
    def setchannels(self, channels):
        self.__wav.setnchannels(channels)

    def setformat(self, format):
        self.__wav.setsampwidth(2)

    def setrate(self, rate):
        self.__wav.setframerate(rate)

    def setperiodsize(self, period): pass

    def write(self, data):
        self.__wav.writeframes(data)

#########################################################################################
# WaveMaker
#########################################################################################
class WaveMaker:
   def __init__(self,filename="test.wav",
         frequency=750.0,
         speed=25.0,eff_speed=15.0,
         vol=-10.,channels=1,
         title="none",track="1",album="none",
         maketextfile=False,middlespeaky=False,prespeaky=False,speaky=True,bookstable=True,pause=True,prepause=True,postpause=False):
      self.sample_rate=22050. # let fixed cuz of espeak!
      self.frequency=frequency
      self.speed=speed
      self.eff_speed=eff_speed
      self.volume=10.0**(float(vol)/20.0) * 32767.0
      self.filename = filename
      self.textfile = filename.replace("wav","txt")
      self.mp3file = filename.replace("wav","mp3")
      self.speechfile = filename.replace("wav","speech")

      self.pcm = WaveWriter(filename)
      self.pcm.setchannels(channels)
      self.pcm.setrate(int(self.sample_rate))
      self.pcm.setformat(12345)

      self.GenerateSamples()

      self.text=str()
      self.maketextfile=maketextfile
      self.prespeaky=prespeaky
      self.middlespeaky=middlespeaky
      self.speaky=speaky
      self.bookstable=bookstable
      self.pause=pause

      self.album=album #id3 tag stuff
      self.title=title
      self.track=track

      if prepause:
         self.Countdown()

   def GenerateSamples(self):
      # pre-calculate some stuff:
      omega = 2.*pi*self.frequency/self.sample_rate  # jupp it is Omega
      period_len = 2.*self.sample_rate/self.frequency    # period in frames

      # calculate sample-lengths: 
      self.dit_len        = (60.0 * self.sample_rate) / (50.0 * float(self.speed))
      self.dit_len        = int(floor(round(self.dit_len/period_len)*period_len))
      self.da_len         = (180.0 * self.sample_rate) / (50.0 * float(self.speed))
      self.da_len         = int(floor(round(self.da_len/period_len)*period_len))
      self.char_pause_len = self.dit_len*3 
      self.word_pause_len = self.dit_len*7 
      self.buffer_len     = self.dit_len*2

      # calculate dit-sample:
      self.dit_sample = str()
      w = omega
      for i in range(self.dit_len):  # calc sine tone
         if i <= period_len:
            value = float(i)/period_len * self.volume*sin(omega * float(i))
         elif i >= self.dit_len-period_len:
            value = float(self.dit_len-i)/period_len * self.volume * sin(omega * float(i))
         else:
            value = self.volume * sin(omega * float(i))
         self.dit_sample += struct.pack("<h", value)
      self.dit_sample += struct.pack("<h", 0.0)*self.dit_len

      #calculate da-sample:
      self.da_sample = str()
      for i in range( self.da_len ):
         if i <= period_len:
             value = float(i)/period_len * self.volume*sin(omega * float(i))
         elif i >= self.da_len-period_len:
             value = float(self.da_len-i)/period_len * self.volume * sin(omega * float(i))
         else:
             value = self.volume * sin(omega * float(i))
         self.da_sample += struct.pack("<h", value)
      self.da_sample += struct.pack("<h", 0.0)*self.dit_len

      # "calculate" pause-sample:
      self.cpause_sample = struct.pack("<h", 0.0)*self.char_pause_len
      self.wpause_sample = struct.pack("<h", 0.0)*self.word_pause_len

      # set buffer size:
      self.pcm.setperiodsize(self.buffer_len)

   def Countdown(self):
      self.WordPause()
      self.WordPause()
      self.WordPause()
      self.WordPause()
      self.Dit()
      self.WordPause()
      self.Dit()
      self.WordPause()
      self.Dit()
      self.WordPause()
      self.WordPause()
      self.WordPause()
      self.WordPause()

   def Pausi(self):
      self.WordPause()
      self.WordPause()
      self.WordPause()
      self.WordPause()

   def WriteText(self):
      print "Saving sent text "
      ff = open(self.textfile,"w")
      print >>ff, self.text
      ff.close()

   def Cleanup(self):
      pp = os.popen ("rm "+self.speechfile+" "+self.filename)
      pp.close()

   def __del__(self):
      if self.pause:
         self.Countdown()
      if self.maketextfile:
         self.WriteText()
      if self.speaky:
         self.Speaky()
      self.CompressAudio()
      self.Cleanup()

   def CompressAudio(self):
      print "Compressing now: "+self.filename
      artist = "Mini-Morse"
      year="2009"
      track=self.track
      album="\""+self.album+"\""
      title="\""+self.title+"\""
      comment="http://g.ziegenhain.com" #"\""+self.text+"\""
      lame="lame -m m -B 16 -b 16 --tt "+title+" --ta "+artist+" --tl "+album+" --ty "+year+" --tn "+track+" --tc "+comment+" "
      if self.speaky:
         if self.prespeaky:
            streamy="sox "+self.speechfile+" "+self.filename+" -t wav -s -w -"
         elif self.middlespeaky:
            streamy="sox "+self.filename+" "+self.speechfile+" "+self.filename+" -t wav -s -w -"
         else:
            streamy="sox "+self.filename+" "+self.speechfile+" -t wav -s -w -"
      else:
         streamy="cat "++self.filename

      pp = os.popen (streamy+" | "+lame+" - "+self.mp3file)
      pp.close()
      pq = os.popen ("eyeD3 --to-v2.3 \""+self.mp3file+"\"")
      pq.close()
      qq = os.popen ("eyeD3 --add-image=\"cover.jpg\":FRONT_COVER \""+self.mp3file+"\"")
      qq.close()

   def Dit(self):
      self.pcm.write(self.dit_sample)
   def Da(self):
      self.pcm.write(self.da_sample)
   def CharPause(self):
      self.pcm.write(self.cpause_sample)
   def WordPause(self):
      self.pcm.write(self.wpause_sample)

   def Morse(self,string):
      print "Writing Morse"
      self.text+=string+" \n"
      for char in string:
         if char == " ":
            self.WordPause()
         elif char in morse_table.keys():
            for sym in morse_table[char]:
               if sym == ".":
                  self.Dit()
               elif sym == "-":
                  self.Da()
            self.CharPause()
         else:
            print "Unknown char: "+char

   def Speaky(self):
      print "Writing speech"
      speech=str()
      if self.prespeaky:
         self.text=self.text[0]
      if self.bookstable:
         for char in self.text.upper():
            if char == " ":
               speech+=". "
            elif char in bookstable.keys():
               speech+=bookstable[char]
            else:
               print "Unknown char: "+char
            speech+=" "
      else:
         speech=self.text            
      tmpfile="tempfile.txt"
      ff = open (tmpfile,"w")
      print >>ff,speech
      ff.close()
      pp = os.popen ("espeak -f "+tmpfile+" --stdout >> "+self.speechfile)
      pp.close()
      pp = os.popen("rm "+tmpfile)

#########################################################################################
# Koch
#########################################################################################
class Koch:
   kochchars = "kmrsuaptlowi.njef0yv,g5/q9zh38b?427c1d6x"

   def __init__(self,lesson=1,frequency=750.,speed=18.,eff_speed=18.0):
      self.frequency = frequency
      self.speed = speed
      self.eff_speed = eff_speed
      self.SetLesson(lesson)

   def Group(self,length=5,count=30,id=1,NewCharMoreOften=None):
      filename="koch."+str(self.lesson)+"."+str(id)+".groups"+str(length)+"."+str(int(self.eff_speed))+"wpm.wav"
      w=WaveMaker(filename=filename,frequency=self.frequency,speed=self.speed,eff_speed=self.eff_speed,
            track=str(id+1),album=self.album,title="Group "+str(id)+" ("+str(int(self.eff_speed))+"wpm)")
      grp=str()
      ccc=self.chars
      if NewCharMoreOften:
         ccc+=self.curchar
      for j in range(0,count):
         grp+=" "
         for i in range(0,length):
            grp+=choice(ccc)
      w.Morse(grp)

   def NewChar(self,count=10):
      filename="koch."+str(self.lesson)+".newchar.wav"
      w=WaveMaker(filename=filename,frequency=self.frequency,speed=self.speed,eff_speed=self.eff_speed,
            track=str(1),album=self.album,title="New char: "+self.curchar,prespeaky=True)
      grp=str()
      for i in range(0,count):
         grp+=self.curchar
         grp+=" "
      for i in range(0,count):
         grp+=self.curchar
      w.Morse(grp)

   def SetLesson(self,lesson):
      self.lesson = lesson
      self.chars = self.kochchars[:lesson]
      self.curchar = self.chars[-1]
      #self.album = "Koch ("+str(int(self.eff_speed))+"wpm) - Lesson "+str(lesson)+" Char "+self.curchar
      self.album = "Koch - Lesson "+str(lesson)+" Char "+self.curchar

   def MakeTutorial(self,ngroups=7):
      speed0 = self.eff_speed
      speed1 = self.speed
      for lesson in range(1,41):
         kk.NewChar()
         
         self.eff_speed = speed0
         self.SetLesson(lesson)
         for id in range(1,int(ngroups/2)+1):
            kk.Group(id=id)
         
         self.eff_speed = speed1
         self.SetLesson(lesson)
         for id in range(int(ngroups)/2+1,ngroups+1):
            kk.Group(id=id)

#########################################################################################
# Groups
#########################################################################################
class Groups:
   def __init__(self,frequency=750.,speed=18.,eff_speed=18.0):
      self.frequency = frequency
      self.speed = speed
      self.eff_speed = eff_speed

   def Group(self,length=5,count=100):
      album = "Groups - ("+str(int(self.eff_speed))+"wpm)"
      ccc="kmrsuaptlowi.njef0yv,g5/q9zh38b?427c1d6x"
      files=""
      for id in range(0,count):
         filename="groups"+str(length)+"."+str(id)+"."+str(int(self.eff_speed))+"wpm.wav"
         files=files+" "+filename.replace("wav","mp3")+" pause.mp3 pause.mp3"
         w=WaveMaker(filename=filename,frequency=self.frequency,speed=self.speed,eff_speed=self.eff_speed,
           track=str(id+1),album=album,title=str(id),middlespeaky=True,pause=False,prepause=False)
         grp=str()
         for i in range(0,length):
            grp+=choice(ccc)
         w.Morse(grp)
      time.sleep(30) # FIXME: wait for compressions to finish
      outfile="groups"+str(length)+"."+str(int(self.eff_speed))+"wpm.mp3"
      pp = os.popen ("cat "+files+" > "+outfile)
      pp.close()
      pp = os.popen ("eyeD3 --album=\""+album+"\" --title=\"-\" --track=1 --add-image=\"cover.jpg\":FRONT_COVER \""+outfile+"\"")
      pp.close()
      for id in range(0,count):
         filename="groups"+str(length)+"."+str(id)+"."+str(int(self.eff_speed))+"wpm.mp3"
         print filename
         pp = os.popen ("rm "+filename)
         pp.close()


#########################################################################################
# Main
#########################################################################################
if len(sys.argv) > 1:
   if sys.argv[1] == "koch":
      kk=Koch()
      kk.MakeTutorial(ngroups=10)
   elif sys.argv[1] == "groups":
      gg=Groups()
      gg.Group()
   elif sys.argv[1] == "n0hff":
      for lesson in ["words100","words500","fixes","longwords"]:
         nn=n0hff(lesson=lesson)
         for id in range(1,12):
            nn.Group(id=id,count=10)
   elif sys.argv[1] == "straight100":
      lesson="words100"
      nn=n0hff(lesson=lesson,pause=False)
      for id in range(1,100):
         nn.Group(id=id,count=1)
else:
   print "call with: <koch|n0hff|straight100|groups>"
