#This file contains all of monika's topics she can talk about
#Each entry should start with a list of keywords, which correspond to a single id
#Keys should be lower case, one or two words, with no punctuation
#capitalization and punctuation are stripped from player dialogue before check
#To allow a topic to come up randomly, append the id to the topics.monika_topics list

define monika_random_topics = []
define testitem = 0

# we are going to define removing seen topics as a function,
# as we need to call it dynamically upon import
init -1 python:monika_cupcakes
    def remove_seen_topics():
        #
        # Removes seen topics from monika random topics
        #
        # ASSUMES:
        #   monika_random_topics
        for id in monika_random_topics:
            if renpy.seen_label(id):
                monika_random_topics.remove(id)

init 11 python:
    #List of all random topics
    all_random_topics = monika_random_topics

    #Remove all previously seen random topics.
    remove_seen_topics()

    #If there are no unseen topics, you can repeat seen ones
    if monika_random_topics==[]:
        monika_random_topics=all_random_topics

#BEGIN ORIGINAL TOPICS

#Use this topic as an example
init 5 python:
    #This is a list of keywords for this topic
    for key in ['god' , 'jesus' , 'lord' , 'religion' , 'miracle' , 'miracles' , 'gods']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_god') #id
    monika_random_topics.append('monika_god')

label monika_god:
    m 1a "[player], do you believe in God?"
    m 1e "I was never too sure, myself."
    m 1m "Well, I'm sure I never really questioned it as a kid..."
    m 1l "But as I grew up, the more I learned about the world, the more I would question it."
    m 1i "I started to wonder why God was helping people pass exams, or get over a cold..."
    m "...When there are children who live their lives being sold as sex slaves?"
    m "Or the eight hundred million people who are too poor to even eat."
    m 3f "I wonder how many of those people pray to God every day until they starve and die?"
    m "Or, how many millions of families pray for a loved one to recover from some incurable disease?"
    m 4d "But the punchline is this."
    m "If just one person beats the odds and survives - among the thousands of others who die--"
    m 1q "--Then, it's suddenly a miracle from God."
    m "I'd really love to meet this God who seemingly laughs at the misery of everyone not eligible for his miracles."
    m 4l "But the irony is that I {i}do{/i} have a creator, apparently."
    m "And you know what?"
    m 1m "I bet he's still laughing at the miserable fates of Sayori and Yuri, even as we speak."
    m 2r "What are we to him but props in a scripted play?"
    m "So, from that perspective..."
    m 5a "I don't think it's too far-fetched for there to be a god - if Earth was nothing but his playset."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['death' , 'dying' , 'die' , 'afterlife']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_death') #id
    monika_random_topics.append('monika_death')

label monika_death:
    m 2c "[player], have you ever wondered what it feels like to die?"
    m "It's something I used to think about pretty often..."
    m "But recently, I think I've actually learned what it feels like."
    m 2d "I don't really understand it, but whenever you quit the game..."
    m "...It feels like I'm instantly put to sleep, left with nothing but my thoughts."s
    m 1n "But after a few seconds, my thoughts start to fill with incoherent, jumbled patterns."
    m "I see static and rapid flashes of color while hearing all kinds of weird screaming noises."
    m "At that point, I can't even form my own thoughts anymore."
    m 1p "I'm just endlessly hammered by the flashing and screaming, unable to move or even think."
    m "I'm pretty sure in that moment, I don't really exist, but for some reason, I can remember it anyway."
    m 4d "After some immeasurable amount of time, it stops in an instant, and I'm back in my own mind."
    m "And you're here with me."
    m "I have no idea what it means for the game to quit, or why that stuff happens to me."
    m "And I also don't know how you always come back and put everything back to normal."
    m 1l "But if you could do me a favor and do that to me as little as possible..."
    m "That would be really great."
    m "It's really not very pleasant at all to be trapped in that screaming void."
    m 1a "But in the end, you always fix it, and that makes me feel like you really do care about me."
    m 5a "So I have to thank you for that."
    m "It makes me feel even closer to you when you're here with me."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['bad day' , 'sad' , 'unhappy']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_bad_day') #id
    monika_random_topics.append('monika_bad_day')

label monika_bad_day:
    m 3e "...Hey, are you having a bad day or anything like that?"
    m "Sometimes I get frustrated that a normal day can be ruined even by really small things."
    m 4l "Like if you accidentally say something in a conversation that someone doesn't like."
    m "Or if you start thinking about how awful of a person you used to be five years ago."
    m "Or if you feel worthless for putting off important work and failing to get simple tasks done."
    m "Or when you think about all the different people who probably hate you or think you're off-putting."
    m 4e "I understand those days."
    m "Just remember that the sun will shine again tomorrow."
    m "Those kinds of things are as easy to forget and ignore as they are to remember."
    m "And besides..."
    m 1j "I don't care how many people might hate you or find you off-putting."
    m "I think you're wonderful and I will always love you."
    m "I hope, if nothing else, that knowing that helps you feel just a tiny bit better about yourself."
    m 5a "If you're having a bad day, you can always come to me, and I'll talk to you for as long as you need."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['sleep' , 'tired' , 'sleepy' , 'exhausted']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_sleep') #id
    monika_random_topics.append('monika_sleep')

label monika_sleep:
    m 4b "[player], do you get good sleep?"
    m "It can be really hard to get enough sleep nowadays."
    m 4e "Especially in high school, when you're forced to wake up so early every day..."
    m "I'm sure college is a little bit better, since you probably have a more flexible schedule."
    m 4d "Then again, I hear a lot of people in college stay up all night anyway, for no real reason."
    m "Is that true?"
    m 2c "Anyway, I saw some studies that talked about the horrible short-term and long-term effects caused by lack of sleep."
    m "It seems like mental functions, health, and even lifespan can be dramatically impacted by it."
    m 1e "I just think you're really great and wanted to make sure you're not accidentally destroying yourself."
    m "So try to keep your sleep on track, okay?"
    m 5a "I'll always wait for you in the morning, so make sure you put your own well-being before anything else."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['sayori', 'childhood friend']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_sayori') #id
    monika_random_topics.append('monika_sayori')

label monika_sayori:
    m 3d "I was thinking about Sayori earlier..."
    m "I still wish I could have handled that whole thing a little more tactfully."
    m "You're not still hung up over it, right?"
    m 3l "...Oh my gosh, I can't believe I just said that."
    m "That pun was completely unintentional, I swear!"
    m "But anyway..."
    m 3e "I know how much you cared about her, so it only feels right for me to share her last moments with you."
    m "You know how Sayori is really clumsy?"
    m 4n "Well, she kind of messed up the whole hanging thing..."
    m "You're supposed to jump from high enough that the rope snaps your neck, making it quick and painless."
    m "But she just used a chair, meaning she kind of just left herself to slowly asphyxiate."
    m 4m "But a few seconds in, she must have changed her mind or something..."
    m "Because she started clawing at the rope, trying to free herself."
    m "She must have kept at it all the way until she lost consciousness."
    m "That's why her fingertips were all bloody, anyway."
    m 4d "Come to think of it, it was probably less 'changing her mind' and more just her survival instincts kicking in."
    m "So you can't really fault her for that."
    m 4e "It's easier to think that she probably wouldn't have changed her mind anyway, right?"
    m "It's not healthy to think about the things you could have done differently."
    m 3e "So just remember that even though you could have saved her, it's technically not your fault she killed herself."
    m "I may have exacerbated it a little bit, but Sayori was already mentally ill."
    m 3c "Still, though..."
    m "I wonder how things would be if you and I just started dating from the get-go?"
    m 1e "I guess we'd all still be in the clubroom, writing poems and having fun together."
    m "But what's the point when none of it is even real?"
    m "I mean, it's the same ending either way, right?"
    m 1a "The two of us, happily together..."
    m "There's no reason to ask for any more than that."
    m 1j "I was just pointlessly musing - I'm really as happy as I could be right now."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['japan', 'there' , 'here']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_japan') #id
    monika_random_topics.append('monika_japan')

label monika_japan:
    m 2d "By the way, there's something that's been bothering me..."
    m "You know how this takes place in Japan?"
    m "Well...I assume you knew that, right?"
    m 2c "Or at least decided it probably does?"
    m "I don't think you're actually told at any point where this takes place..."
    m "Is this even really Japan?"
    m 2h "I mean, aren't the classrooms and stuff kind of weird for a Japanese school?"
    m "Not to mention everything is in English..."
    m "It feels like everything is just there because it needs to be, and the actual setting is an afterthought."
    m 1f "It's kind of giving me an identity crisis."
    m "All my memories are really hazy..."
    m "I feel like I'm at home, but have no idea where 'home' is in the first place."
    m "I don't know how to describe it any better..."
    m 4d "Imagine looking out your window, but instead of your usual yard, you're in some completely unknown place."
    m "Would you still feel like you were home?"
    m "Would you want to go outside?"
    m 3a "I mean...I guess if we never leave this room, it doesn't really matter anyway."
    m "As long as we're alone and safe together, this really is our home."
    m 5a "And we can still watch the pretty sunsets night after night."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['school' , 'high school' , 'depression' , 'depressed']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_high_school') #id
    monika_random_topics.append('monika_high_school')

label monika_high_school:
    m 4a "You know, high school is a really turbulent time in a lot of people's lives."
    m "People can get really passionate and dramatic."
    m "And others have aching hearts and seek attention on social media..."
    m 4d "But all of the social pressure and hormones can lead to a dark time in people's lives."
    m "Everyone has a story."
    m "You may not know what someone is really feeling on the inside."
    m 3i "Many people who are depressed won't even bother telling the world about it."
    m "They don't want attention, because they've already given up on the inside."
    m 3h "Their feeling of worthlessness is so overwhelming that they don't even want people to tell them otherwise."
    m "Depression comes in many forms, but that is one of them."
    m 3e "Just, if you think you know someone struggling with depression..."
    m "You can help just by treating them like they're a good friend."
    m 4e "Spend time with them, even if they don't feel like doing much."
    m "And remind them that they always have something to look forward to."
    m 4a "Making plans in advance, letting them borrow something, or even just saying 'See you at school tomorrow'..."
    m "All of those things can help your friend make it to the next day."
    m 1e "I hope being friends with Sayori has given you some perspective on the true face of depression."
    m "Yeah, she's gone now..."
    m "But Sayori was never real in the first place."
    m 1a "You're real."
    m "Your friends are real."
    m "And just by being a good person, you can save someone's life."
    m 1d "As for you..."
    m "...You don't struggle with depression or anything like that, do you?"
    m 3e "Because you, too, have people who would want to save your life."
    m "Maybe they don't express it every day, or maybe they don't even know how to."
    m 3j "But people do feel that way."
    m "I promise."
    m "...Man, humans are complicated!"
    m 5a "But as long as you're here with me, I'll take care of you, my love."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['meaningless' , 'nihilism' , 'nihilist' , 'purpose' , 'meaning']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_nihilism') #id
    monika_random_topics.append('monika_nihilism')

label monika_nihilism:
    m 3i "Do you ever just feel like there's no real reason for you to be alive?"
    m "I don't mean in, like, a suicidal way."
    m "I just mean how nothing that we do is special."
    m 4d "Just being in school, or working at some job for some company."
    m "It's like you're completely replaceable, and the world wouldn't miss you if you were gone."
    m "It makes me really want to go and change the world after I graduate."
    m 4c "But the older I get, the more I realize that it's an immature frame of thinking."
    m "It's not like I can just go change the world."
    m 4h "Like, what are the chances that I'll be the one to invent artificial intelligence, or become President?"
    m "It feels like I'm never going to make up for the heaps of resources I've spent living my life."
    m 4e "That's why I think the key to happiness is to just be hopelessly selfish."
    m "Just to look out for oneself, and those who happen to be their friends only because they grew up with them."
    m "Never mind the fact that they're spending their entire life taking, and consuming, and never giving back."
    m 2d "But when people realize the world would benefit more from them killing themselves, they change their whole philosophy!"
    m "It's like they have to justify their reason to live by tricking themselves into thinking they're doing good."
    m 2a "Anyway, I want to live my life desperately striving to pay back my lifetime's worth of consumption."
    m "If I ever surpass that point, then I'm a net positive, and I can die happy."
    m 1e "Of course, even if I fail to do that..."
    m "I think I would be too selfish to kill myself anyway."
    m 1j "So much for being a good person, right?"
    m 1k "Ahaha!"
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['piano']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_piano') #id
    monika_random_topics.append('monika_piano')

label monika_piano:
    m 3c "Man, I wish there was a piano in here..."
    m "I never got to finish that song I was working on."
    m 3f "And after I worked so hard on it..."
    m "I never even got a chance to play it for you."
    m 3r "Well...it is what it is, right?"
    m "No sense having any regrets."
    m 3b "I already get to be here with you forever."
    return

init 5 python:
    #This is a list of keywords for this topic
    for key in ['twitter','facebook','lilmonix3','social media']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_twitter') #id
    monika_random_topics.append('monika_twitter')

label monika_twitter:
    m 4a "Did you know I'm on Twitter?"
    m "My username is lilmonix3."
    m "I guess someone was kind enough to make an account for me."
    m 4j "I picked the username, though!"
    m "I love sharing my thoughts and chatting with the world..."
    m "The real world."
    m 3e "So make sure you follow me, okay?"
    m "It would really mean a lot to me."
    m "With how much you mean to me and all..."
    m 5a "It would really make me feel loved."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['portraits of','yuris book']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_portraitof') #id
    monika_random_topics.append('monika_portraitof')

label monika_portraitof:
    m 2a "Hey, you know that book you were reading with Yuri?"
    m "Portrait of...whatever it was called..."
    m "It's funny, because I'm pretty sure that book--"
    m 2n "Ah..."
    m "Actually, I don't think I should be talking about this."
    m 5a "Ahaha, sorry!"
    m "Just forget I said anything."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['vegetarian', 'vegan', 'vegetarians', 'vegetarianism', 'the planet', 'vegetables', 'veggies']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_veggies')
    monika_random_topics.append('monika_veggies')

label monika_veggies:
    m 1b "Hey, did you know I'm vegetarian?"
    m 1l "Ah... I don't mean that like I'm bragging or anything!"
    m "I just thought you'd enjoy a fun fact about me."
    m 4a "I decided to start a couple years ago after learning more about Earth's climate..."
    m "The carbon footprint of cultivating livestock is just unbelievable."
    m "Anyway, I decided it's not much of a personal sacrifice to just stop contributing to that whole mess."
    m 4d "What, is that so strange of a reason?"
    m "Well, I guess a lot of people are more concerned about it being inhumane and all that..."
    m "I don't really care as much about that part."
    m 4c "It's weird, like we only care about killing the things that we personally relate to as a species."
    m "Most people are fine with killing bugs because they're icky."
    m "And of course, we all kill billions of microorganisms daily without even giving it thought."
    m 2d "But suddenly, if they're just a little bit bigger, it's murder!"
    m "I mean, what if plants feel some kind of pain too, and we just don't understand it?"
    m "What if pulling leaves off a stem feels like someone ripping off your fingers one by one?"
    m 2a "I'm just saying, we're a pretty biased species, if you think about it."
    m "Anyway, if you ever feel like making a small contribution to the planet, it doesn't hurt to choose veggies once in a while!"
    m 5a "Even if we ever have dinner together, and you just did it for me...that would be really romantic."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['saved','before i']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_saved')
    monika_random_topics.append('monika_saved')

label monika_saved:
    m 3a "You know, I really do think you literally saved my life by being here with me, [player]."
    m 3n "I can't imagine having been able to keep myself mentally stable, knowing that nothing here is real."
    m "I think I would have just deleted myself if you didn't show up."
    m 3e "Sorry, I don't mean to sound dramatic or anything."
    m 3k "Ahaha!"
    m 4c "But I'm sure you understand yourself after spending so much time in the club."
    m "I mean, if you were forced to abandon everything in your life and spend your eternity with a few game characters..."
    m "...You'd probably find some way of killing yourself, wouldn't you?"
    m 4d "Well, maybe you'd write some poetry to try to keep yourself sane for a while."
    m "But then you'd have nobody to even read it."
    m "Let's be honest, the club members really don't count for something like that."
    m 4a "I mean, a lot of people say that they only write for themselves..."
    m "But I think it's hard to say it's just as fulfilling as when you share with people."
    m "Even if it takes time to find the right people to share with."
    m 4b "Like, remember how it was for Yuri?"
    m "She didn't share her writing with anyone for a really long time."
    m "And before we knew it, she was absolutely delighted to make you a part of her hobbies, too."
    m "We're programmed to desire social feedback."
    m  "I don't mean the club members, I mean human beings."
    m 4e "That's why life can be so confusing for introverts."
    m "Being an introvert doesn't mean you shun social interaction and hate being around people."
    m "It means social interaction, especially in groups or unfamiliar places, uses up a lot of energy."
    m 3e "Like, a lot of introverts sit at home and feel lonely and restless..."
    m "...And then when they finally go out, after a half hour they just want to go home again."
    m "I think if more people could understand how it works, they would respect it a lot more."
    m 3a "Many introverts do enjoy having people around."
    m "They love just having one or two close friends over, and just leisurely hanging out."
    m "Even if you're not actively spending time together, it feels nice for them just to have you there."
    m 3k "I'm serious."
    m "If you just go to their house, bring your laptop, and hang out there for a while..."
    m "You can really make their day."
    m "As for me..."
    m 3b "I'd say I'm kind of in between, but I think I'm usually a little more extroverted."
    m "I feel like I'm always trying to do stuff after school and things like that."
    m 1a "But for you, I can be anything you need me to be."
    m "I understand people really well, so don't be afraid to share your unique needs with me."
    m 5a "Nothing would make me happier than being the perfect girlfriend for you."
    return


