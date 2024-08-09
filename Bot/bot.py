import lightbulb
import requests
from datetime import datetime

def converter_temperatura(tem1,T):
    C_F = tem1 * 1.8 + 32
    F_C = (tem1 - 32)/1.8
    K_C = tem1 - 273.15
    K_F = ((tem1 - 32) * 1.8) - 273.15
    return {'C_F':C_F, 'F_C':F_C, 'K_C':K_C,'K_F':K_F}[T]

def emote_temperatura(temp):
    temp_emote = [":ice_cube:", ":fire:",":cup_with_straw:"]
    if temp <= 21 : emote = temp_emote[0]
    elif  temp >= 28 :  emote = temp_emote[1]
    else : emote = temp_emote[2]
    return emote

bot = lightbulb.BotApp(token=open('./tokens/token_ds.txt', 'r').read(),
                 default_enabled_guilds=(int(open('./tokens/channel_id.txt', 'r').read())))

@bot.command
@lightbulb.command('msg_bot', 'Olá @everyone')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond('*Olá, pessoal!*')


# TODO : verificar requisicao de parametro 
@bot.command
@lightbulb.command('joke', 'Uma piada')# AQUI
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    url = ""
    api_key = open('./tokens/dadJokeAPI_key.txt','r').read()

    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    payload = {}
    headers = {
    'X-RapidAPI-Key': f'{api_key}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    setup = res['body'][0]['setup']
    punchline = res['body'][0]['punchline']
    await ctx.respond(f'*{setup}*\n**{punchline}**')

@bot.command
@lightbulb.command("w","clima")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def w(ctx):
    pass

@w.child
# @lightbulb.option("nome","descrição",type=str)
@lightbulb.option("cidade","descrição",type=str)
@lightbulb.option("estado","descrição",type=str)
@lightbulb.option("país","descrição",type=str)

@lightbulb.command("tempo", "Temperatura da região")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def temp(ctx):
    api_key = open('./tokens/OpenWeatherAPI_key.txt','r').read()
    curr_hour = datetime.hour
    hour_emotes = [":new_moon:", ":sunny:" ]
    country = (ctx.options.país).upper()[0:2]
    city = ctx.options.cidade
    state = ctx.options.estado.upper()[0:2]
    print(country, city)
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={api_key}'
    headers = {
    'x-api-key': f'{api_key}'
    }
    response = requests.request("GET", url, headers=headers)
    res = response.json()
    weather = res['weather'][0]['main']
    print(weather)
    content = res['main']
    _temperatura = converter_temperatura(content['temp'],'K_C')
    _sensacao_termica = converter_temperatura(content['feels_like'],'K_C')
    _temperatura_maxima = converter_temperatura(content['temp_max'],'K_C')
    _temperatura_minima = converter_temperatura(content['temp_min'],'K_C')
    _umidade = content['humidity']
    _emote = None
    weathers = ["Clouds","Rain","Sunny","Snow","Clear"]
    emotes = ["Nublado :cloud:","Chuvoso :cloud_rain:","Ensolarado :sun_with_face:","Nevando :cloud_snow:","Céu Limpo :sunglasses: "]
    if weather in weathers:
        _emote = emotes[weathers.index(weather)]
    format_response = f"""
                Clima de {city} 
                {_emote}
                :thermometer:
                {"#"*35}
                :stopwatch: Temperatura Atual : {_temperatura:.1f} °C  {emote_temperatura(_temperatura)}
                {"-"*35}
                :arrow_down: Temperatura Mínima : {_temperatura_minima:.1f} °C  {emote_temperatura(_temperatura_minima)}
                {"-"*35}
                :arrow_up: Temperatura Máxima : {_temperatura_maxima:.1f} °C  {emote_temperatura(_temperatura_maxima)}
                {"-"*35}
                Sensação Térmica : {_sensacao_termica:.1f} °C  {emote_temperatura(_sensacao_termica)}
                {"-"*35}
                Umidade : {_umidade}%
                {"#"*35}
    """
    await ctx.respond(f'{format_response}')

bot.run()