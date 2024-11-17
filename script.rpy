

default player_notes = []
default viktor_points = 5 #average

default Current_Color = "#a5a5a5"
default User_color = "#670084"
default Manager_color = "#a5a5a5"

default Username = "???"

default Viktor = Character('Viktor', color=Current_Color) 
default Viktoria = Character('Viktoria', color=Current_Color) 
default user = Character(Username, color=User_color)
default Manager = Character('Manager', color=Manager_color)


python early:
    def update_Viktor_color(new_color):
        global Viktor
        global Current_Color
        Current_Color = new_color
        Viktor = Character('Viktor', color=Current_Color)

    def update_user_name(new_name):
        global user
        global Username
        Username = new_name
        user = Character(new_name, color=User_color)

label start:
    "You wake up groggy"
    "A morning this early is not usually a part of your daily routine"
    "Your eyes flutter with both tiredness and resurfacing excitement"
    scene bg bedroom
    user "Ah, right, today is your first day at \"Hasburger inc.\""
    "Through many trials and tribulations, you finally got that full-time job at the biggest fast-food company in the country"
    "......though you are not exactly at the very top of the food chain, you are starting out at the best the bottom has to offer"
    "Quickly picking up the essentials of a new job from your messy room you lay your eyes on your freshly acquired uniform"
    "A yellow uniform with black accents, sporting a bowtie."
    "A curious choice of wear, but I am not going to question the minds of the wealthy"
    user "Ah!"
    user "Almost forgot the badge that comes with the uniform so customers can curse me out using my name, lovely"
    "In a beautiful font the badge displays:"

label username:
    $ Username = renpy.input("Enter your name:")
    $ update_user_name(Username)
    user "[Username] Restaurant staff"
    user "Ah, how nice to see it in writing"

label start2:
    "I stare up at the hanging clock on my wall that reads 7:50"
    user "Oh shi-"
    "I swiftly pack in every item in my bag and rush out the door"
    "I cannot believe I am going to be late on my first day"
    "Fortunately, the restaurant isn't far from my apartment."

label pretutorial:
    scene bg hasburger_street
    "I'm at the door of my future workplace, breathless from running for the first time in a while"
    "7.58"
    user "PHEW"
    user "2 minutes early"
    "I catch my breath and open the door to my new future"
    scene black with fade
    "Instantly I'm faced with the reality that my face is about to hit the ground of this oh-so-spotless floor after I failed to notice the wet floor sign so clearly Infront of me"
    "As I start to accept the fate of my bruised nose and even more so bruised ego, my face isn't planted on the ground like humpty dumpty and his great fall"
    "....instead, I am met with the large arms of a person whose arms are more soft than that of willows blooming in spring"
    ".....why is Shakespeare talking in my head"
    scene bg hasburger_inside
    show viktor normal at left
    "Anyways, as I open my eyes I'm met with a handsome man."
    "I come to realize the grip my palms are invoking on his biceps as I release myself from this shame"
    user "AH- I-I'm SO sorry. I didn't see the sign. And thank you...?"
    Viktor "Ā. Tu gan jau esi jaunais darbinieks. Es esmu Viktors! Jauki iepazīties."
    "*As unknown sounds escape his mouth I only now realize that, shit. Right, the manager told me about this. Here they only speak the local language. One....i'm not familiar with."
    user "Ah, I'm sorry. I don't speak Latvian."
    Viktor "Točna. Tu esi tas jauniņais no Amerikas. My name is Viktor. Nice to meet you. I'll show you to the manager"
    "Phew, finally some words I understand. Ughh I hope this won't make anything too hard for me or others"
    show viktor smile at left

label tutorial:
    default learned = False
    scene bg manager_office
    show manager normal
    "Viktor leads me to the backrooms. I enter what I assume is the managers room. A man in his years looks up at me with a smile on his face"
    hide viktor
    "Victor leaves the room with an encouraging smile on his face and I am left alone with whom I can only assume is the manager"
    Manager "You must be [Username], I have been waiting for your arrival."
    Manager "I assume you only know English, correct?"
    user "Yes, sir. I am unfortunately unfamiliar with the language here, I only just moved here to pursue my dreams." 
    Manager "Well luckily for you, you'll not only have a chance to improve your job skills here but your language skills as well."
    user "R-really?"
    Manager "Yes. See, our staff not only wants to improve on their English skills, which are currently zero to none, they're eager to help you familiarize yourself with our language."
    user "Ah, thank you so much! I'm so grateful to receive your help. I hope I will be as much of a help as you all are."
    Manager "You've met Viktor already, yes? He's the only one in this place that vaguely understands a bit of English besides me, though he may not be able to help you all of the time."
    Manager "I understand English to a certain level. But don't think I'll make your life easier by translating anything for you. You're going to have to learn to communicate by yourself."
    Manager "Now. Any questions to start off with?"
menu:
    "What will be my task for today?":
        $ learned = True
        jump tutorial2
    "...":
        jump tutorial2
label tutorial2:
    if learned:
        user "What will be my task for today?"
    else:
        user "..."
        show manager smile
        Manager "Don't be shy.."
        show manager normal

    Manager "First off, you'll be cleaning the toilets and the restaurant environment. It's the lowest tier of work here, so for a rookie like you it'll be a great starting point."
    Manager "As time goes on, you'll be able to get daily points which will determine at the end of the week if you'll go up a rank."
    Manager "Remember, if you fall below certain points by failing at tasks or challenges, you'll go back to doing chump work. Understood?"
    user "Yes, sir!"
    Manager "I believe I should start you off with some common words or phrases. What did Viktor say to you when you first met?" 
    "Recalling the embarrassing moment, my cheeks blush with a tiny hint of red."
    user "Ah- he said something about \"Tu\" \"darbinieks\" and other words I can't really name off the top of my head"
    Manager "Okay, let us start with the basics."
    Manager "\"Tu\" means \"you\" and \"es\" means \"me\""
    Manager "Ah, actually. Here-"
    "He hands me a notebook, clearly aged but not worn out due to it not having touched many hands"
    Manager "Archive the phrases and words in here, in time I hope this will be filled up till the very last page and we can speak as Latvian equals."
    "He smiles at me tenderly"
    
