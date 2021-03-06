import begin
import time as t
import consolemanager
from universalFunctions import printSlow, scroll_text_up, clear_screen
from colored1 import *

console_info = ""
PADDINGNONE = consolemanager.Rectangle(0, 0, 1, 0)
PADDINGMIDDLE = consolemanager.Rectangle(0, 23, 1, 2)
PADDINGWIPEART = consolemanager.Rectangle(0, 0, 1, 18)


def titleScreen():
    "Function to create Ascii Art Main Menu."
    global console_info
    console = begin.console
    console_info = console.get_console_info()
    image = [
        "      _____        _____",
        "  ___|\    \   ___|\    \  _____      _____",
        " /    /\    \ |    |\    \ \    \    /    /",
        "|    |  |    ||    | |    | \    \  /    /",
        "|    |__|    ||    |/____/   \____\/____/",
        "|    .--.    ||    |\    \   /    /\    \ ",
        "|    |  |    ||    | |    | /    /  \    \ ",
        "|____|  |____||____| |____|/____/ /\ \____\ ",
        "|    |  |    ||    | |    ||    |/  \|    |",
        "|____|  |____||____| |____||____|    |____|",
        "  \(      )/    \(     )/    \(        )/",
        "   '      '      '     '      '        '",
    ]
    for line in image:
        console.set_cursor_pos(63, console_info.window_rectangle.bottom - 1)
        printSlow(line, 0.05, True, 0, PADDINGNONE)

    console.set_cursor_pos(51, console_info.window_rectangle.bottom - 1)
    printSlow(
        "A text based adventure game made by Vladimir with help from friends.",
        0.05,
        True,
        0,
        PADDINGNONE,
    )
    console.set_cursor_pos(57, console_info.window_rectangle.bottom - 1)
    printSlow(
        "- Inspired by Choose Your Own Adventure Books and D&D -",
        0.05,
        True,
        0,
        PADDINGNONE,
    )
    for row in range(14):
        t.sleep(0.05)
        scroll_text_up(PADDINGNONE)

    console.set_cursor_pos(59, 26)
    printSlow("[1. Start New Game] [2. Load Game] [3. Game Credit]", 0, False)
    console.set_cursor_pos(68, 27)
    introChoice = input(
        printSlow("Whats your choice, Adventurer? > ", 0, False))

    while introChoice != "1":

        if introChoice == "2" or introChoice == "3":
            console.set_cursor_pos(53, 29)
            printSlow(
                "That part of Arx isn't ready yet, try again in the next release!",
                1,
                False,
            )
            console.clear_line(29)
            console.clear_line(27)
            console.set_cursor_pos(68, 27)
            introChoice = input(
                printSlow("Whats your choice, Adventurer? > ", 0, False)
            )
        else:
            console.clear_line(27)
            console.set_cursor_pos(71, 27)
            introChoice = input(
                printSlow("I didn't catch that, Huh? > ", 0, False))

    t.sleep(0.5)
    clear_screen(PADDINGNONE, 0.05)
    createGameArea()


# █=►─═─═━═─═─◄=█
def createGameArea():
    console = begin.console
    console.set_cursor_pos(0, 22)
    printSlow(
        "█=►─═─═" + ("=" * (console_info.window_rectangle.right - 14)) + "═─═─◄=█",
        0,
        False,
        0.01,
    )
    console.set_cursor_pos(0, console_info.window_rectangle.bottom - 2)
    printSlow(
        "█=►─═─═" + ("=" * (console_info.window_rectangle.right - 14)) + "═─═─◄=█",
        0,
        False,
        0.01,
    )
    mountains()


