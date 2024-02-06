import discord
from discord.ext import commands
import random


def generate(n,m):
    res="地雷の数 : "+str(n)+"\n"
    chars=[":blue_square:",":one:",":two:",":three:",":four:",":five:",":six:",":seven:",":eight:",":bomb:"]
    rs=set()
    while len(rs)<m:
        rs.add(random.randint(0,n*n-1))

    s=[[0]*n for i in range(n)]

    for r in rs:
        s[r//n][r%n]=9

    for i in range(n):
        for j in range(n):
            if s[i][j]==9:continue
            cnt=0
            for di in range(-1,2):
                for dj in range(-1,2):
                    if not((0<=i+di<n)&(0<=j+dj<n)):continue
                    if s[i+di][j+dj]==9:
                        cnt+=1
            s[i][j]=cnt

    si,sj=0,0
    while si==0:
        r=random.randint(0,(n-2)*(n-2)-1)
        if s[r//(n-2)+1][r%(n-2)+1]==0:
            si,sj=r//(n-2)+1,r%(n-2)+1

    for i in range(n):
        for j in range(n):
            if (i==si)&(j==sj):
                res+=chars[s[i][j]]
            else:
                res+="||"+chars[s[i][j]]+"||"
        res+="\n"
    return res

class minesweeper(commands.Cog):
    def __init__(self,bot):
        print("start minesweeper init")
        self.bot=bot

    @commands.slash_command(description="MineSweeperを生成する:bomb:")
    async def generate(self,ctx: discord.ApplicationContext):
        s=generate(8,8)
        await ctx.respond(s)
    
# @commands.slash_command(description="MineSweeperを生成する:bomb:")
# async def custom(ctx: discord.ApplicationContext,
#                 width: Option(int,required=True, description="1辺の長さ"),
#                 bombs: Option(int,required=True, description="地雷の数")):

def setup(bot):
    bot.add_cog(minesweeper(bot))