import enchant


def convert_token_to_meaningful(token):
    d = enchant.Dict("en_US")
    if d.check(token):
        return token
    else:
        suggest_tokens = d.suggest(token)
        if suggest_tokens == []:
            return token
        elif len(suggest_tokens[0]) > 1:
            return suggest_tokens[0]
        return token
    
    
def convert_line_to_meaningful(line):
    out_tokens = []
    for token in line.split():
        out_token = convert_token_to_meaningful(token.lower())
        out_tokens.append(out_token)
    return ' '.join(out_tokens)
    

