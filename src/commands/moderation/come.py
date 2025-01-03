from highrise import User, Position
from config.config import messages, permissions


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "come"
        self.description = "Teleport a player to a specific position"
        self.aliases = ['come']
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        if user.id not in permissions.owners:
            return await self.bot.highrise.send_whisper(user.id, f"This command is owner only command")
        else:
            response = await self.bot.highrise.get_room_users()
            your_pos = None
            for content in response.content:
                if content[0].id == user.id:
                    if isinstance(content[1], Position):
                        your_pos = content[1]
                        break
            if not your_pos:
                await self.bot.highrise.send_whisper(user.id, f"{messages.invalidPosition}")
                return

            await self.bot.highrise.chat(f"@{user.username} I'm coming ..")
            await self.bot.highrise.walk_to(your_pos)
