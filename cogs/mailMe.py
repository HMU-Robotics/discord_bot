
from encodings import utf_8
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv())
guildID = os.getenv("guild_test")

sender_address = os.getenv("SENDER_EMAIL")
sender_pass = os.getenv("EMAIL_PASSWORD")

dummyDatabase = ["one@gmail.com","two@gmai.com","three@gmail.com"]



class MailMe(commands.Cog):
    def __init__(self,client):
        self.client = client



    @nextcord.slash_command(name="mailme",description="mails a message to a user",guild_ids=[guildID])
    async def mailme(self,ctx:commands.Context,receiver_address,title,message_to_send):
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = title
        message.attach(MIMEText(message_to_send,'plain'))
        session = smtplib.SMTP('mail.cs.hmu.gr', 465)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        # session.sendmail(sender_address, receiver_address, text)
        print(receiver_address,text)
        session.quit()
        await ctx.send('Mail Sent')


    @nextcord.slash_command(name="mailall",description="mails a database of users",guild_ids=[guildID])
    async def mailall(self,ctx:commands.Context,title,message_to_send):
        for x in dummyDatabase:
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = x
            message['Subject'] = title
            message.attach(MIMEText(message_to_send,'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(sender_address, sender_pass)
            text = message.as_string()
            # session.sendmail(sender_address, x, text)
            print(x,text)
            session.quit()
            await ctx.send('Mail Sent')

def setup(bot):
    bot.add_cog(MailMe(bot))