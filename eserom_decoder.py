# Dictionary mapping eserom to plaintext
eserom_dict = {
    #CHARS
    "10":"A",
    "0111":"B",
    "0101":"C",
    "011":"D",
    "1":"E",
    "1101":"F",
    "001":"G",
    "1111":"H",
    "11":"I",
    "1000":"J",
    "010":"K",
    "1011":"L",
    "00":"M",
    "01":"N",
    "000":"O",
    "1001":"P",
    "0010":"Q",
    "101":"R",
    "111":"S",
    "0":"T",
    "110":"U",
    "1110":"V",
    "100":"W",
    "0110":"X",
    "0100":"Y",
    "0011":"Z",

    # NUMS
    "00000":"0",
    "10000":"1",
    "11000":"2",
    "11100":"3",
    "11110":"4",
    "11111":"5",
    "01111":"6",
    "00111":"7",
    "00011":"8",
    "00001":"9",

}

# Function to decode given eserom string
def decode_eserom(eserom):
    output_str = ""
    ese_frags = eserom.split(" ")
    for frag in ese_frags:
        if frag == "":
            output_str += " "
        else:
            # Validate valid fragments.
            try:
                output_str += eserom_dict[frag]
            except:
                print("Error: Invalid Character in Input, please enter a valid eserom string.")

    return output_str


if __name__ == "__main__":
    print("Eserom Decoder")
    eserom = input("Input Eserom String:")
    print(decode_eserom(eserom))
