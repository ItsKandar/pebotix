require('dotenv').config(); //initializes dotenv
const Discord = require('discord.js'); //imports discord.js

const client = new Discord.Client({intents:[
    Discord.GatewayIntentBits.Guilds,
    Discord.GatewayIntentBits.GuildMessages
]}); //creates new clients

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

// Commands
client.on('message', msg => {
    if (msg.content === 'ping') {
      msg.reply('Pong!');
    }
});

//this line must be at the very end
client.login(process.env.RE_TOKEN); //signs the bot in with token