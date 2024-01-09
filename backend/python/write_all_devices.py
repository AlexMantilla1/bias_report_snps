from sys import argv
from config import MODELS
from config import WEAK_INV_REG_VALID_OPTIONS
from config import STRONG_INV_REG_VALID_OPTIONS
from config import LIST_FILE_NAME_DEFAULT
from config import OUTPUT_FILE_NAME_DEFAULT
from device_class import Device


def nice_print(lines):
    for line in lines:
        print(line)


def read_lines_from_list_file() -> list:
    # Reading the list file
    print(
        "Reading the .csv list file ({}) to create the outputs .csv file ({})".format(
            LIST_FILE_NAME_DEFAULT, OUTPUT_FILE_NAME_DEFAULT
        )
    )
    with open(LIST_FILE_NAME_DEFAULT, "r") as f:
        lines = []
        # Lets avoid any blank space
        for line in f.readlines():
            if " " in line:
                lines.append(line.replace(" ", ""))
            else:
                lines.append(line)
        return lines


if __name__ == "__main__":
    try:
        csv_output_file_name = argv[1]
    except:
        print("Error, no argment for the output file")
        quit()

    # Read the lines from the list.csv file
    lines = read_lines_from_list_file()

    # For each line define a device object
    devices_list = []
    for i in range(len(lines)):
        line = lines[i]
        # Split information in line by ';' char
        info = line.split(";")
        device_label = info[0]
        device_model = info[1]
        device_inv_reg = info[2][:-1]

        # Check readed info from the LIST_FILE_NAME_DEFAULT.csv:
        if not (device_model in MODELS):
            print("Error reading the ", LIST_FILE_NAME_DEFAULT, "file!!")
            print(i + 1, " -> ", line)
            print("Error: the readed model (" + device_model + ") is not supported!")
            print("Please see config file.")
            print("MODELS = ", MODELS)
            quit()
        elif (not (device_inv_reg in WEAK_INV_REG_VALID_OPTIONS)) and (
            not (device_inv_reg in STRONG_INV_REG_VALID_OPTIONS)
        ):
            print("Error reading the ", LIST_FILE_NAME_DEFAULT, "file!!")
            print(i + 1, " -> ", line)
            print(
                "Error: the readed device inversion region ("
                + device_inv_reg
                + ") is not supported!"
            )
            print("Please see config file.")
            print("WEAK_INV_REG_VALID_OPTIONS = ", WEAK_INV_REG_VALID_OPTIONS)
            print("STRONG_INV_REG_VALID_OPTIONS = ", STRONG_INV_REG_VALID_OPTIONS)
            quit()

        device_temp = Device(device_label, device_model, device_inv_reg)
        devices_list.append(device_temp)

    # Sort the devices_list by label
    devices_list = sorted(devices_list, key=lambda x: x.id)

    # Save previous info from write file (from the .sh file, not from previous runs)
    with open(OUTPUT_FILE_NAME_DEFAULT, "r") as f:
        meta_info = f.read()

    # Write the bias_all_devices.csv
    print("Writing the outputs .csv file! ({})".format(OUTPUT_FILE_NAME_DEFAULT))
    with open(OUTPUT_FILE_NAME_DEFAULT, "w") as f:
        f.write(meta_info + "\n")
        for device in devices_list:
            output_text = device.info_csv
            f.write(output_text + "\n")
