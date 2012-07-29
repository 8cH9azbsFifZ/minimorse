#!/usr/bin/perl
use Data::Dumper;

# Global variables for configuration
($mycall, $myname) = ("dg6fl", "gerolf");
($wpm, $ewpm) = (18, 18);
#$snr = "-N \"9\""; # SNR noise -10 .. 10 dB


# List of the most common words
my @longwords=("somewhere","newspaper","wonderful","exchange","household","grandfather","overlooked","depending","movement", "handsome","contained","amounting","homestead","workmanship","production","discovered","preventing","misplaced","requested", "breakfast","department","investment","throughout","furnishing","regulation","forwarded","friendship","herewith","foundation", "deportment","geography","important","lemonade","graduation","federated","educational","handkerchief","conversation","arrangement", "nightgown","commercial","exceptional","prosperity","subscription","visionary","federation","heretofore","ingredients","certificate", "pneumonia","interview","knowledge","stockholders","property","chaperone","permanently","demonstrated","immediately","responsible", "Chautauqua","candidacy","supervisor","independent","strawberry","epidemics","specification","agricultural","catalogues","phosphorus", "schedules","rheumatism","temperature","circumstances","convenience","Pullman","trigonometry","bourgeoisie","slenderize","camouflage", "broadcast","defamatory","ramshackle","bimonthly","predetermined","clemency","beleaguered","voluptuous","intoxicating","depository", "pseudonym","indescribable","hieroglyphics","morphologist","Yugoslavia","cynosure","parallelogram","pleasurable","toxicology","bassoonist", "influenza");
my @prefixes=("un","ex","re","de","dis","mis","con","com","for","per","sub","pur","pro","post","anti","para","fore","coun","susp","extr","trans");
my @suffixes=("ly","ing","ify","ally","tial","ful","ure","sume","sult","jure","logy","gram","hood","graph","ment","pose","pute","tain", "ture","cient","spect","quire","ulate","ject","ther");
my @words100=("a","an","the","this","these","that","some","all","any","every","who","which","what","such","other","I","me","my","we", "us","our","you","your","he","him","his","she","her","it","its","they","them","their","man","men","people","time","work","well","May", "will","can","one","two","great","little","first","at","by","on","upon","over","before","to","from","with","in","into","out","for","of", "about","up","when","then","now","how","so","like","as","well","very","only","no","not","more","there","than","and","or","if","but","be", "am","is","are","was","were","been","has","have","had","may","can","could","will","would","shall","should","must","say","said","like","go", "come","do","made","work");
my @words500_3=("did","low","see","yet","act","die","sea","run","age","end","new","set","ago","sun","eye","nor","son","air","way","far","off", "ten","big","arm","few","old","too","ask","get","own","try","add","God","pay","use","boy","got","put","war","car","law","red","sir","yes", "why","cry","let","sat","cut","lie","saw","Mrs","ill");
my @words500_4=("also","case","even","five","head","less","just","mile","once","seem","talk","wall","bank","fill","want","tell","seen","open", "mind","life","keep","hear","four","ever","city","army","back","cost","face","full","held","kept","line","miss","part","ship","thus","week", "lady","many","went","told","show","pass","most","live","kind","help","gave","fact","dear","best","bill","does","fall","girl","here","king", "long","move","poor","side","took","were","whom","town","soon","read","much","look","knew","high","give","feet","done","body","book","dont", "felt","gone","hold","know","lost","name","real","sort","tree","wide","wind","true","step","rest","near","love","land","home","good","till", "door","both","call","down","find","half","hope","last","make","need","road","stop","turn","wish","came","drop","fine","hand","hour","late", "mark","next","room","sure","wait","word","year","walk","take","same","note","mean","left","idea","hard","fire","each","care");
my @words500_5=("young","watch","thing","speak","right","paper","least","heard","dress","bring","above","often","water","think","stand","river", "party","leave","heart","early","built","after","carry","again","fight","horse","light","place","round","start","those","where","alone", "cause","force","house","marry","plant","serve","state","three","white","still","today","whole","short","point","might","human","found", "child","along","began","color","given","large","month","price","small","story","under","world","whose","tried","stood","since","power", "money","labor","front","close","among","begin","court","green","laugh","night","quite","smile","table","until","write","being","cover", "happy","learn","order","reach","sound","taken","voice","wrong");
my @words500_6=("chance","across","letter","enough","public","twenty","always","change","family","matter","rather","wonder","answer","coming", "father","moment","reason","result","appear","demand","figure","mother","remain","supply","around","doctor","follow","myself","return", "system","became","dollar","friend","number","school","second","office","garden","during","become","better","either","happen","person", "toward");
my @words500_7=("hundred","against","brought","produce","company","already","husband","receive","country","America","morning","several","another", "evening","nothing","suppose","because","herself","perhaps","through","believe","himself","picture","whether","between","however","present", "without","national","continue","question","consider","increase","American","interest","possible","anything","children","remember","business", "together");
my @words500_8=("important","themselves","Washington","government","something","condition","president");

