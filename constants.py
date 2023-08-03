# CONSTANTS
# All caps for constant values
# Format (for colors) = red, green, blue (RGB)
# Range = 0-255

FPS = 60
TITLE = "Sudoku"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 540, 540
ROWS, COLS = 9, 9

FONTS = ['dejavusansoblique', 'dejavusans', 'arialunicode',
         'sfnstextcondensed', 'applesdgothicneo', 'menlo',
         'stheitimedium', 'sfnstextcondensedmedium', 'symbol',
         'hiraginosansgb', 'lastresort', 'notoserifmyanmar',
         'helveticaneue', 'sfnsmono', 'ヒラキノ角コシックw8',
         'sfnsdisplaycondensedsemi', 'pingfang', 'noteworthy',
         'notosansoriya', 'sfcompacttext', 'ヒラキノ角コシックw9',
         'sfnsdisplaycondensedblack', 'sfcompactdisplay', 'optima',
         'zapfdingbats', 'sfnsdisplaycondensedthin', 'applebraille',
         'helveticaneuedeskinterface', 'avenirnextcondensed', 'lucidagrande',
         'sfnstextcondensedsemi', 'thonburi', 'arabicuidisplay', 'applebrailleoutline6dot',
         'kohinoortelugu', 'applebraillepinpoint6dot', 'muktamahee', 'newyork', 'sfns',
         'sfnsdisplaycondensed', 'avenir', 'kohinoor', 'notosansmyanmar', 'sfnstextcondensedheavy',
         'ヒラキノ明朝pron', 'avenirnext', 'kohinoorgujarati', 'aquakana', 'palatino', 'applesymbols', 'notonastaliq', 'stheitilight', 'sfnsdisplaycondensedmedium', 'geezapro', 'sfnsdisplaycondensedheavy', 'ヒラキノ角コシックw7', 'times', 'sfnsdisplaycondensedultralight', 'ヒラキノ丸コpronw4', 'ヒラキノ角コシックw6', 'ヒラキノ角コシックw4', 'notosanskannada', 'sfnsdisplaycondensedlight', 'sfnsrounded', 'ヒラキノ角コシックw5', 'markerfelt', 'applebraillepinpoint8dot', 'keyboard', 'ヒラキノ角コシックw1', 'arabicuitext', 'sfnstextcondensedlight', 'sfcompactrounded', 'arialhb', 'applebrailleoutline8dot', 'ヒラキノ角コシックw0', 'applecoloremoji', 'ヒラキノ角コシックw2', 'helvetica', 'kohinoorbangla', 'notosansarmenian', 'ヒラキノ角コシックw3', 'notosanslepcha', 'albayan', 'webdings', 'notosansmandaic', 'rockwell', 'zapfino', 'trebuchetms', 'georgia', 'savoyelet', 'ptsans', 'notosanssaurashtra', 'verdana', 'bodoni72smallcapsbook', 'notosansinscriptionalpahlavi', 'notosanshanunoo', 'timesnewroman', 'sukhumvitset', 'silom', 'notosanscham', 'notosansnko', 'kefa', 'notosanskayahli', 'nadeem', 'kufistandardgk', 'notosansavestan', 'bradleyhand', 'arialnarrow', 'stixgeneral', 'notosanssyriac', 'kannadasangammn', 'papyrus', 'seravek', 'applegothic', 'iowanoldstyle', 'notosanslydian', 'dincondensed', 'notosanschakma', 'kailasa', 'charter', 'farisi', 'arial', 'notosansogham', 'mishafi', 'marion', 'trattatello', 'sinhalamn', 'notosansrejang', 'notosansugaritic', 'corsiva', 'notosanslycian', 'bigcaslon', 'couriernew', 'nisc18030', 'alnile', 'stixintupsmreg', 'superclarendon', 'baghdad', 'athelas', 'stixintupdbol', 'americantypewriter', 'laosangammn', 'notosanstaile', 'notosansthaana', 'luminari', 'stixvar', 'malayalammn', 'stixsizonesymbol', 'muna', 'brushscript', 'bodoni72os', 'myanmarmn', 'notosansjavanese', 'telugumn', 'myanmarsangammn', 'chalkduster', 'stixintupsmbol', 'stixintupdreg', 'notosanssundanese', 'devanagarisangammn', 'phosphate', 'applechancery', 'applemyungjo', 'stixsizonesymreg', 'notosansolchiki', 'futura', 'notosanscarian', 'copperplate', 'ptmono', 'farah', 'malayalamsangammn', 'chalkboardse', 'itfdevanagari', 'banglamn', 'stixnonunibol', 'notosansphagspa', 'notosansyi', 'banglasangammn', 'tamilmn', 'notosanslimbu', 'notosanscypriot', 'notosansrunic', 'gurmukhisangammn', 'gujaratimt', 'diwankufi', 'notosansbamum', 'notosanslisu', 'wingdings3', 'wingdings2', 'notosansglagolitic', 'hoeflertextornaments', 'tamilsangammn', 'bodoniornaments', 'notosansvai', 'notosanstagbanwa', 'cochin', 'skia', 'notosansphoenician', 'devanagarimt', 'kannadamn', 'beirut', 'impact', 'notosanstifinagh', 'kokonor', 'notosanskaithi', 'newpeninimmt', 'stixintupbol', 'notoserifbalinese', 'gurmukhimn', 'stixsizthreesymbol', 'notosansegyptianhieroglyphs', 'notosanssamaritan', 'notosanskharoshthi', 'tahoma', 'diwanthuluth', 'notosanstagalog', 'ayuthaya', 'stixintupreg', 'sinhalasangammn', 'khmersangammn', 'ptserif', 'stixsizthreesymreg', 'snellroundhand', 'chalkboard', 'bodoni72', 'notosansnewtailue', 'notosansinscriptionalparthian', 'stixnonuni', 'mshtakan', 'notosansbuhid', 'laomn', 'sana', 'arialblack', 'baskerville', 'comicsansms', 'inaimathimn', 'notosansbuginese', 'telugusangammn', 'hoeflertext', 'notosanslinearb', 'dinalternate', 'wingdings', 'sathu', 'gujaratisangammn', 'notosanssylotinagri', 'stixsiztwosymbol', 'galvji', 'notosansoldpersian', 'euphemiacas', 'plantagenetcherokee', 'didot', 'stixintsmreg', 'stixnonuniita', 'stixsizfoursymreg', 'microsoftsansserif', 'notosanscuneiform', 'notosansbatak', 'arialrounded', 'stixsiztwosymreg', 'khmermn', 'stixgeneralbolita', 'krungthep', 'notosansoldsoutharabian', 'oriyamn', 'stixsizfoursymbol', 'stixintsmbol', 'notosansold', 'notosansgothic', 'gurmukhi', 'altarikh', 'stixnonunibolita', 'raanana', 'andalemono', 'gillsans', 'mishafigold', 'notosansshavian', 'herculanum', 'notosanstaiviet', 'damascus', 'waseem', 'notosansimperialaramaic', 'stixintdreg', 'ptserifcaption', 'notosansbrahmi', 'stixvarbol', 'notosanscoptic', 'stixsizfivesymreg', 'notosansoldturkic', 'signpainter', 'oriyasangammn', 'stixgeneralbol', 'notosansmongolian', 'shree714', 'stixintdbol', 'songti', 'notosanstaitham', 'notosansmeeteimayek', 'decotypenaskh', 'notosansosmanya']


for fnt in FONTS:
    if fnt == 'timesnewroman':
        print(fnt)
