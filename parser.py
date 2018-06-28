import sys

f= open("hello.html","r+")
parsed = f.read()

par = parsed.split('<tw-storydata')
par = par[1].split('</tw-storydata')
parsed = par[0]

parsed = parsed.replace('&quot;','"')

booleans = []
strings = []
avatarVars = []
seen = []
tokens = parsed.split(' ')


blocks = parsed.split('<tw-passagedata')
passages = []
parsed = ''
passages = []
newPassages = []

for i in range(1, len(blocks)):
    passages.append(blocks[i])


for passage in passages:
    passage = passage.replace('\n',' ')
    tokens = passage.split(' ')

    for tok in tokens:
        if 'Name' in tok:
            print(tok)
        tok = tok.replace('"','')
        if tok not in seen and '$' in tok :
            seen.append(tok)
            if 'Is' in tok or 'UserResponse' in tok or 'Flag' in tok:  
                booleans.append(tok)
            elif 'Avatar1Face' in tok or 'Avatar2Face' in tok or 'Avatar1Body' in tok or 'Avatar2Body' in tok or 'Avatar1Voice' in tok or 'Avatar2Voice' in tok or 'SceneRendering' in tok or 'SceneSound' in tok or 'NarratorSound' in tok or 'GUIScreen' in tok  :
                avatarVars.append(tok)
            else:
                strings.append(tok)



declarations = '//currentNode to be passed in as argument\nstring currentNode = "START";\n\n//to be populated...\n'
for string in strings:
    declarations = declarations + 'string ' + string.replace('$','') + ' = "";\n'
declarations = declarations + '\n//automatically generated code below...\nbool IsAvatarNode = false;\n'
for boolean in booleans:
    declarations = declarations + 'bool ' + boolean.replace('$','') + ' = false;\n'
declarations = declarations + '\nstring nextSentenceA2 = "";\nstring nextSentenceA1 = "";\nstring nextNode = "NONE";\n'
for var in avatarVars:
    declarations = declarations + 'string ' + var.replace('$','') + ' = "";\n'

passages = []
for i in range(1, len(blocks)):
    if '[[' not in blocks[i]:
        blocks[i] = blocks[i] + '\nnextNode = "NONE";\n'
    passages.append(blocks[i])

counter = 0
for passage in passages:
    flags = []
    passage = passage.replace('&quot;','"')
    passage = passage.replace('name=','\nname=')
    passage = passage.replace('tags=','\ntags=')
    passage = passage.replace('UserOptions','\nUserOptions')

    if 'tags="blue"' in passage:
        passage = passage.replace('Avatar1:\n',"\nnextSentenceA1 = ")
        passage = passage.replace('Avatar2:\n',"\nnextSentenceA2 = ")
    else:
        passage = passage.replace('">','">') 
    passage = passage.replace('</tw-passagedata>','')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    lines = passage.split('\n')
    newPassage = ''
    variables = []
    values = []
    Lvalues = []
    Uvalues = []
    Lvariables = []
    Uvariables = []
    n = 0 #number of userresponses
    UserResponses = []
    j = 0
    for line in lines:
        if line.startswith('#'):
            line = ''
        if 'pid="1"' in passage and 'name=' in line:
            line = 'name="START"'
        if 'pid=' in line:
            line = ''
        #establishes if the node is an output node
        if 'tags="blue"' in line:
            line = 'IsAvatarNode = true\n'+ line
        if 'tags="green"' in line:
            line = 'IsAvatarNode = false\n'+ line
        if 'tags="red"' in line:
            line = 'IsAvatarNode = false\n'+ line
            #print(line)
        #handles embedded variables in nextSentence text
        if 'nextSentence' in line:
            words = line.split(' ')
            line = ''
            for word in words:
                if '"$' in word:
                    word.replace('"$','')
                    word = word + ' + "'
                if '$' in word and '"' in word:
                    word = word.replace('$', '+ ')
                    word = word.replace('"','' )
                    word = '" ' + word
                if '$' in word and '"' not in word:
                    word = word.replace('$', '')
                    word = '" + ' + word + ' + "'
                line = line +' '+ word 
            line  = line.replace(' nextSentence', 'nextSentence')
        #collects initialized variables
        #deals with Avatar Nodes
        if 'tags="green"' in passage:
            if '[[' in line:
                line = line.replace('[[','"')
                line = line.replace(']]','"')
                line = 'currentNode = ' + line 
        if 'tags="blue"' in passage:
            if'(set:' in line:
                words = line.split(' ')
                variables.append(words[1].replace('$',''))
                values.append(words[3].replace(')',''))
                if '(if:' not in line:
                    line = ''
            #arrows
            if '[[' in line:
                line = line.replace('[[','"')
                line = line.replace(']]','"')
                line = 'nextNode = ' + line 
        #deals with Logic Nodes
        if 'tags="red"' in passage:
            if '$IsSpecific' in line:
                if '{}' in line:
                    line = 'IsSpecific = false;'
            if'UserOptions' in line:
                line = line.replace('UserOptions:','')
                line = line.replace(' ','')
                line = line.replace(' ','')
                line = line.replace(' ','')
                line = line.replace(' ','')
                numOfoptions = line
                print(numOfoptions)
                print(counter)
                counter = counter + 1
                line = ''
            if'$IsRandom' in line:
                print(line)
            if 'Flag' in line and '$' in line:
                line = line.replace(' is not ',' != ')
                line = line.replace(' is ',' == ')
                line = line.replace(' to ',' = ')
                words = line.split(' ')
                flags.append(words[4].replace('$',''))
                
            #stores number of user responses
            if line.startswith('UserResponse'):
                n = n + 1
                line = line.replace(':','')
                line = line.replace(' ','')
                line = line.replace(' ','')
                line = line.replace(' ','')
                UserResponses.append(line)
                line = ''
            
            #handles declarations
            if '(if:' not in line and '(set:' in line:
                words = line.split(' ')
                Lvariables.append(words[1].replace('$',''))
                Lvalues.append(words[3].replace(')',''))
                line = ''
            if '(if:' in line and '(set:' in line:
                line = line.replace('(if:','if(')
                line = line.replace(')','; }')
                line = line.replace('; }(set:', ' ){')
                line = line.replace(' is not ',' != ')
                line = line.replace(' is ',' == ')
                line = line.replace(' to ',' = ')
                line = line.replace('$','')
                if '"_value_"' in line:
                    words = line.split(' ')
                    line = words[5] + ' = true'
            if '(if:' in line:
                line = line.replace('[ [[', '{ currentNode = "')
                line = line.replace(']] ]', '"; }')
                line = line.replace('(if:','if(')
                line = line.replace('){', ' ){')
                line = line.replace(' is not ',' != ')
                line = line.replace(' is ',' == ')
                line = line.replace(' to ',' = ')
                line = line.replace('$','')
                if 'if( UserResponse' in line:
                    line = line.replace('if( UserResponse','if( IsConditional && UserResponse')
            
            if 'UIKeyboard' in line:
                str = ''
                UserResponse = UserResponses[j]
                j = j + 1
                for i in range(len(flags)):
                    if i == len(flags) - 1:
                        str = str + flags[i] 
                    else: 
                        str = str + flags[i] + ' && '
                str = 'if( ' + str + ' )' + '{ ' + UserResponse + ' = true; }'
                line = line + '\n' + str +'\n'
                flags = []
        newPassage = newPassage + line + '\n'
        newPassage = newPassage.replace('\n\n','\n')     

        #filling values
    
    

    statements = ''
    for i in range(len(variables)):
        statements = statements + variables[i] + ' = ' + values[i] + '\n'
    newPassage = newPassage + statements

    Lstatements = ''
    for i in range(len(Lvariables)):
        Lstatements = Lstatements + Lvariables[i] + ' = ' + Lvalues[i] + '\n'
    newPassage = Lstatements + newPassage 
    

    passage = newPassage
    newPassages.append(passage)
    

