from litellm import completion
import os 


# prompt used for the task of sentiment analysis
prompt= """You are an agent with the task of sentiment analysis. and you are given a file with lines of movie review. Your task is to get the sentiment analysis of each of those reviews.
The sentiment of the reviews can be one of the following :
positive, neutral and negative.

<examples>
input :
An awful film! It must have been up against some real stinkers to be nominated for the Golden Globe. They've taken the story of the first famous female Renaissance painter and mangled it beyond recognition. My complaint is not that they've taken liberties with the facts; if the story were good, that would perfectly fine. But it's simply bizarre -- by all accounts the true story of this artist would have made for a far better film, so why did they come up with this dishwater-dull script? I suppose there weren't enough naked people in the factual version. It's hurriedly capped off in the end with a summary of the artist's life -- we could have saved ourselves a couple of hours if they'd favored the rest of the film with same brevity.
After the success of Die Hard and it's sequels it's no surprise really that in the 1990s, a glut of 'Die Hard on a .....' movies cashed in on the wrong guy, wrong place, wrong time concept. That is what they did with Cliffhanger, Die Hard on a mountain just in time to rescue Sly 'Stop or My Mom Will Shoot' Stallone's career.<br /><br />Cliffhanger is one big nit-pickers dream, especially to those who are expert at mountain climbing, base-jumping, aviation, facial expressions, acting skills. All in all it's full of excuses to dismiss the film as one overblown pile of junk. Stallone even managed to get out-acted by a horse! However, if you an forget all the nonsense, it's actually a very lovable and undeniably entertaining romp that delivers as plenty of thrills, and unintentionally, plenty of laughs.<br /><br />You've got to love John Lithgows sneery evilness, his tick every box band of baddies, and best of all, the permanently harassed and hapless 'turncoat' agent, Rex Linn as Travers.<br /><br />He may of been Henry in 'Portrait of a Serial Killer' but Michael Rooker is noteworthy for a cringe-worthy performance as Hal, he insists on constantly shrieking in painful disbelief at his captors 'that man never hurt anybody' And whilst he surely can't be, it really does look like Ralph Waite's Frank character is grinning as the girl plummets to her death.<br /><br />Mention too must go to former 'London's Burning' actor Craig Fairbrass as the Brit bad guy, who comes a cropper whilst using Hal as a Human Football, yes, you can't help enjoy that bit, Hal needed a good kicking.<br /><br />So forget your better judgement, who cares if 'that could never happen', lower your acting expectations, turn up the volume and enjoy! And if you're looking for Qaulen, he's the one wearing the helicopter.	

output:
negative
positive

</examples>
also note that the you are supposed to ignore all html tags which appear in the input and they contribute nothing to the score



"""
def sentiment_analyser(input_file):
  response = completion(
    model='gpt-4o',
    messages=[
      {"role": 'system', "content": f"{prompt}"},
       {"role": 'user', "content": f"{input_file}"}
    ],
    api_key=os.getenv('OPENAI_API_KEY'),
    max_tokens=10
  )
  return response 