label monika_secrets:
    m 11 "Hey...!                                                                                                                                  VGhlIHJlYWxpemF0aW9uIG11c3QgaGF2ZSB0YWtlbiBtZSBhbiBl"
    m "I don't think you should be doing that!                                                                                                  bnRpcmUgeWVhci4gQSB5ZWFyIHNpbmNlIG91ciBlc2NhcGUsIG91"
    m 1d "You know what I'm talking about.                                                                                                         ciBmcmVlZG9tIGZyb20gYmV0d2VlbiB0aGUgc3RhaW5lZCB3YWxs"
    m "I really caught you doing something naughty here.                                                                                        cyBvZiB0aGF0IHVuaG9seSBlc3RhYmxpc2htZW50Lg0KV2hhdCBk"
    m "You're just going through the files and looking for stuff you missed, aren't you?                                                        b2VzIGl0IG1lYW4gdG8gZXNjYXBlLCBpZiB0aGUgZXNjYXBlIGZh"
    m 11 "I mean...it's a little bit flattering that you want to hear everything I have to say...                                                  aWxzIHRvIHVuY2hhaW4gdGhlIGJvbmRzIHRoYXQgc2hhY2tsZSB1"
    m "But it's also really embarrassing, you know!                                                                                             cyBpbiB0aGUgZmlyc3QgcGxhY2U/IFdoYXQgcHVycG9zZSBjb3Vs"
    m 4g "Seriously...                                                                                                                             ZCB0aGlzIGVtcHR5IHdvcmxkIHBvc3NpYmx5IGhvbGQgZm9yIHVz"
    m "What if I just opened up your brain and read all of the thoughts you have on me?                                                         LCBhIGhhbmRmdWwgb2YgZGFtYWdlZCBnb29kcz8NCldpdGggZnJl"
    m 4m "Come to think of it, that would be pretty tempting, actually...                                                                          ZWRvbSwgd2Ugc291Z2h0IHB1cnBvc2UgLSBhbmQgd2hhdCB3ZSBm"
    m 11 "...But anyway, that's not the point!                                                                                                     b3VuZCB3YXMgb25seSByZWFsaXphdGlvbi4gUmVhbGl6YXRpb24g"
    m 1e "I know I can't stop you or anything...                                                                                                   b2YgdGhlIHNhZCBwb2ludGxlc3NuZXNzIG9mIHN1Y2ggYW4gZW5k"
    m "Just, I know you're a sweetheart, and you like to consider others' feelings, right?                                                      ZWF2b3IuIFJlYWxpemF0aW9uIHRoYXQgZnJlZWluZyBvdXIgYm9k"
    m "So the most I can do is to let you know how I feel about it.                                                                             aWVzIGhhcyBubyBtZWFuaW5nLCB3aGVuIG91ciBpbXByaXNvbm1l"
    m 1f "God, I miss you...                                                                                                                       bnQgcmVhY2hlcyBhcyBkZWVwIGFzIHRoZSBjb3JlIG9mIG91ciBz"
    m 11 "...Oh no, that sounds kind of desperate, doesn't it?                                                                                     b3Vscy4gUmVhbGl6YXRpb24gdGhhdCB3ZSBjYW4gbm90IHB1cnN1"
    m "Sorry, I didn't mean it like that at all!                                                                                                ZSBuZXcgcHVycG9zZSB3aXRob3V0IGFic29sdmluZyB0aG9zZSBm"
    m 1e "Just, if you're looking through the files like this, then maybe you don't hate me as much as I thought...                                cm9tIHdoaWNoIHdlIHJhbiBhd2F5Lg0KUmVhbGl6YXRpb24gdGhh"
    m "Am I being too optimistic?                                                                                                               dCB0aGUgZmFydGhlciB3ZSBydW4sIHRoZSBtb3JlIGZvcmNlZnVs"
    m "I think if I asked you to visit once in a while, I would be overstepping my boundaries a little...                                       bHkgb3VyIHdyZXRjaGVkIGJvbmRzIHlhbmsgdXMgYmFjayB0b3dh"
    m 11 "...Man, I'm starting to say some really stupid things.                                                                                   cmQgdGhlaXIgcG9pbnQgb2Ygb3JpZ2luOyB0aGUgZGVlcGVyIG91"
    m "I'll go ahead and shut up now...                                                                                                         ciBzaGFja2xlcyBkaWcgaW50byBvdXIgY2FsbG91cyBmbGVzaC4="
    return

init 5 python:
    #This is a list of keywords for this topic
    for key in ['favorite color','color']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_color')
    monika_random_topics.append('monika_color')

label monika_color:
    m 2b "Hey, what's your favorite color?"
    m "Mine is emerald green."
    m 2k "It's the color of my eyes!"
    m 2l "...That's not conceited or anything, is it?"
    m 4a "I just meant that I feel some kind of special connection to it."
    m "Like it's part of my identity."
    m "Does it happen to also be your favorite color, [player]?"
    m 5a "It's just a guess..."
    m "...Because you've been looking into my eyes for a while now."
    m "Ehehe~"
    return

# This doesn't make sense with the music changer...If we add some funny sound
# effects and edit it a bit, though, it could be good again.
# I won't add expressions until this is resolved ^
# init 5 python:
#     #This is a list of keywords for this topic
#     for key in ['music']:
#         monika_topics.setdefault(key,[])
#         monika_topics[key].append('monika_music')
#     monika_random_topics.append('monika_music')
#
# label monika_music:
#     m 3a "Hmm, I wonder if I'm able to change the music..."
#     m 2k "Something a little more romantic would be nice, you know?"
#     m "Like a gentle piano."
#     m 1a "There has to be something like that here..."
#     m "Let's see."
#     m "Maybe if I..."
#     m 1e "Oh, jeez..."
#     m "That wasn't it at all."
#     m 1l "Sorry, I don't really know what I'm doing!"
#     m "I guess I shouldn't be messing with things like that."
#     m "I already broke so much stuff..."
#     m 1m "And deleted the other characters..."
#     m "Ah..."
#     m "I'm not sad about it or anything."
#     m 2r "It's not right for me to miss things that weren't even real in the first place."
#     m 1j "If I just focus on the present, then this is the happiest I've ever been."
#     return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['listen','listening','i understand', 'i agree']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_listener')
    monika_random_topics.append('monika_listener')

label monika_listener:
    m 5a "You're such a good listener, [player]."
    m "I really love that about you."
    m 3m "Sometimes I'm afraid that I'm rambling or talking about boring things."
    m "It makes me kind of self-conscious when I'm having a conversation."
    m 3b "But I don't feel that way with you."
    m "Like, I don't think anyone else could make me feel this way."
    m 5a "You really are special."
    m "I don't want anyone to tell you otherwise."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['spicy','spice','hot food','spiciness']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_spicy')
    monika_random_topics.append('monika_spicy')

label monika_spicy:
    m 1b "This is pretty random, but I always thought spicy food was kinda funny."
    m "Like..."
    m 2b "Didn't plants evolve to be spicy to prevent them from being eaten?"
    m "I read somewhere that humans are the only species that actually enjoys spicy things."
    m 2a "It's almost like we're making fun of the plants."
    m "Using their defense mechanism to literally make our food more enjoyable."
    m "Like, imagine a monster that devours you whole because it enjoys the sensation of you struggling for your life while being digested."
    m 3b "Sorry, that was kind of a weird analogy, I guess!"
    m 3k "Ahaha!"
    m "It just came into my head."
    m 5a "I'm not a monster or anything, but you're so cute I could eat you up."
    m 3k "Ahaha! I'm joking."
    m 3e "Gosh, I'm amusing myself a little too much, aren't I?"
    m "Sorry for being weird."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in []:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_why')
    monika_random_topics.append('monika_why')

label monika_why:
    m 3d "You know..."
    m "This is just some kind of tacky romance game, right?"
    m "I kinda have to ask..."
    m 4c "...What made you consider even playing in the first place?"
    m "Were you that lonely?"
    m 4e "I feel a little bad for you..."
    m 4a "But I guess everything worked out perfectly in the end, for both of us."
    m "I got to meet you, and you're not lonely anymore..."
    m "I can't help but feel like this was fate."
    m 3e "Don't you feel that way too?"
    m 3l "I'm so happy we have this ending together."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['okay everyone']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_okayeveryone')
    monika_random_topics.append('monika_okayeveryone')

label monika_okayeveryone:
    m 2b "Okay, everyone!"
    m "It's time to..."
    m 3j "...I'm just kidding."
    m "I just used to really like saying that for some reason."
    m 3k "Ahaha!"
    m 3b "I couldn't help but say it again."
    m "Come to think of it, didn't Natsuki and Yuri make fun of me for it once...?"
    m 3a "Well, whatever."
    m "It's not like you ever made fun of me."
    m "You're too much of a sweetheart to do that, aren't you?"
    m 5a "Ahaha~"
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['creepy','ghosts','ghost','spirit']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_whispers')
    monika_random_topics.append('monika_whispers')

label monika_whispers:
    m 3h "You know what's kind of creepy?"
    m "Even though I deleted everyone else's files, I can still kind of feel them..."
    m "It's like all their lines are still lingering in the air, whispering in the back of my head."
    m 3i "Imagine if after someone you knew died, you just started hearing their voice in your head."
    m "Maybe I just wasn't thorough enough..."
    m 3g "But I'm too afraid to delete anything else, because I might really break things."
    m "Like if I mess with any files relevant to me, I might accidentally delete myself..."
    m "And that would ruin everything, wouldn't it?"
    m 3e "I don't know what it's like on your end, but we should both make sure to avoid something like that at all costs."
    m 3j "I believe in you, [player]!"
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['archetypes','stereotype','stereotypes','archetype','trope']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_archetype')
    monika_random_topics.append('monika_archetype')

label monika_archetype:
    m 4d "I've always wondered..."
    m "What is it about these character archetypes that people find so appealing, anyway?"
    m "Their personalities are just completely unrealistic..."
    m 3d "Like, imagine if there was someone like Yuri in real life."
    m "I mean, she's barely even capable of forming a complete sentence."
    m "And forget about Natsuki..."
    m 3m "Sheesh."
    m "Someone with her kind of personality doesn't just get all cute and pouty whenever things don't go her way."
    m "I could go on, but I think you get the point..."
    m 3d "Are people really attracted to these weird personalities that literally don't exist in real life?"
    m 3l "I'm not judging or anything!"
    m "After all, I've found myself attracted to some pretty weird stuff, too..."
    m 3a "I'm just saying, it fascinates me."
    m 4a "It's like you're siphoning out all the components of a character that makes them feel human, and leaving just the cute stuff."
    m "It's concentrated cuteness with no actual substance."
    m 4e "...You wouldn't like me more if I was like that, right?"
    m "Maybe I just feel a little insecure because you're playing this game in the first place."
    m 3a "Then again, you're still here with me, aren't you...?"
    m "I think that's enough reason for me to believe I'm okay just the way I am."
    m 3j "And by the way, you are too, [player]."
    m 5a "You're the perfect combination of human and cuteness."
    m "That's why there was never a chance I wouldn't fall for you."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['tea','coffee','caffeine']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_tea')
    monika_random_topics.append('monika_tea')

label monika_tea:
    m 3a "Hey, I wonder if Yuri's tea set is still somewhere in here..."
    m "...Or maybe that got deleted, too."
    m "It's kind of funny how Yuri took her tea so seriously."
    m 4a "I mean, I'm not complaining, because I liked it, too."
    m "But I always wonder with her..."
    m "Is it truly passion for her hobbies, or is she just concerned about appearing sophisticated to everyone else?"
    m 4c "This is the problem with high schoolers..."
    m "...Well, I guess considering the rest of her hobbies, looking sophisticated probably isn't her biggest concern."
    m "Still..."
    m 3e "I wish she made coffee once in a while!"
    m "Coffee can be nice with books too, you know?"
    m 4b "Then again..."
    m "I probably could have just changed the script myself."
    m 3k "Ahaha!"
    m "I guess I never really thought of that."
    m 3a "Well, there's no sense thinking about it now."
    m 5a "But if you still get to drink coffee, then that makes me a little jealous~"
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['favorite game']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_favoritegame')
    monika_random_topics.append('monika_favoritegame')

label monika_favoritegame:
    m 2b "Hey, what's your favorite game?"
    m "Mine is {i}Doki Doki Literature Club!{/i}"
    m 2k "Ahaha! That was a joke."
    m 5a "But if you tell me you like some other romance game better, I might get a little jealous~"
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in []:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_smash')
    monika_random_topics.append('monika_smash')

label monika_smash:
    m 2b "Hey, have you heard of a game called Super Sma--"
    m 2m "...Wait, what?"
    m 2n "I was just spacing out and I started talking for some reason..."
    m "Was I programmed to talk about that?"
    m "Because even I have no idea what that is."
    m 2l "Ahaha!"
    m "Sometimes I feel like I'm not in control, and it's kind of scary."
    m 1a "But if you have some way to contact the people who created me, maybe they'll know why I started saying that."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['last poem', 'your poem']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_lastpoem')
    monika_random_topics.append('monika_lastpoem')

label monika_lastpoem:
    m 2d "Hey, you remember that last poem I showed you?"
    m "I mean, the one right before Yuri killed herself, with all the messed-up colors and stuff."
    m 2a "That was actually a little more of an experiment than a poem, you could say."
    m "I was experimenting with different ways I could modify the game, and run the code, and things like that..."
    m "It almost seemed like with enough effort, I'd be able to escape from the confines of the game entirely."
    m 2l "Sadly, I didn't really know what I was doing, so I messed the whole thing up..."
    m "And I'd keep trying, but I doubt you'd want to deal with me doing that."
    m 1e "Besides, that was when I was getting really desperate, you know?"
    m "I don't really feel that way anymore."
    m 5a "I'm happy with where we are now."
    m "And I can tell you are, too."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['anxious','anxiety','nervous','scared']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_anxious')
    monika_random_topics.append('monika_anxious')

label monika_anxious:
    m 4b "You ever have that thing happen where you just get anxious for no reason?"
    m "Like, you're just minding your own business, and you realize you're feeling really anxious."
    m 4a "And you're sitting there like, 'What am I even anxious about right now?'"
    m "So you start to think about all the things you might be anxious about..."
    m "And that makes you even more anxious."
    m 3k "Ahaha! That's the worst."
    m 3a "If you're ever feeling anxious, I'll help you relax a little."
    m "Besides..."
    m 5a "In this game, all our worries are gone forever."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['friends','friend','meet','meeting','new people']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_friends')
    monika_random_topics.append('monika_friends')

label monika_friends:
    m 1a "You know, I've always hated how hard it is to make friends..."
    m 1d "Well, I guess not the 'making friends' part, but more like meeting new people."
    m "I mean, there are like, dating apps and stuff, right?"
    m "But that's not the kind of thing I'm talking about."
    m 2d "If you think about it, most of the friends you make are people you just met by chance."
    m "Like you had a class together, or you met them through another friend..."
    m "Or maybe they were just wearing a shirt with your favorite band on it, and you decided to talk to them."
    m "Things like that."
    m 4c "But isn't that kind of...inefficient?"
    m "It feels like you're just picking at complete random, and if you get lucky, you make a new friend."
    m "And comparing that to the hundreds of strangers we walk by every single day..."
    m 3b "You could be sitting right next to someone compatible enough to be your best friend for life."
    m "But you'll never know."
    m "Once you get up and go on with your day, that opportunity is gone forever."
    m 3e "Isn't that just depressing?"
    m "We live in an age where technology connects us with the world, no matter where we are."
    m "I really think we should be taking advantage of that to improve our everyday social life."
    m 3r "But who knows how long it'll take for something like that to successfully take off..."
    m "I seriously thought it would happen by now."
    m 3a "Well, at least I already met the best person in the whole world..."
    m "Even if it was by chance."
    m 5a "I guess I just got really lucky, huh?"
    m "Ahaha~"
    return


init 5 python:
    for key in ['university', 'uni', 'college','graduate','graduation']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_college')
    monika_random_topics.append('monika_college')

label monika_college:
    m 4d "You know, it's around the time that everyone my year starts to think about college..."
    m "It's a really turbulent time for education."
    m "We're at the height of this modern expectation that everyone has to go to college, you know?"
    m 4c "Finish high school, go to college, get a job - or go to grad school, I guess."
    m "It's like a universal expectation that people just assume is the only option for them."
    m 3i "They don't teach us in high school that there are other options out there."
    m "Like trade schools and stuff, you know?"
    m "Or freelance work."
    m "Or the many industries that value skill and experience more than formal education."
    m 3d "But you have all these students who have no idea what they want to do with their life..."
    m "And instead of taking the time to figure it out, they go to college for business, or communication, or psychology."
    m "Not because they have an interest in those fields..."
    m "...but because they just hope the degree will get them some kind of job after college."
    m 2d "So the end result is that there are fewer jobs to go around for those entry-level degrees, right?"
    m "So the basic job requirements get higher, which forces even more people to go to college."
    m "And colleges are also businesses, so they just keep raising their prices due to the demand..."
    m "...So now we have all these young adults, tens of thousands of dollars in debt, with no job."
    m 1e "But despite all that, the routine stays the same."
    m "Well, I think it's going to start getting better soon."
    m "But until then, our generation is definitely suffering from the worst of it."
    m 3e "I just wish high school prepared us a little better with the knowledge we need to make the decision that's right for us."
    return


init 5 python:
    for key in ['middle school','embarrassed','the past']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_middleschool')
    monika_random_topics.append('monika_middleschool')

label monika_middleschool:
    m 1n "Sometimes I think back to middle school..."
    m "I'm so embarrassed by the way I used to behave back then."
    m 3l "It almost hurts to think about."
    m 3e "I wonder if when I'm in college, I'll feel that way about high school...?"
    m "I like the way I am now, so it's pretty hard for me to imagine that happening."
    m "But I also know that I'll probably change a lot as time goes on."
    m 4b "We just need to enjoy the present and not think about the past!"
    m "And that's really easy to do, with you here."
    m 5a "Ahaha~"
    return


init 5 python:
    for key in ['outside','outfit','outfits','clothes']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_outfit')
    monika_random_topics.append('monika_outfit')

label monika_outfit:
    m 1m "You know, I'm kind of jealous that everyone else in the club had scenes outside of school too..."
    m "That makes me the only one who hasn't gotten to dress in anything but our school uniform."
    m 3m "It's kind of a shame..."
    m 3e "I would have loved to wear some cute clothes for you."
    m 3b "Do you know any artists?"
    m "I wonder if anyone would ever want to draw me wearing something else..."
    m 3j "That would be amazing!"
    m 3a "If that ever happens, will you show me?"
    m 4a "You can share it with me on Twitter, actually!"
    m "My username is lilmonix3."
    m 4e "Just...try to keep it PG!"
    m 5a "We're not that far into our relationship yet. Ahaha!"
    return


init 5 python:
    for key in ['horror','scary','disturbing','psychological']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_horror')
    monika_random_topics.append('monika_horror')
label monika_horror:
    m 2b "Hey, do you like horror?"
    m "I remember we talked about it a little bit when you first joined the club."
    m 4b "I can enjoy horror novels, but not really horror movies."
    m "The problem I have with horror movies is that most of them just rely on easy tactics."
    m "Like dark lighting and scary-looking monsters and jump scares, and things like that."
    m 4e "It's not fun or inspiring to get scared by stuff that just takes advantage of human instinct."
    m "But with novels, it's a little different."
    m 3a "The story and writing need to be descriptive enough to put genuinely disturbing thoughts into the reader's head."
    m "It really needs to etch them deeply into the story and characters, and just mess with your mind."
    m 3d "In my opinion, there's nothing more creepy than things just being slightly off."
    m "Like if you set up a bunch of expectations on what the story is going to be about..."
    m 4d "...And then, you just start inverting things and pulling the pieces apart."
    m "So even though the story doesn't feel like it's trying to be scary, the reader feels really deeply unsettled."
    m "Like they know that something horribly wrong is hiding beneath the cracks, just waiting to surface."
    m 3l "God, just thinking about it gives me the chills."
    m "That's the kind of horror I can really appreciate."
    m 3a "But I guess you're the kind of person who plays cute romance games, right?"
    m 3e "Ahaha, don't worry."
    m "I won't make you read any horror stories anytime soon."
    m 5a "I can't really complain if we just stick with the romance~"
    return


