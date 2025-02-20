import discord
import requests

TOKEN = "MTM0MjA3NTQxMzg3MDAyMjcyOA.GC-YXN.OTylQcfypJO5oMwaG3howCjOABYJLbjwLeaUBw"  # Replace with your actual bot token
BRAWL_API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjJlZmFlMGY0LTEyNWYtNDk4NC04NGRhLWUyMjc2MjQ0MmQ0MiIsImlhdCI6MTc0MDA0Njc2Nywic3ViIjoiZGV2ZWxvcGVyL2EzOTQ0YmFmLTRkYWItNTlhZC04MDBhLTcwOWNlYmJjMWU0OCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMC4wLjAuMCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.GKbMfeUe46zqr5bcUq6PWB5uppIGa-u7K00c1jq3zQDMtCEtGhRNV04V0vlTHcdczsk4B0LcAO19IFbKFIT_0w"  # Replace with your actual API key

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.slash_command(name="spectate", description="Get player battle details")
async def spectate(ctx, player_id: str, num: int, mode: str):
    headers = {"Authorization": f"Bearer {BRAWL_API_KEY}"}
    url = f"https://api.brawlstars.com/v1/players/%23{player_id}"  # %23 is '#' in URL encoding
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        trophies = data["trophies"]
        await ctx.respond(f"Player {name} has {trophies} trophies.")
    else:
        await ctx.respond("Failed to fetch player data.")

bot.run(TOKEN)
