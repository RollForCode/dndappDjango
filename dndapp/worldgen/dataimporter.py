from worldgen.models import *
# from worldgen.dataimporter import *
Races = [
"Tiefling",
"HalfOrc",
"Halfling",
"HalfElf",
"Dwarf",
"Dragonborn",
"Human",
"Gnome",
"Elf"
]

Name = [
## ELF
{
'race':'Elf',
'firstNameMale': [
"Erdan",
"Enialis",
"Elgoth",
"Carydion",
"Carric",
"Bvachan",
"Borel",
"Berrian",
"Beiro",
"Aust",
"Arromar",
"Ariandar",
"Arannis",
"Aramil",
"Alathar",
"Alarcion",
"Aelar",
"Farlien",
"Adran",
"Ferel",
"Gaerlan",
"Galinndan",
"Hadarai",
"Hein",
"Himo",
"Iafalior",
"Immeral",
"Ivellios",
"Kaelthorn",
"Laethan",
"Erevan",
"Laucian",
"Leliar",
"Leodor",
"Lorak",
"Lorifir",
"Mindartis",
"Morian",
"Oleran",
"Paelias",
"Peren",
"Quarion",
"Riardon",
"Rolen",
"Rylef",
"Savian",
"Seylas",
"Soveliss",
"Tevior",
"Thamior",
"Tharivol",
"Theren",
"Varis",
"Veyas"
],

'firstNameFemale': [
"Keyleth",
"Jelenneth",
"Irva",
"Ielenia",
"Felosial",
"Enna",
"Drusilia",
"Caelynn",
"Birel",
"Bethrynna",
"Ayrthwil",
"Atalya",
"Aryllan",
"Antinua",
"Andraste",
"Anastrianna",
"Althaea",
"Lia",
"Adrie",
"Lyfalia",
"Meriele",
"Mialee",
"Naivara",
"Quelenna",
"Quillathe",
"Ronefel",
"Sariel",
"Shanairra",
"Shava",
"Silaqui",
"Leshanna",
"Therirastra",
"Thia",
"Thirya",
"Vadania",
"Valanthe",
"Velene",
"Venefiq",
"Xanaphia",
"Zereni"
],

'lastName': [
"Xiloscient",
"Woodenhawk",
"Sunshadow",
"Summergale",
"Stormwolf",
"Starflower",
"Silverfrond",
"Sianodel",
"Riverwall",
"Oakenheel",
"Nightbreeze",
"Nailo",
"Moonwhisper",
"Mooncairn",
"Moonbrook",
"Meliamne",
"Liadon",
"Ilphekiir",
"Holimion",
"Graytrails",
"Goldpetal",
"Gemflower",
"Gemblossom",
"Galanodel",
"Evenwind",
"Diamonddew",
"Briarfell",
"Balefrost",
"Autumnloft",
"Amastacia",
"Amakiir"
]},
## HUMAN
{
'race':'Human',
'firstNameMale': [
"Madian",
"Leyten",
"Lavant",
"Krynt",
"Khemed",
"Jeras",
"Haseid",
"Hagar",
"Gryphero",
"Fenton",
"Feck",
"Falken",
"Eddan",
"Dyrk",
"Dungarth",
"Dodd",
"Daylen",
"Dalkon",
"Cale",
"Bram",
"Bardeid",
"Aseir",
"Arando",
"Anlow",
"Malfier",
"Markus",
"Mehmen",
"Meklan",
"Namen",
"Navaren",
"Nerle",
"Nilus",
"Ningyan",
"Norris",
"Quentin",
"Semil",
"Sevenson",
"Steveren",
"Sudeiman",
"Talfen",
"Tamond",
"Taran",
"Tavon",
"Tegan",
"Vanan",
"Vincent",
"Zasheir"
],

'firstNameFemale': [
"Zasheida",
"Yasheira",
"Xandrilla",
"Vencia",
"Tylsa",
"Tura",
"Tanika",
"Seipora",
"Saidi",
"Sachil",
"Rosalyn",
"Remora",
"Pharana",
"Mirabel",
"Meilil",
"Lorelei",
"Kasaki",
"Jasmal",
"Hama",
"Hallan",
"Ceidil",
"Brey",
"Azura",
"Atala"
],

'lastName': [
"Shanks",
"Seratolva",
"Sell",
"Roxley",
"Revenmar",
"Redraven",
"Ratley",
"Pyncion",
"Oakenheart",
"Netheridge",
"Moonridge",
"Lynchfield",
"Leerstrom",
"Lamoth",
"Kroft",
"Kreel",
"Iscalon",
"Hindergrass",
"Gullscream",
"Guddath",
"Grantham",
"Goldrudder",
"Fryft",
"Fletcher",
"Shattermast",
"Shaulfer",
"Silvergraft",
"Stavenger",
"Stormchapel",
"Strong",
"Swiller",
"Talandro",
"Tamil",
"Towerfall",
"Umbermoor",
"Van Devries",
"Van Gandt",
"Van Hyden",
"Varcona",
"Varzand",
"Voortham",
"Vrye",
"Webb",
"Welfer",
"Wilxes",
"Wintermere",
"Wygarthe",
"Arkalis",
"Armanci",
"Bilger",
"Blackstrand",
"Brightwater",
"Carnavon",
"Caskajaro",
"Coldshore",
"Coyle",
"Cresthill",
"Cuttlescar",
"Daargen",
"Dalicarlia",
"Danamark",
"Donoghan",
"Drumwind",
"Dunhall",
"Ereghast",
"Falck",
"Fallenbridge",
"Faringray"
]},
## GNOME
{
'race':'Gnome',
'firstNameMale': [
"Alston",
"Alvyn",
"Boddynock",
"Brocc",
"Burgell",
"DImble",
"Eldon",
"Erky",
"Fonkin",
"Frug",
"Gerbo",
"Gimble",
"Glim",
"Jebeddo",
"Kellen",
"Namfoodle",
"Orryn",
"Roondar",
"Sheebo",
"Sindri",
"Warryn",
"Wrenn",
"Zook"
],

'firstNameFemale': [
"Bimpnottin",
"Breena",
"Caramip",
"Carlin",
"Donella",
"Duvamil",
"Ella",
"Ellyjobell",
"Ellywick",
"Lilli",
"Loopmottin",
"Lorilla",
"Mardnab",
"Nissa",
"Nyx",
"Oda",
"Orla",
"Roywyn",
"Shamil",
"Tana",
"Waywocket",
"Zanna"
],

'lastName': [
"Aleslosh",
"Ashhearth",
"Badger",
"Beren",
"Cloak",
"Daergel",
"Doublock",
"Filchbatter",
"Fnipper",
"Folkor",
"Garrick",
"Ku",
"Murnig",
"Nackle",
"Nim",
"Ningel",
"Oneshoe",
"Pock",
"Raulnor",
"Sheppen",
"Sparklegem",
"Stumbleduck",
"Timbers",
"Turen"
]},
{
'race':'Dragonborn',
'firstNameMale': [
"Andujar",
"Arjhan",
"Armagan",
"Armek",
"Arzan",
"Axaran",
"Balasar",
"Belaxarim",
"Bharash",
"Brevarr",
"Djemidor",
"Donaar",
"Draxan",
"Fayal",
"Ghesh",
"Grax",
"Heskan",
"Inzul",
"Iojad",
"Khiraj",
"Kreytzen",
"Kriv",
"Lejek",
"Mar",
"Medrash",
"Mehen",
"Nadarr",
"Nazir",
"Nedam",
"Nevek",
"Pandjed",
"Patrin",
"Ravaran",
"Razaan",
"Rhogar",
"Sarax",
"Sarram",
"Savaxis",
"Shamash",
"Shedinn",
"Siangar",
"Sirizan",
"Sunan",
"Szuran",
"Tajan",
"Tamajon",
"Tarhun",
"Tenahn",
"Torinn",
"Toxal",
"Tzegyr",
"Vantajar",
"Vharkus",
"Xafiq",
"Zarkhil"
],

'firstNameFemale': [
"Akra",
"Artana",
"Biri",
"Daar",
"Farideh",
"Haraan",
"Havilar",
"Jheri",
"Kalas",
"Kava",
"Khagra",
"Korinn",
"Leytra",
"Mishann",
"Myrka",
"Nala",
"Naya",
"Perra",
"Raiann",
"Sarcha",
"Shirren",
"Sirivistra",
"Sora",
"Sufana",
"Surina",
"Tamara",
"Thava",
"Uadjit",
"Vrumadi",
"Zovra"
],

'lastName': [
"Arkhor",
"Avandra",
"Bharzim",
"Bhezrizma",
"Clethtinthiallor",
"Daardendrian",
"Delmirev",
"Drachedandion",
"Fenkenkabradon",
"Halendros",
"Kepeshkmolik",
"Kerrhylon",
"Kimbatuul",
"Lantheon",
"Librankarsk",
"Linxakasendalor",
"Maaldestir",
"Marturang",
"Myastan",
"Nemmonis",
"Norixius",
"Ophinshtalajiir",
"Prexijandilin",
"Sahandrian",
"Sanalosi",
"Shalastar",
"Shestendeliath",
"Tamrion",
"Turathi",
"Turnuroth",
"Vaazruz",
"Varalan",
"Verthisathurgiesh",
"Yarjerit"
]},
{
'race':'Dwarf',
'firstNameMale': [
"Kildrak",
"Hlant",
"Harvek",
"Halzar",
"Halagmar",
"Haeltar",
"Grimmalk",
"Glint",
"Ghorvas",
"Garmûl",
"Gardain",
"Flint",
"Ferrek",
"Fargrim",
"Ezegan",
"Erag",
"Einkil",
"Eberk",
"Dyrnar",
"Dolmen",
"Delg",
"Darrak",
"Darkûl",
"Dain",
"Bruenor",
"Brottor",
"Borkûl",
"Bariken",
"Barendd",
"Balfam",
"Baern",
"Baelnar",
"Avamir",
"Auxlan",
"Arnan",
"Alberich",
"Agaro",
"Adrik",
"Wolvar",
"Vondal",
"Vistrum",
"Veit",
"Vabûl",
"Ulfgar",
"Tredigar",
"Travok",
"Traubon",
"Tordek",
"Thorin",
"Thorbalt",
"Thoradin",
"Taklinn",
"Swargar",
"Smethykk",
"Sharak",
"Sabakzar",
"Rurik",
"Rozag",
"Roken",
"Rogath",
"Rangrim",
"Oskar",
"Orsik",
"Orobok",
"Morgran",
"Morak",
"Melgar",
"Maulnar",
"Mardam",
"Malagar",
"Lurtrum",
"Kurman",
"Krim",
"Krag",
"Korlag"
],

'firstNameFemale': [
"Zebel",
"Vronwe",
"Vistra",
"Veklani",
"Vauldra",
"Torgga",
"Torbera",
"Thurlfara",
"Sannl",
"Roksana",
"Rokel",
"Riswyn",
"Praxana",
"Marnia",
"Mardred",
"Lurka",
"Lokara",
"Liftrasa",
"Krystolari",
"Kristryd",
"Kathra",
"Ilde",
"Hlin",
"Helja",
"Gurdis",
"Gunnloda",
"Grenenzel",
"Finelln",
"Fenryl",
"Falkrunn",
"Eldeth",
"Diesa",
"Dagnal",
"Beyla",
"Bardryn",
"Audhild",
"Artin",
"Amber"
],

'lastName': [
"Zarkanan",
"Ungart",
"Trakeln",
"Torunn",
"Skandalor",
"Silvertarn",
"Rumnaheim",
"Rockharvest",
"Ramcrown",
"Markolak",
"Loderr",
"Litgehr",
"Irongull",
"Ironfist",
"Holderhek",
"Hackshield",
"Grimtor",
"Gorunn",
"Garkalan",
"Frostbeard",
"Fireforge",
"Evermead",
"Drakantal",
"Deepmiddens",
"Dankil",
"Copperhearth",
"Brawnanvil",
"Battlehammer",
"Barrelhelm",
"Balderk",
"Ambershard"
]},
{
'race':'HalfElf',
'firstNameMale': [
"Adran",
"Aelar",
"Alarcion",
"Alathar",
"Aramil",
"Arannis",
"Ariandar",
"Arromar",
"Aust",
"Beiro",
"Berrian",
"Borel",
"Bvachan",
"Carric",
"Carydion",
"Elgoth",
"Enialis",
"Erdan",
"Erevan",
"Farlien",
"Ferel",
"Gaerlan",
"Galinndan",
"Hadarai",
"Hein",
"Himo",
"Iafalior",
"Immeral",
"Ivellios",
"Kaelthorn",
"Laethan",
"Laucian",
"Leliar",
"Leodor",
"Lorak",
"Lorifir",
"Mindartis",
"Morian",
"Oleran",
"Paelias",
"Peren",
"Quarion",
"Riardon",
"Rolen",
"Rylef",
"Savian",
"Seylas",
"Soveliss",
"Tevior",
"Thamior",
"Tharivol",
"Theren",
"Varis",
"Veyas",
"Anlow",
"Arando",
"Aseir",
"Bardeid",
"Bram",
"Cale",
"Dalkon",
"Daylen",
"Dodd",
"Dungarth",
"Dyrk",
"Eddan",
"Falken",
"Feck",
"Fenton",
"Gryphero",
"Hagar",
"Haseid",
"Jeras",
"Khemed",
"Krynt",
"Lavant",
"Leyten",
"Madian",
"Malfier",
"Markus",
"Mehmen",
"Meklan",
"Namen",
"Navaren",
"Nerle",
"Nilus",
"Ningyan",
"Norris",
"Quentin",
"Semil",
"Sevenson",
"Steveren",
"Sudeiman",
"Talfen",
"Tamond",
"Taran",
"Tavon",
"Tegan",
"Vanan",
"Vincent",
"Zasheir"
],

'firstNameFemale': [
"Adrie",
"Althaea",
"Anastrianna",
"Andraste",
"Antinua",
"Aryllan",
"Atalya",
"Ayrthwil",
"Bethrynna",
"Birel",
"Caelynn",
"Drusilia",
"Enna",
"Felosial",
"Ielenia",
"Irva",
"Jelenneth",
"Keyleth",
"Leshanna",
"Lia",
"Lyfalia",
"Meriele",
"Mialee",
"Naivara",
"Quelenna",
"Quillathe",
"Ronefel",
"Sariel",
"Shanairra",
"Shava",
"Silaqui",
"Therirastra",
"Thia",
"Thirya",
"Vadania",
"Valanthe",
"Velene",
"Venefiq",
"Xanaphia",
"Zereni",
"Atala",
"Azura",
"Brey",
"Ceidil",
"Hallan",
"Hama",
"Jasmal",
"Kasaki",
"Lorelei",
"Meilil",
"Mirabel",
"Pharana",
"Remora",
"Rosalyn",
"Sachil",
"Saidi",
"Seipora",
"Tanika",
"Tura",
"Tylsa",
"Vencia",
"Xandrilla",
"Yasheira",
"Zasheida"
],

'lastName': [
"Amakiir",
"Amastacia",
"Autumnloft",
"Balefrost",
"Briarfell",
"Diamonddew",
"Evenwind",
"Galanodel",
"Gemblossom",
"Gemflower",
"Goldpetal",
"Graytrails",
"Holimion",
"Ilphekiir",
"Liadon",
"Meliamne",
"Moonbrook",
"Mooncairn",
"Moonwhisper",
"Nailo",
"Nightbreeze",
"Oakenheel",
"Riverwall",
"Sianodel",
"Silverfrond",
"Starflower",
"Stormwolf",
"Summergale",
"Sunshadow",
"Woodenhawk",
"Xiloscient",
"Arkalis",
"Armanci",
"Bilger",
"Blackstrand",
"Brightwater",
"Carnavon",
"Caskajaro",
"Coldshore",
"Coyle",
"Cresthill",
"Cuttlescar",
"Daargen",
"Dalicarlia",
"Danamark",
"Donoghan",
"Drumwind",
"Dunhall",
"Ereghast",
"Falck",
"Fallenbridge",
"Faringray",
"Fletcher",
"Fryft",
"Goldrudder",
"Grantham",
"Guddath",
"Gullscream",
"Hindergrass",
"Iscalon",
"Kreel",
"Kroft",
"Lamoth",
"Leerstrom",
"Lynchfield",
"Moonridge",
"Netheridge",
"Oakenheart",
"Pyncion",
"Ratley",
"Redraven",
"Revenmar",
"Roxley",
"Sell",
"Seratolva",
"Shanks",
"Shattermast",
"Shaulfer",
"Silvergraft",
"Stavenger",
"Stormchapel",
"Strong",
"Swiller",
"Talandro",
"Tamil",
"Towerfall",
"Umbermoor",
"Van Devries",
"Van Gandt",
"Van Hyden",
"Varcona",
"Varzand",
"Voortham",
"Vrye",
"Webb",
"Welfer",
"Wilxes",
"Wintermere",
"Wygarthe",
"Zatchet",
"Zethergyll"
]},
{
'race':'Halfling',
'firstNameMale': [
"Alton",
"Ander",
"Arthan",
"Cade",
"Carvin",
"Corby",
"Corrin",
"Cullen",
"Egen",
"Eldon",
"Ernest",
"Errich",
"Finnan",
"Garret",
"Gedi",
"Heron",
"Jeryl",
"Keffen",
"Kylem",
"Kynt",
"Leskyn",
"Linal",
"Lyle",
"Merric",
"Milo",
"Neff",
"Orne",
"Osborn",
"Perrin",
"Quarrel",
"Rabbit",
"Reed",
"Rilkin",
"Roscoe",
"Snakebait",
"Tarfen",
"Titch",
"Tuck",
"Wellby",
"Whim"
],

'firstNameFemale': [
"Andry",
"Bree",
"Caliope",
"Callie",
"Cora",
"Emily",
"Euphemia",
"Jillian",
"Kithri",
"Lavinia",
"Lidda",
"Merla",
"Nedda",
"Paela",
"Piper",
"Portia",
"Rixi",
"Sabretha",
"Seraphina",
"Shaena",
"Teg",
"Tilly",
"Toira",
"Trym",
"Vani",
"Verna",
"Vexia",
"Vil",
"Vzani",
"Zanthe",
"Ziza"
],

'lastName': [
"Angler",
"Battlestone",
"Blackwater",
"Brushgather",
"Daggersharp",
"Deepstrider",
"Goodbarrel",
"Greenbottle",
"High-hill",
"Hilltopple",
"Hollowpot",
"Leagallow",
"Puddle",
"Raftmite",
"Silverfin",
"Skiprock",
"Tanglestrand",
"Tealeaf",
"Thorngage",
"Tosscobble",
"Tricker",
"Underbough",
"Willowrush",
"Yellowcrane"
]},
##HalfOrc
{
'race':'HalfOrc',
'firstNameMale': [
"Dench",
"Feng",
"Gell",
"Henk",
"Holg",
"Imsh",
"Keth",
"Krusk",
"Mhurren",
"Ront",
"Shump",
"Thokk"
],

'firstNameFemale': [
"Baggi",
"Emen",
"Engong",
"Kansif",
"Myev",
"Neega",
"Ovak",
"Ownka",
"Shautha",
"Sutha",
"Vola",
"Volen",
"Yevelda"
],

'lastName': [
"NotApplicable",
"NotApplicabl"
]},
{
'race':'Tiefling',
'firstNameMale': [
"Akmenos",
"Amnon",
"Ankhus",
"Archidius",
"Arkadi",
"Armarius",
"Armillius",
"Balmoloch",
"Barakas",
"Calderax",
"Cavian",
"Cenereth",
"Chorum",
"Corynax",
"Dacian",
"Daelius",
"Damaceus",
"Damakos",
"Decimeth",
"Demedor",
"Demerian",
"Dynachus",
"Ekemon",
"Grassus",
"Halius",
"Heleph",
"Iados",
"Incirion",
"Kairon",
"Kalaradian",
"Kamien",
"Kazimir",
"Kzandro",
"Leucis",
"Machem",
"Maetheus",
"Malfias",
"Marchion",
"Melech",
"Menerus",
"Mordai",
"Morthos",
"Namazeus",
"Nensis",
"Pelanos",
"Prismeus",
"Pyranikus",
"Razortail",
"Sejanus",
"Severian",
"Skamos",
"Suffer",
"Syken",
"Tarkus",
"Therai",
"Vaius",
"Xerek",
"Zeth",
"Zevon"
],

'firstNameFemale': [
"Affyria",
"Akta",
"Anakis",
"Bryseis",
"Cataclysmia",
"Criella",
"Damaia",
"Domitia",
"Dorethau",
"Ea",
"Excellence",
"Hacari",
"Iritra",
"Kallista",
"Lachira",
"Lerissa",
"Levatra",
"Makaria",
"Mecretia",
"Milvia",
"Nemia",
"Nericia",
"Orianna",
"Phelaia",
"Precious",
"Rain",
"Reita",
"Samantia",
"Sunshine",
"Tenerife",
"Traya",
"Velavia",
"Zaidi",
"Zethaya"
],

'lastName': [
"Amarzian",
"Art",
"Carnago",
"Carrion",
"Chant",
"Creed",
"Despair",
"Domarien",
"Excellence",
"Iscitan",
"Meluzan",
"Menetrian",
"Paradas",
"Poetry",
"Quest",
"Random",
"Reverence",
"Romazi",
"Sarzan",
"Serechor",
"Shadowhorn",
"Sorrow",
"Szereban",
"Temerity",
"Torment",
"Torzalan",
"Trelenus",
"Trevethor",
"Tryphon",
"Vadu",
"Vrago",
"Weary"
]}
]

## elf, human, gnome, dragonborn,dwarf, halfElf
## halfling, halfOrc
"""
{
'race':'Gnome',
'firstNameMale': [
],

'firstNameFemale': [
],

'lastName': [
]},
"""

def raceImporter():
	for race in Races:
		if Race.objects.filter(race=race):
			continue
		else:
			r = Race(race=race)
			r.save()

def nameImporter():
	for name in Name:
		r = name['race']
		print(r)
		race = Race.objects.get(race=r)
		# Male iterator
		for thisName in name['firstNameMale']:
			if race.name_first_male_set.filter(name=thisName):
				continue
			else:
				race.name_first_male_set.create(name=thisName)
		# Female iterator
		for thisName in name['firstNameFemale']:
			if race.name_first_female_set.filter(name=thisName):
				continue
			else:
				race.name_first_female_set.create(name=thisName)
		# Last iterator
		for thisName in name['lastName']:
			if race.name_last_set.filter(name=thisName):
				continue
			else:
				race.name_last_set.create(name=thisName)