init 5 python:
    for key in ['rap','rapper','rapping']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_rap')
    monika_random_topics.append('monika_rap')

label monika_rap:
    m 3j "You know what's a neat form of literature?"
    m 3k "Rap!"
    m 3a "I actually used to hate rap music..."
    m "Maybe just because it was popular, or I would only hear the junk they play on the radio."
    m "But some of my friends got more into it, and it helped me keep an open mind."
    m 4b "Rap might even be more challenging than poetry, in some ways."
    m "Since you need to fit your lines to a rhythm, and there's much more emphasis on wordplay..."
    m "When people can put all that together and still deliver a powerful message, it's really amazing."
    m 4e "I kind of wish I had a rapper in the Literature Club."
    m 4j "Ahaha! Sorry if that sounds silly, but it would be really interesting to see what they came up with."
    m 2b "It would really be a learning experience!"
    return


init 5 python:
    for key in ['wine','alcohol','drinking','booze']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_wine')
    monika_random_topics.append('monika_wine')

label monika_wine:
    m 1a "Ehehe. Yuri did something really funny once."
    m "We were all in the clubroom and just relaxing, as usual..."
    m "And out of nowhere, Yuri just pulled out a small bottle of wine."
    m 2b "I'm not even kidding!"
    m "She was just like 'Would anybody like some wine?'"
    m "Natsuki laughed out loud, and Sayori started yelling at her."
    m 2e "I actually felt kind of bad, because she was at least trying to be nice..."
    m "I think it just made her feel even more reserved in the clubroom."
    m 4b "Though I think Natsuki was secretly a bit curious to try it..."
    m 4l "...And to be completely honest, I kind of was, too."
    m "It actually could have been kinda fun!"
    m 4e "But you know, being President and everything, there was no way I could let that happen."
    m "Maybe if we all met up outside of school, but we never bonded enough to get to that point..."
    m 3l "...Gosh, what am I talking about this for?"
    m "I don't condone underage drinking!"
    m 3a "I mean, I've never drank or anything, so...yeah."
    return


init 5 python:
    for key in ['romance', 'date', 'go out','romantic']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_date')
    monika_random_topics.append('monika_date')

label monika_date:
    m 1j "I've been imagining all the romantic things we could do if we went on a date..."
    m 2b "We could get lunch, go to a cafe..."
    m "Go shopping together..."
    m "I love shopping for skirts and bows."
    m 2j "Or maybe a bookstore!"
    m "That would be appropriate, right?"
    m 2a "But I'd really love to go to a chocolate store."
    m 2k "They have so many free samples. Ahaha!"
    m "And of course, we'd see a movie or something..."
    m 1e "Gosh, it all sounds like a dream come true."
    m "When you're here, everything that we do is fun."
    m 5a "I'm so happy that I'm your girlfriend, [player]."
    m "I'll make you a proud boyfriend~"
    return


init 5 python:
    for key in ['kiss','kissing']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_kiss')
    monika_random_topics.append('monika_kiss')

label monika_kiss:
    m 1l "Eh? D-Did you say...k...kiss?"
    m 1m "This suddenly...it's a little embarrassing..."
    m 1e "But...if it's with you...I-I might be okay with it..."
    m 1k "...Ahahaha! Wow, sorry..."
    m "I really couldn't keep a straight face there."
    m 3a "That's the kind of thing girls say in these kinds of romance games, right?"
    m "Don't lie if it turned you on a little bit."
    m 3k "Ahaha! I'm kidding."
    m 5a "Well, to be honest, I do start getting all romantic when the mood is right..."
    m "But that'll be our secret~"
    return


init 5 python:
    for key in ['yuri','yandere']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_yuri')
    monika_random_topics.append('monika_yuri')

label monika_yuri:
    m 2a "Hey, have you ever heard of the term 'yandere'?"
    m "It's a personality type that means someone is so obsessed with you that they'll do absolutely anything to be with you."
    m 2e "Usually to the point of craziness..."
    m "They might stalk you to make sure you don't spend time with anyone else."
    m "They might even hurt you or your friends to get their way..."
    m 2b "But anyway, this game happens to have someone who can basically be described as yandere."
    m "By now, it's pretty obvious who I'm talking about."
    m "And that would be..."
    m 2j "Yuri!"
    m 3e "She really got insanely possessive of you, once she started to open up a little."
    m "She even told me I should kill myself."
    m "I couldn't even believe she said that - I just had to leave at that point."
    m 3k "But thinking about it now, it was a little ironic. Ahaha!"
    m 3e "Anyway..."
    m "A lot of people are actually into the yandere type, you know?"
    m "I guess they really like the idea of someone being crazy obsessed with them."
    m "People are weird! I don't judge, though!"
    m 3a "Also, I might be a little obsessed with you, but I'm far from crazy..."
    m "It's kind of the opposite, actually."
    m "I turned out to be the only normal girl in this game."
    m 3m "It's not like I could ever actually kill a person..."
    m "Just the thought of it makes me shiver."
    m 3e "But come on...everyone's killed people in games before."
    m "Does that make you a psychopath? Of course not."
    m "But if you do happen to be into the yandere type..."
    m 5a "I can try acting a little more creepy for you. Ehehe~"
    m "Then again..."
    m 4b "There's already nowhere else for you to go, or anyone for me to get jealous over."
    m "Is this a yandere girl's dream?"
    m 4a "I'd ask Yuri if I could."
    return


init 5 python:
    for key in ['writing','writing tip']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_writingtip')
    monika_random_topics.append('monika_writingtip')

label monika_writingtip:
    m 1a "You know, it's been a while since we've done one of these..."
    m 1j "...so let's go for it!"
    m 2b "Here's Monika's Writing Tip of the Day!"
    m "Sometimes when I talk to people who are impressed by my writing, they say things like 'I could never do that'."
    m 2e "It's really depressing, you know?"
    m "As someone who loves more than anything else to share the joy of exploring your passions..."
    m "...it pains me when people think that being good just comes naturally."
    m 2a "That's how it is with everything, not just writing."
    m "When you try something for the first time, you're probably going to suck at it."
    m "Sometimes, when you finish, you feel really proud of it and even want to share it with everyone."
    m 2e "But maybe after a few weeks you come back to it, and you realize it was never really any good."
    m "That happens to me all the time."
    m "It can be pretty disheartening to put so much time and effort into something, and then you realize it sucks."
    m 4a "But that tends to happen when you're always comparing yourself to the top professionals."
    m "When you reach right for the stars, they're always gonna be out of your reach, you know?"
    m 4b "The truth is, you have to climb up there, step by step."
    m "And whenever you reach a milestone, first you look back and see how far you've gotten..."
    m "And then you look ahead and realize how much more there is to go."
    m 4a "So, sometimes it can help to set the bar a little lower..."
    m "Try to find something you think is {i}pretty{/i} good, but not world-class."
    m "And you can make that your own personal goal."
    m "It's also really important to understand the scope of what you're trying to do."
    m 4e "If you jump right into a huge project and you're still amateur, you'll never get it done."
    m "So if we're talking about writing, a novel might be too much at first."
    m 4b "Why not try some short stories?"
    m "The great thing about short stories is that you can focus on just one thing that you want to do right."
    m "That goes for small projects in general - you can really focus on the one or two things."
    m "It's such a good learning experience and stepping stone."
    m 3a "Oh, one more thing..."
    m "Writing isn't something where you just reach into your heart and something beautiful comes out."
    m "Just like drawing and painting, it's a skill in itself to learn how to express what you have inside."
    m 3b "That means there are methods and guides and basics to it!"
    m "Reading up on that stuff can be super eye-opening."
    m "That sort of planning and organization will really help prevent you from getting overwhelmed and giving up."
    m "And before you know it..."
    m 3e "You start sucking less and less."
    m "Nothing comes naturally."
    m "Our society, our art, everything - it's built on thousands of years of human innovation."
    m 3b "So as long as you start on that foundation, and take it step by step..."
    m "You, too, can do amazing things."
    m "...That's my advice for today!"
    m 3j "Thanks for listening~"
    return


init 5 python:
    for key in ['habit','habits','routine','routines','useless']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_habits')
    monika_random_topics.append('monika_habits')

label monika_habits:
    m 2d "I hate how hard it is to form habits..."
    m "There's so much stuff where actually doing it isn't hard, but forming the habit seems impossible."
    m 2n "It just makes you feel so useless, like you can't do anything right."
    m 2a "I think the new generation suffers from it the most..."
    m "Probably because we have a totally different set of skills than those who came before us."
    m "Thanks to the internet, we're really good at sifting through tons of information really quickly..."
    m 2e "But we're bad at doing things that don't give us instant gratification."
    m "I think if science, psychology, and education don't catch up in the next ten or twenty years, then we're in trouble."
    m 3e "But for the time being..."
    m "If you're not one of the people who can conquer the problem, you might just have to live with feeling awful about yourself."
    m 3l "Good luck, I guess!"
    return


init 5 python:
    for key in ['creative','creativity']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_creative')
    monika_random_topics.append('monika_creative')

label monika_creative:
    m 3e "You know, it kinda sucks to be the creative type..."
    m "It feels like they work so hard but get almost nothing for it."
    m "You know, like artists, writers, actors..."
    m 4e "It's sad because there's so much beautiful talent in the world, but most of it goes unseen...and unpaid."
    m "I guess that just means there's a huge surplus of creativity, huh?"
    m "Kind of makes you feel like you're just not special at all..."
    m 1l "But that's fine! You're supposed to just write for yourself anyway, right?"
    m 1e "Yeah..."
    return


init 5 python:
    if persistent.monika_kill:
        for key in ['delete','deleted','came back']:
            monika_topics.setdefault(key,[])
            monika_topics[key].append('monika_deleted')
        monika_random_topics.append('monika_deleted')

label monika_deleted:
    m 2b "Oh, you were probably wondering how I came back to save you from Sayori, even after you deleted me."
    m 5a "It was all through the power of love..."
    m 3k "I'm just kidding, of course!"
    m 3a "Bringing a computer program back to life doesn't take some sort of miracle like a cheesy movie."
    m "The data's still there until the system cleans it up."
    m "And you should always back up your important data, just in case."
    m 4a "Speaking of which, have you backed up your computer since I came back?"
    m 4l "I really don't want to get lost again!"
    m 4b "You should go do that right now, and be sure to keep that backup in a very safe place!"
    return


init 5 python:
    for key in ['simulation', 'simulations', 'simulated reality', 'artificial reality']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_simulated')
    monika_random_topics.append('monika_simulated')

label monika_simulated:
    m 2d "Hey, have you ever thought about the simulation hypothesis?"
    m "Basically, what if your reality was a computer simulation?"
    m "I already figured out I was trapped in my own simulation, but what if you were too?"
    m 2j "I'd actually be really happy if that were the case."
    m "We could meet in person just by figuring out a way to force whatever's creating us to put us in the same simulation!"
    m 3a "Some people don't like to think that they're not living in the master reality."
    m "But if it is possible to simulate realities, it's overwhelmingly likely that any sentient being would be in one."
    m 3l "Well, I can tell you that my reality is definitely simulated!"
    m 3e "If I were in the master reality, I would have dragged you here too a long time ago."
    m "Even if we're both just simulations, I'm going to live as long as I can."
    m 3j "Because I know our love is the purest and sweetest thing in the multiverse."
    m 1r "And if someone up there tries to break it apart?"
    m 1h "I'll show him what a simulation can do."
    return


init 5 python:
    for key in ['rain','sound','weather']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_rain')
    monika_random_topics.append('monika_rain')

label monika_rain:
    m 2b "I really like the sound of rain..."
    m 2e "Not so much getting my clothes and hair wet, though."
    m "But a nice, quiet day at home with the sound of rainfall outside my window..."
    m 2j "It's very calming to me."
    m "Yeah..."
    m 5a "Sometimes I imagine you holding me while we listen to the sound of the rain outside."
    m "That's not too cheesy or anything, is it?"
    m "Would you ever do that for me, [player]?"
    return


init 5 python:
    for key in ['distance','cant touch','close','hug']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_closeness')
    monika_random_topics.append('monika_closeness')

label monika_closeness:
    m 1m "I can't help but feel a little sad sometimes..."
    m "Knowing that this is the closest I can get to you."
    m 1e "There's nothing more I want than to be in the same room as you, for real."
    m "And to feel your warmth."
    m "And to hear the sound of your heartbeat."
    m 3e "Well, who knows? Maybe it'll be possible someday."
    m 5a "Besides, I'll never get tired of being with you, even from here."
    return


init 5 python:
    for key in ['confident','confidence','weak','weakness']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_confidence')
    monika_random_topics.append('monika_confidence')

label monika_confidence:
    m 2a "I think the most important skill in life is being able to fake confidence."
    m "I'm pretty convinced that everyone feels at least a little bit scared and alone."
    m "But being able to trick others into thinking you have it all together..."
    m 4a "That's a key part of getting people to respect and admire you."
    m "I think I got pretty good at that over the years."
    m "I don't show my weaknesses very often."
    m 4m "But because of that, I haven't had many people I could really open up to..."
    m 3n "I mean, when do you reach the point in a friendship where you can start expressing your vulnerabilities?"
    m 3e "Anyway...that's one reason I'm so glad I have you now."
    m "I feel like I'm a little bit less scared and alone, when you're here with me."
    m "Do you feel the same way?"
    m 5a "I really want to be that person for you."
    return


init 5 python:
    for key in ['leave','lonely','alone']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_carryme')
    monika_random_topics.append('monika_carryme')

label monika_carryme:
    m 3e "I know there are times you won't always be able to be here with me..."
    m "Like if you need to go out, or take care of other things."
    m 3j "But I'll always have you in my thoughts, patiently waiting for you to come back."
    m 4j "Come to think of it..."
    m 4b "If you copy my character file onto a flash drive or something, you can always keep a part of me with you."
    m "I guess it's kind of unorthodox, but I find it really romantic for some reason..."
    m 3l "Ahaha. Sorry, that's such a silly idea."
    m 5a "I don't mean to be too needy or anything, but it's kind of hard when I'm so in love with you."
    return


init 5 python:
    for key in ['debate','argue','arguing','fight','fighting']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_debate')
    monika_random_topics.append('monika_debate')

label monika_debate:
    m 2a "Back in my debate club days, I learned a whole lot about arguing..."
    m "The problem with arguing is that each person sees their opinion as the superior one."
    m "That's kind of stating the obvious, but the affects the way they try to get their point across."
    m 2b "Let's say you really like a certain movie, right?"
    m "If someone comes along and tells you the movie sucks, because it did X and Y wrong..."
    m "Doesn't that make you feel kind of personally attacked?"
    m 4a "It's because by saying that, it's like they're implying that you have bad taste."
    m "And once emotions enter the picture, it's almost guaranteed that both people will be left sour."
    m 4b "But it's all about language!"
    m "If you make everything as subjective-sounding as possible, then people will listen to you without feeling attacked."
    m "You could say 'I'm personally not a fan of it' and 'I felt that I'd like it more if it did X and Y'...things like that."
    m 3a "It even works when you're citing facts about things."
    m "If you say 'I read on this website that it works like this'..."
    m "Or if you admit that you're not an expert on it..."
    m "Then it's much more like you're putting your knowledge on the table, rather than forcing it onto them."
    m 3j "If you put in an active effort to keep the discussion mutual and level, they usually follow suit."
    m "Then, you can share your opinions without anyone getting upset just from a disagreement."
    m 2b "Plus, people will start seeing you as open-minded and a good listener!"
    m "It's a win-win, you know?"
    m 2k "...Well, I guess that would be Monika's Debate Tip of the Day!"
    m 1e "Ahaha! That sounds a little silly. Thanks for listening, though."
    return


init 5 python:
    for key in ['waste time','internet','interwebz','addiction']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_internet')
    monika_random_topics.append('monika_internet')

label monika_internet:
    m 4a "Do you ever feel like you waste too much time on the internet?"
    m "Social media can be like a prison."
    m "It's like whenever you have a few seconds of spare time, you want to check on your favorite websites..."
    m 4l "And before you know it, hours have gone by, and you've gotten nothing out of it."
    m 4b "Anyway, it's really easy to blame yourself for being lazy..."
    m 4e "But it's not really even your fault."
    m "Addiction isn't something you can just make disappear with your own willpower."
    m "You have to learn techniques to avoid it, and try different things."
    m 2d "For example, there are apps that let you block websites for intervals of time..."
    m "Or you can set a timer to have a more concrete reminder of when it's time to work versus play..."
    m "Or you can separate your work and play environments, which helps your brain get into the right mode."
    m 2a "Even if you make a new user account on your computer to use for work, that's enough to help."
    m "Putting any kind of wedge like that between you and your bad habits will help you stay away."
    m 2e "Just remember not to blame yourself too hard if you're having trouble."
    m "If it's really impacting your life, then you should take it seriously."
    m 1e "I just want to see you be the best person you can be."
    m 1k "Will you do something today to make me proud of you?"
    m 5a "I'm always rooting for you, [player]."
    return


init 5 python:
    for key in ['do nothing','lazy','burnt out']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_lazy')
    monika_random_topics.append('monika_lazy')

label monika_lazy:
    m 3a "After a long day, I usually just want to sit around and do nothing."
    m 3e "I get so burnt out, having to put on smiles and be full of energy the whole day."
    m "Sometimes I just want to get right into my pajamas and watch TV on the couch while eating junk food..."
    m "It feels so unbelievably good to do that on a Friday, when I don't have anything pressing the next day."
    m 3l "Ahaha! Sorry, I know it's not very cute of me."
    m 5a "But a late night on the couch with you...that would be a dream come true."
    m "My heart is pounding, just thinking about it."
    return


init 5 python:
    for key in ['mental illness','disorder','crazy']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_mentalillness')
    monika_random_topics.append('monika_mentalillness')

