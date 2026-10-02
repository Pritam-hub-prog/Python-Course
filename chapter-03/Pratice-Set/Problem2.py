letter = '''
           Dear <|name|>
           You are selected!
           <|Date|>
           '''

print(letter.replace("<|name|>", "Pritam").replace("<|Date|>", "18 Sept 2026"))