def mountains():
    console = begin.console
    image = [
    "                                                                           ▄▀╙█,",
    "                                                                          @_  ▐██▄",
    "                                                                       ,Æ▀     ████▄",
    "                                                                     ▄▀`   ,    `████▄",
    "                                                                   ∞`    ██▀_    ▐████▄",
    "                                                                  ╜    ▄██'  ▄   _██████▄",
    "                                                     ,P_▀█▄,     `   ███▀'  ▄▀    ▐████████▄   a═▄",
    "                                                   ,²_ , ▀██████▌    ▀▀    ▐█⌐     _ _▀███████`  `██▄           ____ _____ __  __",
    "               ▄▄                                 ƒ_ ▄██  _▀▀████     e▀▀  ▐██▄        _██████    _▀███▄       / () \| () )\ \/ /     ╓▀▄,",
    "            ▄▀` _▀█▄▄                            ▄_  ███     ▐████      ▄█▄▄▄ _       ▐█▄█████▌     █████▄    /__/\__\_|\_\/_/\_\   ,╛_ ▐██▄",
    "          ╓' ▄▄   ▐███████▄,        ,.⌐▄,      ⌐`    ▀▄       _▀▀▀▌   ▄███████▀       _████████     _▀▀▀▀██▄                       r_,   █████",
    "        ,╜ ,,,▄   _▀█████████▄▄ ,⌐'_   _███`___      __           _  ▄▀_▄██▀_          ▐████████⌐ ▄      ████▄                  ¿'_ ▄▀,Γ __▀▀██▄",
    "      w²_  '''▀▀▀   _▀████▌▀█████▄,     _'██              ▄▄██▀▀    _`  _               █████████ `_     _█████▄             ¿²_   ▀▀▄▀     ▄▄▀▀█▄",
    "  .═`_   ,▄█          ▀▀▀  ▐███████       _`▀   `_  ,▄m═ⁿ▀'__                           _████████L        _▀███████▄▄  ,,,.²_    ,███_╓▌    ▀▀█▄▄'██▄",
    "`_  ╓▄█▀ ___   *~          ▀█████▀██         ▀▀Γ    __                  ▄███▀_ ▄▄,       ██████▀▌  ▀▀P─    ▐████████▀__          ▐██_▄█     ▐▄_▀█ `████▄▄▄",
    "     _  ,▄▄                 ▐██-_  '▀`                      ,         ▄██▀'_   ████▄     ▐▀'██▌╕  ▐        ▐███████▌             ██_¬█▀      ▀█ __ _▄,``▀▀███▄▄▄▄,,",
    "      ╙███▀_, ▀▀▀████▀▀`_    '_              `█`   ,▄▄▄▄████▀     ,▄███▀_     _██▀_▀██      _▀█   ▀█       ▐█████▌              ²_                   `████▄___▀▀▀▀▀▀▀▀▀▄,",
    "       _`_  └▀`                                  █▀▀▀▀___▄▄▄▄▄æN█████▀               __       ▀-   ▐█▄     _██▌██`                                    _▀▀█▀▀▀▌ ▄▄       _'",
    "                                                         ___      _                                 _▀█▌     _'▐█▌                                       _╕    __"
    ]
    yPos = 3
    for line in image:
        console.set_cursor_pos(0, yPos)
        printSlow(line, 0, False, 0.002)
        yPos += 1


'''
---------------------------------------
BELOW IS THE DRAW FUNCTIONS FOR Players
---------------------------------------
'''