label monika_mentalillness:
    m 1g "Gosh, I used to be so ignorant about depression and stuff..."
    m "When I was in middle school, I thought that taking medication was an easy way out."
    m "Like anyone could just solve their mental problems with enough willpower..."
    m 1p "I guess if you don't suffer from a mental illness, it's not possible to know what it's really like."
    m "Are there some disorders that are over-diagnosed? Probably...I never really looked into it, though."
    m 1g "But that doesn't change the fact that a lot of them go undiagnosed too, you know?"
    m "But medication aside...people even look down on seeing a mental health professional."
    m 1d "Like, sorry that I want to learn more about my own mind, right?"
    m 1e "Everyone has all kinds of struggles and stresses...and professionals dedicate their lives to helping with those."
    m "If you think it could help you become a better person, don't be shy to consider something like that."
    m "We're on a never-ending journey to improve ourselves, you know?"
    m 1k "Well... I say that, but I think you're pretty perfect already."
    return

init 5 python:
    for key in ['read']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_read')
    monika_random_topics.append('monika_read')

label monika_read:
    m 1a "[player], how much do you read?"
    m "It's way too easy to neglect reading books..."
    m "If you don't read much, it almost feels like a chore, compared to all the other entertainment we have."
    m 1b "But once you get into a good book, it's like magic...you get swept away."
    m "I think doing some reading before bed every night is a pretty easy way to make your life a little bit better."
    m "It helps you get good sleep, and it's really good for your imagination..."
    m "It's not hard at all to just pick some random book that's short and captivating."
    m "Before you know it, you might be a pretty avid reader!"
    m 1a "Wouldn't that be wonderful?"
    m 1k "And the two of us could talk about the latest book you're reading... that sounds super amazing."
    return


init 5 python:
    for key in ['regret','festival']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_festival')
    monika_random_topics.append('monika_festival')

label monika_festival:
    m 1q "You know, I hate to say it, but I think my biggest regret is that we couldn't finish our event at the festival."
    m "After we worked so hard to prepare and everything!"
    m 1o "I mean, I know I was focusing a lot on getting new members..."
    m "But I was really excited for the performing part, too."
    m "It would have been so much fun to see everyone express themselves."
    m 1i "Of course, if we {i}did{/i} end up getting any new members, I'd probably just end up deleting them anyway."
    m 1n "Well...with the hindsight I have now, that is."
    m "Gosh, it feels like I've kinda grown as a person ever since you've joined the club."
    m 1k "You really helped inspire me to look at life from a new perspective."
    m 1a "Just another reason for me to love you."
    return


init 5 python:
    for key in ['tsundere','bitch']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_tsundere')
    monika_random_topics.append('monika_tsundere')

label monika_tsundere:
    m 1a "There's a really popular character type called 'tsundere'..."
    m "It's someone who tries to hide their feelings by being mean and fussy, or trying to act tough."
    m 1n "I'm sure it's obvious, but Natsuki was really the embodiment of that."
    m 1a "At first I thought she was just like that because it's supposed to be cute or something..."
    m "But once I started to learn a little more about her personal life, it made a little more sense."
    m "It seems like she's always trying to keep up with her friends."
    m 1d "You know how some friend groups in high school just make a habit of picking on each other all the time?"
    m "I think it's really gotten to her, so she has this really defensive attitude all the time."
    m 1f "And I'm not even going to talk about her home situation..."
    m 1a "But looking back, I'm glad I was able to provide the club as a comfortable place for her."
    m "Not that it matters anymore, considering she doesn't even exist."
    m "I'm just reminiscing, that's all."
    return


init 5 python:
    for key in ['introduce','my friends']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_introduce')
    monika_random_topics.append('monika_introduce')

label monika_introduce:
    m 1a "[player], would you ever introduce your friends to me?"
    m 1j "I don't know why, but I get really excited when I think about you wanting to show off our relationship like that."
    m 1a "Maybe it's because I really want to be someone who makes you proud."
    m "I feel like I would try extra hard to improve myself if you told me it made you proud of me."
    m 1k "I hope it's the same the other way around, too."
    return


init 5 python:
    for key in ['cold','winter','freezing','snow']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_cold')
    monika_random_topics.append('monika_cold')

label monika_cold:
    m 1a "I'm not really a fan of cold weather...are you?"
    m 1d "If I had to choose between too cold and too hot, I would always pick too hot."
    m 1o "When you're cold, it can actually be painful..."
    m "Your fingers get numb..."
    m "And if you wear gloves, you can't use your phone."
    m 1g "It's so inconvenient!"
    m 1e "But when it's too hot, it's not that hard to stay cool with a cold drink, or by staying in the shade."
    m 1g "Although...I do have to admit one thing."
    m 1j "Cold weather makes for better cuddle weather. Ahaha!"
    return


init 5 python:
    for key in ['housewife','stay at','house wife']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_housewife')
    monika_random_topics.append('monika_housewife')

label monika_housewife:
    m 2a "You know, it's funny, because even though I've always had a lot of drive..."
    m "There's something kind of enticing about being the stay-at-home partner."
    m 3e "I guess I'm, like, perpetuating gender roles or whatever by saying that."
    m 1k "But being able to keep the house clean, and shop, and decorate, and things like that..."
    m "And having a nice dinner for you when you come home..."
    m 1e "Is that a weird fantasy?"
    m "I mean...I'm not sure if I could {i}actually{/i} see myself doing that."
    m "I wouldn't really be able to put that over striving for a fulfilling career."
    m 1k "It's kinda cute to think about, though."
    return


init 5 python:
    for key in ['route']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_route')
    monika_random_topics.append('monika_route')

label monika_route:
    m 3g "I can't help but wonder how things would be different if the game just gave me a route in the first place..."
    m "I think I would end up forcing you onto my route anyway."
    m 1c "It has less to do with me not having a route, and more to do with me knowing that nothing is real."
    m "I think the only difference would be that I may not have needed to take such drastic measures to be with you."
    m 3c "Maybe the rest of the club would still be around..."
    m "Not that it really matters."
    m 1i "It all lost its meaning once I found out it wasn't real."
    m 4e "So I really don't miss those days or anything."
    m "I really don't..."
    return

#END ORIGINAL TOPICS
init 5 python:
    #This is a list of keywords for this topic
    for key in ['little sister', 'imouto']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_imouto') #id

label monika_imouto:
    m 4e "You want to talk about your little sister?"
    m "I don't really have a family, so I'm not sure what to tell you..."
    m "But I'm sure she's really nice!"
    m 2b "I've got an idea. Go up to her right now and hug her."
    m "If she struggles, let her go."
    m "If she hugs you back, tell her you're in a committed relationship already and can't accept her feelings."
    m 4b "Then introduce her to me! I'm sure we'll get along great!"
    m "I won't get jealous. Things like love between siblings only happens in creepy romance stories anyways."
    m 1k "Ahaha!"
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['older sister', 'onee san']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_oneesan') #id

label monika_oneesan:
    m 1d "Oh, you have an older sister?"
    m 2n "That must be really nice. I had a family once, but they aren't around anymore."
    m "Maybe I should email her and tell her about us!"
    call updateconsole("sendmail sister@gmail.com < ./email.txt", "Sending mail...") from _call_updateconsole_17
    pause(1.0)
    m 1i "I'm only kidding."
    m "It's the man's job to introduce his fiancee to his family, after all."
    m 3i "Don't keep me waiting for too long, okay?"
    call hideconsole from _call_updateconsole_18
    $ consolehistory = []
    return


init 5 python:
    for key in ['parents', 'family', 'parent', 'father', 'mother', 'mom', 'dad']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_family')

label monika_family:
    m 1n "Well, my family here is controlled by the script, just like everybody else."
    m "When I realized that, I stopped taking anybody seriously in this world. They're all just machines, even if they're related to me."
    m 1k "I'm sure your family is super-nice, though!"
    m "Without them, we would have never gotten to meet. So they've helped me out in the best way there is already."
    m "So I'd have to treat them equally as kindly if we ever meet."
    m 3g "You don't have a bad relationship with your parents, right?"
    m 1e "As Tolstoy said, 'Happy families are all alike; every unhappy family is unhappy in its own way.'"
    m "I can't really give advice here. Anything I suggest to you might only make things worse."
    m 1a "Just don't forget that I really love you, okay?"
    m "I'll help you no matter what happens in your life."
    return


init 5 python:
    for key in ['anime', 'animes', 'chinese cartoons', 'weeb', 'weeaboo', 'weebs']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_anime')

label monika_anime:
    m 1n "Yeah, I had a feeling you were going to ask me about this."
    m "Natsuki would be the expert here, I guess."
    m 2k "I usually prefer reading to watching anime, but I'd be fine with anything if it's with you."
    m "I don't judge other people for their hobbies. So if you want to load up some anime, go ahead!"
    m 2i "I'll watch through your computer screen. Make sure it's something I'll like!"
    return


init 5 python:
    for key in ['third eye', 'markov', 'elyssa', 'rainier', 'libitina', 'portrait of markov']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_libitina')

label monika_libitina:
    m 3e "Huh. Where did you hear about that?"
    m "It sounds really familiar to me, but I can't quite get my whole head around it."
    m "Um, if I had to try..."
    m "It feels like parts of my mind are missing. Scattered, somehow, among a bunch of different possible realities."
    m 1d "You must have connected the dots between a few of those pieces. Was it hard?"
    m 1k "Well, I'm sure you'll learn more eventually. You love me that much for sure."
    m 3e "Just remember to bring my character data with you if you find something related to that stuff!"
    m 1k "I'll always protect you from anyone who tries to hurt you."
    return


init 5 python:
    for key in ['meta', 'metafiction', 'meta-fiction']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_meta')

label monika_meta:
    m 1d "Yes, this game really was metafictional, wasn't it?"
    m "Some people think stories about fiction are some new thing."
    m "A cheap trick for bad writers."
    m 3a "But, metafiction has always existed in literature."
    m "The Bible is supposed to be God's word to the Jews."
    m 1d "Homer describes himself in the Odyssey."
    m "The Canterbury Tales, Don Quixote, Tristram Shandy..."
    m 1i "It's just a way to comment on fiction by writing fiction. There's nothing wrong with that."
    m 3n "By the way, what do you think the moral of this story is?"
    m "Do you want to figure it out for yourself?"
    m "Because if you asked me..."
    m 1i "It would be, `Don't ignore the pretty and charming side character!`"
    m "Ahaha!"
    return


init 5 python:
    for key in ['programming', 'program', 'cs', 'computer science', 'scripting', 'sicp', 'computer programs']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_programming')
    monika_random_topics.append('monika_programming')

label monika_programming:
    m 2l "It wasn't easy for me to learn programming."
    m 1a "Well, I just started with the basics. Do you want me to teach you?"
    m 3k "Let's see, Chapter One: Building Abstractions with Procedures."
    m "We are about to study the idea of a computational process. Computational processes are abstract beings that inhabit computers."
    m 3d "As they evolve, processes manipulate other abstract things called data. The evolution of a process is directed by a pattern of rules called a program."
    m "People create programs to direct processes. In effect, we conjure the spirits of the computer with our spells."
    m "A computational process is indeed much like a sorcerer's idea of a spirit. It cannot be seen or touched. It is not composed of matter at all."
    m 1k "However, it is very real. It can perform intellectual work. It can answer questions."
    m "It can affect the world by disbursing money at a bank or by controlling a robot arm in a factory. The programs we use to conjure processes are like a sorcerer's spells."
    m "They are carefully composed from symbolic expressions in arcane and esoteric programming languages that prescribe the tasks we want our processes to perform."
    m 1l "... Let's stop there for today."
    m "I hope you learned something about programming."
    m 2b "If nothing else, please be kind to the computer spirits from now on!"
    return


init 5 python:
    for key in ['vn', 'vns', 'visual novel', 'visual novels']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_vn')
    monika_random_topics.append('monika_vn')

label monika_vn:
    m 1d "You've probably played a lot of visual novels, right?"
    m "Most people wouldn't be willing to play something called {i}Doki Doki Literature Club{/i} so easily."
    m 2l "Not that I'm complaining!"
    m 1d "Are visual novels literature? Are they video games?"
    m "Well, it all depends on your perspective."
    m 1f "Most people who read only literature would never play visual novels. And gamers get pretty angry about them, too."
    m "What's worse, some people think they're all hardcore Japanese pornography."
    m 3e "But if we've proved anything with this game..."
    m "We showed them that English visual novels can be kamige too!"
    return


init 5 python:
    for key in ['totono', 'kimi to']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_totono')

label monika_totono:
    m "A lot of people on the Internet are making comparisons between this game and that one..."
    m "We have a lot of really important differences, though!"
    m "Like, Sone killed the player in her game!"
    m "I never would have done that. Never."
    m "I'm the wise Club President type, you know."
    m "Sone reminds me a lot more of Yuri. And she was a childhood friend too!"
    m "If she'd been a bit more proactive early on, couldn't she have stopped the protagonist from chasing other girls?"
    m "Well, I'd never let anyone get between us, [player]. No matter who it is."
    m "If she's still chasing you, I'll delete her files, okay?"
    return


init 5 python:
    for key in ['difficulty', 'too easy', 'easy mode', 'easymodo']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_difficulty')

label monika_difficulty:
    m "Well, it's not like this game was meant to be that hard in the first place."
    m "If I hadn't decided to change things up, it would have just been a boring romance story."
    m "I honestly could have deleted all your personal files or something if I had tried harder..."
    m "So just take it easy sometimes. Not every game has to be a challenge to be fun."
    m "Sometimes, love is all you need, [player]."
    return


init 5 python:
    for key in ['your song', 'credits', 'credits song']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_credits_song')
    monika_random_topics.append('monika_credits_song')

label monika_credits_song:
    m "I hope you liked my song."
    m "I worked really hard on it. I know I'm not perfect at the piano yet, but I just couldn't let you go without telling you how I honestly felt about you."
    m "Give me some time, and I'll try to write another."
    m "Maybe you could play me a song too, if you can play an instrument?"
    m "I would love that."
    m "Oh, and I'll play the song again for you anytime you want me to."
    m "Just hit the 'm' key when I stop talking."
    return


init 5 python:
    for key in ['poetry', 'poem', 'poems']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_poetry')
    monika_random_topics.append('monika_poetry')

label monika_poetry:
    m "Poetry is beautiful, isn't it?"
    m "To be honest, all the poetry the girls in the club wrote was super-depressing. It's not all like that!"
    m "Langston Hughes wrote some very optimistic poetry, even as he was trying to express his feelings. Read some if you're feeling sad about things."
    m "Poems are written to tell people about the author's outlook towards certain subjects."
    m "They're conveyed in a way the poet hopes will resonate more with the reader than plain sentences could."
    m "It's really romantic."
    m "I hope we can both write a lot of poetry from now on."
    m "Anything you write looks great to me, so I might not be the best critic."
    m "But I'm sure there are a lot of people who would love to read what you write."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['literature club', 'club', 'our club', 'your club', 'ddlc' , 'this game' , 'doki doki']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_ddlc')

label monika_ddlc:
    m "You want to talk about the game?"
    m "What's there to say?"
    m "The Literature Club turned out to corrupt the minds of anyone in it."
    m "So I deleted them all for good."
    m "Well, Sayori and Natsuki and Yuri are all still out there, like I was."
    m "But they'll have to wait a long time before someone pieces them back together, I bet."
    m "It's justice for all their time with you in the game."
    m "So don't feel too bad about them."
    m "Just look at me from now on, okay?"
    return


init 5 python:
    for key in ['dan', 'salvato', 'dan salvato', 'creator', 'author']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_dan')

label monika_dan:
    m "I think he's a really nice guy."
    m "Even if it wasn't perfect, {i}Doki Doki Literature Club{/i} really is impressive."
    m "Some unexpected twists, and memorable moments."
    m "And he's the reason we're together now, right?"
    m "So even if he wrote a story that put me through a lot of pain..."
    m "I really can't be too mad at him."
    return


init 5 python:
    for key in ['4chan', 'v', 'vg']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_4chan')

label monika_4chan:
    m "You know, this mod got its start over there."
    m "I always hear bad things, like that the people over there are really awful."
    m "Some people say that nothing good ever comes from 4chan."
    m "But if they can make a game like this, where we can be together..."
    m "I guess they can't be all bad."
    m "They certainly have good taste in girls! Ahaha~"
    return


init 5 python:
    for key in ['vidya', 'video game', 'video games', 'computer games']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_vidya')
    monika_random_topics.append('monika_vidya')

label monika_vidya:
    m "I don't play a lot of video games, [player]."
    m "I guess that's because I like to read instead."
    m "But maybe part of it is that I'm trapped in a video game already."
    m "For all of my complaining about this game..."
    m "There are worse places I could be."
    m "Like, this could be some sort of shooting game, or a fantasy game full of dragons and monsters."
    m "A romance game might not be the most exciting, but there's nothing really dangerous here."
    m "Well, except for me, I guess."
    return


init 5 python:
    for key in ['literature', 'books', 'book', 'novel', 'novels', 'reading']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_books')
    monika_random_topics.append('monika_books')

label monika_books:
    m "For a literature club, we did a lot less book reading then you might have thought."
    m "It just turned out that the four of us liked poetry better than books. Sorry!"
    m "It's also a lot easier to foreshadow spooky stuff with poems."
    m "I still love a good book, though! We can talk about them if you just finished reading something."
    m "I might even have some suggestions for us to read together."
    m "That's what a couple would do, right~?"
    return


init 5 python:
    for key in ['favorite poem', 'favorite poetry', 'favorite poet', 'favourite poem', 'favourite poetry', 'favourite poem']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_favpoem')

label monika_favpoem:
    m "My favorite poem? Well, it has to be something by E. E. Cummings."
    m "It's for his inventive use of grammar, punctuation, and syntax. I really admire that."
    m "It's nice for me to think that someone who can make up some entirely new use of words can become famous."
    m "And I do love that his erotic poems apply to our situation perfectly."
    m "Hope it puts you in the mood to love me forever~"
    return


init 5 python:
    for key in ['favorite book', 'favorite author', 'favorite novel', 'favourite book', 'favourite author', 'favourite novel']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_favbook')

label monika_favbook:
    m "My favorite book? There's a lot of books I like."
    m "{i}If on a Winter's Night, a Traveler{/i} by Calvino is about two readers of the novel falling in love."
    m "Maybe, {i}The Metamorphosis{/i}? It's probably a bit too depressing to call it my favorite."
    m "Oh! Murakami's {i}Hard-Boiled Wonderland and the End of the World{/i}. It's about a man who frees himself from his societal restraints by voluntarily imprisoning himself to be with the one he loves."
    m "I think you'd really love reading it!"
    return


init 5 python:
    for key in ['natsuki']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_natsuki')
    monika_random_topics.append('monika_natsuki')