label phrases:
    $ learned = False
    Manager "Now then, let's get some phrases in."
    Manager "First off, \"Nāc šurp!\", an informal way of saying \"Atnāc šeit!\", means \"Come here!\", whenever someone yells that, you should go to them and see what they need from you"
    Manager " \"Paldies\" means thank you, likewise \"atvainojos\" means I'm sorry and \"piedod\" forgive me"
    show manager smile
    "I hastily try to write everything down when suddenly he comes closer to me"
    Manager "Hey, you focusing?"
    "I blush out of sheer suddenness"
    user "Y-Yes, sir." 
    show manager normal
    Manager "Now then, what does \"Nāc šurp\" mean?"
    user "Ah-"

menu:
    "I'm sorry":
        jump tutorial_end
    "Come here":
        $ learned = True
        jump tutorial_end
    "Thank you":
        jump tutorial_end

label tutorial_end:
    if learned:
        Manager "Good!"
    else:
        Manager "Ah, you'll need to work on that"

    Manager "Okay then, the last of the basics: \Hello\" is informally \"Čau\" and \"Sveiki\". Good day :\"Labdien\".  And goodbye \"Atā\" and more formally \"Uz redzēšanos\""
    Manager "Yes is \"Jā\" and no \"Nē\". Ah and here - the alphabet. You should revise it when you can. It is quite similar to the English one"
    "I add the slip of paper with the pronunciations and alphabet to my notebook and excitedly smile"
    Manager "Victor will help you out where he can, in dire situations you can come to me. Remember! Make good use of that notebook, it's precious to me" 
    "I thank him and he leads me outside"
    hide manager normal
    show viktor normal at left
    "Victor is standing there, waiting for me"
    scene bg hasburger_inside
    show viktor smile at left
    Viktor "Ah, how was it?"
    "he sports a supportive smile"
    show viktor normal at left
    user "Pretty good, I learned some stuff"
    user "Ciau"
    "I say as best as I can, mimicking the manager"
    "A playful smile plays on his mouth"
    show viktor smile at left
    Viktor "Haha, that is adorable"
    Viktor "It's more like ch-au, like the ch in Cheetos"
    show viktor normal at left
    "A light blush crossesmy face"
    user "AH, y-yes, Čau?"
    "With his hand he brushes my head like a younger siblings"
    Viktor "See! You'll get there in no time!"

label pretask:
    Viktor "Now then, as the manager probably mentioned, you're cleaning duty today."
    Viktor "Since you're fresh meat, which will it be? The bathrooms or the main floor?"
    user "Hmm"
menu:
    "The bathrooms, I'm feeling adventurous.":
        Viktor "Interesting choice, then. Let's go."
        jump bathroom
    "I'll stick to the main floor.":
        jump main_floor

label bathroom:
    scene bg supp
    show viktor normal at left
    "He ushers me to the back, where all the cleaning supplies lie"
    "He turns around to grab some spray, paper towels and a cleaning cloth"
    "Handing me the items he exclaims"
    Viktor "These will be your essentials and right there-"
    "He points to the corner where a broom and dustpan lies"
    Viktor "In case you need to sweep up the floor"
    scene bg bathroom
    show viktor normal at left
    "He leads me into the bathroom, he points at the floor"
    Viktor "Grīda"
    "Ah, i understood what he needed and opened my notebook to take notes"
    "Pointing to the trash he says"
    Viktor "Miskaste"
    Viktor "And when it needs to be thrown out people say \"Izmet ārā\" and then you need to \"Izmest ārā miskasti.\""
    Viktor "Paper towels are \"Papīra dvieļi\" and the toilet bowl is \"tualetes pods\". The bathroom all in all is called \"Vannas istaba\"."
    Viktor "If you need any help, call out to me. I'll help wherever I can."
    show viktor smile at left
    "With a soft smile he leaves me to my devices"
    hide viktor with dissolve
    user "Time to put in some elbow grease"
    "Grasping the supplies in my hands, I head into the Bathroom."
    user "Okay firstly. I need some paper towels. What was it in Latvian again?"
    $ task = renpy.input("Enter paper towels in latvian :")
    if task == "papīra dvieļi":
        user "Ah, yes. Of course, papīra dvieļi."
        $ viktor_points += 1
    else:
        user "Ah, shit. I should consult my notebook." 
    "I clean up the surrounding area as best as I can with the paper towels and head into one of the stalls, I see the toilet bowl"
    user "I should clean it, what was it again?"

    $ task = renpy.input("Enter toilet bowl in Latvian:")
    if task == "tualetes pods":
        user "Ah, yes. Of course, tualetes pods."
        $ viktor_points += 1
    else:
        user "Ah, shit. I should consult my notebook."


label main_floor:
    scene bg hasburger_inside
    show viktoria normal
    "As soon as you enter the restaurant, you nearly fall on your face before a kind hand reaches out to balance you. You look up and find a beautiful woman staring at you"
    user "ooooo"
    "to be continued......"
    #to be continued......

    return




