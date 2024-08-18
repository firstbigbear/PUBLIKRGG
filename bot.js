const { Telegraf, Markup } = require('telegraf');
const cc = require('cryptocompare');

const cryptocompare_API_key = 'a3025b6d7a2472633c9b5345b9228dbd';
cc.setApiKey(cryptocompare_API_key);

const bot = new Telegraf('6789972418:AAENfEGvgOrJDySlYvV4YAOxBsBxiwhqhFY');

const channel_1_button = Markup.inlineKeyboard([
  Markup.button.url('freeairdropland1', 'https://t.me/freeairdropland1')
]);

const launch_button = Markup.inlineKeyboard([
  Markup.button.url('دریافت کلید🔑', 'https://t.me/Hamsterfrkeysbot/Key')
]);

const CHANNEL_NAME = '@freeairdropland1';

async function isUserMember(userId) {
  try {
    const member = await bot.telegram.getChatMember(CHANNEL_NAME, userId);
    return ['member', 'administrator', 'creator'].includes(member.status);
  } catch (error) {
    console.error(`Error: ${error}`);
    return false;
  }
}

bot.start(async (ctx) => {
  const userId = ctx.from.id;
  if (await isUserMember(userId)) {
    ctx.reply('برای استفاده از ربات لطفا در کانال زیر عضو شوید\n\nپس از عضویت بر روی /join کلیک کنید', channel_1_button);
  } else {
    ctx.reply('رای استفاده از ربات لطفا در کانال زیر عضو شوید\n\nپس از عضویت بر روی /join کلیک کنید', channel_1_button);
  }
});

bot.command('join', async (ctx) => {
  const userId = ctx.from.id;
  if (await isUserMember(userId)) {
    ctx.reply('🇬🇧This Bot Provides Hamster Kombat 3d bike Key Codes For Free\n\n🇮🇷این ربات بصورت رایگان کد های کلید همستر را در اختیار شما قرار میدهد.\n\n🇷🇺 Этот робот бесплатно предоставит вам коды ключей хомяка.\n\nCoded by @freeairdropland1', launch_button);
  } else {
    ctx.reply('شما هنوز عضو نشدید');
  }
});

bot.launch();