parsed = ''
for passage in newPassages:
    lines = passage.split('\n')
    passage = ''
    for line in lines:
        if 'name=' in line:
            nameLine = line + '\n'
            line  = ''

        passage = passage + line + '\n'
    passage = nameLine + passage 
    
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    lines = passage.split('\n')
    passage = ''
    for line in lines:
        if 'name=' in line:
            line = line.replace('name=', 'if( currentNode == ') + '){'
        else:
            line = '    ' + line
        if 'tags=' in line:
            line = ''
        if 'if(' not in line and ' = ' in line:
            line = line + ';'
        passage = passage + line + '\n'

    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')
    passage = passage.replace('\n\n','\n')

    passage = passage + '}\n\n'
    passage = passage.replace('_NextNodeTitle_','NONE')
    passage = passage.replace('_animationID_','NONE')

    lines = passage.split('\n')
    n = 0
    possibles = []
    for line in lines:        
        if 'if( IsConditional' in line:
            n = n + 1
            tokens = line.split('currentNode = ')
            toks = tokens[1].split(' ')
            tok = toks[0].replace(';','')
            if tok not in possibles:
                possibles.append(tok)

    parsed = parsed + passage + '\n'
        

endcondition = '		if (currentNode == "NONE") {\n			List<string> dialogueOutput = new List<string> ();\n			dialogueOutput.Add ("END");\n			dialogueOutput.Add ("END");\n			dialogueOutput.Add ("END");\n			dialogueOutput.Add ("END");\n			dialogueOutput.Add ("END");\n			dialogueOutput.Add ("END");\n			dialogueOutput.Add ("END");\n			dialogueOutput.Add ("END");\n			dialogueOutput.Add ("END");\n			return dialogueOutput;\n\n		}else {\n\n'    
endtext = '			//recurses if current node is not an output/avatar node\n			if (IsAvatarNode == false) {\n                dialogueInput [0] = currentNode;\n 				return GetNext (dialogueInput);\n			}\n			List<string> dialogueOutput = new List<string> ();\n\n			dialogueOutput.Add (nextNode);\n			dialogueOutput.Add (nextSentenceA1);\n			dialogueOutput.Add (nextSentenceA2);\n			dialogueOutput.Add (Avatar1Face);\n			dialogueOutput.Add (Avatar1Body);\n			dialogueOutput.Add (Avatar1Voice);\n			dialogueOutput.Add (Avatar2Face);\n			dialogueOutput.Add (Avatar2Body);\n			dialogueOutput.Add (Avatar2Voice);\n			dialogueOutput.Add (SceneRendering);\n			dialogueOutput.Add (SceneSound);\n			dialogueOutput.Add (NarratorSound);\n			dialogueOutput.Add (GUIScreen);\n			return dialogueOutput;\n		}\n	}\n}\n'
toptext = 'using System.Collections;\nusing System.Collections.Generic;\nusing UnityEngine;\n\npublic class Dialogue : MonoBehaviour {\n\n	// Use this for initialization\n	void Start () {\n\n	}\n\n	// Update is called once per frame\n	void Update () {\n	}\n\n	public List<string> GetNext(List<string> dialogueInput){\n\n'


#add indentation
decs = declarations.split('\n')
pars = parsed.split('\n')
declarations = ''
parsed = ''
for dec in decs:
    dec = '		' + dec
    declarations = declarations + dec + '\n' 
for par in pars:
    par = '		' + par
    parsed = parsed + par + '\n' 

parsed = toptext + declarations + endcondition + parsed + endtext

out = open("out.txt","w+")
out.write(parsed)

