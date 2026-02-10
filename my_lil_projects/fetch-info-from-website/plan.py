"""
Plano:
    ver como pdfkit transforma websites em html

    depois de analisar alguns sites, há diferente situações de mostrar resultados:
        . há alguns divs com class "ftp-folder" e tabelas escondidas de "ftp-folder-content"
        . há só tabela com tabelas continua
        . há alguns links para sites exteriores 
        . vai logo para site exterior, mas com tabela igual a original
        . há tabela com diferentes divisões, com divisão inicial não aquela que eu preciso
        . há divisões com ftp-folder só que depois vem um pdf em vez de uma tabela
        
        . todas tabelas são bootstrap (bom)

        . tabelas guardam row em tr, por isso dá para extrair row completa com bs4
        . quando há ftp-folder com pdf, pdf link esta contido dentro de iftame tag e da para conseguir link
        . no table, é preciso usar selenium para clicar. Maioria dot rabalho se calhar sera feito pelo bs4
        . para aceder a ftp-folder e tabela usar bs4

    criar código para diferentes situações:
        . ftp-folder:
            . divisão certa (escalões)
            . divisão errada
            . pdf
        . tabela:
            . divisão certa (escalões)
            . divisão errada 
        . site exterior (geralmente multicrono.com):
            . tabela
            . ???
    
    o que para usar:
        . ftp-folder : selenium para clicar
        . divisão errara : selenium para clicar
        . pdf : tentar conseguir link da pdf e usar pdfplumber
        . tabela : bs4 para retirar <tr>
    
    mostrar a prova
    retirar distâncias da prova

    
    criar menu
    criar tambem código para casos especificos?
    
    

    
    
    
"""
