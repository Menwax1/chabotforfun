import os
import time
os.system('cls')




time.sleep(1)
os.system('cls')
print ("Shalom, I'm the ChaBot.")
your_first = input ("What's your name?\n")
your_last = input ("What's your last name?\n")
print ("Nice to meet you,", (your_first),(your_last), end='')
year = input (", what class are you?\n")
if year.lower() == "freshman" or year.lower() == "firstyear":
   print ("We're excited to meet you. We would love if you could come to Chabad for a Shabbat dinner, you'll be able to have a fun jewish experience while also meeting other " + str(year), end='')
   print (" and learn more about your Jewish heritage with Sinai Scholars classes with other Jews of all backgrounds.", end='')
   learn_more = input(" Would you like to learn more? Type 'learn more' to know more. ")
else: 
    print("We're sorry we haven't met you yet. We would love if you could come to Chabad for a Shabbat dinner where you can meet other " + str(year), end='')
    print ("s and learn more about your Jewish heritage you can dive deeper with Sinai Scholars classes with other Jews of all backgrounds.", end='')
    learn_more = input(" Would you like to learn more? Type 'learn more' to know more. You can type 'remind me' to get a reminder.\n")
if learn_more.lower() == "learn more":
    Shabbat = input ("We have friday night dinner, TXT 'shabbat' if you wish to attend. TXT 'remind me' to get a reminder.\n")
if Shabbat.lower() == "remind me" or learn_more.lower() == "remind me":
        print ("You'll get a reminder to rsvp in 10 seconds")
        time.sleep(1)
        print ("9")
        time.sleep(1)
        print ("8")
        time.sleep(1)
        print ("7")
        time.sleep(2)
        print ("5 more secs.")
        time.sleep(5)
        os.system('cls')
        reminder_shabbat = input ("TXT 'shabbat' to rsvp.\n")
        if Shabbat.lower() == "shabbat" or reminder_shabbat.lower() == "shabbat":
            allergies = input ("TXT your allergeies (write 'no' if you don't have any)", end='')
            if allergies.lower() == "no":
                print ("Ok. Thanks.")
            else:
                #print ("We will try to have food without "  + str(allergies), + ", when you RSVP!!!")
                print (f"We will try to have food without {allergies} when you RSVP!!!")

        print ("Ok, you have officaly rsvped. I hope to update you soon. veiw the website at... ")