# This is a Python program to pick a random episode of the TV show 'The Simpsons'.
# Currently, the program will select random episodes from Seasons 1-8 only.

# Additionally, the program provides useful information for watching these episodes.
# - Disney+: Provides the season number and episode number within that season.
# - DVD:     Provides the season number and disc number.

import random
import sys

# Dictionary of all episodes from Seasons 1-8.
# Key is overall episode number, value is episode name.
first_178_episodes_dict = {
    # SEASON 1
    # Disc 1
    1: "SIMPSONS ROASTING ON AN OPEN FIRE",
    2: "BART THE GENIUS",
    3: "HOMER'S ODYSSEY",
    4: "THERE'S NO DISGRACE LIKE HOME",
    5: "BART THE GENERAL",
    # Disc 2
    6: "MOANING LISA",
    7: "CALL OF THE SIMPSONS",
    8: "THE TELLTALE HEAD",
    9: "LIFE ON THE FAST LANE",
    10: "HOMER'S NIGHT OUT",
    # Disc 3
    11: "THE CREPES OF WRATH",
    12: "KRUSTY GETS BUSTED",
    13: "SOME ENCHANTED EVENING",
    
    # SEASON 2
    # Disc 1
    14: "BART GETS AN F",
    15: "SIMPSON AND DELILAH",
    16: "TREEHOUSE OF HORROR",
    17: "TWO CARS IN EVERY GARAGE AND THREE EYES ON EVERY FISH",
    18: "DANCIN' HOMER",
    19: "DEAD PUTTING SOCIETY",
    # Disc 2
    20: "BART VS. THANKSGIVING",
    21: "BART THE DAREDEVIL",
    22: "ITCHY & SCRATCHY & MARGE",
    23: "BART GETS HIT BY A CAR",
    24: "ONE FISH, TWO FISH, BLOWFISH, BLUE FISH",
    25: "THE WAY WE WAS",
    # Disc 3
    26: "HOMER VS. LISA AND THE 8TH COMMANDMENT",
    27: "PRINCIPAL CHARMING",
    28: "OH BROTHER, WHERE ART THOU?",
    29: "BART'S DOG GETS AN F",
    30: "OLD MONEY",
    31: "BRUSH WITH GREATNESS",
    # Disc 4
    32: "LISA'S SUBSTITUTE",
    33: "THE WAR OF THE SIMPSONS",
    34: "THREE MEN AND A COMIC BOOK",
    35: "BLOOD FEUD",
    
    # SEASON 3
    # Disc 1
    36: "STARK RAVING DAD",
    37: "MR. LISA GOES TO WASHINGTON",
    38: "WHEN FLANDERS FAILED",
    39: "BART THE MURDERER",
    40: "HOMER DEFINED",
    41: "LIKE FATHER, LIKE CLOWN",
    # Disc 2
    42: "TREEHOUSE OF HORROR II",
    43: "LISA'S PONY",
    44: "SATURDAYS OF THUNDER",
    45: "FLAMING MOE'S",
    46: "BURNS VERKAUFEN DER KRAFTWERK",
    47: "I MARRIED MARGE",
    # Disc 3
    48: "RADIO BART",
    49: "LISA THE GREEK",
    50: "HOMER ALONE",
    51: "BART THE LOVER",
    52: "HOMER AT THE BAT",
    53: "SEPARATE VOCATIONS",
    # Disc 4
    54: "DOG OF DEATH",
    55: "COLONEL HOMER",
    56: "BLACK WIDOWER",
    57: "THE OTTO SHOW",
    58: "BART'S FRIEND FALLS IN LOVE",
    59: "BROTHER, CAN YOU SPARE TWO DIMES?",
    
    # SEASON 4
    # Disc 1
    60: "KAMP KRUSTY",
    61: "A STREETCAR NAMED MARGE",
    62: "HOMER THE HERETIC",
    63: "LISA THE BEAUTY QUEEN",
    # Disc 2
    64: "TREEHOUSE OF HORROR III",
    65: "ITCHY & SCRATCHY: THE MOVIE",
    66: "MARGE GETS A JOB",
    67: "NEW KID ON THE BLOCK",
    68: "MR. PLOW",
    69: "LISA'S FIRST WORD",
    # Disc 3
    70: "HOMER'S TRIPLE BYPASS",
    71: "MARGE VS. THE MONORAIL",
    72: "SELMA'S CHOICE",
    73: "BROTHER FROM THE SAME PLANET",
    74: "I LOVE LISA",
    75: "DUFFLESS",
    # Disc 4
    76: "LAST EXIT TO SPRINGFIELD",
    77: "SO IT'S COME TO THIS: A SIMPSONS CLIP SHOW",
    78: "THE FRONT",
    79: "WHACKING DAY",
    80: "MARGE IN CHAINS",
    81: "KRUSTY GETS KANCELLED",
    
    # SEASON 5
    # Disc 1
    82: "HOMER'S BARBERSHOP QUARTET",
    83: "CAPE FEARE",
    84: "HOMER GOES TO COLLEGE",
    85: "ROSEBUD",
    86: "TREEHOUSE OF HORROR IV",
    # Disc 2
    87: "MARGE ON THE LAM",
    88: "BART'S INNER CHILD",
    89: "BOY-SCOUTZ 'N THE HOOD",
    90: "THE LAST TEMPTATION OF HOMER",
    91: "$PRINGFIELD",
    92: "HOMER THE VIGILANTE",
    # Disc 3
    93: "BART GETS FAMOUS",
    94: "HOMER AND APU",
    95: "LISA VS. MALIBU STACY",
    96: "DEEP SPACE HOMER",
    97: "HOMER LOVES FLANDERS",
    98: "BART GETS AN ELEPHANT",
    # Disc 4
    99: "BURNS' HEIR",
    100: "SWEET SEYMOUR SKINNER'S BAADASSSSS SONG",
    101: "THE BOY WHO KNEW TOO MUCH",
    102: "LADY BOUVIER'S LOVER",
    103: "SECRETS OF A SUCCESSFUL MARRIAGE",
    
    # SEASON 6
    # Disc 1
    104: "BART OF DARKNESS",
    105: "LISA'S RIVAL",
    106: "ANOTHER SIMPSONS CLIP SHOW",
    107: "ITCHY & SCRATCHY LAND",
    108: "SIDESHOW BOB ROBERTS",
    109: "TREEHOUSE OF HORROR V",
    110: "BART'S GIRLFRIEND",
    # Disc 2
    111: "LISA ON ICE",
    112: "HOMER BADMAN",
    113: "GRAMPA VS. SEXUAL INADEQUACY",
    114: "FEAR OF FLYING",
    115: "HOMER THE GREAT",
    116: "AND MAGGIE MAKES THREE",
    117: "BART'S COMET",
    # Disc 3
    118: "HOMIE THE CLOWN",
    119: "BART VS. AUSTRALIA",
    120: "HOMER VS. PATTY & SELMA",
    121: "A STAR IS BURNS",
    122: "LISA'S WEDDING",
    123: "TWO DOZEN AND ONE GREYHOUNDS",
    124: "THE PTA DISBANDS!",
    # Disc 4
    125: "'ROUND SPRINGFIELD",
    126: "THE SPRINGFIELD CONNECTION",
    127: "LEMON OF TROY",
    128: "WHO SHOT MR. BURNS? (PART ONE)",
    
    # SEASON 7
    # Disc 1
    129: "WHO SHOT MR. BURNS? (PART TWO)",
    130: "RADIOACTIVE MAN",
    131: "HOME SWEET HOMEDIDDLY-DUM-DOODILY",
    132: "BART SELLS HIS SOUL",
    133: "LISA THE VEGETARIAN",
    134: "TREEHOUSE OF HORROR VI",
    # Disc 2
    135: "KING-SIZE HOMER",
    136: "MOTHER SIMPSON",
    137: "SIDESHOW BOB'S LAST GLEAMING",
    138: "THE SIMPSONS 138TH EPISODE SPECTACULAR",
    139: "MARGE BE NOT PROUD",
    140: "TEAM HOMER",
    141: "TWO BAD NEIGHBORS",
    # Disc 3
    142: "SCENES FROM THE CLASS STRUGGLE IN SPRINGFIELD",
    143: "BART THE FINK",
    144: "LISA THE ICONOCLAST",
    145: "HOMER THE SMITHERS",
    146: "THE DAY THE VIOLENCE DIED",
    147: "A FISH CALLED SELMA",
    148: "BART ON THE ROAD",
    # Disc 4
    149: "22 SHORT FILMS ABOUT SPRINGFIELD",
    150: """RAGING ABE SIMPSON AND HIS GRUMBLING GRANDSON IN
    \"THE CURSE OF THE FLYING HELLFISH\"""",
    151: "MUCH APU ABOUT NOTHING",
    152: "HOMERPALOOZA",
    153: "SUMMER OF 4 FT. 2",
    
    # SEASON 8
    # Disc 1
    154: "TREEHOUSE OF HORROR VII",
    155: "YOU ONLY MOVE TWICE",
    156: "THE HOMER THEY FALL",
    157: "BURNS, BABY BURNS",
    158: "BART AFTER DARK",
    159: "A MILHOUSE DIVIDED",
    # Disc 2
    160: "LISA'S DATE WITH DENSITY",
    161: "HURRICANE NEDDY",
    162: "EL VIAJE MISTERIOSO DE NUESTRO JOMER",
    163: "THE SPRINGFIELD FILES",
    164: "THE TWISTED WORLD OF MARGE SIMPSON",
    165: "MOUNTAIN OF MADNESS",
    166: "SIMPSONCALIFRAGILISTICEXPIALA(D'OH)CIOUS",
    # Disc 3
    167: "THE ITCHY & SCRATCHY & POOCHIE SHOW",
    168: "HOMER'S PHOBIA",
    169: "BROTHER FROM ANOTHER SERIES",
    170: "MY SISTER, MY SITTER",
    171: "HOMER VS. THE EIGHTEENTH AMENDMENT",
    172: "GRADE SCHOOL CONFIDENTIAL",
    173: "THE CANINE MUTINY",
    # Disc 4
    174: "THE OLD MAN AND THE LISA",
    175: "IN MARGE WE TRUST",
    176: "HOMER'S ENEMY",
    177: "THE SIMPSONS SPIN-OFF SHOWCASE",
    178: "THE SECRET WAR OF LISA SIMPSON"
}

# Defining the menu function
def menu():
    print("""Welcome to The Simpsons Random Episode Picker!
This program currently features every episode from Seasons 1-8.
- Enter 'R' for a random episode from any season
- Enter a numeric key from '1' to '8' to pick a random episode from a season
(e.g. enter '1' for a random Season 1 episode, '2' for Season 2, etc.)                   
- Enter 'Q' to quit.""")

# Defining the Disney+ episode number function, which specifies the season
# and episode numbers as listed on Disney+ (e.g. Season 2: Episode 1, etc.)
def disney_number():
    # SEASON 1
    if random_episode_number <= 13:
        print(f"Disney+: Season 1, Episode {random_episode_number}.")

    # SEASON 2  
    elif random_episode_number <= 35:
        print(f"Disney+: Season 2, Episode {random_episode_number - 13}.")
    
    # SEASON 3
    elif random_episode_number == 36:
        print(f"Disney+: This episode is currently unavailable to stream.")
    elif random_episode_number <= 59:
        print(f"Disney+: Season 3, Episode {random_episode_number - 35 - 1}.")
    
    # SEASON 4
    elif random_episode_number <= 81:
        print(f"Disney+: Season 4, Episode {random_episode_number - 59}.")
    
    # SEASON 5
    elif random_episode_number <= 103:
        print(f"Disney+: Season 5, Episode {random_episode_number - 81}.")

    # SEASON 6
    elif random_episode_number <= 128:
        print(f"Disney+: Season 6, Episode {random_episode_number - 103}.")
    
    # SEASON 7
    elif random_episode_number <= 153:
        print(f"Disney+: Season 7, Episode {random_episode_number - 128}.")
    
    # season 8
    else:
        print(f"Disney+: Season 8, Episode {random_episode_number - 153}.")

