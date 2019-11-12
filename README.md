# AutoTextArt
A python program that converts images into text

When called from the command line on an image, will convert that image into a version of that image using text.
Specifically, uses the UTF-8 braille symbols to draw the image. Because the blank-braille symbol displays thinner
than other symbols in some contexts, gives the option to replace that symbol with a given other symbol.

For example, the program could be run with the following command:

python3 auto_text_art.py crab.jpg ⢀

and, given the crab.jpg file included in this repository, outputs:

```
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀
⢀⢀⢀⢀⢀⣀⣴⣾⡿⠛⠋⠋⢀⢀⢀⢀⠈⠙⠛⢿⣷⣦⣄⡀⢀⢀⢀⢀⢀
⢀⢀⢀⢔⣿⣿⣿⣏⣠⣤⣶⠆⢀⢀⢀⢀⠰⢶⣤⣄⣹⣿⣿⣿⣷⡄⢀⢀⢀
⢀⢠⣷⣿⣿⣿⣿⣿⠿⠋⢀⢀⢀⢀⢀⢀⢀⢀⠙⠻⣿⣿⣿⣿⣿⣿⡆⢀⢀
⢀⡼⣿⣿⣿⣿⠟⠁⢀⣀⢀⢀⢀⢀⢀⢀⢀⢀⣀⢀⠈⠻⢿⣿⣿⣿⣧⡀⢀
⢀⣷⣿⣿⡇⢀⢀⢀⣈⣿⣷⣤⣤⣤⣤⣤⣤⣾⣿⣁⢀⢀⢀⢸⣿⣿⣿⠃⢀
⢀⠘⢿⣿⣿⣿⣶⣿⣟⢿⣿⣟⣻⣹⣿⣿⣿⣿⡿⣻⣿⣶⣿⣿⣿⡿⠋⢀⢀
⢀⢀⢀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡿⠛⠁⢀⢀⢀⢀
⢀⢀⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣦⡀⢀⢀
⣰⣿⠟⠉⣤⣴⣾⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣷⣦⣤⡉⠻⣿⣦⢀
⣿⠃⢀⣼⡟⠋⣠⣾⠟⣱⣿⠛⠻⠿⠿⠟⠛⢿⣯⠻⣷⣤⠉⢻⣷⡀⠈⣿⢀
⠈⢀⠸⣿⠃⢀⣿⡇⢀⣿⣧⣀⢀⢀⢀⢀⣀⣸⣿⠁⠘⣿⡆⠈⣿⡇⢀⠁⢀
⢀⢀⢀⠻⢀⠸⣿⡁⢀⠙⢿⣿⡧⢀⢀⢸⣿⡿⠏⢀⢀⣿⠇⢀⠟⢀⢀⢀⢀
⢀⢀⢀⢀⢀⢀⢀⠉⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠉⢀⢀⢀⢀⢀⢀⢀⢀
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠿⠋⠁⢀⣤⣴⣴⣿⣿⣿⣿⣷⣦⣤⡀⠈⠙⠻⢿⣿⣿⣿⣿⣿
⣿⣿⡿⡫⢀⢀⢀⠰⠟⠛⠉⣹⣿⣿⣿⣿⣏⡉⠛⠻⠆⢀⢀⢀⠈⢻⣿⣿⣿
⣿⡟⠈⢀⢀⢀⢀⢀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⢀⢀⢀⢀⢀⢀⢹⣿⣿
⣿⢃⢀⢀⢀⢀⣠⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣷⣄⡀⢀⢀⢀⠘⢿⣿
⣿⠈⢀⢀⢸⣿⣿⣿⠷⢀⠈⠛⠛⠛⠛⠛⠛⠁⢀⠾⣿⣿⣿⡇⢀⢀⢀⣼⣿
⣿⣧⡀⢀⢀⢀⠉⢀⠠⡀⢀⠠⠄⠆⢀⢀⢀⢀⢀⠄⢀⠉⢀⢀⢀⢀⣴⣿⣿
⣿⣿⣿⣷⣤⡀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠁⢀⢀⢀⢀⣤⣾⣿⣿⣿⣿
⣿⡿⠛⠉⠉⠁⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠈⠉⠉⠙⢿⣿⣿
⠏⢀⣠⣶⠛⠋⠁⣀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣀⠈⠙⠛⢶⣄⢀⠙⣿
⢀⣼⣿⠃⢠⣴⠟⠁⣠⠎⢀⣤⣄⣀⣀⣠⣤⡀⠐⣄⠈⠛⣶⡄⠈⢿⣷⢀⣿
⣷⣿⣇⢀⣼⡿⢀⢸⣿⢀⠘⠿⣿⣿⣿⣿⠿⠇⢀⣾⣧⢀⢹⣷⢀⢸⣿⣾⣿
⣿⣿⣿⣄⣿⣇⢀⢾⣿⣦⡀⢀⢘⣿⣿⡇⢀⢀⣰⣿⡿⢀⣸⣿⣠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
```

The output looks better with monospaced fonts.
