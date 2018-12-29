def onQQMessage(bot,contact,member,content):
    if content == '-hello':
        bot.SendTo(contact,"��ã�IDIOT")
    elif content == '-stop':
        bot.SendTo(contact,"qq关闭")
        bot.Stop()