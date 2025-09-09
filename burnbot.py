name = input("what is your name?: ")
age = int(input("how old are you?: "))
fav_distro = input("what distro does your slow ass use?: ")
fav_coding_lang = input("what garbage language do you build your useless programs in?: ")
fav_wm = input("how do you navigate your pitiful system?: ")

def burnbot(name, age, fav_distro, fav_coding_lang, fav_wm):
    

    if name == "brody":
        print("kys(kind young soul)")
        return
    elif name == "zachary flower":
        print("give me a A you ignorant ignoramus, dead built like a encephalopod")
    else:
        print(f"{name}, Wow that sounds stupid, why did your parents name you that")

    if age in range(0, 15):
        print("get off this program and grab your ipad.")
    elif age in range(16, 36):
        print("Go f*** yourself, Mcdonalds is calling to you, why are you even looking at this, get yo bread up.")
    elif age == 37:
        print("Wow the worst age, go get to you midlife crisis alread. DW you'll be dead soon enough.")
    elif age in range(38, 99999999):
        print("cant you die already here ill give you some more time and save you from waisting any more of your pitiful life")
        return
    else:
        print("Thats not your age have fun lying")
        return
    
    if fav_distro == "arch":
        print("What a ego you have, stop tinkering with your esoteric system and get some work done. also you arnt special")
    elif fav_distro == "ubuntu":
        print("About as unique as a cardbord box. 'I want to use something that works!!' I dont care just use Windows or use a real OS")
    else:
        print("Wow you listed a distro not even in my list you should feel special for not being apart of the fun now sit in the corner and brag about this accomplishment")
    
    if fav_coding_lang == "python":
        print("Have fun using the slowest peice of garbage for the rest of your pathetic life, and dont get me started on the python is super addaptibe to almost any program I dont care. you are still using the most bloaded peice of trash")
    elif fav_coding_lang == "java":
        print("you dont deserve a roast just think about how much you like to use java")
        return
    else:
        print(f"Thats a stupid choice. Your about as useless as {fav_coding_lang} your a dissapointment")
    
    if fav_wm == "i3":
        print("Have fun in your config files while all of us do acctual work you should be ashamed of yourself. And no your i3 config does not look cool get a job or a real hobbie")
    elif fav_wm == "gnome":
        print("You just suck go navigate your dumbed down wm like the baby you are")
    else:
        print(f"Great you picked another varient of garbage I bet {fav_wm} suck but than again im not going to try it because I dont care and neither should you")

    return print(f"Wow that was disapointing you are the worst person I can imagine im going to let you look over your answers and think about your actions {name}, {age}, {fav_distro}, {fav_coding_lang}, {fav_wm}")

print(burnbot(name, age, fav_distro, fav_coding_lang, fav_wm))