# Defining the DVD disc finder, which specifies the episode's season
# and disc number for the DVD version.
def disc_finder():
    # SEASON 1
    if random_episode_number <= 5:
        print("DVD: Season 1, Disc 1.")
    elif random_episode_number <= 10:
        print("DVD: Season 1, Disc 2.")
    elif random_episode_number <= 13:
        print("DVD: Season 1, Disc 3.")

    # SEASON 2
    elif random_episode_number <= 19:
        print("DVD: Season 2, Disc 1.")
    elif random_episode_number <= 25:
        print("DVD: Season 2, Disc 2.")
    elif random_episode_number <= 31:
        print("DVD: Season 2, Disc 3.")
    elif random_episode_number <= 35:
        print("DVD: Season 2, Disc 4.")

    # SEASON 3
    elif random_episode_number <= 41:
        print("DVD: Season 3, Disc 1.")
    elif random_episode_number <= 47:
        print("DVD: Season 3, Disc 2.")
    elif random_episode_number <= 53:
        print("DVD: Season 3, Disc 3.")
    elif random_episode_number <= 59:
        print("DVD: Season 3, Disc 4.")

    # SEASON 4
    elif random_episode_number <= 63:
        print("DVD: Season 4, Disc 1.")
    elif random_episode_number <= 69:
        print("DVD: Season 4, Disc 2.")
    elif random_episode_number <= 75:
        print("DVD: Season 4, Disc 3.")
    elif random_episode_number <= 81:
        print("DVD: Season 4, Disc 4.")

    # SEASON 5
    elif random_episode_number <= 86:
        print("DVD: Season 5, Disc 1.")
    elif random_episode_number <= 92:
        print("DVD: Season 5, Disc 2.")
    elif random_episode_number <= 98:
        print("DVD: Season 5, Disc 3.")
    elif random_episode_number <= 103:
        print("DVD: Season 5, Disc 4.")

    # SEASON 6
    elif random_episode_number <= 110:
        print("DVD: Season 6, Disc 1.")
    elif random_episode_number <= 117:
        print("DVD: Season 6, Disc 2.")
    elif random_episode_number <= 124:
        print("DVD: Season 6, Disc 3.")
    elif random_episode_number <= 128:
        print("DVD: Season 6, Disc 4.")

    # SEASON 7
    elif random_episode_number <= 134:
        print("DVD: Season 7, Disc 1.")
    elif random_episode_number <= 141:
        print("DVD: Season 7, Disc 2.")
    elif random_episode_number <= 148:
        print("DVD: Season 7, Disc 3.")
    elif random_episode_number <= 153:
        print("DVD: Season 7, Disc 4.")

    # SEASON 8
    elif random_episode_number <= 159:
        print("DVD: Season 8, Disc 1.")
    elif random_episode_number <= 166:
        print("DVD: Season 8, Disc 2.")
    elif random_episode_number <= 173:
        print("DVD: Season 8, Disc 3.")
    else:
        print("DVD: Season 8, Disc 4.")