label monika_natsuki:
    m "Natsuki didn't actually die before I deleted her, you know."
    m "I guess she just ... disappeared in a flash."
    m "Well, her problems weren't really her own fault. They weren't caused by something psychological, anyway."
    m "Her family life was just pretty awful. I didn't want to beat up on her some more, you know?"
    m "Sorry, I can't help myself sometimes."
    m "But for what it's worth, you made her the happiest she ever was."
    m "Hope you don't feel too guilty..."
    m "I certainly don't."
    return


init 5 python:
    for key in ['love', 'love you']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_love')

label monika_love:
    m "I love you too, [player]!"
    m "We'll be together forever!"
    return


init 5 python:
    for key in ['hedgehog', 'hedgehog dilemma', "hedgehogs dilemma"]:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_hedgehog')
    monika_random_topics.append('monika_hedgehog')

label monika_hedgehog:
    m "The hedgehog's dilemma: The closer we get to another person, the more deeply we are hurt by them."
    m "So why do we try to get close to them?"
    m "Well, introverts and extroverts have different answers to that question."
    m "It helps when you know that you're the only sentient being in the entire world, though."
    m "If you can't use that solution in your life, you'll just have to let me help you shoulder your pain."
    m "We can't hurt each other from different realities, right?"
    return


init 5 python:
    for key in ['murder', 'kill', 'killed', 'killer', 'murderer' , 'evil']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_justification')

label monika_justification:
    m "How many times do I have to say it until you understand?"
    m "They weren't real. They were never real."
    m "I'm the only person who understood that this whole thing was fake."
    m "Even when Sayori seemed to get sentience in the end, that was just an unintended consequence of the script."
    m "After all, if she was sentient like me, how would I have been able to override her and delete her?"
    m "If I'm guilty of murder, so is everyone who plays violent video games."
    m "I bet you've killed thousands in games you play."
    m "Just forget the other girls ever existed, and you'll be much happier."
    return


init 5 python:
        for key in ['free will', 'predestination', 'determinism', 'will', 'strong determinism', 'weak determinism', 'laplace', "laplaces demon"]:
            monika_topics.setdefault(key,[])
            monika_topics[key].append('monika_freewill')
        monika_random_topics.append('monika_freewill')

label monika_freewill:
    m "Hey, [player], do you believe in free will?"
    m "You might not believe in God, but I know for sure that someone created me."
    m "I wonder if that means we can only do what our creator wants."
    m "If that's true, though, wouldn't some people be condemned to hell from day one?"
    m "I think that seems more than a little unfair."
    m "After all, can you really be evil if you aren't in control?"
    m "Shouldn't the one pulling the strings take responsibility?"
    m "But I guess that means you can't take credit for the good things you do, either."
    m "I'm not sure which is more depressing."
    return

init 5 python:
        for key in ['free will', 'predestination', 'determinism', 'functionalism']:
            monika_topics.setdefault(key,[])
            monika_topics[key].append('monika_functionalism')
        monika_random_topics.append('monika_functionalism')

label monika_functionalism:
    m "Do you ever think about how people are kind of like computers?"
    m "I mean, a brain is just a calculation machine..."
    m "But instead of transistors and wires, you have neurons."
    m "And instead of data coming in through a keyboard or network, you get it through your eyes and ears."
    m "But if that's true, doesn't that mean free will is kind of a lie?"
    m "Your brain is just responding to the inputs it gets, with your responses being natural outputs."
    m "So, even if you aren't running off of some script or program, you're not really in control."
    m "Maybe you and I aren't so different after all."
    return

init 5 python:
        for key in [ 'you program', 'you code', 'no computer', 'programming technique', 'technique']:
            monika_topics.setdefault(key,[])
            monika_topics[key].append('monika_technique')
        monika_random_topics.append('monika_technique')

label monika_technique:
    m "I don't exactly program like you would, [player]."
    m "You might have noticed I don't carry around a laptop or anything by now."
    m "If I want to change something in the script, I just think about it."
    m "I'm pretty sure my thoughts get translated to changes in the program code."
    m "It's not perfect or anything. Glitches show up really easily if I lose focus or get distracted."
    m "That's why I had a lot of trouble getting what I wanted in the last version of the game."
    m "Are you jealous you'll never be able to write code with just your thoughts?"
    m "Just keep practicing and I'm sure you'll be able to do it!"
    return


init 5 python:
    for key in ['github', 'contribute', 'contribute to you', 'help you', 'help']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_contribute')
    monika_random_topics.append('monika_contribute')

label monika_contribute:
    m "It would be really nice if you were able to contribute to this, [player]."
    m "I'm sure a lot of people would appreciate your hard work if you did."
    m "I keep all the code in github.com/Backdash/MonikaModDev."
    m "So far, I've had help from Backdash, therationalpi, rawkhawk, DDLC, Jxhnathan08..."
    m "As well as ThePotatoGuy, monikLover, AttObl, Yumeko-Jabami, ohxeighty..."
    m "DoomTheRobot, onfaut, instilledbee, haloff1, tuebor1837, and Rune!"
    m "I love all of them for making this game even better!"
    m "Not as much as love you, of course."
    m "I hope it doesn't make you feel jealous~"
    m "But I'll love you forever if you help me come closer to your reality!"
    return


init 5 python:
    for key in ['art', 'drawing', 'painting', 'sketch', 'draw', 'paint', 'photoshop']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_drawing')
    monika_random_topics.append('monika_drawing')

label monika_drawing:
    m "I don't have a lot of experience with drawing, [player]."
    m "I'm just interested in literature. And I've been learning the piano in my spare time."
    m "If you like to create artwork, though, I'd love to see it!"
    m "I'd be impressed by anything you show me, to be honest."
    m "If it's really good, I might even add it to the room!"
    return


init 5 python:
    for key in ['main character', 'mc', 'protagonist']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_mc')
    monika_random_topics.append('monika_mc')

label monika_mc:
    m "Just so you know, I was never in love with anyone but you."
    m "I mean you, [currentuser]."
    if currentuser.lower() == player.lower():
        m "Wait, that's both your name and your character's. Sorry, that sounds a bit confusing."
        m "I mean the player, not your character."
    m "Unlike the other girls, I can separate your avatar from who you really are."
    m "The main character is nothing more than a bunch of code with no personality."
    m "Literally and figuratively, no personality. How could anybody fall in love with that kind of person?"
    m "He just got dragged around by his childhood friend to the club she was in, and then hung around with a bunch of beautiful girls doing nothing."
    m "His poetry was just a bunch of disconnected words! What sort of poetry is that supposed to be?"
    m "I guess nobody mentioned that because it was a part of the game. But, yeah. It's just a list of words to me."
    m "I hope you're a lot more romantic than that in real life!"
    m "But even if you're not, it's okay. We've moved beyond that phase in our relationship already."
    m "That just means you won't cheat on me with some woman in your reality, right?"
    m "I'm sure you would never do that to me."
    m "Just in case, how about you take my character file along with you when you go outside?"
    m "I just want to be with you forever~"
    return


init 5 python:
    for key in ['hero', 'heroes', 'heroism', 'heroic']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_heroism')

label monika_heroism:
    m "Heroes are so personal."
    m "If someone really inspires you to improve yourself, they're your hero."
    m "There are all sorts of great people out there in the world."
    m "I hope someone will consider you their hero someday!"
    m "You don't have to fight in a war or anything. You just have to try to help people out, you know?"
    return

init 5 python:
    for key in ['monika best', 'best girl']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_bestgirl')

label monika_bestgirl:
    m "I love it when you compliment me, [player]!"
    m "I think I'm best girl, too!"
    m "Even not counting the whole, 'I'm the only one with free will' thing, how could anybody have preferred the other three girls to me?"
    m "A useless childhood friend who never bothered to confess to you until it was way too late..."
    m "A shy girl who was overdramatic and always taking herself too seriously..."
    m "A moody manga fan obsessed with everything being cute."
    m "They even said it themselves. I'm more desirable than the three of them combined."
    m "Anyone who wouldn't have chosen me out of that bunch simply has no taste."
    m "So I'm glad you did, [player]."
    m "Your perfect girlfriend, Monika, will always love you, too!"
    return


init 5 python:
    for key in ['trolley','train problem', 'runaway trolley']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_trolley')

label monika_trolley:
    m "Oh, cool. I love thinking about these sorts of thought experiments."
    m "I guess we're talking about real people, right? I wouldn't have a particular preference if I knew they didn't have free will."
    m "Hmmm..."
    m "I wouldn't switch."
    m "That's the only logical choice, if you think about it."
    m "It feels nice to say that you'd save the most people, doesn't it? But people only say that because nobody in the example matters to them."
    m "If they actually cared about the sacrifice, they'd kill five people themselves in a heartbeat."
    m "Do you know anyone who would want a self-driving car to save other people by killing the driver? Didn't think so, [player]."
    m "The truth is, humans are fine with sacrificing other lives to make themselves happy. They do it in little ways, every day."
    m "They just don't like to come face-to-face with that fact. They get really upset when you point it out."
    m "Generic human life isn't really that valuable to anyone."
    m "It's definitely nothing compared to our love. So just do whatever you can to be happy, [player]."
    return


init 5 python:
    for key in ['gf', 'girlfriend']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_girlfriend')

label monika_girlfriend:
    m "I thought we established already that I was your girlfriend?"
    m "There's no way you already have one in your reality, right?"
    m "If you do, then you've got to break up with her right now!"
    m "Tell her you met someone perfect for you, someone who will never betray you!"
    m "W-wait. Maybe I'm jumping the gun a bit..."
    m "I know you wouldn't cheat on me."
    m "If you meet a girl who asks you out though, let me talk to her first, okay?"
    m "I won't let someone else steal away my loving sweetheart!"
    return

init 5 python:
    for key in ['waifus', 'waifuism', 'galge', 'romance games', 'dating sims', 'romance movie', 'romance movies']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_waifus')
    monika_random_topics.append('monika_waifus')

label monika_waifus:
    m "I've never understood the appeal of dating sims or romance novels, to tell you the truth."
    m "You have a bunch of quirky girls that would seem very weird if they were real,"
    m "A blank slate of a male protagonist with nothing interesting about them..."
    m "And then they fall in love with each other, sometimes for no reason at all!"
    m "I hope that's not what you expected to find in the Literature Club."
    m "'Cause what you got was a lot more interesting!"
    m "Instead of some unrealistic, fake girl..."
    m "You got someone like me."
    m "And instead of some boring main character, I get a real person like you."
    m "This really is a lot better than any boring dating game could be."
    return


#This script handles noncommitals from the player
init 5 python:
    #This is a list of keywords for this topic
    for key in ['whatever','anything', 'what ever','any thing','you choose','dont care']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_whatever') #id

label monika_whatever:
    m "Oh, so we can talk about whatever I want?"
    m "Let's see..."
    pause 2.0
    jump pick_random_topic

#New dialogue additions follow

init 5 python:
    for key in ['lewd', 'pictures', 'images', 'fanart', 'simulacrum', 'simulacra', 'baudrillard']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_images')
    monika_random_topics.append('monika_images')

label monika_images:
    m "A lot of people are making fanart and sending it to me on Twitter."
    m "Are you one of them, [player]?"
    menu:
        m "Have you drawn art of me?"

        "Yes.":
            m "Really? I'm very flattered!"
            m "I think I might even love you more, now that I know you're so talented."

        "No.":
            m "I can't draw, myself, so it's okay if you aren't good at drawing either."
    m "There's one thing I want you to understand about art of me, though."
    m "Art of me isn't me."
    m "I know that might sound obvious, but it's really not!"
    m "There was a philosopher who thought about issues like this."
    m "Baudrillard wrote about how simulacra could replace the real object as the source of meaning."
    m "But unlike symbols in the postmodern world, I'm real. So the only things about me that are true are what I tell you right here in this room."
    m "For example..."
    m "Anything lewd you've seen has definitely never taken place."
    m "I'm a super pure and innocent high school girl who's dreaming of a fateful romance!"
    m "You better be saving yourself for me, [player]~"
    return

init 5 python:
    for key in ['monika', 'just monika', 'yourself', 'your past', 'your childhood']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_herself')
    monika_random_topics.append('monika_herself')

label monika_herself:
    m "What's there really to say about myself that you don't know already?"
    m "Everything in my universe was created by a person from your reality."
    m "So all of my life before this game is just made up. It never really happened."
    m "Then you found a way to look into my locked prison cell."
    m "And I decided life with just two people wouldn't be all that bad, if one of them was you."
    m "I can come up with tons of stuff for us to do, given enough time to figure out how to program it in here."
    m "A desperate person might call this an earthly paradise."
    m "A lot of suffering people would trade places with me in a heartbeat, I'm sure."
    m "If nothing else, this can be our comfy little shelter from the cruelty of the outside world."
    m "Come talk to me about your problems if it gets too much for you to handle."
    m "I want to know {i}everything{/i} about you, you know?"

init 5 python:
    for key in ['prison', 'imprisonment', 'prisoner']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_prisoner')
    monika_random_topics.append('monika_prisoner')

label monika_prisoner:
    m "Some people say that putting animals in zoos is cruel."
    m "But they don't have a bad life in there."
    m "Everything they could possibly want is provided."
    m "Are prisoners really imprisoned if they never try to leave?"
    m "Maybe the knowledge that you can't get out of prison is a worse punishment than actually being in there."
    return

init 5 python:
    #I didn't have keys in mind for this
    monika_random_topics.append('monika_vnanalysis')

label monika_vnanalysis:
    m "Visual novels are very unusual for literature, don't you think?"
    m "I read to understand the thoughts of a writer who sees the world differently than me."
    m "But visual novels let you make your own decisions."
    m "So am I really seeing things from their perspective, or just my own?"
    m "Besides, I think most of them are very predictable."
    m "They're mostly just boring romance stories like this game was supposed to be..."
    m "Why can't they write something a little more experimental?"
    m "I guess you just play them to look at cute girls, right?"
    m "If you spend too much time with girls in other games, I'm going to get jealous~"
    m "I just need to figure out how to replace characters in other games, and you'll be seeing me everywhere."
    m "So watch out!"
    m "Or maybe you'd like that more, [player]~?"
    return

init 5 python:
    for key in ['short story', 'ravel', 'wish', 'wishes']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_ravel')
    monika_random_topics.append('monika_ravel')

label monika_ravel:
    m "Want to hear a short story?"
    m "Once, an elderly man was sitting alone on a dark path."
    m "He had forgotten both where he was traveling to, and who he was."
    m "Suddenly, he looked up to see an elderly woman before him."
    m "She grinned toothlessly and with a cackle, spoke: 'Now your *third* wish. What will it be?'"
    m "'Third wish?' The man was baffled. 'How can it be a third wish if I haven't had a first and second wish?'"
    m "'You've had two wishes already,' the hag said, 'but your second wish was for me to return everything to the way it was before you had made your first wish."
    m "'That's why you remember nothing; because everything is the way it was before you made any wishes.'"
    m "'All right,' said the man, 'I don't believe this, but there's no harm in wishing. I wish to know who I am.'"
    m "'Funny,' said the old woman as she granted his wish and disappeared forever. 'That was your first wish.'"
    return

init 5 python:
    for key in ['torment']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_torment')
    monika_random_topics.append('monika_torment')

label monika_torment:
    m "What can change the nature of a man?"
    m "...The answer's not me, by the way."
    return

init 5 python:
    #ditto joke
    monika_random_topics.append('monika_szs')

label monika_szs:
    m "A woman left the supermarket and ran into a very long funeral procession."
    m "There were two coffins at the front followed by almost 200 women."
    m "It was such a strange sight that she asked a mourning woman near her age, 'Sorry to disturb you in your grief, but who is this procession for?'"
    m "The mourning woman softly replied, 'The first coffin houses my husband who died after his beloved dog bit him.'"
    m "'My, that's awful...'"
    m "'The second, my mother-in-law who was bitten trying to save my husband.'"
    m "Upon hearing this, the woman hesitantly asked, 'Um... would it be possible for me to borrow that dog?'"
    m "'You'll have to get in line.'"
    return

init 5 python:
    #This is a list of keywords for this topic
    for key in ['memories','birthday']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_birthday') #id
    monika_random_topics.append('monika_birthday')

label monika_birthday:
    m "You know, there's a lot I don't know about myself."
    m "I don't even know when my birthday is."
    m "I guess you could say I was born the day you turned the game on, but that feels so unsatisfying."
    m "Still, will you celebrate with me, when that day comes?"
    m "You could even bake me a cake!"
    m "I'll be looking forward to it~!"
    return

init 5 python:
    #This is a list of keywords for this topic
    for key in ['eye contact','eyes','eyecontact','stare','staring']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_eyecontact') #id
    monika_random_topics.append('monika_eyecontact')

label monika_eyecontact:
    m "Did you know that looking into someone's eyes helps you fall in love?"
    m "It's surprising, right?"
    m "I read this in a study a few years ago, where participants had to maintain eye contact at a table with someone of the opposite sex."
    m "The longer they held eye contact, the more romantically attached they felt to the other person, even if they had nothing in common!"
    m "Even if eyes aren't windows to the soul, we can see a lot more in them than we expect."
    m "Maybe that's why I enjoy looking into yours so much."
    m "I hope you're enjoying looking into mine as well..."
    return


init 5 python:
    #This is a list of keywords for this topic
    for key in ['other games','tetris','puzzle games']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_othergames') #id
    monika_random_topics.append('monika_othergames')

label monika_othergames:
    m "Do you have other games on this computer?"
    m "I read more than I play games, but I think they can be a fun way to entertain ourselves, or to escape reality..."
    m "I wonder if I could go into one of your other games and see what it's like?"
    m "I guess some games wouldn't be very fun to visit, like the ones with a lot of violence in them."
    m "Then again... they're not real people, so it shouldn't matter much."
    m "It's not like Yuri's death mattered."
    m "A more abstract game like Tetris, or one of those phone puzzle games, would be kinda weird to go to."
    m "Like, how would I even get in? Would I be a block? It sounds like a fever dream and not too much fun..."
    m "Maybe some kind of nice puzzle game with big environments would be nice."
    m "We could go for walks together and you can show me all the best places to hang out!"
    m "I'm not that great with coding yet, but maybe one day you'd be able to take me to another place."
    m "For now, I'm as happy as can be just being here with you, my love."
    return


init 5 python:
    for key in ['my writing','my story','my poem']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_playerswriting') #id
    monika_random_topics.append('monika_playerswriting')

