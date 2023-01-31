#!/usr/bin/env python3
"""
SÉRIE DE EXERCÍCIOS 3

A BD de um determinado clube de vídeos consiste de um ficheiro em 
formato CSV com os seguintes campos por linha: ID (numérico), 
título (texto), realizador (texto), género (texto), data e duração em
minutos. Linhas iniciadas com #, ; ou // são consideradas comentários 
e devem ser ignoradas. Linhas em branco ou apenas com pontos também 
devem ser ignoradas.
"""

import sys
import textwrap
from functools import partial
from itertools import chain
from datetime import datetime

import curses
from docopt import docopt

################################################################################
##   ARRANQUE DO SCRIPT
################################################################################

def main(argv=()):
    global movie_db, invalid_lines
    movie_db, invalid_lines = importDB()
    if len(argv) <= 1:
        curses.wrapper(startTextUI)
    else:
        execCmdLineOptions(sys.argv)

################################################################################
##   VARIÁVEIS E PARÂMETROS COMUNS ENTRE OS DOIS TIPOS DE INTERFACE
################################################################################

# A BD de filmes em memória e uma lista com as linhas corrompidas
movie_db = []
invalid_lines = []

################################################################################
##   INTERFACE COM UTILIZADOR UTILIZANDO A NOSSA MINI-API 
##   PARA A BIBLIOTECA CURSES (ver em baixo...)
################################################################################

def startTextUI(main_screen_):
    global main_screen
    try:
        main_screen = main_screen_
        initColors()
        execMainMenu(main_screen)
    except KeyboardInterrupt:
        showError("CTRL+C pressionado. O programa vai terminar!")
    except Exception as ex:
        showError("Erro inesperado: {}!".format(ex))
        raise


def execMainMenu(parent_screen):
    while True:
        initScreen(parent_screen)
        option = menu(
            title="CATÁLOGO",
            options=(
                ("E", "Exibir catálogo"),
                ("I", "Exibir linhas inválidas"),
                ("P", "Pesquisar catálogo"),
                ("T", "Terminar"),
            ),
        ) 
        if option == 'E':
            execShowCatalog(parent_screen)
        elif option == 'P':
            execSearchMenu(parent_screen)
        elif option == 'T':
            sys.exit(0)
        else:
            showError("Opção desconhecida")        


def execShowCatalog(parent_screen):
    catalog = catalogToText(movie_db) if movie_db else ["<CATÁLOGO VAZIO>"]
    pager("VÍDEOS EM CATÁLOGO:", catalog, width=80)


def execSearchMenu(parent_screen):
    while True:
        initScreen(parent_screen)
        option = menu(
            title="PESQUISAR CATÁLOGO",
            options=(
                ("1", "Pesquisar por título"),
                ("2", "Pesquisar por género"),
                ("3", "Pesquisar por ano"),
                ("4", "Pesquisar por realizador"),
                ("V", "Voltar ao menu anterior"),
                ("T", "Terminar"),
            ),
        )
        if option == '1':
            execSearchByTitle(parent_screen)
        elif option == '2':
            execSearchByGender(parent_screen)
        elif option == 'V':
            break
        elif option == 'T':
            sys.exit(0)
        else:
            showError("Opção desconhecida")        


def execSearchByTitle(parent_screen):
    execSearchQuery(
        parent_screen, 
        label='Título',
        found_msg="VÍDEOS COM TÍTULO: '{}'",
        not_found_msg="Não foram encontrados filmes com o título '{}'!",
        search_fn=searchByTitle
    )


def execSearchByGender(parent_screen):
    execSearchQuery(
        parent_screen, 
        label='Género',
        found_msg="VÍDEOS PARA O GÉNERO: '{}'",
        not_found_msg="Não foram encontrados filmes do género '{}'!",
        search_fn=searchByGenre
    )


def execSearchQuery(parent_screen, label, found_msg, not_found_msg, search_fn):
    initScreen(parent_screen)
    search = newScreen(length=3, width=40, color_pair='MENU')
    while True:        
        txt_input = acceptTextInput(search, label, 2, 2)
        if not txt_input:
            break
        search.addstr(3, 2, label)
        results = search_fn(movie_db, txt_input)
        if results:
            pager(found_msg.format(txt_input), catalogToText(results), width=80)
            initScreen(parent_screen)
            initScreen(search, color_pair='MENU')
        else:
            showInfo(not_found_msg.format(txt_input))
            initScreen(search, color_pair='MENU')


# TPC: ACABAR RESTANTES PESQUISAS!

################################################################################
##   INTERFACE COM UTILIZADOR UTILIZANDO A LINHA DE COMANDOS
################################################################################