# List of common abbreviations
my @words_qrp=( "+","73","88","AA","AB","ABT","ADR","AGN","AM","ANT","AS","B4","BCI", "BCL","BK","BN","BUG","C","CFM","CL","CLD","CLG","CQ","CW","DLD","DLVD", "DR","DX","ES","FB","FM","GA","GM","GN","GND","GUD","HI","HR","HV","HW", "K","LID","MA","MILS","MSG","N","NCS","ND","NIL","NM","NR","NW","OB","OC", "OM","OP","OPR","OT","PBL","PSE","PWR","PX","QRG","QRH","QRI","QRJ","QRK", "QRL","QRM","QRN","QRO","QRP","QRQ","QRS","QRT","QRU","QRV","QRW","QRX", "QRY","QRZ","QSA","QSB","QSD","QSG","QSK","QSL","QSM","QSN","QSO","QSP", "QST","QSU","QSW","QSX","QSY","QSZ","QTA","QTB","QTC","QTH","QTR","R", "RCD","RCVR","REF","RFI","RIG","RTTY","RX","SASE","SED","SIG","SKED","SRI", "SSB","SVC","T","TFC","TKS","TMW","TNX","TT","TU","TVI","TX","TXT","UR", "URS","VFO","VY","WA","WB","WD","WDS","WKD","WKG","WL","WUD","WX","XCVR", "XMTR","XTAL","XYL","YL","BURO","HPE","CU","SN","TEST","TEMP","MNI","RST", "599","5NN","559","CPY","DE","OK","RPT","ANI","BCNU","BD","BLV","CC","CK", "CNT","CO","CONDX","CPSE","CRD","CUD","CUAGN","CUL","ELBUG","ENUF","FER", "FONE","FREQ","GB","GD","GE","HVY","II","INPT","LSN","PA","PP","RPRT","RPT", "SA","STN","SUM","SWL","TRX","WID");

## @method rnd($max)
# Return a random number in interval [0:max]
# @param max The maximal value
sub rnd
{
	my $max = shift;
	my $rnd_01 = rand; # random number in (0;1)
	my $rnd = int ($rnd_01*($max+1));
	$rnd = $max if $rnd > $max;
	return $rnd;
}

## @method rnd_words($num_words,$rwords_array)
# Return a list of random words
# Example: print rnd_words (10,\@longwords);
# @param Number of words to return
# @param Reference to an array of words
sub rnd_words
{
	my $num_words = shift;
	my $rwords = shift;
	my @words = @$rwords;
	my $max = $#words;
	my $wrds;
	for (my $i = 0; $i < $num_words; $i++)
	{
		my $rnd = rnd ($max);
		$wrds = "$wrds ".@words[$rnd];
	}
	return $wrds;
}

## @method gen_call
# Generate a plausible call sign
sub gen_call
{
	my @call_appendices = ("/qrp", "/mobile");
	my $call = "zb1hq";
	# TBD: generate call
	# TBD: appendices
	return $call;
}

## @method gen_rst
# Generate a plausible rst report
sub gen_rst
{
	my $rst = "599";
	# TBD: implement random
	return $rst;
}


## @method generate_mp3($string,$outfile)
# Generate an mp3 file $outfile using ebook2cw of $string.
# @param $string The text to convert into cw
# @param $outfile The filename of the final mp3
sub generate_mp3
{
	my $text = shift;
	my $outfile = shift;
	my $infile = "test.txt";
	open (FILE, ">$infile") or die "Cannot open $infile for writing.\n";
	print FILE $text;
	close (FILE);
	my $tempoutfile = "test"; #0000.mp3 will be added by ebook2cw
	my $tempoutfile_ebook2cw = "$tempoutfile"."0000.mp3";
	my $author = "DG6FL";
	my $title = "Morse Code";
	my $year = 2012;
	# FIXME: check if exists
	my $cmd = "ebook2cw $snr -w $wpm -e $ewpm -o $tempoutfile -a \"$author\" -t \"$title\" -k \"$comment\" -y $year $infile";
	`$cmd`;
	`rm $infile`;
	`mv $tempoutfile_ebook2cw $outfile`;
}


## @method gen_qth
# Generate a plausible QTH
sub gen_qth 
{
	# TBD: maidenhead
	# TBD: WGS
	# TBD: cities
	# TBD: randomize
	my $qth = "JO40DA";
	return $qth;
}
	
