# White Red Orange Yellow Green Cyan Blue Magenta Lavender Pearl
import os
import sys
import argparse


colors = ["White", "Red", "Orange", "Yellow", "Green", "Cyan", "Blue", "Magenta", "Lavender", "Pearl"]
sd_path = "/Volumes/STS"

def operation():
    print()
    selected_op = input("[E]ncode / [D]ecode / [Q]uit: ")
    print()
    print("-" * 15)
    if selected_op.lower() == "d":
        decode()
    elif selected_op.lower() == "e":
        encode()
    elif selected_op.lower() == "q":
        quit()
    else:
        print("Invalid Operation")
    operation()

def decode():
    folders = os.listdir(sd_path)
    new_list = []
    unmatched = []
    print("Decoding folder names...")
    for f in folders:
        f_path = sd_path + "/" + f
        split_name = f.split(" ")
        if os.path.isdir(f_path) and len(split_name) > 2:
            index = split_name[0].split("-")
            try:
                color_index = colors.index(index[0])
                if (len(index) > 1):
                    mult = int(index[1]) * 10
                else:
                    mult = 0
                final_index = color_index + mult
                final_name = f.replace(split_name[0], str(final_index).zfill(2))
                new_list.append(final_name)
                final_path = sd_path + "/" + final_name
                os.rename(f_path, final_path)
            except ValueError:
                unmatched.append(f)
                pass
    print("Finished decoding.")
    print("-" * 15)
    print("\nDecoded:\n")
    for n in sorted(new_list):
        print(n)
    print()
    print("-" * 15)
    print("\nUnmatched:\n")
    for u in sorted(unmatched):
        print(u)
    print("-" * 15)



def encode():
    folders = os.listdir(sd_path)
    new_list = []
    unmatched = []
    print("Encoding folder names...")
    for f in folders:
        f_path = sd_path + "/" + f
        split_name = f.split(" ")
        if os.path.isdir(f_path) and len(split_name) > 2:
            try:
                index = int(split_name[0])
                if index < 90:
                    color_index = index % 10
                    mult = int((index - color_index) / 10)
                    final_color = colors[color_index]
                    if mult > 0:
                        final_color = final_color + "-" + str(mult)
                    final_name = f.replace(split_name[0], final_color)
                    new_list.append(final_name)
                    final_path = sd_path + "/" + final_name
                    os.rename(f_path, final_path)
            except ValueError:
                unmatched.append(f)
                pass
    print("Finished encoding.")
    print("-" * 15)
    print("\nEncoded:\n")
    # print("-" * 15)
    for n in sorted(new_list):
        print(n)
    print()
    print("-" * 15)
    print("\nUnmatched:\n")
    for u in sorted(unmatched):
        print(u)
    print("-" * 15)



if __name__ == "__main__":
    
    print("\nSTS_RENAMER\nFolder renamer for the 4MS STS module\nDeveloped by Icaro Ferre\n")

    parser = argparse.ArgumentParser()
    parser.add_argument("-op", type=str, default="",help="Operation")
    args = parser.parse_args()
    
    if args.op == "encode":
        encode()
    elif args.op == "decode":
        decode()
    else:
        operation()
    

