import re


COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "111111", "letmein", "admin", "welcome", 
    "12345678", "Hello@123","P@ssw0rd",
  "Admin123",
  "Qwerty123",
  "Password123",
  "abc123",
  "123456",
  "password",
  "12345678",
  "qwerty",
  "12345",
  "123456789",
  "P@55w0rd",
  "Welcome1",
  "11111",
  "Football1",
  "Monkey1",
  "liverpool1",
  "princess1",
  "iloveyou",
  "adobe123",
  "photoshop",
  "p@ssw0rd1",
  "welcome123",
  "login",
  "princess",
  "master",
  "qwertyuiop",
  "solo",
  "passw0rd",
  "cookie",
  "starwars",
  "trustno1",
  "dragon",
  "pass1234",
  "baseball1",
  "letmein1",
  "master1",
  "monkey12",
  "mustang",
  "access14",
  "batman1",
  "passw0rd1",
  "genesis",
  "654321",
  "superman1",
  "guitar1",
  "marina",
  "charlie1",
  "michelle1",
  "corvette",
  "Bigdog1",
  "cookie1",
  "natasha1",
  "rockstar",
  "freedom1",
  "muffin1",
  "fantasy1",
  "daniel1",
  "pepper1",
  "blowfish",
  "mercedes1",
  "success1",
  "butthead1",
  "pepper01",
  "21122112",
  "aaron431",
  "01012011",
  "manutd",
  "ginger01",
  "redsox1",
  "winter1",
  "tigger1",
  "Samantha1",
  "slayer1",
  "charmed1",
  "007700",
  "789456123",
  "password01",
  "thomas1",
  "cocacola1",
  "jp1989",
  "qazwsx1",
  "7777777",
  "freddy",
  "nirvana1",
  "myspace1",
  "123gas321",
  "passw0rd01",
  "sparky1",
  "bowling1",
  "minnie",
  "mickeymouse",
  "alabama1",
  "reallyme",
  "69696969",
  "cooldude1",
  "red123",
  "dirtyharry",
  "harley1",
  "Internet1",
  "booboo1",
  "sample1",
  "123abc",
  "lovers1",
  "0987654321",
  "q1w2e3r4",
  "defender",
  "green1",
  "98765432",
  "maverick1",
  "tintin",
  "poopoo1",
  "aaaaa1",
  "asdfghjkl",
  "bubbles1",
  "testing123",
  "darkness",
  "frankie",
  "scoobydoo",
  "passwords",
  "maximus",
  "malibu",
  "raphael",
  "drowssap1",
  "windows1",
  "paris1",
  "check123",
  "321654987",
  "members",
  "aaaaaa1",
  "blasters",
  "bonded007",
  "williams",
  "titanic1",
  "master12",
  "cheyenne",
  "telecom",
  "lemons",
  "killer123",
  "marathon",
  "hhhhhh1",
  "eastern",
  "francis",
  "asdzxc",
  "homerun",
  "peewee",
  "junior1",
  "green123",
  "babygirl1",
  "spongebob1",
  "magicman",
  "isabel",
  "isabella",
  "angel123",
  "star1234",
  "james1",
  "apple123",
  "ncc1701e",
  "slapdragon",
  "butterfly1",
  "start123",
  "qwerasdf",
  "hannah1",
  "pass123",
  "pretty",
  "rolling",
  "rocknroll",
  "wizard1",
  "nathan1",
  "metallic@",
  "246810",
  "spitfire",
  "smashing",
  "bagpipes",
  "sandman1",
  "naughty",
  "inspector",
  "kingkong",
  "gizmodo1",
  "FTPaccess21",
  "secret123",
  "brittany1",
  "456258",
  "stargate",
  "fighter",
  "orange1",
  "passion1",
  "hottie1",
  "homepage",
  "angel12",
  "danger",
  "workerbee",
  "viper1",
  "magical",
  "dogface208",
  "jellybean",
  "poolshark",
  "135790",
  "bigrob",
  "charles1",
  "bookworm1",
  "tabasco",
  "eljefe",
  "remington1",
  "mypass1",
  "7894561",
  "power123",
  "secret12",
  "tinman",
  "trinity1",
  "cookie123",
  "perfect1",
  "service123",
  "star69",
  "images1",
  "winston1",
  "solomon1",
  "kingpin",
  "holidays",
  "enternow",
  "alphas1",
  "spiderman1",
  "smooth1",
  "passthison",
  "private12",
  "crochet1",
  "appleseed",
  "snowdog",
  "tigger12",
  "momoney1",
  "fastcars1",
  "007007",
  "cupojoe",
  "marshall1",
  "fireball1",
  "mymelody1",
  "abcdef"

]

def analyze_password(password):
    feedback = []
    score = 0


    length = len(password)
    if length >= 16:
        score += 5
    elif length >= 12:
        score += 4
    elif length >= 10:
        score += 3
    elif length >= 8:
        score += 2
    elif length >= 6:
        score += 1
    if length < 8:
        feedback.append("Password is too short (use at least 8 characters, ideally 12+).")


    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Password should include at least 1 number.")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback = ["This is a commonly used password and is very unsafe, regardless of length or characters."]


    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Moderate"
    else:
        strength = "Strong"
    

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }