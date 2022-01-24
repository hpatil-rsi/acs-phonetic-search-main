# Name of the index that is created by these scripts
index_name="soundex-index"

# Index field name and the analyzer to setup. Give the name of the field and the phonetic analyzer name to use from the list below. 
# analyzers = "doubleMetaphone", "beiderMorse", "caverphone1", "caverphone2", "cologne", "haasePhonetik", "koelnerPhonetik", "metaphone", "nysiis", "refinedSoundex", "soundex"
# https://azuresdkdocs.blob.core.windows.net/$web/python/azure-search-documents/latest/azure.search.documents.indexes.models.html?highlight=phonetic%20encoders#azure.search.documents.indexes.models.PhoneticEncoder
indexField = {
                "name" : "name",
                "analyzer_name" : "soundex"
            }
# The tests to use for validating the phonetic analyzers
testGroups = [
    # ["john", "jon", "jhon"],
    # ["smith", "smyth", "schmidt"],
    # ["harrison", "harison", "harisen", "herisen"],
    # ["catie", "caty", "cathy", "kathy", "katie"],
    # ["teresa", "theresa"],
    # ["johnathan", "jonathan"],
    #["burger","berger","barger","bergar","bergur","bargur"]
     #["JONES MCDEARTH", "JONAS SAXTON", "JONATHON BURNSIDE", "JONATHON WHITWORTH", "JONAH FARR", "JONAH KELSO", "JON SHORES", "JONAH MEJIA", "JONAS WELLS", "JONATHAN ALMANZA", "JONAS CASE", "JONATHAN PICARD", "JONAS CAMERON", "JONATHAN BENNETT", "JONAH YOO", "JONAH HINSON", "JONATHON LEMUS", "JON LISTER", "JON SNIPES", "JON MOSELEY", "JONAS MABE", "JONATHON GALARZA", "JONAH HENDRICK", "JONATHAN HORTON", "JON WINSLOW", "JONATHON RIDENOUR", "JONNIE SEITZ", "JONAH SPERRY", "JON HARTMANN", "JON SETTLE", "JONATHON LINCOLN", "JONAS PARTIN", "JONAS HIGGINBOTHAM", "JONATHON LINDQUIST", "JONATHAN MAY", "JON MCFARLANE", "JONAH BURNEY", "JON SMITH", "JON AUGUSTINE", "JON FREESE", "JONAS ONEAL", "JONATHON DOBSON", "JONNIE BARNEY", "JONAS DONALD", "JONATHON SAAVEDRA", "JONAH STEPHENSON", "JONATHAN CHURCH", "JONAS HAYDEN", "Jonathon96965", "Jonathan16113", "Jonathon58945", "Jon61797", "Jonathon14178", "Joni33467", "Jonathan87656", "Jon81378", "Jon87115", "Jon56112", "Jonathan54689", "Jonathon28699", "Joni63149", "Jonathan72993", "Jonathan93754", "Jonathon51992", "Joni88558", "Jonathan72489", "Jon81173", "Jon95383", "Jonathan69476", "Jon84534", "Jonathon59816", "Jon28515", "Jon53229", "Jonathan62927", "Jonathon42127", "Jonathon35193", "Jon1941", "Jonathon35199", "Joni2486", "Joni75912", "Joni33724", "Joni27151", "Jonathan41323", "Jon19914", "Jon76734", "Joni74667", "Joni24917", "Jonathon93655", "JOHN HALL", "JOHNNY TRIMBLE", "Johnnie94368", "Johnnie91663", "John75332", "Johnnie23555", "JUAN BAXTER", "JUANA HATHAWAY", "JUANDALYNN GOLDSTEIN", "JUANA FOUNTAIN"]
]