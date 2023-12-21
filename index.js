require('dotenv/config'); //initializes dotenv

const path = require('node:path');
const fs = require('node:fs');
const { RE_TOKEN } = require('.env');
const { Client,GatewayIntentBits } = require('discord.js'); //imports discord.js
const eventHandler = require("")

const client = new Client({
    intents:[
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.GuildMembers,
        GatewayIntentBits.MessageContent,
    ],
}); //creates new clients

module.exports = client; //exports the client

client.commands = new Collection();
const commandsPath = path.join(__dirname, 'commands');
const commandFiles = fs.readdirSync(commandsPath).filter(file => file.endsWith('.js'));
const eventsPath = path.join(__dirname, 'events');
const eventFiles = fs.readdirSync(eventsPath).filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
    const filePath = path.join(commandsPath, file);
    const command = require(`${commandsPath}/${file}`);
    client.commands.set(command.data.name, command);
}

client.once(Events.ClientReady, client => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on(Events.InteractionCreate, async interaction => {
    const command = client.commands.get(interaction.commandName);
    try {
        await command.execute(interaction);
    }
    catch(error) {
        console.error(error);
        await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
    }
});

//this line must be at the very end
//Well no, it doesn't have to be at the very end, but it's best practice to put it at the end
client.login(RE_TOKEN); //Logs the bot with the token