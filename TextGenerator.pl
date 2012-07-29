#!/usr/bin/perl

my $longwords=["somewhere","newspaper","wonderful","exchange","household","grandfather","overlooked","depending","movement", "handsome","contained","amounting","homestead","workmanship","production","discovered","preventing","misplaced","requested", "breakfast","department","investment","throughout","furnishing","regulation","forwarded","friendship","herewith","foundation", "deportment","geography","important","lemonade","graduation","federated","educational","handkerchief","conversation","arrangement", "nightgown","commercial","exceptional","prosperity","subscription","visionary","federation","heretofore","ingredients","certificate", "pneumonia","interview","knowledge","stockholders","property","chaperone","permanently","demonstrated","immediately","responsible", "Chautauqua","candidacy","supervisor","independent","strawberry","epidemics","specification","agricultural","catalogues","phosphorus", "schedules","rheumatism","temperature","circumstances","convenience","Pullman","trigonometry","bourgeoisie","slenderize","camouflage", "broadcast","defamatory","ramshackle","bimonthly","predetermined","clemency","beleaguered","voluptuous","intoxicating","depository", "pseudonym","indescribable","hieroglyphics","morphologist","Yugoslavia","cynosure","parallelogram","pleasurable","toxicology","bassoonist", "influenza"];
my $prefixes=["un","ex","re","de","dis","mis","con","com","for","per","sub","pur","pro","post","anti","para","fore","coun","susp","extr","trans"];
my $suffixes=["ly","ing","ify","ally","tial","ful","ure","sume","sult","jure","logy","gram","hood","graph","ment","pose","pute","tain", "ture","cient","spect","quire","ulate","ject","ther"];
my $words100=["a","an","the","this","these","that","some","all","any","every","who","which","what","such","other","I","me","my","we", "us","our","you","your","he","him","his","she","her","it","its","they","them","their","man","men","people","time","work","well","May", "will","can","one","two","great","little","first","at","by","on","upon","over","before","to","from","with","in","into","out","for","of", "about","up","when","then","now","how","so","like","as","well","very","only","no","not","more","there","than","and","or","if","but","be", "am","is","are","was","were","been","has","have","had","may","can","could","will","would","shall","should","must","say","said","like","go", "come","do","made","work"];
my $words500_3=["did","low","see","yet","act","die","sea","run","age","end","new","set","ago","sun","eye","nor","son","air","way","far","off", "ten","big","arm","few","old","too","ask","get","own","try","add","God","pay","use","boy","got","put","war","car","law","red","sir","yes", "why","cry","let","sat","cut","lie","saw","Mrs","ill"];
my $words500_4=["also","case","even","five","head","less","just","mile","once","seem","talk","wall","bank","fill","want","tell","seen","open", "mind","life","keep","hear","four","ever","city","army","back","cost","face","full","held","kept","line","miss","part","ship","thus","week", "lady","many","went","told","show","pass","most","live","kind","help","gave","fact","dear","best","bill","does","fall","girl","here","king", "long","move","poor","side","took","were","whom","town","soon","read","much","look","knew","high","give","feet","done","body","book","dont", "felt","gone","hold","know","lost","name","real","sort","tree","wide","wind","true","step","rest","near","love","land","home","good","till", "door","both","call","down","find","half","hope","last","make","need","road","stop","turn","wish","came","drop","fine","hand","hour","late", "mark","next","room","sure","wait","word","year","walk","take","same","note","mean","left","idea","hard","fire","each","care"];
my $words500_5=["young","watch","thing","speak","right","paper","least","heard","dress","bring","above","often","water","think","stand","river", "party","leave","heart","early","built","after","carry","again","fight","horse","light","place","round","start","those","where","alone", "cause","force","house","marry","plant","serve","state","three","white","still","today","whole","short","point","might","human","found", "child","along","began","color","given","large","month","price","small","story","under","world","whose","tried","stood","since","power", "money","labor","front","close","among","begin","court","green","laugh","night","quite","smile","table","until","write","being","cover", "happy","learn","order","reach","sound","taken","voice","wrong"];
my $words500_6=["chance","across","letter","enough","public","twenty","always","change","family","matter","rather","wonder","answer","coming", "father","moment","reason","result","appear","demand","figure","mother","remain","supply","around","doctor","follow","myself","return", "system","became","dollar","friend","number","school","second","office","garden","during","become","better","either","happen","person", "toward"];
my $words500_7=["hundred","against","brought","produce","company","already","husband","receive","country","America","morning","several","another", "evening","nothing","suppose","because","herself","perhaps","through","believe","himself","picture","whether","between","however","present", "without","national","continue","question","consider","increase","American","interest","possible","anything","children","remember","business", "together"];
my $words500_8=["important","themselves","Washington","government","something","condition","president"];
my $words_qrp=[ "+","73","88","AA","AB","ABT","ADR","AGN","AM","ANT","AS","B4","BCI", "BCL","BK","BN","BUG","C","CFM","CL","CLD","CLG","CQ","CW","DLD","DLVD", "DR","DX","ES","FB","FM","GA","GM","GN","GND","GUD","HI","HR","HV","HW", "K","LID","MA","MILS","MSG","N","NCS","ND","NIL","NM","NR","NW","OB","OC", "OM","OP","OPR","OT","PBL","PSE","PWR","PX","QRG","QRH","QRI","QRJ","QRK", "QRL","QRM","QRN","QRO","QRP","QRQ","QRS","QRT","QRU","QRV","QRW","QRX", "QRY","QRZ","QSA","QSB","QSD","QSG","QSK","QSL","QSM","QSN","QSO","QSP", "QST","QSU","QSW","QSX","QSY","QSZ","QTA","QTB","QTC","QTH","QTR","R", "RCD","RCVR","REF","RFI","RIG","RTTY","RX","SASE","SED","SIG","SKED","SRI", "SSB","SVC","T","TFC","TKS","TMW","TNX","TT","TU","TVI","TX","TXT","UR", "URS","VFO","VY","WA","WB","WD","WDS","WKD","WKG","WL","WUD","WX","XCVR", "XMTR","XTAL","XYL","YL","BURO","HPE","CU","SN","TEST","TEMP","MNI","RST", "599","5NN","559","CPY","DE","OK","RPT","ANI","BCNU","BD","BLV","CC","CK", "CNT","CO","CONDX","CPSE","CRD","CUD","CUAGN","CUL","ELBUG","ENUF","FER", "FONE","FREQ","GB","GD","GE","HVY","II","INPT","LSN","PA","PP","RPRT","RPT", "SA","STN","SUM","SWL","TRX","WID"];


