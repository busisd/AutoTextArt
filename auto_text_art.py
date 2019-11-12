from PIL import Image
import sys

dot_size = [4,4]
char_pixel_size = [dot_size[0]*2, dot_size[1]*4]
# char_pixel_size = [8, 16]

def fit_image_to_text(old_img):
	'''
		Returns an image based off the given image. The new image has
		width and height divisible by the sizes defined in 
		char_pixel_size, with the old image copied onto the
		top left.
	'''
	
	new_img_width = old_img.size[0]
	if new_img_width % char_pixel_size[0] != 0:
		new_img_width += char_pixel_size[0] - (new_img_width % char_pixel_size[0])
	
	new_img_height = old_img.size[1]
	if new_img_height % char_pixel_size[1] != 0:
		new_img_height += char_pixel_size[1] - (new_img_height % char_pixel_size[1])
	
	new_img = Image.new("RGB", (new_img_width, new_img_height), color = (255, 255, 255))
	new_img.paste(old_img)
	return new_img

def get_avg_color(img, box = None):
	'''
		Given an image, calculates the average color of every pixel
		in the image in the region given by box. If box is None,
		averages the entire image.
		
		box = (x_start, y_start, width, height)
	'''
	
	if box is None:
		box = (0,0,img.size[0],img.size[1])
	
	total_pixels = 0
	total_color = [0,0,0]
	
	for x in range(box[0],box[0]+box[2]):
		for y in range(box[1],box[1]+box[3]):
			total_pixels += 1
			cur_pixel = img.getpixel((x, y))
			for i in range(len(total_color)):
				total_color[i] += cur_pixel[i]
			
	avg_color = [i/total_pixels for i in total_color]
	return(avg_color)

def img_block_to_dot(img, color_bound, x_start, y_start):
	'''
		Given an image and a start location, returns whether or not 
		that dot of a braille character should be filled in.
		
		Returns true if should be filled, false otherwise.
	'''
	
	dot_avg_color = get_avg_color(img, (x_start, y_start, dot_size[0], dot_size[1]))
	dot_avg = sum(dot_avg_color)/len(dot_avg_color)
	bound_avg = sum(color_bound)/len(color_bound)
	
	return dot_avg < bound_avg
	
exp_order=[0, 1, 2, 6, 3, 4, 5, 7]
def img_block_to_braille(img, color_bound, x_start, y_start):
	'''
		Given an image and a start location, returns a braille character
		that best fits that region of the image. For each 1/8 portion of
		the braille character, fills it in if the pixel is < color_bound
		and doesn't if pixel is >= color_bound.
	'''
	
	final_ord = 0
	cur_exp = 0
	for x in range(x_start, x_start+char_pixel_size[0], dot_size[0]):
		for y in range(y_start, y_start+char_pixel_size[1], dot_size[1]):
			if img_block_to_dot(img, color_bound, x, y):
				final_ord += 2**exp_order[cur_exp]
			cur_exp += 1
	return chr(final_ord + ord('⠀'))

def img_to_braille(img):
	'''
		Given an image, converts it to a text representation in braille.
	'''
	
	out_str = ""
	avg_color = get_avg_color(img)
	fit_img = fit_image_to_text(img)
	for y in range(0, fit_img.size[1], char_pixel_size[1]):
		for x in range(0, fit_img.size[0], char_pixel_size[0]):
			out_str += img_block_to_braille(fit_img, avg_color, x, y)
		out_str += "\n"
		
	fit_img.close()
	return out_str


'''
⠉⡛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣸⡀⡀⡀⡀⠄⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡀⡀⡀⡀⡀⠄⠄⠉⠛⠿⢿⣿⣿⣿⣿⡿⠿⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿
⣿⡀⡀⡀⡀⡀⡀⡀⡀⡀⠄⠉⢉⣴⠏⠉⢁⡀⡀⠄⠄⠄⠄⠄⣄⠄⣸
⣯⡀⡀⠄⠄⠄⠄⠄⠄⢀⣴⣶⡤⠿⢉⡀⡀⡀⡀⡀⡀⡀⠄⠄⢠⡄⣸
⣿⣿⣷⣤⣀⠄⠄⠄⣠⣾⣿⣿⣧⠄⠄⠄⠄⠄⡀⡀⡀⡀⠠⢀⣾⢟⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣧⡀⠄⠄⠄⢀⣀⣷⣽⣴⣋⣥⣾⣿⣿
⣿⣿⣿⣿⣿⢟⣿⣿⣿⡿⠋⠄⠄⠉⠉⠉⠒⠲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⡿⠋⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡋⠄⣀⢀⣤⣤⣌⣁⣀⣀⡀⡀⠄⠄⠄⠘⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣾⣿⣿⣶⣾⣿⣿⣿⣾⣷⣶⣶⣶⣦⣄⣨⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
'''

def invert_braille_char(braille_char):
	'''
		Given a braille unicode character, converts it into the opposite
		braille unicode character (all dots are blank and all blanks are
		dots).
	'''
	
	old_char_normalized = ord(braille_char) - ord('⠀')
	if (old_char_normalized < 0 or old_char_normalized > 255):
		raise ValueError(braille_char+" is not a valid braille character")
	new_char_normalized = old_char_normalized ^ 255
	return chr(new_char_normalized + ord('⠀'))
	
def invert_braille_string(braille_string):
	'''
		Given a string of braille and non-braille characters,
		return a string that is identical except all braille
		characters are inverted.
	'''
	
	out_str = ""
	for cur_char in braille_string:
		new_char = cur_char
		char_normalized = ord(cur_char) - ord('⠀')
		
		if (char_normalized >= 0 and char_normalized <= 255):
			new_char = invert_braille_char(cur_char)
		
		out_str += new_char
	
	return out_str

def clean_braille_spaces(braille_string, blank_char = " "):
	'''
		Given a string of braille and non-braille characters,
		replaces all instance of the "empty" braille character
		with the given character. (Text editors may display the empty 
		braille symbol as thinner than other braille characters, so it 
		may be preferable to replace is with a sparse braille character
		or a space).
		
		Optional argument: blank_char, the char to replace blanks with.
		Defaults to a space.
	'''
	out_str = ""
	for cur_char in braille_string:
		if cur_char == "⠀": #empty braille
			out_str += blank_char
		else:
			out_str += cur_char
		
	return out_str
	
def make_art(filename, blank_char = " "):
	'''
		Given a filename, converts it to a braille text-art.
		
		Replaces blanks in the output with the given 
		blank_char, defaults to space.
	'''
	
	img_in = Image.open(filename)
	with open("output_"+filename.split(".")[0]+".txt", 'w') as out_file:
		out_str = img_to_braille(img_in)
		out_file.write(clean_braille_spaces(out_str, blank_char))
		out_file.write("\r\n")
		out_file.write(clean_braille_spaces(invert_braille_string(out_str), blank_char))
	img_in.close()


def main():	
	if (len(sys.argv) < 2):
		print("Proper usage: python3 auto_text_art.py filename [blank_char]")
		return
	filename = sys.argv[1]
	
	blank_char = " "
	if ((len(sys.argv)) > 2):
		blank_char = sys.argv[2]
		
	make_art(filename, blank_char)

if __name__=="__main__":
	main()
