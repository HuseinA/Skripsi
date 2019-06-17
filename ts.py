import pickle
a={'Closer':['Rock'], 'I Surrender Dear':['Jazz'], 'Six To Four':['Jazz'], 'Wow':['Hip Hop'], 'All The Way':['Jazz'], 'Bartier Cardi':['Hip Hop'], 
'Know Your Enemy':['Rock'], 'Two Years Of Torture':['Jazz','Pop'], "Doin' It Right":['Electronic','Pop'], 'You Make Me Feel So Young':['Jazz','Pop'], 
'Remind Me':['Hip Hop'], 'Headlight':['Pop'], 'Slime':['Hip Hop'], 'Tragic Endings':['Hip Hop'], 'Man of the Woods':['Pop'], 'Good Times Bad Times':['Rock'], 
'Whole Lotta Love':['Rock'], 'Tell Me':['Rock'], 'Wait':['Pop','Rock','Hip Hop'], 'Instant Crush':['Electronic','Pop'], 'The Worst Crime':['Electronic','Rock'],
'I Wish I Were In Love Again':['Jazz','Pop'], 'Fragments of Time':['Electronic','Pop'], 'I Like It':['Hip Hop','Pop','Electronic'], 'Poison Heart':['Electronic','Rock','Pop'], 
'Sing Me to Sleep':['Electronic','Pop','Hip Hop'], 'Something In The Way':['Rock'], 'Force':['Electronic'], 'Legendary Child':['Rock'],
'Old Shoes [& Picture Postcards]':['Jazz','Pop','Rock'], 'The Spectre':['Electronic','Pop'], 'Murder City':['Rock'], 'Wave':['Pop'], 'Together':['Pop'], 
'Closing Time':['Jazz','Pop','Rock'], 'HERO':['Pop'], 'Before The Lobotomy':['Rock'], "Breezin'":['Jazz'], 'Ready For It':['Pop','Electronic','Hip Hop'], 
'You Know Youre Right':['Rock'], 'I Do':['Hip Hop'], 'You Move':['Electronic','Rock'], 'Just One Of Those Things':['Jazz','Pop'], 'This Masquerade':['Jazz'],
"Don't Let The Sun Catch You Cryin'":['Jazz','Pop'], 'Smells Like Teen Spirit':['Rock'], 'Best 4 You':['Pop'], 
'Another Reflection':['Hip Hop','Electronic','Jazz'], 'Motorcycle':['Hip Hop'], 'Stairway To Heaven':['Rock'], 'Sauce':['Pop'], 'Come as you are':['Rock'], 
'I Did Something Bad':['Pop','Electronic','Hip Hop'], 'Give Life Back to Music':['Electronic','Pop'], 'Girls Like You':['Pop','Electronic','Hip Hop'], 'Morning Light':['Pop'], 
'Let The Good Times Roll':['Jazz','Pop'], 'River':['Hip Hop'], 'Going Backwards':['Electronic','Pop','Rock'], 'A Day by Atmosphere Supreme':['Hip Hop','Electronic','Jazz'], 
'Heat':['Hip Hop'], 'The Final View':['Hip Hop','Electronic','Jazz'], 'Drip':['Hip Hop'], 'Tired':['Electronic','Pop','Hip Hop'], "Don’t Blame Me":['Pop','Electronic','Hip Hop'], 'Help Me Out':['Pop','Electronic'], 'So This Is Love':['Jazz'],
'Rock And Roll':['Rock'], 'Poorman':['Electronic','Rock'], 'The Game of Love':['Electronic','Pop'],

'Black Dog':['Rock'],
'Beautiful':['Rock'],
'Affirmation':['Jazz'],
'Within':['Electronic','Pop'],
'Best Life':['Hip Hop'],
'Lonely':['Jazz','Pop','Rock'],
'Cover Me':['Electronic','Pop','Rock'],
'Kumomi':['Hip Hop','Electronic','Jazz'],
'Higher Higher':['Pop'],
'Where Are You':['Pop','Jazz'],
'There_s No You':['Jazz'],
'No Peace':['Hip Hop'],
'Delicate':['Pop','Electronic','Hip Hop'],
'Witchcraft':['Jazz','Pop'],
'See The Light':['Rock'],
'Beyond':['Electronic','Pop'],
'Bet My Heart':['Pop'],
'Framed':['Hip Hop'],
'Alone':['Electronic','Pop','Hip Hop'],
'End Game':['Pop','Electronic','Hip Hop'],
'21 Guns':['Rock','Pop'],
'Lord Forgive Me':['Hip Hop'],
'Lady':['Jazz'],
'So Much Love':['Electronic','Rock','Pop'],
'Come Rain Or Come Shine':['Jazz','Pop'],
'Faded':['Electronic','Pop','Hip Hop'],
'Bodak Yellow':['Hip Hop'],
'fly':['Pop'],
'Kashmir':['Rock'],
'Drain You':['Rock'],

'adagio':['Classic'],
'arioso':['Classic'],
'fur elise':['Classic'],
'gymnopedie no 1':['Classic'],
'gymnopedie no 2':['Classic'],
'la flamande':['Classic'],
'les baricades misterieuses':['Classic'],
'march from the magic flute':['Classic'],
'moonlight sonata movement 1':['Classic'],
'pathetique sonata movement 2':['Classic'],
'piano sonata k 310 mvt 1':['Classic'],
'piano sonata k 545 mvt 1':['Classic'],
'piano sonata k 545 mvt 2':['Classic'],
'rondo from piano sonata no 58':['Classic'],
'sonata in g minor mvt 1':['Classic'],
'sonata in g minor mvt 2':['Classic'],
'song without words':['Classic'],
'the entertainer rag':['Classic'],
'the peace patrol':['Classic'],
'twopart invention in e':['Classic'],
}
pickle.dump(a,open('databin/multilabelclasstes.p','wb'))
#b=pickle.load(open('songclass.p','rb'))
"""res={'Hip Hop':0,'Pop':0,'Electronic':0,'Rock':0,'Jazz':0,'Classic':0}
n=0
for x in a.values():
    #n+=1
    if x in res:
        res[x]+=1
    else:
        for y in x:
                res[y]+=1
print[res]"""
#b=pickle.load(open('databin/latih6010.p','rb'))
#print([x for x in b if x[4]=='You Know Youre Right'])

#x=pickle.dump({'Best 4 You':'Pop','Girls Like You':'Pop','Help Me Out':'Pop','Wait':'Pop','Hero':'Pop','Nirvana - Come as you are':'Rock','Nirvana - Drain_You':'Rock','Nirvana - Smells Like Teen Spirit':'Rock','Nirvana - Something In The Way':'Rock','Nirvana - You Know Youre Right':'Rock'},open('man.p','wb'))
