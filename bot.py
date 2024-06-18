import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def bilgi(ctx):
    await ctx.send("Sosyal Medya:Instagram: #SıfırAtık, #ÇevreciYaşam, #Sürdürülebilirlik gibi hashtag'leri takip ederek ilham verici içeriklere ulaşabilirsiniz.Facebook: Çevre dostu ürünler satan ve sürdürülebilir yaşam tarzı ile ilgili bilgi paylaşan gruplara katılabilirsiniz.YouTube: Çevre ve sürdürülebilirlik konulu videolar izleyebilirsiniz.Ek Öneriler:Yerel Çevre Gruplarına Katılın: Bölgenizdeki çevre aktivistleri ile iletişime geçerek onların çalışmalarına katkıda bulunabilirsiniz.Çevre Dostu Ürünler Tercih Edin: Mümkün olduğunca geri dönüştürülmüş veya sürdürülebilir kaynaklardan üretilmiş ürünler satın alın.Enerji ve Su Tasarrufu Yapın: Işıkları kapatın, elektronik cihazları fişten çekin, duş sürenizi kısaltın ve muslukları kapatmayı unutmayın.Toplu Taşıma, Bisiklet veya Yürüyüş Kullanın: Mümkün olduğunca özel araç kullanmaktan kaçının.Atıklarınızı Geri Dönüştürün ve Kompostlayın: Geri dönüştürülebilir atıklarınızı ayrı toplayın ve kompostlanabilir atıklarınızı kompostlayın.")
bot.run("")