def execCmdLineOptions(argv):
    script_name = argv[0].rpartition('/')[2]
    doc = """
BD de vídeos

Usage:
  {0} exibir
  {0} invalidas
  {0} pesquisar (-t TITULO | -g GENERO)

Options:
  -h --help     Mostra a ajuda.
  exibir        Exibe um resumo dos vídeos em catálogo do catálogo.
  invalidas     Exibe as linhas inválidas.
  -v --version         Mostra a versão.
""".format(script_name)
    args = docopt(doc, version='Versão 1')

    if args['exibir']:
        showCatalog(movie_db)

    elif args['invalidas']:
        showInvalidLines()

    elif args['pesquisar']:        
        showSearch(args)


def showCatalog(iterable):
    assert iterable
    for line in catalogToText(iterable):
        print(line)


def showSearch(args):
    if args['TITULO']:
        results = searchByTitle(movie_db, args['TITULO'])
    elif args['GENERO']:
        results = searchByGenre(movie_db, args['GENERO']) 
    else:
        raise ValueError('Critério de pesquisa não especificado.')

    if results:
        showCatalog(results)
    else:
        print('Não foram encontrados resultados para a pesquisa.')


def showInvalidLines():
    if invalid_lines:
        for line in invalid_lines:
            print(line)
    else:
        print("Não foram detectadas linhas inválidas.")


def catalogToText(iterable):
    assert movie_db
    yield from summaryTableHeader()
    for movie in iterable:
        genero = '/'.join(gen[:3] for gen in movie['generos'])
        yield "{:12} | {:30} | {:30}".format(                                            
            str(movie['data'].date()), 
            movie['titulo'], 
            genero,
        )


def summaryTableHeader():
    yield "{:^12} | {:^30} | {:^30}".format(
        "DATA", 
        "TÍTULO",
        "GÉNERO"
    )
    yield "-" * 80

################################################################################
##   GESTÃO DO CATÁLOGO DE VÍDEOS
################################################################################

# Parâmetros de formatação da BD em formato CSV
DELIM = ','
GENRES_DELIM = '/'
DATE_FMT = '%Y-%m-%d'


def searchByTitle(iterable, title):
    title = title.lower()
    results = (movie for movie in iterable if title in movie['titulo'].lower())
    return nonEmptyOrNone(results)


def searchByGenre(iterable, genre):
    genre = genre.lower()
    results = (movie 
               for movie in iterable 
               for genre_ in movie['generos'] if genre in genre_.lower())
    return nonEmptyOrNone(results)


def nonEmptyOrNone(iterator):
    try:
        elem = next(iterator)
    except StopIteration:
        return None
    else:
        return chain([elem], iterator)


def iterRelevantLines(iterable):
    for line in iterable:
        line = line.strip()
        if not line:
            continue
        if line[0] in ('#', ';') or line[:2] == '//':
            continue
        yield line


def importDB(db_file_name='bdvideos.txt', report_invalid_lines=False):
    movieDB = []
    invalid_lines = []
    with open(db_file_name) as fich:
        for line in iterRelevantLines(fich):
            try: 
                atributos = line.split(',')
                movieDB.append(makeMovie(atributos))
            except (ValueError, IndexError) as ex:
                if report_invalid_lines:
                    print("ERRO: Ocorreu um problema numa linha ->", line)
                    print(ex)
                invalid_lines.append(line)
    return movieDB, invalid_lines


def makeMovie(attrs):
    return {
        'id':              int(attrs[0]),
        'titulo':          attrs[1],
        'titulo_original': attrs[2],
        'director':        attrs[3],
        'generos':         attrs[4].split(GENRES_DELIM),
        'data':            datetime.strptime(attrs[5].strip(), DATE_FMT),
        'duracao':         int(attrs[6]),
    }

################################################################################
##   MINI-API PARA A BIBLIOTECA CURSES
################################################################################

# Cores da nossa aplicação
colors = {
    'SCREEN': (1, curses.COLOR_WHITE, curses.COLOR_BLUE),
    'MENU':   (2, curses.COLOR_RED, curses.COLOR_WHITE),
    'PAGER':  (3, curses.COLOR_RED, curses.COLOR_WHITE), 
    'ERROR':  (4, curses.COLOR_WHITE, curses.COLOR_RED),
    'INFO':   (5, curses.COLOR_WHITE, curses.COLOR_RED),
    'PUSHED_BUTTON': (6, curses.COLOR_RED, curses.COLOR_BLACK)
}

# Pequena pausa em ms para que alterações possam ser observadas
STANDARD_PAUSE = 100

