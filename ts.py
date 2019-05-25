import pickle
a={'Closer':'Rock', 'I Surrender Dear':'Jazz', 'Six To Four':'Jazz', 'Wow':'Hip Hop', 'All The Way':'Jazz', 'Bartier Cardi':'Hip Hop', 
'Know Your Enemy':'Rock', 'Two Years Of Torture':'Jazz', "Doin' It Right":'Electronic', 'You Make Me Feel So Young':'Jazz', 
'Remind Me':'Hip Hop', 'Headlight':'Pop', 'Slime':'Hip Hop', 'Tragic Endings':'Hip Hop', 'Man of the Woods':'Pop', 'Good Times Bad Times':'Rock', 
'Whole Lotta Love':'Rock', 'Tell Me':'Rock', 'Wait':'Pop', 'Instant Crush':'Electronic', 'The Worst Crime':'Electronic',
'I Wish I Were In Love Again':'Jazz', 'Fragments of Time':'Electronic', 'I Like It':'Hip Hop', 'Poison Heart':'Electronic', 
'Sing Me to Sleep':'Electronic', 'Something In The Way':'Rock', 'Force':'Electronic', 'Legendary Child':'Rock',
'Old Shoes (& Picture Postcards)':'Jazz', 'The Spectre':'Electronic', 'Murder City':'Rock', 'Wave':'Pop', 'Together':'Pop', 
'Closing Time':'Jazz', 'HERO':'Pop', 'Before The Lobotomy':'Rock', "Breezin'":'Jazz', 'Ready For It':'Pop', 
'You Know Youre Right':'Rock', 'I Do':'Hip Hop', 'You Move':'Electronic', 'Just One Of Those Things':'Jazz', 'This Masquerade':'Jazz',
"Don't Let The Sun Catch You Cryin'":'Jazz', 'Smells Like Teen Spirit':'Rock', 'Best 4 You':'Pop', 
'Another Reflection':'Hip Hop', 'Motorcycle':'Hip Hop', 'Stairway To Heaven':'Rock', 'Sauce':'Pop', 'Come as you are':'Rock', 
'I Did Something Bad':'Pop', 'Give Life Back to Music':'Electronic', 'Girls Like You':'Pop', 'Morning Light':'Pop', 
'Let The Good Times Roll':'Jazz', 'River':'Hip Hop', 'Going Backwards':'Electronic', 'A Day by Atmosphere Supreme':'Hip Hop', 
'Heat':'Hip Hop', 'The Final View':'Hip Hop', 'Drip':'Hip Hop', 'Tired':'Electronic', "Don’t Blame Me":'Pop', 'Help Me Out':'Pop', 'So This Is Love':'Jazz',
'Rock And Roll':'Rock', 'Poorman':'Electronic', 'The Game of Love':'Electronic',

'Black Dog':'Rock',
'Beautiful':'Rock',
'Affirmation':'Jazz',
'Within':'Electronic',
'Best Life':'Hip Hop',
'Lonely':'Jazz',
'Cover Me':'Electronic',
'Kumomi':'Hip Hop',
'Higher Higher':'Pop',
'Where Are You':'Pop',
'There_s No You':'Jazz',
'No Peace':'Hip Hop',
'Delicate':'Pop',
'Witchcraft':'Jazz',
'See The Light':'Rock',
'Beyond':'Electronic',
'Bet My Heart':'Pop',
'Framed':'Hip Hop',
'Alone':'Electronic',
'End Game':'Pop',
'21 Guns':'Rock',
'Lord Forgive Me':'Hip Hop',
'Lady':'Jazz',
'So Much Love':'Electronic',
'Come Rain Or Come Shine':'Jazz',
'Faded':'Electronic',
'Bodak Yellow':'Hip Hop',
'fly':'Pop',
'Kashmir':'Rock',
'Drain You':'Rock',

'adagio':'Classic',
'arioso':'Classic',
'fur elise':'Classic',
'gymnopedie no 1':'Classic',
'gymnopedie no 2':'Classic',
'la flamande':'Classic',
'les baricades misterieuses':'Classic',
'march from the magic flute':'Classic',
'moonlight sonata movement 1':'Classic',
'pathetique sonata movement 2':'Classic',
'piano sonata k 310 mvt 1':'Classic',
'piano sonata k 545 mvt 1':'Classic',
'piano sonata k 545 mvt 2':'Classic',
'rondo from piano sonata no 58':'Classic',
'sonata in g minor mvt 1':'Classic',
'sonata in g minor mvt 2':'Classic',
'song without words':'Classic',
'the entertainer rag':'Classic',
'the peace patrol':'Classic',
'twopart invention in e':'Classic',
}
#pickle.dump(a,open('databin/songclass.p','wb'))
"""b=pickle.load(open('songclass.p','rb'))
res={'Hip Hop':0,'Pop':0,'Electronic':0,'Rock':0,'Jazz':0}
for x in b:
    if b[x] in res:
        res[b[x]]+=1
print(b)"""

res={'Hip Hop':[1,0],'Pop':[3,0],'Electronic':[10,0],'Rock':[230,0],'Jazz':[30,0],'Classic':[12,0]}
a=[[v[0],k] for k,v in res.items()]
a.sort(reverse=True)
print(a[:3])


#b=pickle.load(open('databin/latih6010.p','rb'))
#print([x for x in b if x[4]=='You Know Youre Right']) 

#x=pickle.dump({'Best 4 You':'Pop','Girls Like You':'Pop','Help Me Out':'Pop','Wait':'Pop','Hero':'Pop','Nirvana - Come as you are':'Rock','Nirvana - Drain_You':'Rock','Nirvana - Smells Like Teen Spirit':'Rock','Nirvana - Something In The Way':'Rock','Nirvana - You Know Youre Right':'Rock'},open('man.p','wb'))
