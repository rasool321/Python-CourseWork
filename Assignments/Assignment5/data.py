# ================= Backend Data =================

# Fake DB (includes free, premium, and content users)
db = {
    "rasool@gmail.com": {"password": "1234", "type": "free"},
    "siri@gmail.com":   {"password": "abcd", "type": "premium"},
    "artist@gmail.com": {"password": "xyz",  "type": "content"}
}

# Songs Database grouped by Artist
songs_db = {
    "The Weeknd": [
        "Blinding Lights", "Save Your Tears", "Starboy", "The Hills", "Can't Feel My Face",
        "In the Night", "Earned It", "I Feel It Coming", "After Hours", "Reminder"
    ],
    "Anirudh": [
        "Why This Kolaveri Di", "Arabic Kuthu", "Vaathi Coming", "Chellamma", "Don’t Worry Da",
        "Jalabulajangu", "So Baby", "Nee Partha Vizhigal", "Kadhal Kan Kattudhe", "Surviva"
    ],
    "Thaman": [
        "Butta Bomma", "Ala Vaikunthapurramuloo Theme", "Samajavaragamana", "Leharaayi", "Blockbuster"
    ],
    "DSP": [
        "Srivalli", "Oo Antava", "Ringa Ringa", "Seeti Maar", "Top Lesi Poddi",
        "Aa Ante Amalapuram", "Jagadam Theme", "Nuvvostanante", "Chaila Chaila", "Pakka Local"
    ],
    "BRO": [
        "Apocalypse", "K.", "Sweet", "Nothing’s Gonna Hurt You Baby", "Heavenly"
    ]
}