sub rnd
{
	my $max = shift;
	my $rnd_01 = rand; # random number in [0;1]
	my $rnd = int ($rnd_01*($max+1));
	$rnd = $max if $rnd > $max;
	return $rnd;
}

print rnd(12);
#	qso_call="cq cq cq de <call>/qrp /mobile <pse> k"
#	qso_tnx="gd dr om es tnx fer call ="
#	qso_rst="rst <579> <579> qth nr thun thun ="
#	qso_name="<my> name <hr> is <name> ="
#	qso_ok="hw <copy>?"
#	qso_ok="<yourcall> de <call>"
#	qso_reply="r"
#	qso_reply= "tnx fer info dr <name> = "
#	qso_rig="rig is <ft 857> es pwt abt 100 wtts ant is loop ="
#	qso_rig="<my> rig is a <...> ="
#	qso_pwr="<my> pwr is <abt> <123> watts wtts ="
#	qso_ant="ant hr is gipole,gp,logper,longwire,lw,loop,mag,yagi,beam="
#	qso_atu="i use an <sgc 239 atu>="
#	qso_ok="hw dr <name>? <yourcall> de <mycall> k"
#	qso_tnx="mni tnx fer nice qso="
#	qso_qsl="qsl via buro is ok="
#	qso_end="<best> 73="
#	qso_wx="wx <clear,cloudy,rainy,snow,sunny>="
#	qso_temp="temp hr is abt <1> C="


