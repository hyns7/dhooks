from dhooks import Embed, Webhook

###
webhook_url = "<INSERT WEBHOOK URL HERE>"
###

client = Webhook(webhook_url)

# NOTE: Following code has a solid rundown of all methods
#       within the embed class.

em1 = Embed()

em1.color = 0x00FF00  # colors should be a hexadecimal value
em1.description = """This description supports
[named links](https://discord.com) as well.

``` \n
yes, even code blocks```
"""

em1.timestamp = "2018-04-30T05:34:26-07:00"

em1.set_author(
    name='Author Goes Here',
    icon_url='https://i.imgur.com/rdm3W9t.png',
    url='https://discord.com/'
)

em1.set_title(
    title='title ~~(did you know you can have markdown here too?)~~',
    url='https://discord.com/'
)

em1.add_field(
    name="Field 1 :smiley:",
    value="some of these properties have certain limits...",
    inline=False
)

em1.add_field(
    name="Field 2 😱",
    value="try exceeding some of them!",
    inline=False
)

em1.add_field(
    name="Field 3 🙄",
    value="Jokes, dont do that.",
    inline=False
)

em1.add_field("Field 4 🙄", "these last two")
em1.add_field("Field 5 🙄", "are inline fields")

em1.add_field('hello', 'bob')
# deletes the last field, supply an index, equivilant to em1.fields.pop(-1)
em1.del_field(-1)

em1.set_thumbnail('https://cdn.discordapp.com/embed/avatars/0.png')
em1.set_image('https://cdn.discordapp.com/embed/avatars/0.png')

em1.set_footer(
    text='Time Stamp is here =>',
    icon_url='https://cdn.discordapp.com/embed/avatars/0.png'
)

em2 = Embed(description='hey')

# you can send multiple embeds or a single embed.
client.send('hello there.', embeds=[em1, em2])