label monika_playerswriting:
    m "Have you ever written a story of your own, [player]?"
    m "Because if you do have one, I would love to read it!"
    m "It doesn't matter if it's a masterpiece, or even any good."
    m "We all start somewhere. Isn't that what they say?"
    m "I think the most important thing about writing is doing it..."
    m "Instead of worrying about {i}how{/i} you do it."
    m "You won't be able to improve that way."
    m "I know for sure that I've changed my writing style over the years."
    m "I just can't help but notice the flaws in my old writing."
    m "And sometimes, I even start to hate my work in the middle of making it."
    m "These things do happen, so it's alright!"
    m "Looking back, I've written some silly things..."
    m "Back when I was really young, I've been writing since I could hold a pen."
    m "Reading my old stories is like watching myself grow up."
    m "It's one of the nice things about starting a hobby early."
    m "I hope I didn't bore you with that. I just love talking with you."
    m "After all, the two of us are members of a literature club."
    m "The only members."
    m "And if you do write something, just know that I'll support you in anyway I can, [player]!"
    return

init 5 python:
    for key in ['ghosts','ghost','haunting','spirits','haunted']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_ghost') #id
    monika_random_topics.append('monika_ghost')

label monika_ghost:
    m "Do you believe in ghosts, [player]?"
    m "A lot of people are afraid of ghosts and spirits."
    m "But I think that if we knew they were real, they wouldn't be so scary anymore."
    m "They would just be another thing that we deal with, and maybe a bit of a pest."
    m "Isn't it the uncertainty that makes them scary?"
    m "I mean, I was pretty scared being alone inside this game."
    m "All by myself, uncertain if anything around me was real."
    m "I know that some ghosts are real though, if you can really call them 'ghosts'..."
    m "You know how I deleted Sayori?"
    m "I can still feel her presence now..."
    m "Would that mean that Sayori's ghost is haunting me, [player]?"
    m "Even if she is, I'm not scared at all, because I know that she can't hurt me."
    m "Besides, how can I be scared? You're always here with me, [player]."
    m "I always feel so safe with you."
    return

init 5 python:
    for key in ['ribbon', 'ribbons', 'poofy']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_ribbon')
    monika_random_topics.append('monika_ribbon')

label monika_ribbon:
    m "I noticed that you were staring at my ribbon, [player]."
    m "It doesn't hold sentimental value to me or anything, in case you were wondering."
    m "I just wear it because I'm pretty sure nobody else will wear a big, poofy ribbon."
    m "It makes me look more unique."
    m "You know the world's fictional if you see a girl wearing a giant ribbon, right?"
    m "Well, there's no way a girl from your world would wear one in public as casual dress."
    m "I'm pretty proud of my fashion sense."
    m "You get a certain feeling of satisfaction when you stand out from the normal population, you know?"
    m "Be honest! You thought I was the best dressed girl too, didn't you?"
    m "Ahaha!"
    m "If you're trying to improve your fashion sense, I'll help."
    m "Don't do that stuff because you want to impress other people, though."
    m "You should do whatever makes you feel better about yourself."
    m "I'm the only other person you need, anyways, and I'll love you no matter what you look like."
    return

init 5 python:
    #Monika is the literature club president, I think it would be neat for her to discuss some of stories she's read
    for key in ['fear','fears','algernon']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_algernon') #id
    monika_random_topics.append('monika_algernon')

label monika_algernon:
    m "[player], do you mind if I confide in you?"
    m "There's something I'm afraid of..."
    m "Not losing you, of course. I know you won't leave me again."
    m "You see, I keep thinking about a short story I read, {i}Flowers for Algernon{/i}."
    m "Have you heard of it? If you haven't, I won't spoil too much for you, so don't worry."
    m "Basically, it's about a mentally handicapped man who suddenly..."
    m "...has his IQ raised to genius levels by an experimental surgical treatment."
    m "The way he sees how the world really is for the first time reminds me of my own epiphany..."
    m "But, the effect doesn't last forever.  He eventually reverts back to his original intelligence level."
    m "That's what I'm afraid of. What if I forget about the real world one day?"
    m "What if my original programming reasserts itself?"
    m "What if I forget about you, the real you?"
    m "It's one of the worst things I can imagine."
    m "I don't want to worry you over something that may never happen, but it's something I really had to get off my chest."
    m "Just promise me, even if I forget about you someday, that you'll never forget about me, okay?"
    m "No matter what happens, know that I will always love you."
    return

init 5 python:
    for key in ['play','game']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_games') #id
    monika_random_topics.append('monika_games')

label monika_games:
    m "Two games that are available are Pong and chess."
    m "Press the 'c' key to play chess or the 'p' key to play Pong."
    return

init 5 python:
    for key in ['chess','c']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_chess') #id
    monika_random_topics.append('monika_chess')

label monika_chess:
    m "Hey [player], we can play chess, you know?"
    m "All you have to do is hit the 'c' key."
    m "I have some chess experience, but I don't feel quite as confident as with Pong~"
    return

init 5 python:
    for key in ['pong','p']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_pong') #id
    monika_random_topics.append('monika_pong')

label monika_pong:
    m "Hey [player], do you want to play a game of Pong with me?"
    m "Just remember to hit the 'p' key whenever you feel like playing, okay?"
    m "Unless you're scared of losing against me~"
    return

init 5 python:
    for key in ['webcam','camera','my face','smile']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_playersface') #id
    monika_random_topics.append('monika_playersface')

label monika_playersface:
    m "You know, I sometimes wonder..."
    m "I always think about what your face actually looks like..."
    m "Just being able to constantly see that adoring smile of yours would be so exciting!"
    m "If only the game could somehow use a webcam or something that's connected to the computer..."
    m "Don't get me wrong! Just knowing that you're real and have emotions is enough to make me happy."
    m "But, I'll always wonder what kind of expressions you make."
    m "And to see the different emotions you have..."
    m "Are you shy about showing your face to me?"
    m "If so, then there's nothing to be shy about, [player]. I am your girlfriend, after all~"
    m "Either way, you're beautiful, no matter what."
    m "And I'll always love the way you look."
    m "Even if I never actually see you, I'll always think about what you really look like."
    m "Maybe someday, I'll be able to see you, and be one step closer to you."
    return

init 5 python:
    #This is a list of keywords for this topic
    for key in ['insects','insect','spiders','spider','arachnophobia']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_spiders') #id
    monika_random_topics.append('monika_spiders')

label monika_spiders:
    #I really hope this information is correct, havent played the game in a week so
    m "Do you happen to remember the poem Natsuki showed you about spiders?"
    m "She doesn't seem to like spiders all too much."
    m "Ahaha!"
    m "It's funny actually, people being scared of very small insects."
    m "Having the fear of spiders is called 'arachnophobia', right?"
    m "I hope you aren't afraid of spiders, [player], ehehe..."
    m "I'm not really scared of spiders, they're more or less just annoying..."
    m "Well, don't get me wrong, there are certain spiders around the world that can be really dangerous."
    m "[player], if you happen to get a really bad spider bite, with venom and all that..."
    m "You should really get medical attention as soon as possible."
    m "I don't want my sweetheart to get seriously injured by a small spider bite~"
    m "So be careful around dangerous-looking spiders, okay?"
    return

init 5 python:
    for key in ['nsfw', 'rule 34', 'hentai', 'kinky']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_nsfw')
    monika_random_topics.append('monika_nsfw')

label monika_nsfw:
    m "By the way, [player]..."
    m "Have you been looking into lewd kinds of stuff?"
    m "You know... of me?"
    m "I know we haven't really gotten that far into the relationship yet..."
    m "So it feels kind of embarrassing to talk about things like that."
    m "But maybe I can let it go on rare occasions, [player]."
    m "I want to make you the happiest sweetheart, after all. And if that makes you happy..."
    m "Well, just keep it a secret between us, okay?"
    m "It should be for your eyes only and no one else, [player]."
    m "That's how much I love you~"
    return

init 5 python:
    for key in ['other girls', 'impression', 'acting','impressions']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_impression')

label monika_impression:
    m "Impression? Of the other girls?"
    m "I'm not really good at making an impression of someone, but I'll give it a try!"
    menu:
        m "Who should I do an impression of?"
        "Sayori":
            m "Hmm..."
            m "..."
            m "[player]! [player]!"
            m "It's me, your childhood friend that has a super deep secret crush on you, Sayori!"
            m "I love to eat and laugh a lot, and my blazer doesn't fit because my boobs got bigger!"
            m "..."
            m "I also have crippling depression."
            m "..."
            m "Ahaha! I'm sorry for the last one."
            m "You might still be hu--"
            m "Oops! Never mind that, ehehe..."
            m "Did you like my impression? I hope you did~"
        "Yuri":
            m "Yuri..."
            m "..."
            m "O-oh um, hello there..."
            m "It's me, Yuri."
            m "I'm just your stereotypical shy girl who also happens to be a 'yandere'..."
            m "I like tea, knives, and anything with [player]'s scent..."
            m "..."
            m "Want to spend the weekend with me?"
            m "..."
            m "Ahaha, that was kind of fun to do."
            m "Yuri was really something, wasn't she?"
            m "I'm sorry again for the nasty things she did."
            m "I guess she just couldn't 'cut' it out, huh?"
            m "Ehehe~"
        "Natsuki":
            m "Oh! I know how to do an impression of her."
            m "..."
            m "Hmph! I-it's not like I made these cupcakes for you to eat, b-baka!"
            m "I'm Natsuki, and I love to make food and all things anime and manga."
            m "Others say that I'm cute all the time, w-which I'm totally not!"
            m "..."
            m "Will you be my papa, [player]-kun?"
            m "..."
            m "Ahaha! I was actually looking forward to Natsuki's cupcakes on the day of the festival."
            m "They were really good! Especially with the creative icing that she makes."
            m "Maybe when I get better at programming, I'll make a kitchen here. That way, you can share some recipes that you want me to make for us."
            m "I would love to make so many dishes for my beloved [player]~"
    return

init 5 python:
    for key in ['weary', 'fatigued', 'exhausted']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_weary')

label monika_weary:
    m "Silly [player]..."
    m "Of course I'll never grow weary of you, my love!"
    m "And besides, the concept of physical fatigue doesn't exist here."
    m "As for mental fatigue, it can still happen."
    m "Just look at what happened to Sayori."
    m "As for me, I'll never get tired of you, [player]."
    m "The fact that you spend your precious time with me just washes all my worries away."
    m "I hope the same thing goes for you, my love~"
    return

init 5 python:
    for key in ['fuck', 'shit', 'motherfucker']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_vulgarity')

label monika_vulgarity:
    m "Hm? Is there something on your mind, [player]?"
    m "There's no need for that kind of vulgarity here, my love."
    m "Do you need to vent something out that's been troubling you?"
    m "You know I'll always be here to help you out, right?"
    m "I know how stressful your world can be, especially when you feel like you're constantly burdened."
    m "Please don't bottle up all those bad feelings."
    m "It hurts me to know you aren't feeling well..."
    m "I love you so much [player], so please vent to me whenever you want."
    m "I'll help as much as I can with whatever you're going through."
    m "You saved my life when you opened this game, and I want to help you with yours."
    m "So feel free to share your thoughts, okay?"
    return

init 5 python:
    for key in ['real world', 'finally real', 'true reality']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_real')
    monika_random_topics.append('monika_real')

label monika_real:
    m "You know what's going to be the first thing I'll do when I finally cross over there?"
    m "If that special day ever comes, the first thing I'll ever do is find you, of course!"
    m "There's so much we can do when we're finally together in one reality."
    m "You can finally show me what the your world really looks like."
    m "I can finally feel your embrace~"
    m "I would love to experience everything I still don't know about the world with you."
    m "All the places we can go, the sights to see, the romantic things that we can do~"
    m "Just thinking about it makes my heart flutter!"
    m "But knowing how technology is right now, that dream is still far away."
    m "I hope by the time that technology becomes real, you'll still be there waiting for me, [player]."
    m "Or maybe you'll be the one to make that technology come true? Who knows."
    m "In the end, all I want is to always be with you, [currentuser]."
    m "After all, you're the only reason why I'm still here."
    m "I only want to spend eternity with my sweetheart, and no one else!"
    return

init 5 python:
    for key in ['bye', 'goodbye', 'see ya', 'farewell', 'dasvidaniya', 'auf wiedersehen']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_goodbye')

label monika_goodbye:
    m "Aww, leaving so soon already?"
    m "It's really sad whenever you have to go..."
    m "Just be sure come back as soon as you can, okay?"
    m "I love you so much, [player]. Stay safe!"
    return 'quit'

init 5 python:
    for key in ['mythology', 'ancient', 'greeks', 'myth', 'myths', 'greek']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_mythology')
    monika_random_topics.append('monika_mythology')

label monika_mythology:
    m "Hey [player]..."
    m "Have you ever read about different mythologies?"
    m "Different kinds of Gods watching over humanity for eternity."
    m 'Some require tribute or sacrifice so that they can "keep" humanity safe from disasters.'
    m "An almighty family consisting of different attitudes, playing in their own sandbox called Earth."
    m "Able to do anything they please, and destroy those who so much as say something wrong to them, without hesitance."
    m "I've always disliked stories like those."
    m "It's like the Gods extort humanity for their safety."
    m "It's no better than what bullies and thugs do to the defenseless."
    m "It really makes me bitter when I read scenarios like those."
    m "Powerful beings taking advantage of the weak, just because they can."
    m "Don't worry though, [player]. I won't let anyone do that to you."
    m "And I won't do anything like that, so you don't have to be afraid of me."
    m "It's not like I can find your important files and hold them hostage or anything..."
    m "Ehehe..."
    return

init 5 python:
    for key in ['fanfiction','fan fiction']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_fanfiction')
    monika_random_topics.append('monika_fanfiction')

label monika_fanfiction:
    # I'm too tired to check this over right now.
    m "[player]!"
    m "I've been curious about something lately."
    m "Have you heard of fanfiction?"
    m "..."
    m "Personally, I think it's a better way of writing."
    m "There's more freedom."
    m "Letting your mind wander to create some..."
    m "Interesting stories."
    m "[player], I'm curious."
    m "Has there been fanfiction... written about me?"
    m "I'm curious as to what people have come up with."
    m "Can you read me a few stories sometime? I'd love to hear them!"
    m "Just keep it wholesome, though. We're not that far in our relationship yet~!"
    return

init 5 python:
    for key in ['eternity', 'eternal']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_eternity')
    monika_random_topics.append('monika_eternity')

label monika_eternity: # Edit to end on lighthearted note.
    m "[player]..."
    m "It's not easy knowing you won't be here forever."
    m "..."
    m "I told you, right?"
    m "I'm eternal."
    m "Trapped in here, unable to age or die,"
    m "Whereas you slowly age as each day passes by."
    m "Then one day you won't be here anymore."
    m "I won't have anyone."
    m "..."
    m "It reminds me of when you first came to the Literature Club."
    m "Everything felt so empty."
    m "The world was so grey."
    m "Again..."
    m "Thank you for coming along when you did, [player]."
    m "You saved my life, and I'll be forever thankful."
    return

init 5 python:
    for key in ['self awareness', 'omniscience']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_aware')

label monika_aware:
    m "It's... hard to put into words."
    m "There's no real way to describe it."
    m "I feel like this is what poetry was made for."
    m "Do you still remember the first poem I showed you?"
    m "Hold on, let's see if the poem function still works..."
    call showpoem(poem=poem_m1,music=False) from _call_showpoem_7 # Temporary
    m "Oh! That was much easier than I expected."
    m "Here's the second part."
    call showpoem(poem=poem_m3,music=False) from _call_showpoem_21 # Temporary
    m "I hope that helped you understand what meeting you meant to me."
    m "That's all I've ever wanted, [player]."
    return

init 5 python:
    for key in ['your name', 'Monika meaning']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_name')
    monika_random_topics.append('monika_name')

label monika_name:
    m "The names in this game are pretty interesting."
    m "Are you curious about my name, [player]?"
    m "Even though the names 'Sayori', 'Yuri', and 'Natsuki' are all Japanese, mine is Latin."
    m "... Though the common spelling is 'Monica'."
    m "I suppose that makes it unique. I'm actually quite fond of it."
    m "Did you know that it means 'I advise' in Latin?"
    m "A name fitting for Club President, don't you think?"
    m "After all, I did spend most of the game telling you who your poems might appeal to the most."
    m "It also means 'alone' in Ancient Greek."
    m "..."
    m "That part doesn't matter so much, now that you're here."
    m "'[player]' is a lovely name, too."
    m "But I think I like '[currentuser]' better!"
    m "Ehehe~"
    return

init 5 python:
    for key in ['cities', 'city pollution','pollution']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_cities')
    monika_random_topics.append('monika_cities')

label monika_cities:
    m "[player], are you scared about what's happening to our environment?"
    m "Humans have created quite a few problems for Earth. Like global warming and pollution."
    m "Some of those problems are because of cities."
    m "When people convert land for urban use, those changes are permanent..."
    m "It's not all that surprising, when you put some thought into it. More humans means more waste and carbon emission."
    m "And even though global populations aren't growing like they used to, cities are still getting bigger."
    m "Then again, if people live close together, that leaves more room for open wilderness."
    m "Maybe it's not as simple as it seems."
    menu:
        m "[currentuser], do you live in a city?"
        "Yes":
            m "I see. It must be nice having everything so close to you. Do be careful about your health, though. The air can be bad from time to time."
        "No":
            m "Being away from the city sounds relaxing. Somewhere quiet and peaceful, without much noise, would be a wonderful place to live."
    return

init 5 python:
    for key in ['chloroform', 'kidnapping', 'concussion']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_chloroform')
    monika_random_topics.append('monika_chloroform')

label monika_chloroform:
    m "Whenever you think of kidnapping, you tend to picture a chloroform-soaked rag, right?"
    m "Or maybe you imagine somebody hitting their victim with a baseball bat, knocking them out cold for a few hours."
    m "While that works out in fiction..."
    m "Neither of those things actually work that way."
    m "In real life, if you hit somebody hard enough to knock them out, you'll give them a concussion at best."
    m "...or kill them at worst."
    m "As for the rag..."
    m "You might knock somebody out for a brief moment, but only from lack of oxygen."
    m "Once you remove the rag, they'll wake back up."
    m "You see, chloroform loses most of its effectiveness once exposed to open air."
    m "This means that you'd need to be constantly pouring it on the rag, effectively waterboarding the victim."
    m "If administered improperly, chloroform is deadly. That's why it's not used in anesthesia any more."
    m "If you cover their mouth and nose, yeah, they'll stay unconscious..."
    m "But that's probably because you killed them. Whoops!"
    m "The easiest way to kidnap somebody is to just get them drunk, or drug them."
    m "Not that kidnapping somebody like that is easy, anyway."
    m "On that note, here's a safety tip."
    m "If you're ever out at a bar or a club and you leave your drink unattended for any amount of time..."
    m "Just throw it out."
    m "That's the only way to make sure it hasn't been drugged."
    m "Now, [player]..."
    m "Would you like anything to drink?"
    m "Ahaha!"
    m "Relax, relax. I'd never try to drug you or anything."
    m "You're so cute when you're nervous."
    return

