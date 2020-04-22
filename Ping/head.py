import random
import colors

def main_header():
    header_1 = r"""
    

        &&&&&&&&&&&&&&&&&&   &&    &&&&&&          &&   &&&&&&&&&&&&&&&&&
        &&              &&   &&    &&  &&          &&   &&             &&
        &&              &&   &&    &&   &&         &&   &&             &&
        &&              &&   &&    &&    &&        &&   &&             &&
        &&              &&   &&    &&     &&       &&   &&             &&
        &&&&&&&&&&&&&&&&&&   &&    &&      &&      &&   &&   &&&&&&&&&&&&
        &&                   &&    &&       &&     &&   &&
        &&                   &&    &&        &&    &&   &&
        &&                   &&    &&         &&   &&   &&
        &&                   &&    &&          &&  &&   &&
        &&                   &&    &&           && &&   &&
        &&                   &&    &&            &&&&   &&&&&&&&&&&&&&&&&

        """

    header_2 = r"""


        _________________
        ||             ||  ||  ||\\          ||  ||============||
        ||             ||  ||  || \\         ||  ||            ||
        ||             ||  ||  ||  \\        ||  ||            ||
        ||             ||  ||  ||   \\       ||  ||            ||
        ||_____________||  ||  ||    \\      ||  ||      ======||
        ||                 ||  ||     \\     ||  ||
        ||                 ||  ||      \\    ||  ||
        ||                 ||  ||       \\   ||  ||
        ||                 ||  ||        \\  ||  ||
        ||                 ||  ||         \\ ||  ||
        ||                 ||  ||          \\||  ||==============


        """

    hdr_num=random.randint(1,2)
    if hdr_num ==1:
        print(colors.color.PURPLE+ header_1 + colors.color.ENDC)
        print(colors.color.GREEN + "To exit press Ctrl + c" + colors.color.ENDC)
    if hdr_num ==2:
        print(colors.color.CYAN + header_2 + colors.color.ENDC)
        print(colors.color.GREEN + "To exit press Ctrl + C" + colors.color.ENDC)