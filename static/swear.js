function validateForm() {
  var question = document.forms["myForm"]["question"].value.toLowerCase();
  var answer = document.forms["myForm"]["answer"].value.toLowerCase();
  var swear_words = ["arse", "arsehole", "as useful as tits on a bull", "balls", "bastard", "beaver", "beef curtains", "bell", "bellend", "bent", "berk", "bint", "bitch", "blighter", "blimey", "blimey o'reilly", "bloodclaat", "bloody", "bloody hell", "blooming", "bollocks", "bonk", "bugger", "bugger me", "bugger off", "built like a brick shit-house", "bukkake", "bullshit", "cack", "cad", "chav", "cheese eating surrender monkey", "choad", "chuffer", "clunge", "cobblers", "cock", "cock cheese", "cock jockey", "cock-up", "cocksucker", "cockwomble", "codger", "cor blimey", "corey", "cow", "crap", "crikey", "cunt", "daft", "daft cow", "damn", "dick", "dickhead", "did he bollocks!", "did i fuck as like!", "dildo", "dodgy", "duffer", "fanny", "feck", "flaps", "fuck", "fuck me sideways!", "fucking cunt", "fucktard", "gash", "ginger", "git", "gob shite", "goddam", "gorblimey", "gordon bennett", "gormless", "he’s a knob", "hell", "hobknocker", "I'd rather snort my own cum", "jesus christ", "jizz", "knob", "knobber", "knobend", "knobhead", "ligger", "like fucking a dying man's handshake", "mad as a hatter", "manky", "minge", "minger", "minging", "motherfucker", "munter", "muppet", "naff", "nitwit", "nonce", "numpty", "nutter", "off their rocker", "penguin", "pillock", "pish", "piss off", "piss-flaps", "pissed", "pissed off", "play the five-fingered flute", "plonker", "ponce", "poof", "pouf", "poxy", "prat", "prick", "prick", "prickteaser", "punani", "punny", "pussy", "randy", "rapey", "rat arsed", "rotter", "scrubber", "shag", "shit", "shite", "shitfaced", "skank", "slag", "slapper", "slut", "snatch", "sod", "sod-off", "son of a bitch", "spunk", "stick it up your arse!", "swine", "taking the piss", "tits", "toff", "tosser", "trollop", "tuss", "twat", "twonk", "u fukin wanker", "wally", "wanker", "wankstain", "wazzack", "whore"];

  for (var i = 0; i < swear_words.length; i++) {
    if (question.includes(swear_words[i]) || answer.includes(swear_words[i])) {
      alert("Question or answer contains the word, `" + swear_words[i] + "` which cannot be used in this website.");
      return false;
    }
  }

  return true;
}