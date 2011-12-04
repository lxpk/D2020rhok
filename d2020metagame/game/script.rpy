# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define p = Character('Primer', color="#c8ffc8")
define j = Character('Julie', color="#c8ffc8")
define y = Character("You")

image bg office = "office.png"
image bg computer = "computer.png"

# The game starts here.
label start:
    scene bg office
    p "You are in an office. There is a computer."

    
    y "Who am I?"

    menu:
        "Pick up the computer.":
            jump pickUpTheComputer
            
        "Jump out the window.":
            jump jumpOutTheWindow
    return
    
label jumpOutTheWindow:
    p "You jump out the window. You see a sign:"
    p "THINK YOU'RE PRETTY CLEVER?"
    jump start

label pickUpTheComputer:
    scene bg computer
    p "You pick up the computer."
    p "Type the following EXACTLY:"
    p "print(\"Hello World\");"
    jump naming
    
label naming:
        p "What's your name?"
        menu:
            "Nell":
                jump nellTalk
        return
       
label nellTalk:
    j "Hello Nell. You are now a programmer! You can make your own games! My name is Julie. Would you like to learn how to make a health games?"
    $ name = "Nell"
    $ gender = "F"
    jump julieTalk

label julieTalk:
    j "I'm Julie I made Mobile Adventure Walks and it’s a health game."
    y "I want to make a health game too! What is your game like?" 
    j "I don't want to bias your game idea with mine but I'll ask you some questions and after you tell me what you want to make, I'll tell you how I made mine."
    j "Who do you want to play your game?"
    menu:
        "Kids":
                jump kids
        "Teens":
                jump teens
        "Adults":
                jump adults
    return
        
label kids:
    j "Awesome!  We built our game for adults, but then found out that kids really liked it, too."
    jump julietalk2

label teens:
    j "Awesome!  We built our game for adults, but then found out that teens really liked it, too."
    jump julietalk2
    
label adults:
    j "Awesome!  We built our game for adults, but then found out that kids and teens also liked it."

label julietalk2:
    j "Now that you know who will play, why might they play?"
    menu:
        "They decided for the first time to become healthier":
            jump talk2healthier
        "They struggle sticking to a healthy life over time and they want to try something new":
            jump talk2struggle
        "They want to have fun (and you’ll trick into becoming healthier)":
            jump talk2fun
    return
    
label talk2healthier:
    j "Excellent!  Write down what triggered their decision for them and look at it often as you design your game."
    jump julietalk3

label talk2struggle:
    j "Cool!  This is a tough audience to keep, but we care about these people, too.  You’ll need to keep your game exciting, dynamic, and give them room to make mistakes and still come back."
    jump julietalk3

label talk2fun:
    j "Awesome!  This is our core target.  Fun can keep people playing – and it doesn’t matter how good your advice is in the game, you need people to do it for it to work."
    jump julietalk3

label julietalk3:
    j "How much does your audience care about fun?"
    menu:
        "They need fun!  If it's not fun, they won't stick with it":
            jump julietalk3fun
        "They love data and information.":
            jump julietalk3info
    return
    
label julietalk3fun:
    j "We think so, too!  You’ll probably want to test your ideas that you think are fun with your friends, because fun is important, but harder than you’d think to get right.  In Mobile Adventure Walks, we get people to exercise by accident."
    jump julietalk4
    
label julietalk3info:
    j "Ok, but be really careful here.  Sometimes people think they want lots of data, but they fade pretty quickly because either it’s not helping them or it’s too hard to keep track.  If you do choose to show info and data, test how people react in the short-term and over time."
    jump julietalk4

label julietalk4:
    j "It sounds like you know your audience.  What do you want your game to help them with?"
    menu:
        "eating":
            jump julietalk4eating
        "exercise":
            jump julietalk4exercise
        "weight":
            jump julietalk4weight
    return
    
label julietalk4eating:
    j "Cool!  Think about whether you want to help them before they eat, after they eat.  If you want to help with their eating, remember, your major competition is your nemesis, the warm gooey cookie."
    jump julietalk5
    
label julietalk4exercise:
    j "Excellent!  That’s what we chose to do, too.  It’s easier to make exercise fun than dieting.  Find out if your target likes exercise, or if you need to avoid that word (some people hate the words “health” and “exercise”."

label julietalk4weight:
    j "Nice!   Weight loss games are super tricky to get right, so test, test, test.  And then do more testing.  You’ve got to get them playing and coming back even if they have a bad week, and that’s when it’s toughest."

label julietalk5:
    j "Do you know what their biggest problem is that gets in the way of them living healthier?"
    menu:
        "They love food / hate exercise":
            jump julietalk5lovehate
        "They don't have time to shop / cook / exercise":
            jump julietalk5time
        "They don't have any social support":
            jump julietalk5social
        "Just plain old not motivated - they do the right thing for a while, but can't stick with it":
            jump julietalk5motivated
    return
    
label julietalk5lovehate:
    j "Ok, now give them a fun game that they can love almost as much as food and that doesn’t feel like exercise.  We think our players fall into this category, that’s why we never use the word exercise."
    jump julietalk6

label julietalk5time:
    j "That’s tricky.  So, make sure you build a game that rewards small acts people can make to be healthier.  There’s a lot of them, so get thinking."
    jump julietalk6
    
label julietalk5social:
    j "That’s cool – you can support them in the game.  Think of all the ways you can build in support."
    jump julietalk6
    
label julietalk5motivated:
    j "It’s a tough audience, but think how much you’ll be changing their lives.  We are helping this group by focusing our game on fun, and getting them to exercise by accident.  Make sure you test this audience, because they are super picky."
    jump julietalk6

label julietalk6:
    j "Want some extra tips?"
    menu:
        "Yes":
            jump julietalk6yes
        "No":
            jump julietalk6no
    return

label julietalk6yes:
    jump julietalktips

label julietalk6no:
    jump julietalkend
    
label julietalktips:
    j "Here are some tips!"
    j "Think about whether or not you want to include these things in your game:"
    j "Points: How do you you measure their progress?"
    j "Recognition: How do they feel accomplished?"
    j "Goals: short & long-term objectives for them to win."
    j "Vocabulary: Use the right language for the right people."
    j "Fun: If you say it's fun, it better be fun (no pressure!)"
    j "Be careful when using:"
    j "Competition (you may make the winner happy and everyone else sad and often everyone goes back to their old ways after the competition ends)"
    j "Beware Rewards (sometimes real rewards make people de-motivated, so use sparingly and keep on testing)"
    j "That's enough tips!"
    jump julietalkend

label julietalkend:
    j "That's enough advice and discussion. Now go make your game!"
    j "Want to see what it’s like to play a fun health game?  Download Mobile Adventure Walks on your iPhone and see for yourself!"
    j "We’re super excited for you as you build your health game."
    j "Be sure to test along the way with your friends, and enjoy all the new ideas they give you."
    j "The world needs more fun ways to be healthy, so get going and enjoy the experience!"
    return