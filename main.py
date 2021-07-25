#import discord API
from discord.ext import commands
#import date
from datetime import date

#declarations

bot = commands.Bot(command_prefix="b.")
today = date.today()
print ("Today's date: " +str(today.month) + " " +str(today.day))



#first event 
@bot.command()
async def on_ready(self):
  print("We have logged in as {0.user}".format(bot))
#@bot.event
#async def on_ready():
#  channel = bot.get_channel(id=868165602823536640)
#  await channel.send("Welcome! BirthDay Bot is here to wish you a #happy birthday. Please insert your name and bday in the fomat: b.set #name month day")


#second event: if bot registers a message
#based on specific message, answer specifically 
#only replies when someone uses prefix
@bot.command()
async def Hello(ctx):
  if ctx.author == bot.user:
    return
  await ctx.channel.send("```Hello!```")



#third event: if asked for date (this is for test)
@bot.command()
async def date(ctx):
  if ctx.author == bot.user:
    return 
  text = "`Month: " + str(today.month) + " Day: " + str(today.day) + " Year: " + str(today.year) + "`"
  await ctx.channel.send(text)


#input test
@bot.command()
async def test(ctx, arg1, arg2):
  await ctx.send("you passed {} and {}".format(arg1, arg2))



#official fourth event - input birthday and tells if its your birthday
@bot.command()
async def set(ctx, name, month, day):
  nowMonth = str(today.month)
  bdayMonth = month
  nowDay = str(today.day)
  bdayDay = day
  if (nowMonth == bdayMonth and nowDay == bdayDay):
   await ctx.send("`Today is your birthday!🎂🎉`")
   await ctx.send("`HAPPY BIRTHDAY!!🎈🎉🎁🥳🎂💫`")

  else:
   await ctx.send("`Today is not your birthday🙁 but here's a cake anyway🎂`")
   #try to put the months as a word?
  if (int(month) == 1): #??? #try
    month = "January"
  elif (int(month)== 2):
    month = "February"
  elif (int(month)== 3):
    month = "March"
  elif (int(month)== 4):
    month = "April"
  elif (int(month)== 5):
    month = "May"
  elif (int(month) == 6): 
    month = "June"
  elif (int(month)== 7):
    month = "July"
  elif (int(month)== 8):
    month = "August"
  elif (int(month)== 9):
    month = "September"
  elif (int(month)== 10):
    month = "October"
  elif (int(month)== 11):
    month = "November"
  elif (int(month)== 12):
    month = "December"
  else:
    month = "<Invalid Month Number!!!>"
  await ctx.send("`{}'s birthday is on {} the {}`".format(name, month, day))

#fifth event - a help menu
@bot.command()
async def Help(ctx):
  if ctx.author == bot.user:
    return
  await ctx.channel.send("```Help is here!\nTo set Birthday: b.set (name) (month) (day)\nExample: Alicenessa 7 25\nTo get current date: b.date\n To simply greet the bot: b.Hello```")


#trying to store the data in a list:
#some_list = []
#    user_message = message.content.split()
#    some_list.append(user_message)
#for i in some_list:
#        del i[0]# delete's command tagevent four,
  

#line to run bot by token (token taken by discord admin) DONT MESS WITH THIS
bot.run("ODY4MTY4ODYxNjk3MDUyNzAz.YPrvQg.fnE5X5tJaDtL0uE3aMVp4XeSt5s")



