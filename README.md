# han-english-reform
 
Just execute "score.py", enter your sentence, and you're good to go!

Explanation:

I am a Japanese language learner and have been for several years. It is consistently fun to share beginner's tips on reading the language with my friends. One of them is the function of Kanji, in that while Chinese is built on pseudo-symbolic characters, Japanese is only partially built this way. There are multiple scripts in Japanese: two phonetic, and one logographic. Often, in order to identify the phonetics of a word, a kanji (logographic) will be combined with a phonetic (always hiragana in this context). This is so that there is some level of understanding allowed from other languages, but phonetic integrity is kept. For English speakers, the following emoji analogy works best:


😃 ing -- (smiling)

😃 ppy - (happy)


Now, of course, there are distinctions between how the Chinese and Japanese use characters (手紙 means "letter" in Japanese and "toilet paper" in Chinese), but the point stands.

But what if English used this system?

I developed a Python script to do the majority of the leg work. For context, I'm using my own Han radical component system ( Han radical stand-ins for the Latin alphabet : neography (reddit.com) ) for the phonetic component, as Katakana does not include enough characters for the English language.

The program works like so:

I use a tokenization corpus to separate the words into their contextual parts of speech.

I then use a stemming system to determine what the root stem of a word is.

If a word is a noun, adjective, adverb, or verb, then I use the Simplified Chinese script to adapt the character. If it is too long, then I include the character(s) and use the remainder of a lemmatized version of the original word to add a phonetic component (such as "s", "ing", "ly", etc...)

All other words use Han and are phonetic.

Here are some example sentences and their components:

"It was the best of times, it was the worst of times."

它是大匚木人口人大匚目㇆时间大、它是大匚木人坏目㇆时间大。