WAIT_FOR_KEY_PRESS_MSG = "Pressione qualquer tecla para continuar..."

# Variável gloval que representa o ecrã principal
main_screen = None


def initColors():
    for color_spec in colors.values():
        curses.init_pair(*color_spec)


def colorPair(pair_key):
    return curses.color_pair(colors[pair_key][0])


def initScreen(screen, color_pair='SCREEN', cursor_visib=1):
    curses.curs_set(cursor_visib)
    screen.clear()
    screen.bkgd(' ', colorPair(color_pair))
    screen.box()
    screen.refresh()


def newScreen(x=2, y=5, length=20, width=40, color_pair='SCREEN', cursor_visib=1):
    screen = curses.newwin(length+2, width+2, y, x)
    initScreen(screen, color_pair, cursor_visib)
    return screen


def pause(screen, pause_delay=STANDARD_PAUSE):
    screen.refresh()
    curses.napms(pause_delay)


def waitForKeyPress(screen, x=None, y=None, msg=WAIT_FOR_KEY_PRESS_MSG):
    if x and y:
        screen.addstr(y, x, msg, curses.A_REVERSE)
    else:
        screen.addstr(msg, curses.A_REVERSE)
    prev_cursor_visib = curses.curs_set(0)
    screen.getkey()
    curses.curs_set(prev_cursor_visib)
    pause(screen)


def msgBox(msg, width, color_pair):
    """
               Top border
               Blank line
        Content (X lines)
               Blank line
                OK button
      +     Bottom border
    -----------------------
      X + 5 extra lines
    """
    curses.flash()
    lines = textwrap.wrap(msg, width=width)
    length = len(lines)
    screen = curses.newwin(length + 5, width + 5, 10, 10)
    initScreen(screen, color_pair=color_pair)
    for y, line in enumerate(lines, 2):
        screen.addstr(y, 2, line)
    screen.addstr(length + 3, 43, "  OK  ", curses.A_REVERSE)
    prev_cursor_visib = curses.curs_set(0)
    screen.getkey()
    screen.addstr(length + 3, 43, "  OK  ", colorPair('PUSHED_BUTTON'))
    pause(screen)
    curses.curs_set(prev_cursor_visib)
    main_screen.redrawwin()
    main_screen.refresh()


def showError(error_msg, width=50, length=1, color_pair='ERROR'):
    msgBox(error_msg, width, color_pair)


def showInfo(info_msg, width=50, length=4, color_pair='INFO'):
    msgBox(info_msg, width, color_pair)


def acceptOption(screen, x, y, options):
    option = None
    while True:
        screen.addstr(y, x, ">> ")
        option = screen.getkey().upper()
        if option in options:
            screen.addstr(y, x, ">> " + option)
            break
        pause(screen)
    pause(screen)
    return option


def acceptTextInput(screen, label, x, y, max_chars=20):
    label += ": "
    screen.addstr(y, x, label)
    prev_cursor_visib = curses.curs_set(2)
    curses.echo()
    screen.refresh()
    txt_input = screen.getstr(y, x + len(label), max_chars)
    curses.noecho()
    curses.curs_set(prev_cursor_visib)
    return txt_input.decode().strip()


def menu(options, title="", x=2, y=5, width=50):
    menu_ = newScreen(x, y, len(options)+4, width, color_pair='MENU')
    fmt = partial(str.format, "{:<20}")

    menu_.addstr(2, 2, fmt(title))
    for y, option in enumerate(options, 3):
        menu_.addstr(y, 2, fmt(option[0] + ". " + option[1]))

    option_cmds = [option[0].upper() for option in options]
    return acceptOption(menu_, 2, len(options) + 4, option_cmds)


def pager(title, text, x=2, y=2, width=50, length=20):
    pager_ = newScreen(x, y, length, width, color_pair='PAGER')
    pager_.addstr(1, 1, title)
    y = 2
    for line in text:
        pager_.addstr(y, 1, line[:width])
        if y % (length - 2) == 0:
            msg = "QUALQUER TECLA PARA AVANÇAR"
            waitForKeyPress(pager_, (width - len(msg))//2 - 2, length, msg)
            initScreen(pager_, color_pair='PAGER')
            pager_.addstr(1, 1, title)
            y = 2
        else:
            y += 1
    msg = "TODOS OS RESULTADOS EXIBIDOS"
    waitForKeyPress(pager_, (width - len(msg))//2 - 2, length, msg)
    pager_.refresh()


################################################################################

# Isto tem que ficar aqui para que tudo esteja definido antes 
# de se invocar o main

if __name__ == '__main__':
    main(sys.argv)