## @method gen_rig
# Generate a plausible rig
sub gen_rig
{
	my @rigs = ("ft 857", "ft 817", "ats4", "vertex vx 1700");
	my $rig = rnd_words(1, \@rigs);
	return $rig;
}

## @method gen_name
# Generate a plausible name
sub gen_name
{
	# TBD implement
	my $name = "franz";
	return $name;
}

## @method gen_pwr
# Generate a plausible power
sub gen_pwr
{
	my $pwr = rnd (200);
	# FIXME: modulo 5 numbers!
	return $pwr;
}

## @method gen_ant
# Generate a plausible antenna
sub gen_ant
{
	my @a = ("dipole","gp","logper","longwire","lw","loop","mag","yagi","beam");
	my $ant = rnd_words(1, \@a);	
	return $ant;
}

## @method gen_atu
# Generate a plausible antenna tuner
sub gen_atu 
{
	my @a = ("sgc 237","elecraft t1", "z match");
	my $atu = rnd_words(1, \@a);
	return $atu;
}

## @method gen_wx
# Generate a plausible weather
sub gen_wx
{
	my @w = ("clear","cloudy","rainy","snow","sunny");
	my $wx = rnd_words(1, \@w);
	return $wx;
}

## @method generate_qso
# Generate a random QSO
sub generate_qso 
{
	my $qso;
	my $call = gen_call();

	# call
	my @qso_cq = ("cq cq cq", "cq cq", "cq cq cq cq cq");
	my @qso_cq_appendices = ("", "test", "pse");
	$qso_cq = rnd_words(1,\@qso_cq)." de $call $call".rnd_words(1,\@qso_cq_appendices)." k";

	# reply
	my @ack = ("r", "r r");
	my $reply = "$mycall de $call =";
	my @reply_tnx = ("gd dr om es tnx fer call =", "tnx fer info dr $myname");
	my $qso_rep = rnd_words(1, \@ack)."\n$reply\n".rnd_words(1,\@reply_tnx); 

	# rst
	my $rv = gen_rst();
	my @rsts = ("rst ", "ur rst is ", "rst rst is");
	my @rvl = ("$rv", "$rv $rv", "$rv $rv $rv");
	my $qso_rst = rnd_words(1, \@rsts)." ".rnd_words(1,\@rvl)." =";

	# qth 
	my $qth = gen_qth();
	my @loc = ("qth nr $qth =", "my qth is $qth =", "qth $qth =", "my qth is $qth $qth =", "");
	my $qso_qth = rnd_words(1, \@loc);

	# endreply
	my @endrep = ("hw?", "hw copy?", "hw dr $myname? $mycall de $call k");
	my $qso_endreply = rnd_words(1, \@endrep);

	# name
	my $name = gen_name();
	my @nm = ("my name hr is $name =", "name hr is $name =", "my name is $name =", "name $name =", "");
	my $qso_name = rnd_words(1, \@nm);

	# rig 
	my $rig = gen_rig();
	my @rr = ("my rig is a $rig =", "rig hr is $rig =", "my rig $rig =", "rig is $rig =", "");
	my $qso_rig = rnd_words(1, \@rr);

	# power
	my $pwr = gen_pwr();
	my @pp = ("pwr abt $pwr =", "pwr is $pwr =", "sending out $pwr watts =", "my pwr is abt $pwr wtts =", "");
	my $qso_pwr = rnd_words(1, \@pp);

	# antenna
	my $ant = gen_ant();
	my $atu = gen_atu();
	my @aa = ("ant is $ant =", "my ant is a $ant =", "ant hr is a $ant =", "");
	my @ab = ("i use an $atu =", ""); 
	my $qso_ant = rnd_words(1, \@aa)." ".rnd_words(1, \@ab);

	# weather
	my $weather = gen_wx ();
	#	qso_temp="temp hr is abt <1> C="
	
	# endqso
	my @eqso = ("mni tnx fer nice qso =", "qsl via buro is ok =", "");
	my @eeqso = ("best 73", "73", "73 73");
	my $qso_end = rnd_words(1, \@eqso)."\n".rnd_words(1, \@eeqso)." de $call <sk>";

	$qso = "$qso $qso_cq\n";
	$qso = "$qso $qso_rep\n";
	$qso = "$qso $qso_rst\n";
	$qso = "$qso $qso_qth\n";
	$qso = "$qso $qso_rig\n";
	$qso = "$qso $qso_name\n";
	$qso = "$qso $qso_pwr\n";
	$qso = "$qso $qso_ant\n";
	$qso = "$qso $qso_wx\n";
	$qso = "$qso $qso_endreply\n";
	$qso = "$qso $qso_end\n";
	print $qso;
 	my $date = `date +"%Y-%m-%d_%H:%m"`;
	chomp ($date);
	my $filename = "qso_$date";
	generate_mp3 ($qso, $filename);
}


generate_qso();