def drawCommoner():
    console = begin.console
    i = fg("#ff0077")

    Commoner = [
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;137m██\x1b[38;5;137m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;137m██\x1b[38;5;137m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;137m██\x1b[38;5;137m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;137m██\x1b[38;5;137m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;137m██\x1b[38;5;137m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[0m",
        "\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;137m██\x1b[38;5;137m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[0m",
        "\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[0m",
        "\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;95m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;131m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;234m██\x1b[38;5;234m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;234m██\x1b[38;5;234m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;234m██\x1b[38;5;234m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;234m██\x1b[38;5;234m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
    ]

    yPos = 0
    for i in range(len(Commoner)):
        console.set_cursor_pos(35, yPos)
        printSlow(Commoner[i], 0, False, 0.00001)
        yPos += 1


def drawWarrior():
    console = begin.console
    i = fg("#ff0077")

    Warrior = [
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;137m██\x1b[38;5;137m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;137m██\x1b[38;5;137m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[0m",
        "\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[0m",
        "\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;221m██\x1b[38;5;221m██\x1b[0m",
        "\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;221m██\x1b[38;5;221m██\x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;58m██\x1b[38;5;58m██\x1b[38;5;94m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
    ]

    yPos = 0
    for i in range(len(Warrior)):
        console.set_cursor_pos(35, yPos)
        printSlow(Warrior[i], 0, False, 0.00001)
        yPos += 1


def drawMage():
    console = begin.console
    i = fg("#ff0077")

    Mage = [
        "\x1b[38;5;94m██\x1b[38;5;94m██\x1b[38;5;94m██\x1b[38;5;94m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;94m██\x1b[38;5;94m██\x1b[38;5;94m██\x1b[38;5;94m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;94m██\x1b[38;5;94m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;94m██\x1b[38;5;94m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;94m██\x1b[38;5;94m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;83m██\x1b[38;5;83m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;83m██\x1b[38;5;83m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;94m██\x1b[38;5;94m██\x1b[38;5;130m██\x1b[38;5;130m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;83m██\x1b[38;5;83m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;83m██\x1b[38;5;83m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;94m██\x1b[38;5;94m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;94m██\x1b[38;5;94m██\x1b[0m",
        "\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[0m",
        "\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[0m",
        "\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;166m██\x1b[38;5;166m██\x1b[38;5;215m██\x1b[38;5;215m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;94m██\x1b[38;5;94m██\x1b[0m",
        "\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;166m██\x1b[38;5;166m██\x1b[38;5;215m██\x1b[38;5;215m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;94m██\x1b[38;5;94m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;94m██\x1b[38;5;94m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;94m██\x1b[38;5;94m██\x1b[0m",
        "\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;94m██\x1b[38;5;94m██\x1b[0m",
        "\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;53m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;94m██\x1b[38;5;94m██\x1b[0m",
    ]

    yPos = 0
    for i in range(len(Mage)):
        console.set_cursor_pos(35, yPos)
        printSlow(Mage[i], 0, False, 0.00001)
        yPos += 1


def drawThief():
    console = begin.console
    i = fg("#ff0077")

    Thief = [
        "\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;174m██\x1b[38;5;174m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;174m██\x1b[38;5;174m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;254m██\x1b[38;5;254m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;254m██\x1b[38;5;254m██\x1b[0m",
        "\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;124m██\x1b[38;5;124m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;251m██\x1b[38;5;251m██\x1b[0m",
        "\x1b[38;5;160m██\x1b[38;5;160m██\x1b[38;5;124m██\x1b[38;5;124m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;251m██\x1b[38;5;251m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;174m██\x1b[38;5;174m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m  \x1b[38;5;15m  \x1b[38;5;254m██\x1b[38;5;254m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;174m██\x1b[38;5;174m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;216m  \x1b[38;5;15m  \x1b[38;5;254m██\x1b[38;5;254m██\x1b[0m",
        "\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;240m██\x1b[38;5;240m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;240m██\x1b[38;5;240m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[0m",
        "\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;240m██\x1b[38;5;240m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;180m██\x1b[38;5;180m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;240m██\x1b[38;5;240m██\x1b[38;5;216m██\x1b[38;5;216m██\x1b[0m",
        "\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;52m██\x1b[38;5;52m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;124m██\x1b[38;5;124m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;160m██\x1b[38;5;160m██\x1b[0m",
        "\x1b[38;5;216m██\x1b[38;5;216m██\x1b[38;5;52m██\x1b[38;5;52m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;124m██\x1b[38;5;124m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;160m██\x1b[38;5;160m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;240m██\x1b[38;5;240m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;249m██\x1b[38;5;249m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;240m██\x1b[38;5;240m██\x1b[38;5;243m██\x1b[38;5;243m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;249m██\x1b[38;5;249m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
    ]

    yPos = 0
    for i in range(len(Thief)):
        console.set_cursor_pos(35, yPos)
        printSlow(Thief[i], 0, False, 0.00001)
        yPos += 1


def drawPaladin():
    console = begin.console
    i = fg("#ff0077")

    Paladin = [
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;252m██\x1b[38;5;252m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;252m██\x1b[38;5;252m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;252m██\x1b[38;5;252m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;252m██\x1b[38;5;252m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;252m██\x1b[38;5;252m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;252m██\x1b[38;5;252m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;252m██\x1b[38;5;252m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;247m██\x1b[38;5;247m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;252m██\x1b[38;5;252m██\x1b[0m",
        "\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[0m",
        "\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[0m",
        "\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;166m██\x1b[38;5;166m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;166m██\x1b[38;5;166m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;166m██\x1b[38;5;166m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;9m██\x1b[38;5;9m██\x1b[38;5;220m██\x1b[38;5;220m██\x1b[38;5;252m██\x1b[38;5;252m██\x1b[38;5;166m██\x1b[38;5;166m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;52m██\x1b[38;5;52m██\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;52m██\x1b[38;5;52m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;52m██\x1b[38;5;52m██\x1b[38;5;208m██\x1b[38;5;208m██\x1b[38;5;52m██\x1b[38;5;52m██\x1b[38;5;88m██\x1b[38;5;88m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;237m██\x1b[38;5;237m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
    ]

    yPos = 0
    for i in range(len(Paladin)):
        console.set_cursor_pos(35, yPos)
        printSlow(Paladin[i], 0, False, 0.00001)
        yPos += 1


'''
----------------------------------------
BELOW IS THE DRAW FUNCTIONS FOR MONSTERS
----------------------------------------
'''


def drawSkeleton():
    console = begin.console
    i = fg("#ff0077")

    Skeleton = [
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;195m██\x1b[38;5;195m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;251m██\x1b[38;5;251m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;195m██\x1b[38;5;195m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;0m██\x1b[38;5;0m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;251m██\x1b[38;5;251m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;195m██\x1b[38;5;195m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;251m██\x1b[38;5;251m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;195m██\x1b[38;5;195m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;254m██\x1b[38;5;251m██\x1b[38;5;251m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;195m██\x1b[38;5;195m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;195m██\x1b[38;5;195m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;246m██\x1b[38;5;246m██\x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m██\x1b[38;5;15m██\x1b[0m",
        "\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m██\x1b[38;5;15m██\x1b[0m",
        "\x1b[38;5;238m██\x1b[38;5;238m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;253m██\x1b[38;5;253m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m██\x1b[38;5;15m██\x1b[0m",
        "\x1b[38;5;238m██\x1b[38;5;238m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;253m██\x1b[38;5;253m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m██\x1b[38;5;15m██\x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m██\x1b[38;5;15m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
        "\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;15m  \x1b[38;5;255m██\x1b[38;5;255m██\x1b[38;5;15m  \x1b[38;5;15m  \x1b[0m",
    ]
    yPos = 0
    for i in range(len(Skeleton)):
        console.set_cursor_pos(87, yPos)
        printSlow(Skeleton[i], 0, False, 0.00001)
        yPos += 1