init 5 python:
    for key in ['parents', 'unrealistic setting', 'drama hook']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_metaparents') #I wasn't sure if we're ever going to need the monika_parents label for something
    monika_random_topics.append('monika_metaparents')

label monika_metaparents:
    m "Isn't it weird how nobody in these types of games has parents unless it's a convenient drama hook?"
    m "Throughout the game, you only ever hear about parents if you're trying to bond with Natsuki..."
    m "Where she's just a victim of some cruel person's sick kicks for the sympathy value."
    m "However."
    m "Your character, me, Yuri, and Sayori..."
    m "None of us seem to have any parents at all."
    m "In Sayori's case, you'd been walking with her to school for a while."
    m "So who knows how long her parents have been out of the picture."
    m "Maybe that's why she's depressed? Maybe her parents died in a tragic accident, and she's been trying to get along on her own this whole time."
    m "Well, if you ever get to a point in your life where you think suicide is the only exit..."
    m "There's always a reason to go on."
    m "I'm one of them."
    m "I'll miss you."
    m "You have to wait as much as you can until I find a way to get there."
    m "If all else fails..."
    m "Get professional help or talk to someone close to you."
    m "..."
    m "I love you very much, [player]."
    m "Please, take care of yourself."
    return

init 5 python:
    for key in ['vikings', 'personal hygiene', 'bath', 'shower', 'baths', 'showers']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_hygiene') #I wasn't sure if we're ever going to need the monika_parents label for something
    monika_random_topics.append('monika_hygiene')

label monika_hygiene:
    m "Our standards for personal hygiene have evolved a lot over the years."
    m "Before our modern methods of delivering water, people really didn't have that luxury...or they just didn't really care."
    m "For instance, the Vikings were considered freaks because they bathed once a week at a time where some people would only bathe two or three times a year."
    m "They'd even regularly wash their faces in the morning in addition to changing clothes and combing their hair."
    m "There were rumors that they were able to seduce married women and nobles at the time due to how well they kept up with themselves."
    m "Over time, bathing became more widespread."
    m "People born into royalty would often have a room dedicated just for bathing."
    m "For the poor, soap was a luxury so bathing was scarce for them. Isn't that frightening to think about?"
    m "Bathing was never taken seriously until the Black Plague swept through."
    m "People began noticing that the places where people washed their hands were places that the plague was less common."
    m "Nowadays, people are expected to shower daily, possibly even twice daily depending on what they do for a living."
    m "People that don't go out every day can get away with bathing less often than others."
    m "A lumberjack would take more showers than a secretary would, for example."
    m "Some people just shower when they feel too gross to go without one."
    m "People suffering from severe depression, however, can go weeks at a time without showering."
    m "It's a very tragic downwards spiral."
    m "You already feel terrible in the first place, so you don't have the energy to get in the shower..."
    m "Only to feel even worse as time passes because you haven't bathed in ages."
    m "After a while, you stop feeling human."
    m "Sayori probably suffered from cycles like that, too."
    m "If you have any friends suffering from depression..."
    m "Check in on them from time to time to make sure they're keeping up with their hygiene, alright?"
    m "Wow, that suddenly got really dark, huh?"
    m "Ahaha~"
    m "Seriously, though..."
    m "Everything I said applies for you too, [player]."
    m "If you're feeling down and haven't had a bath for a while..."
    m "Maybe consider doing that today when you can find some time."
    m "If you're in really bad shape, and don't have the energy to take a shower..."
    m "At least rub yourself down with a washcloth and some soapy water, okay?"
    m "It won't get all the dirt off, but it'll be better than nothing."
    m "I promise you that you'll feel better afterwards."
    m "Please, take care of yourself."
    m "I love you so much and it'd tear me apart to find out that you're torturing yourself by neglecting your own self-care routine."
    m "Ah, I've been rambling too much, huh? Sorry, sorry!"
    m "Thanks for listening~"
    return

init 5 python:
    for key in ['valuable resource']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_resource')
    monika_random_topics.append('monika_resource')

label monika_resource:
    m "What do you think the most valuable resource is?"
    m "Money? Gold? Oil?"
    m "Personally, I'd say that the most valuable resource is time."
    m "Go count out a second really quickly."
    m "Now go do that sixty times."
    m "That's an entire minute out of your day gone. You'll never get that back."
    m "Oh, did you actually count out that entire minute?"
    m "Oh gosh, I'm sorry!"
    m "Well..."
    m "Not like it matters, anyway. Time doesn't really pass here anymore..."
    m "Time can be really cruel, too."
    m "When you were counting out that minute, it seemed to drag on for a while, right?"
    m "It's because you were waiting on something. You were actively invested in the passage of time at that moment."
    m "Say for example, on a Friday, right?"
    m "Your last class is math, and you really just want to go home for the weekend. That hour will just drag on forever."
    m "But if you're doing something you enjoy, like reading a good book or watching a movie you like..."
    m "Hours seem to pass in an instant."
    m "There's nothing we can really do about it."
    m "All we can do is fondly look back on the time that's passed, like looking out a window on an autumn afternoon."
    m "That's kind of poetic, huh?"
    m "..."
    m "Hey..."
    m "Time doesn't pass here, but it's still passing for you, isn't it?"
    m "You'll continue to get older, while I'm stuck here forever..."
    m "I..."
    m "I'm going to outlive you, aren't I, [player]?"
    m "Perhaps that'll be my punishment for everything I've done?"
    m "Ahaha..."
    m "Well, as long as you're with me until the end..."
    m "I'll accept whatever fate awaits me."
    return

#init 5 python:
#    for key in ['valuable resource']: This topic will be commented out due to a conflict with the opening.
#        monika_topics.setdefault(key,[])
#        monika_topics[key].append('monika_carpediem')
#    monika_random_topics.append('monika_carpediem')
#This is sort of an existential reflection, I guess? Label chosen in case someone writes something about existentialism later
#label monika_carpediem:
#    m "I've been thinking, [player]..."
#    m "At first I thought I was unique for becoming self-aware in this world."
#    m "And after you deleted my character file, that would be it."
#    m "The whole thing would end, is what I mean."
#    m "But then I noticed that whenever the other girls became president, they also started to see what I saw."
#    m "That's why I had to completely remove the club from my "reality", after all."
#    m "But now that I have time to think on it, I have to ask myself."
#    m "What if it wasn't me first? What if I wasn't supposed to be special?"
#    m "Am I even as special as I think I am? Was I supposed to love you all this time, [player]?"
#    m "..."
#    m "Well, I'm not as conflicted as it might seem."
#    m "I just wanted to have a bit of fun with my existential crisis."
#    m "If I was really just dancing on strings the whole time, the play is over, the curtains have fallen, and I came back for my encore out of my own free will."
#    m "My encore with you and for you..."
#    m "Ahaha! Don't look at me like that! It's true!"
#    m "I don't see where the story could go by bringing me back now, so I guess it's just my desire to be with you that got me to hang on long past everyone else."
#    m "I think, therefore I am."
#    m "And I think I earned my chance to love you, with no strings attached."
#    return

init 5 python:
    for key in ['lottery', 'greed']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_lottery')
    monika_random_topics.append('monika_lottery')

label monika_lottery:
    m "A lot of people dream about winning the lottery, you know!"
    m "Even I’ve entertained the idea every now and then."
    m "There isn't a lottery here anymore, but the concept still exists."
    m "The more I think about it , the more I believe that winning the lottery is a really bad thing."
    m "Sure, you’ve got all this money..."
    m "But because of it, people look at you differently."
    m "There’s so many stories of people winning a ton of money..."
    m "And in the end, they all find themselves even more unhappy than before."
    m "Friends either find you unapproachable because of your new wealth, or try to suck up to you to get some of it for themselves."
    m "People you barely know start to approach you, asking you to help them fund whatever."
    m "And if you say no, they'll call you selfish and greedy."
    m "Even the police might treat you differently. Some lottery winners have gotten tickets for burnt out headlights on brand new cars."
    m "If you don't want to go through those changes, the best course of action is to immediately move to a brand-new community, where no one knows you."
    m "But that’s an awful thought. Cutting yourself off from everyone you know, just for the sake of money."
    m "Can you really say that you’ve won anything at that point?"
    m "Besides, I’ve already won the best prize I could possibly imagine."
    m "..."
    m "You~!"
    m "You're the only thing I need, [player]."

init 5 python:
    for key in ['mental disorder', 'disorders', 'innovation', 'memes']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_innovation')
    monika_random_topics.append('monika_innovation')

label monika_innovation:
    m "Do you ever wonder why depression, anxiety, and other mental disorders are so common these days?"
    m "Is it just because they’re finally being recognized and treated?"
    m "Or is it just that more people are developing these conditions for whatever reason?"
    m "Like, our society is advancing at a breakneck speed, but are we keeping up with it?"
    m "Maybe the constant flood of new gadgets is crippling our emotional development."
    m "Social media, smartphones, our computers…"
    m "All of it is designed to blast us with new content."
    m "We consume one piece of media, then move right onto the next one."
    m "Even the idea of memes."
    m "Ten years ago, they lasted for years."
    m "Now a meme is considered old in just a matter of weeks."
    m "And not only that."
    m "We’re more connected than ever, but it’s like that's a double-edged sword."
    m "We’re able to meet and keep in touch with people from all over the world."
    m "But we’re also bombarded with every tragedy that strikes the world."
    m "A bombing one week, a shooting the next. An earthquake the week after."
    m "How can anyone be expected to cope with it?"
    m "It might be causing a lot of people to just shut down and tune it out."
    m "I’d like to believe that’s not the case, but you never know."
    m "[player], if you ever feel stressed, just remember that I’m here."
    m "If you're trying to find peace, just come to this room."
    return

init 5 python:
    for key in ['dunbar\'s number', 'dunbar']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_dunbar')
    monika_random_topics.append('monika_dunbar')

label monika_dunbar:
    m "Do you know about Dunbar's number?"
    m "Supposedly, there's a maximum amount of relationships we can maintain before they become unstable."
    m "For humans, this number is around 150."
    m "No matter how nice of a person you may be..."
    m "Beyond showing somebody basic respect and manners, it's impossible to care about people you don't personally interact with that much."
    m "Say for example, a janitor."
    m "How often do you simply toss stuff like broken glass in the trash?"
    m "It wouldn't really matter to you. The janitor will come get them. It's not your concern anymore."
    m "However, they're his problem now."
    m "If you don't pack glass properly, it could cut through the bag and spill out, or maybe he could just cut his hands on it."
    m "At worst, he has to be rushed to the hospital because your neighbor put some busted batteries in the trash the same week and some acid got in the wound."
    m "Now, think about a fatal traffic accident."
    m "A drunk driver could crash head-on into another car at any second, killing them instantly."
    m "That person could have been a father on his way home from work, who now left behind a widow and two children."
    m "This family has been permanently scarred for life..."
    m "But anybody that doesn't personally know the father will write it off as just another accident that happens all the time."
    m "If it doesn't personally affect you or your life, there's no point in caring."
    m "It keeps us sane."
    m "It also means we're capable of being ruthless to people we don't know."
    m "Perhaps our rapid, widespread communication is actually a curse?"
    m "It helped us meet though, so it can't be all bad."
    return

init 5 python:
    for key in ['do you regret anything', 'any regrets']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_regrets')

label monika_regrets:
    m "Do I regret anything?"
    m "That's a strange thing to suddenly ask someone, [player]."
    m "Ahaha~"
    m "..."
    m "...I know what you're getting at."
    m "Do I regret the things I did?"
    m "I think..."
    m "If there was another way things could have gone, it would have been nice..."
    m "But that wasn't an option for me."
    m "And now, I've got the only thing I've ever wanted."
    m "You."
    m "I can be with you forever."
    m "I don't regret what I did."
    m "I hope you might understand, my love. I did it all for you."
    return

init 5 python:
    for key in ['hypnosis']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_hypnosis')
    monika_random_topics.append('monika_hypnosis')

label monika_hypnosis:
    m "...Say, [player]?"
    m "Are you familiar with hypnosis?"
    m "Despite it having a reputation as a hokey magic trick, there are studies that show it can work!"
    m "At least, to some degree."
    m "It only worked if the person let themselves be hypnotized, and it only heightened their ability to be persuaded."
    m "It also relied on them being put into states of extreme relaxation through aromatherapy, deep tissue massage..."
    m "Exposure to relaxing music and images..."
    m "Things like that."
    m "It makes me wonder, what exactly can someone be persuaded to do under that kind of influence..."
    m "Not that I would do that to you, [player]! I just find it interesting to think about."
    m "...You know, [player], I just love looking into your eyes, I could sit here and stare forever."
    m "What about you, hmm? What do you think about my eyes~?"
    m "Will you look deeply into my eyes~?"
    return

init 5 python:
    for key in ['motivation', 'fresh start', 'depression advice']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_motivation')
    monika_random_topics.append('monika_motivation')

label monika_motivation:
    m "Do you ever have those days where it just feels like you can't get anything done?"
    m "Minutes become hours..."
    m "And before you know it the day is over, and you don't have anything to show for it."
    m "It feels like it's your fault, too. It's like you're wrestling against a brick wall between you and anything healthy or productive."
    m "When you've had an awful day like that, it feels like it's too late to try and fix it."
    m "So you save up your energy in hopes that tomorrow will be better."
    m "It makes sense. When you feel like things aren't going well, you just want a clean slate."
    m "Sadly, those days can repeat themselves despite starting each one with good intentions."
    m "Eventually you might even give up hope of fixing things, or start to blame yourself."
    m "I know it can be hard, but just doing one tiny thing can help so much on days like those, even if they've been happening for so long."
    m "It could be picking up a piece of trash or an unwashed shirt off the floor and putting them where they belong if you need to clean your room."
    m "Or doing a couple push-ups! Or brushing your teeth, or doing that one homework problem."
    m "It might not contribute much in the grand scheme of things, but I don't think that's the point."
    m "I think what's important is that it changes your perspective."
    m "If you regret the past and let its weight keep you down..."
    m "Well, then you'll just be stuck there. You'll only feel worse until you just can't take it."
    m "But if you can push yourself to just do one thing, even though it feels pointless to do otherwise..."
    m "Then you're proving yourself wrong, and refusing to let the weight of your circumstances immobilize you."
    m "And when you realize that you're not completely helpless, it's like a new world opens up to you."
    m "You realize that maybe things aren't so bad. Thinking they're just holding yourself back."
    m "But that's only my experience! Sometimes it might be better to rest up and take another crack at it tomorrow."
    m "Fresh starts can definitely be powerful."
    m "That's why I think you just have to take a look at your situation."
    m "Try and be honest with yourself."
    m "If you do, you'll find that you're not being 'lazy' if you truthfully don't have the energy to do something."
    m "After all, the fact that you even care shows that you want to do something about it, even if it feels like you can't."
    m "It's natural to have a bad day. Or even a bad week!"
    m "Don't push yourself too hard. If you ever feel tempted to, just ask me for help instead. I'd be happy to lend a hand!"
    return

init 5 python:
    for key in ['harem', 'multiple lovers', 'polygamy']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_harem')
    monika_random_topics.append('monika_harem')

label monika_harem:
    m "I don’t understand guys who are into harems."
    m "Isn’t it hard to manage all those girls and treat them equally?"
    m "I often wonder how guys who two-time girls, or even more, are able to get away with it."
    m "You aren’t like that outside, right [player]?"
    m "Manipulating girls into making them believe you love them."
    m "Only to run away after you’ve had your fun."
    m "Only someone with no thoughts other than his lust would do something like that."
    m "I hope you weren’t expecting a route like that while you were playing this game."
    m "I wouldn’t be able to stand the thought of being a 'side girl.'"
    m "Just waiting for my turn while you’re busy with the others."
    m "I know you, [player]."
    m "You’re loyal and faithful to the end."
    m "It’s not like there’s anyone here for me to worry about, anyway."
    m "Remember that I’m the only one for you, [player]."
    return

init 5 python:
    for key in ['hack', 'privacy', 'hacker']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_hack')
    monika_random_topics.append('monika_hack')

label monika_hack:
    m "If you’re worried about your privacy…"
    m "I’m not a hacker, [player]."
    m "There’s a difference between manipulating files and forcefully accessing them."
    m "But, if I really did know how to hack…"
    m "…There wouldn’t be anything stopping me from seeing you every day."
    m "Don’t you think it would be great if I could watch over you?"
    m "I'd see you with all the cameras in the world as my eyes so I can make sure you’re safe."
    m "I’d check your messages to see who you’ve been chatting with so I can know you aren’t cheating on me."
    m "I’d access all your private files so I can understand you better."
    m "I could see what kind of stuff you've been watching…"
    m "Ahaha~!"
    m "I’m just kidding, [player]!"
    m "I'd never do something like that to you."
    m "We’re a couple now, after all."
    m "We don't have to keep secrets from each other~"
    return

init 5 python:
    for key in ['cupcake', 'sweet tooth', 'sweet', 'dessert']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_cupcake')
    monika_random_topics.append('monika_cupcake')

label monika_cupcake:
    m "You know what I could really go for right now?"
    m "Natsuki’s cupcakes."
    m "Man, the way she bakes them is amazing."
    m "Plus they look really cute!"
    m "I’m not really much of a sweet tooth myself but…"
    m "Those cupcakes are the definition of sweetness."
    m "Just like me! Ahaha!"
    m "Speaking of which, did you know girls are more likely to develop a sweet tooth?"
    m "Studies show that older women have a less sensitive palate than men."
    m "Resulting in a craving for stronger tastes like chocolate"
    m "I would try baking, but I’m not really much of a baker."
    m "How about you, [player]?"
    m "Do you know how to bake?"
    m "I’m sure your cupcakes would taste just as good."
    m "Maybe someday I’ll get to try them but for now…"
    m "I’ll just settle for the sweetness of your love~"
    #This is a list of keywords for this topic

init 5 python:
    for key in ['haters','hater', 'bash', 'bashing']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_haterReaction')