# THE PROGRAM
user_input = ''
while user_input != 'q':
    menu()
    # Menu choices
    user_input = input("Please enter your selection here: ").lower()

    if user_input == 'q':
        sys.exit("Thank you for using The Simpsons Random Episode Picker!")
    
    elif user_input == '1':
        random_episode_number = random.randint(1,13)
            
    elif user_input == '2':
        random_episode_number = random.randint(14,35)
                
    elif user_input == '3':
        random_episode_number = random.randint(36,59)
                
    elif user_input == '4':
        random_episode_number = random.randint(60,81)
                
    elif user_input == '5':
        random_episode_number = random.randint(82,103)
                
    elif user_input == '6':
        random_episode_number = random.randint(104,128)
            
    elif user_input == '7':
        random_episode_number = random.randint(129,153)
                
    elif user_input == '8':
        random_episode_number = random.randint(154,178)
            
    elif user_input == 'r':
        random_episode_number = random.randint(1,178)

    else:
        print("ERROR: Invalid selection. Please restart program.")

    # Displaying the randomly selected episode to the user.
    print(f"""\nThe Simpsons Random Episode Picker has chosen...
    Episode #{random_episode_number}: "{first_178_episodes_dict[random_episode_number]}".""")

    # Displaying the Disney+ & DVD disc information to the user.
    disney_number()
    disc_finder()
    print('')