from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

START_MANUAL = (
    "Hello from Performance Pickleball! Welcome to our vibrant community and here's what you can do with this bot:\n\n"
    "/aboutus: Want to know more about us? Read about our founders' story!\n"
    "/freemember: Become a member for free today!\n"
    "/web: Get a link to our website!\n"
    "/faq: See the questions that others asked most!"
)

FAQ_TEXT = (
    "📌 <b>Frequently Asked Questions</b>\n\n"
    "1. <b>How do I book a court?</b>\nDownload the Court Reserve App and book directly from there!\n\n"
    "2. <b>What are your operating hours?</b>\nWe’re open 9am–12am daily. We make 24h pickleball a possibility!\n\n"
    "3. <b>Can I cancel a booking?</b>\nCan’t make it to a session? No problem! Cancel 72 hours in advance, and you have three flexible options:\n"
    "  - Make-Up Class: Join another class.\n"
    "  - Class Banking: Save the session for later.\n"
    "  - Pause Option: Temporarily put your enrollment on hold.\n\n"
    "4. <b>Do you provide rental paddles/balls?</b>\nYes, we do! You can add them as part of your purchase when booking the court. Their prices are:\n"
    "  - paddles: $5 each per session\n"
    "  - balls: $5 per session for 3 balls\n\n"
    "5. <b>Where are you located?</b>\nSee our location on Google Maps: <a href='https://maps.app.goo.gl/VrhDVkzZ2ciaE4ZAA?g_st=com.google.maps.preview.copy'>📍 Click here</a>"
)

ABOUT_US = (
    "Here's the link to our story:\n <a href='https://www.performancepickleball.org/about-us'>Click here</a>"
)

BECOME_MEMBER = (
    "<b>Here are the steps to become a member:</b>\n"
    "1. <b>Download the <b>Court Reserve</b> app.</b> Link to download for "
    "<a href='https://apps.apple.com/us/app/courtreserve/id1392556575'>iOS</a> and "
    "<a href='https://play.google.com/store/apps/details?id=com.courtreserve&hl=en_SG&pli=1'>Android</a>\n\n"
    "2. Create your account by following the steps. When you reach the \"Join Organization\" page, search for Performance Pickleball. "
    "Pick your membership (Basic Dinker is free!)\n\n"
    "3. Set up a payment profile. From the home page, click on \"More\" at the bottom right of the screen > Payment Profiles > Create payment profile.\n\n"
    "4. And now you're all set! You can use <b>Court Reserve</b> to:\n"
    "  - <b>Book Courts</b>: Click on \"reserve\" slots to book your court time\n"
    "  - <b>Join Programs</b>: Participate in Open play, lessons, events and leagues"
)

TOKEN = '7395989430:AAG6fsOxuyQTPEhoIrUJYAmXdtSyxs7qVfI'

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_MANUAL)

# /faq command
async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💬 Ask something else", callback_data="ask_other")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(FAQ_TEXT, reply_markup=reply_markup, parse_mode="HTML", disable_web_page_preview=True)


# Ask something else callback
async def handle_ask_other_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query: CallbackQuery = update.callback_query
    await query.answer()

    await query.message.reply_text(
        "You can reach us directly at @maverickgrp or +65 8891 2037 on WhatsApp & Telegram! 💬",
        disable_web_page_preview=True,
        parse_mode="Markdown"
    )

# about-us
async def about_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_US, parse_mode="HTML", disable_web_page_preview=False)

# become-member
async def become_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BECOME_MEMBER, parse_mode="HTML", disable_web_page_preview=True)

# web
async def send_website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here's our official website: \nhttps://www.performancepickleball.org/", parse_mode="HTML", disable_web_page_preview=False)

# Run the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("faq", faq))
    app.add_handler(CommandHandler("aboutus", about_us))
    app.add_handler(CommandHandler("freemember", become_member))
    app.add_handler(CommandHandler("web", send_website))
    app.add_handler(CallbackQueryHandler(handle_ask_other_callback, pattern="ask_other"))
    app.run_polling()