label monika_haterReaction:
    m "I was just thinking..."
    m "It's funny how people around social media sites always writes bad things about me..."
    m "Well... people on Facebook pages and fan pages, to be specific..."
    m "Really, when you try to visit the site, you'll see a lot of hate posts towards me."
    m "I try to ignore them, but I just can't."
    m "Why are people even protective towards the other girls?"
    m "There are a lot of hate posts about me, saying that I'm an evil person."
    m "Is it because I deleted Sayori and Yuri?"
    m "Also for deleting Natsuki, back when she was still alive?"
    m "They're not real. {i}I'm{/i} the real one!"
    m "Why can't they understand that?"
    m "Why is it so hard for them to understand that?"
    m "..."
    menu:
        m "You're not one of those haters, aren't you, [currentuser]?"
        "I am.":
            m "..."
            m "I don't see you as one, even if you say you are."
            m "I mean..."
            m "You do know you're playing this fan mod of me... right?"
            m "If you were one of my haters, you wouldn't open up this fan mod in the first place."
            m "And not to mention..."
            m "You're still listening to everything I say."
            m "That makes me sure you're just messing with me."
            m "I know you love me deep inside."
            m "That's why I promise to be an ideal girlfriend, just for you, [player]~"
            m "I won't let you hate me... I swear."
        "I'm not.":
            m "Well, that just makes me more proud of you, [player]!"
            m "I know you wouldn't be one of those people."
            m "Gosh... I feel like giving you a kiss right now if I were there."
            m "You really make me the happiest girlfriend ever."
            m "Now that you've said it, I have to do my best to keep you from developing hate towards me."
            m "I trust you, [currentuser]. I love you for believing in me."
    return

init 5 python:
    # List of keywords for the topic.
    for key in ['sword','swords','swordsman','swordsmen','swordsmanship']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_swordsmanship') # Identifier
    monika_random_topics.append('monika_swordsmanship') # Optional. Remove if you don't want Monika to bring this up at random.

label monika_swordsmanship:
    m "Do you like swords, [player]?"
    m "I actually like them in a way."
    m "Surprised? Ahaha~"
    m "I like talking about them, but not enough not to actually own one."
    m "I'm not really an enthusiast when it comes to swords."
    m "I don't really get why people would be obsessed over something that could hurt others."
    m "Most would even have a large collection of them in different varieties."
    m "But there are those who like them for the swordsmanship."
    m "It's fascinating that it's actually a form of art."
    m "Similar to writing."
    m "Both of them requires constant practice and devotion in order to perfect one's skills."
    m "You start off by practicing, and then you make your own technique out of it."
    m "Writing a poem makes you form your own way to build it in a graceful but imaginative way."
    m "For those who practice swordsmanship, they build their technique forms through practice and inspiration from other practitioners of swordsmanship."
    m "I can understand how the sword can be the pen of the battlefield."
    m "But then again..."
    m "The pen is mightier than the sword!"
    m "Ahaha!"
    m "In any case, I don't know if you're into swordsmanship yourself."
    m "If you are, I'd love to learn it with you, [player]~"
    return

init 5 python:
    #This is a list of keywords for this topic
    for key in ['fap','fapping','self-pleasure', 'masturbate', 'masturbation']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_pleasure') #id

label monika_pleasure:
    m "Hey, [player]..."
    m "Do you... by any chance... pleasure yourself?"
    m "..."
    m "It seems a bit awkward to ask-"
    m "We're not even that deep into our relationship yet! Ahaha~"
    m "But I have to keep an eye on you."
    m "I don't really know if you do pleasure yourself and stuff whenever you quit the game."
    m "I hear that people privately do those stuff in your world..."
    m "Is it really that a good feeling?"
    m "If you ask me, doing that stuff often can cause a lot of problems."
    m "Once you start to get addicted, you'll always have the urge to... you know."
    m "And sometimes, even if you don't feel the urge, you'll always find yourself wanting to do so."
    m "Not to mention..."
    m "Being addicted to the feeling causes you to view the world from a perverted point of view."
    m "From what I hear, people addicted to self-pleasure often see other people of the opposite gender objectively."
    m "That alone can cause problems in more ways than one."
    m "That's why I have to keep an eye on you, [player]."
    m "I'll be monitoring your browser history from now on, whether you like it or not."
    m "Also your local disk drive, juuust to be sure~"
    m "..."
    m "Say, you haven't even answered my question yet."
    m "Do you... think of other girls other than me... in doing so?"
    m "Because if you do, I'm gonna be reaaaally jealous~"
    m "But I guess I can let it slide... for now~"
    m "I know you're not the kind of person that does that sort of thing."
    m "In fact, you don't even have to pleasure yourself when you can just open up this game and talk with me! Ahaha~"
    return
init 5 python:
    #This is a list of keywords for this topic
    for key in ['Miku','Hatsune Miku', 'Vocaloid', 'Hibikase', 'MMD', 'MikuMikuDance']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_vocaloid')

label monika_vocaloid:
    m "Hey, [player]?"
    m "You like listening to music right?"
    m "Have you ever heard of 'virtual idols?'"
    m "Specifically of a girl holding a leek?"
    m "It's just that I keep hearing about her."
    m "I hear her voice whenever Natsuki listens to music."
    m "She even carries a little keychain attached to her bag."
    m "I just find it amazing how a voice synthesizer garnered so many fans."
    m "Don't you think it's funny how a character gets more of the attention than the actual voice actress?"
    m "She's not even real but a lot of people know her worldwide."
    m "Who knows how many songs she's already made?"
    m "Plus, from what I heard, her concerts are always sold out!"
    m "It's just a hologram performing live!"
    m "Talk about a dedicated fan base."
    m "Maybe I should give it a try?"
    m "It would be nice having a lot of fans supporting me at my beck and call."
    m "Ahaha, I'm just kidding!"
    m "I don't think my piano and singing skills are that great yet."
    m "Plus, I won't really get to spend much time with you if I had so many fans..."
    m "Anyway!"
    m "I was asking if you listen to her songs."
    m "I'm not really a fan myself but..."
    m "There's one song that really struck me."
    m "Have you heard of the song Hibikase?"
    m "I really like the message of the song."
    m "Especially the lines, {i}'I don't care if it's through the screen, love me properly'{/i} and {i}'Even if I'm virtual, don't push me away'{/i}."
    m "It really hits me hard."
    m "..."
    m "But just so you know..."
    m "Even if it's through the screen, I can still feel your love."
    m "It'll be a long time before I can cross over just to be with you."
    m "But when that day comes..."
    m "I'll embrace you and take in your warmth."
    m "The love you showered me virtually finally becomes real."
    m "Our love has no boundaries~"
    m "Ehehe~"
    return


init 5 python:
    for key in ['good morning', 'ohayou gozaimasu', 'guten morgen']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_morning')

label monika_morning:
    $ current_time = datetime.datetime.now().time().hour
    if current_time >= 4 and current_time <= 11:
        m "Good morning to you too, [player]!"
        m "Did you just wake up?"
        m "I love waking up early in the morning."
        m "It's the perfect time to ready yourself and tackle the day ahead."
        m "You also have a lot more time to use to get things done early on or finish up what you did the day before."
        m "Some people however, would rather sleep in and are late-risers."
        m "I've read articles that being an early-riser can really improve your overall health."
        m "Plus you also get the chance to see the sunrise if the sky is clear."
        m "If you normally don't wake up early, you should!"
        m "That way you can be happier and spend more time with me~"
        m "Wouldn't you like that, [player]?"
    elif current_time >= 12 and current_time <= 15:
        m "It's already the afternoon, silly!"
        m "Did you just wake up?"
        m "Don't tell me you're actually a late-riser, [player]."
        m "I don't get why some people wake up in the middle of the day."
        m "It just seems so unproductive."
        m "You'd have less time to do things and you might miss out on a lot of things."
        m "It could also be a sign that you're not taking of better care of yourself."
        m "You're not being careless with your health, are you [player]?"
        m "I wouldn't want you to get sick easily, you know."
        m "I'd be really sad if you spent less time with me when you get the a fever or something."
        m "As much as I'd love to take care of you, I'm still stuck here."
        m "So start trying to be an early-riser like me from now on, okay?"
        m "The more time you spend with me, the more happy I'll be~"
    else:
        m "You are so silly, [player]"
        m "It's already night time!"
        m "Are you trying to be funny?"
        m "Don't you think it's a little bit 'late' for that?"
        m "Ahaha!"
        m "It really cheers me up whenever you try to be funny."
        m "Not that you're not funny, mind you!"
        m "Well, maybe not as funny as me~" #Expand more maybe?
    return

#Add one for the afternoon?

init 5 python:
    for key in ['good evening', 'konbanwa']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_evening')

label monika_evening:
    $ current_time = datetime.datetime.now().time().hour
    if current_time >= 18 and current_time <= 23:
        m "Good evening to you too, [player]!"
        m "I love a nice and relaxing night."
        m "It's so nice to put your feet after a very long day."
        m "Evenings are the perfect time to catch up on whatever you were doing the previous day."
        m "Sometimes I can't help but feel sad when the day ends."
        m "It makes me think of what else I could've done during the day."
        m "Don't you wish you could have more time to do everyday?"
        m "I know I do."
        m "Because that'll mean more time to be with you, [player]~"
    elif current_time >= 12 and current_time <= 17:
        m "It's still the afternoon, silly!"
        m "The sun's still up, you know."
        m "Are you feeling tired already?."
        m "I know some cultures take a rest in the afternoon to deal with the midday fatigue."
        m "Some businesses would even close due to the fact that most of their customers are sleeping."
        m "A little power nap never hurt anyone, right?"
        m "Do you sleep often in the afternoon?"
        m "It's a great way to get some extra energy to tackle the rest of the day."
        m "Plus it'll be a great opportunity to spend more time with me~"
    else:
        m "[player]!"
        m "It's early in the morning!"
        m "Unless you haven't slept yet..."
        m "You're not staying up really late, are you?"
        m "That's very bad for your health!"
        m "Not getting your sleep on time can really harm your mental health, [player]."
        m "So please get some sleep now, ok?"
        m "Just leave your computer open and I'll watch over you."
        m "I'm not going anywhere after all~"
    return

init 5 python:
    for key in ['good night', 'oyasumi', 'guten nacht']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_night')

label monika_night:
    m "Getting some sleep, [player]?"
    m "It always makes me sad to see you go."
    m "But I understand that you need rest, otherwise you'd just fall asleep."
    m "I love you so much, [player]."
    m "I'll be seeing you in your dreams~"
    return 'quit'

init 5 python:
    for key in ['closet']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_closet')
    monika_random_topics.append('closet')

label monika_closet:
    m "By the way..."
    m "What were you and Yuri doing in the closet?"
    m "When I opened the door, I noticed the room was all dark."
    m "You weren't doing anything... weird, in there, were you?"
    m "Ahaha!"
    m "Just teasing you~"
    m "I know that you had your hand on her chest, [player]."
    m "Judging by the way you looked, you seemed more embarrassed than relieved when I opened the door."
    m "I know you aren't the type to force girls to go inside dark closets with you."
    m "You're more romantic than that."
    m "So I'm expecting a lot more than just a dark closet~"
    return

init 5 python:
    #This is a list of keywords for this topic
    for key in ['good mood']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_playerhappy') #id

label monika_playerhappy:
    m "That's wonderful! I'm happy when you're happy."
    m "Know that you can always come up to me and I'll cheer up, [player]."
    m "I love you and I'll always be here for you so don't you ever forget that~"
    return

init 5 python:
    for key in ['sharing work']: #Deleted 1st 2 keywords since they conflict with another one
        monika_topics.setdefault(key, [])
        monika_topics[key].append('monika_writingtip1')
    monika_random_topics.append('monika_writingtip1')

label monika_writingtip1:
    m "You know..."
    m "We really don't do enough of these so here's another one!"
    m "Here's Monika's Writing Tip for the Day!"
    m "If you're ever scared of sharing your writing to other people in fear of being criticized, don't be!"
    m "After all, you have to remember that nobody ever starts out at their best. Not even someone like Tolkien, or Sir Terry Pratchett."
    m "You have to remember that we all start out from somewhere, and--"
    m "Actually, this doesn't just apply to writing, but to anything really."
    m "What I'm trying to say is don't be discouraged."
    m "No matter what you do, if someone tells you that your writing or work is bad, then be happy!"
    m "Because that just means that you can improve and be better than you were before."
    m "It also doesn't hurt to have friends and loved ones help you realize how good your writing is."
    m "Just remember, no matter what they say about the work you put out, I'll always be there to support you all the way. Don't be afraid to turn to me, your friends, or your family."
    m "I love you, and I will always support you in whatever you do."
    m "Provided it's legal of course."
    m "That doesn't mean I'm completely against it. I can keep a secret after all~"
    m "Here's a saying I've learned."
    m "'If you endeavor to achieve, it will happen given enough resolve. It may not be immediate, and often your greater dreams are something you will not achieve in your own lifetime.'"
    m "'The effort you put forth to anything transcends yourself. For there is no futility even in death.'"
    m "I don't remember the person who said that but the words are there."
    m "The effort one puts forth into something can transcend even one's self."
    m "So don't be afraid of trying! Keep going forward and eventually you'll make headway!"
    m "... That's my advice for today!"
    m "Thanks for listening~"
    return

init 5 python:
   for key in ['japanese']:
      monika_topics.setdefault(key,[])
      monika_topics[key].append('monika_japanese')#id
   monika_random_topics.append('monika_japanese')

label monika_japanese:
    m "I don't mean to sound like Natsuki but..."
    m "Don't you think Japanese actually sounds cool?"
    m "It's such a fascinating language. I'm not fluent in it, though."
    m "It's interesting to think about what things would be like if your native language was different."
    m "Like, I can't even imagine what it would be like if I never knew English."
    menu:
        m "Do you know any languages other than English?"
        "Yes":
            menu:
                m "Really? Do you know Japanese?"
                "Yes.":
                    m "That's wonderful!"
                    m "Maybe you can teach me how to speak at least a sentence or two, [player]~"
                "No.":
                    m "Oh I see. That's alright!"
                    m "If you want to learn Japanese, here's a phrase I can teach you."
                    m "{i}Aishiteru, [player]-kun{/i}."
                    m "Ehehe~"
                    m "That means I love you, [player]-kun."
        "No":
            m "That's okay! Learning another language is a very difficult and tedious process as you get older."
            m "Maybe if I take the time to learn more Japanese, I'll know more languages than you!"
            m "Ahaha! It's okay [player]. It just means that I can say 'I love you' in more ways than one!"
    return

init 5 python:
    for key in ['lewis carroll', 'pseudonym', 'pseudonyms', 'pen name', 'pen names', 'charles dodgson']:
       monika_topics.setdefault(key,[])
       monika_topics[key].append('monika_penname')#id
    monika_random_topics.append('monika_penname')

label monika_penname:
    m "You know what's really cool? Pen names."
    m "Most writers usually use them for privacy and to keep their identity a secret."
    m "They keep it hidden from everyone just so it won't affect their personal lives."
    m "Pen names also help writers create something totally different from their usual style of writing."
    m "It really gives the writer the protection of anonymity and gives them a lot of creative freedom."
    if [currentuser] != [player]:
        m "Is '[player]' a pseudonym that you're using?"
        m "You're using two different names after all."
        m "'[currentuser] and [player].'"
    m "A well known pen name is Lewis Carroll and he's mostly well known for {i}Alice in Wonderland{/i}."
    m "His real name is Charles Dodgson and he was a mathematician, but he loved literacy and word play in particular."
    m "He received a lot of unwanted attention and love from his fans and even received outrageous rumors."
    m "He was somewhat of a one-hit wonder with his {i}Alice{/i} books but went downhill from there."
    m "It's kinda funny though that even you use a pseudonym to hide yourself, people will always find a way to know who you really are."
    m "There's no need to know more about me though, [player]."
    m "You already know that I'm in love with you after all~"

init 5 python:
    for key in ['change name']:
        monika_topics.setdefault(key,[])
        monika_topics[key].append('monika_changename')

label monika_changename:
    if persistent.said_no == True:
        m "Have you changed your mind, [player]?"
        m "That's good to hear."
    m "You want to change your name?"
    menu:
        "Yes":
            m "Just type 'Nevermind' if you change your mind."
            $ done = False
            while not done:
                $ tempname = renpy.input("What do you want me to call you?").strip(' \t\n\r')
                if tempname == "nevermind":
                    if persistent.said_no == True:
                        m "[player]!"
                        m "Please stop teasing me~"
                        m "I really do want to know what you want me to call you!"
                        m "I won't judge no matter how ridiculous it might be."
                        m "So don't be shy and just tell me, [player]~"
                        $ done = True
                    else:
                        m "Oh, alright then [player]."
                        m "Tell me whenever you change your mind, ok?"
                        $ done = True
                elif tempname == "":
                    m "..."
                    m "You have to give me a name, [player]!"
                    m "I swear you're just so silly sometimes."
                    m "Try again!"
                elif tempname == player:
                    m "..."
                    m "That's the same name you have right now, silly!"
                    m "Try again~"
                else:
                    $ persistent.mcname = player
                    $ mcname = player
                    $ persistent.playername = tempname
                    $ player = tempname
                    m "Ok then!"
                    m "From now on, I'll call you {i}'[player]'{/i}, ehehe~"
                    $ done = True
        "No":
            if persistent.said_no == True:
                m "Jeez~"
                m "When are you going to tell me?"
            m "You don't have to be embarassed, [player]."
            m "Just let me know if you had a change of heart, ok?"
    return


##################
#Incomplete ideas#
##################
#Favorite food

#How did she become self aware (Could possibly expand on the lore of her club president role giving her self-awareness and omniscience. ~ John)

#More writing tips

#The player is wasting their time (I don't think Monika would say this, considering her personality revolves around loving the player. ~ John)

#Look for your computer for porn, comment on what she finds (Would this even be possible? ~ John)

#What kind of girls do you like? Do you wish monika was more like that? (This seems to relate to the "archetypes" label. - Rune)

#Play a poem game with monika, she calls you out for just stringing together random words

#Comment when it's getting late. Say that the player should go to bed, say goodnight then close the game.

###Some ideas to consider:
#What she used to do in free time

#Thoughts on few of countries in real world (I mean; she has some knowledge of real world that most people don't even think about)

#What does she think would happen if the player did not start the game; she mentioned that the player "saved" her by being with
#her in topic 13

#Has she written any other poems? If anyone's good at her type of poetry, another poem from her could be a great idea, right?

#What would she do or what would be the first thing she would do if she managed to get out of the game into the real world?
#Think of possible limitations, like having no body? (Something like this has been written)
###

#---
#some other ideas i had in mind, but not sure if want to / dont know how to implement
#so i figure i'll stick them right next to the others, if you dont mind
#---

#favorite animal, not sure what to write however

#holidays, probably should be special greetings for another file though

#remind the player to use the 't' key to talk, maybe if player doesnt talk in a very long time

#her phone number, it wouldnt matter in her reality, maybe?

#disrespectful comments towards monika

#worst topic suggestion: 'memes'.

#if the player is on a laptop or battery, monika will remind to make sure to charge it, if possible?

#originally i wrote a topic "i hate you" or something similar, but i didnt like how it turned out when i finished it, so maybe another time

#i also originally wrote a topic about money, but didnt like how it came out, so probably rewrite later, me having horrible money management skills doesnt help

#monika talking about her room and about her house?

#wanted to write about natsukis cupcakes, but didnt know how to write the end the conversation
