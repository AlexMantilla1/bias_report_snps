from sys import argv
from config import MODELS
from config import INV_REG_DEFAULT
from config import LIST_FILE_NAME_DEFAULT


def get_devices_lines_from_file(file_name: str) -> str:
    # Read the scs file
    print("Reading the spectre netlist .scs file! ({})".format(file_name))
    with open(file_name, "r") as f:
        full_text = f.read()
        top_ckt = full_text.split("subckt")[-1]
        top_ckt = top_ckt.split("ends")[0]
        lines = top_ckt.split("\n")

    # Parse the file looking for devices with models.
    useful_lines = ""
    labels_found = []
    for mod in MODELS:
        for line in lines:
            # Get the lines with the models
            # and ignore all devices with label different that "M"
            if (mod in line) and (line[0] == "M" or line[0:2] == "SW"):
                info = line.split(" ")
                # Avoid to repeat instances (found 'nch_tgo5' in 'nch_tgo5_mac' definition)
                if info[0] in labels_found:
                    continue
                # expected: {device_label};{device_model};{invertion_region}
                device_line = "{};{};{}".format(info[0], mod, INV_REG_DEFAULT)
                useful_lines = useful_lines + device_line + "\n"
                labels_found.append(info[0])

    return useful_lines[:-1].split("\n")


def write_list_file(devices_info: str) -> None:
    print(
        "Writing the .csv file with device list! ({}) ".format(LIST_FILE_NAME_DEFAULT)
    )
    output_file = LIST_FILE_NAME_DEFAULT
    with open(output_file, "w") as f:
        f.write(devices_info)
    return


if __name__ == "__main__":
    # Get the netlist file name (spectre format)
    try:
        scs_file_name = argv[1]
    except:
        print("Error, no argment for scs file")
        quit()

    # Read the scs file to get all lines with device definition.
    devices_lines = get_devices_lines_from_file(scs_file_name)

    # Split M devices and SW devices
    devices_lines_M = list(filter(lambda x: x[0] == "M", devices_lines))
    devices_lines_SW = list(filter(lambda x: x[0:2] == "SW", devices_lines))
    # Sort the devices lines
    devices_lines_M = sorted(
        devices_lines_M, key=lambda x: int(x.split(";")[0].replace("M", ""))
    )
    devices_lines_SW = sorted(
        devices_lines_SW, key=lambda x: int(x.split(";")[0].replace("SW", ""))
    )
    for line_SW in devices_lines_SW:
        devices_lines_M.append(line_SW)

    # Write the list.csv file with the device lines
    write_list_file("\n".join(devices_lines_M) + "\n")
