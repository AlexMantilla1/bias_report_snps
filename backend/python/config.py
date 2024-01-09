MODELS = [
    "nld24_g5_iso_mac",
    "nch_tgo5_mac_hvnwnbl_od3_6t",
    "nch_tgo5_mac",
    "nch_tgo5",
    "pch_tgo5_mac",
    "pch_tgo5",
    "pa28_g5_mac",
]
""" MODELS:
The get_devices_from_csv.py script looks for the MOS modelds listed @ MODELS
to grab them and list the devices created with this models at the spectre .scs netlist file.
"""

#############################################################################################################
#############################################################################################################

INV_REG_DEFAULT = "STRONG_INV"
""" INV_REG_DEFAULT:
For this version, all devices are assumed to be bias at the inversion region described by INV_REG_DEFAULT.
To change this for a specfic device, go to the list.csv file and change the third colum of the desired device
with a value from INV_REG_VALID_OPTIONS 
"""

WEAK_INV_REG_VALID_OPTIONS = ["WEAK_INV", "WEAK_INVERSION", "WEAK"]
STRONG_INV_REG_VALID_OPTIONS = ["STRONG_INV", "STRONG_INVERSION", "STRONG"]
""" INV_REG_VALID_OPTIONS:
For this version, all devices are assumed to be biased at the inversion region described by INV_REG_DEFAULT.
To change this for a specfic device, go to the list.csv file and change the third colum of the desired device
with a value from WEAK_INV_REG_VALID_OPTIONS or STRONG_INV_REG_VALID_OPTIONS
"""

LIST_FILE_NAME_DEFAULT = "list.csv"
""" LIST_FILE_NAME_DEFAULT:
This is the default name for the file that list all the devices from the spectre .scs netlist file
the expected format for this csv file is:
{device_label} ; {device_model} ; {invertion_region}
"""

OUTPUT_FILE_NAME_DEFAULT = "bias_all_devices.csv"
""" OUTPUT_FILE_NAME_DEFAULT:
This is the default name for the output.csv file, this file contains the expresions for the custom compiler
"""

#############################################################################################################
#############################################################################################################

MARK_DEVICE_LABEL_CSV = "--MXX--"
""" MARK_DEVICE_LABEL_CSV:
The Device class will look for the mark described by MARK_DEVICE_LABEL_CSV @ the core file
to replace it with the transistor label to build the bias_all_devices.csv
"""

MARK_WEAK_INV_LOWER_CSV = "--MWIL--"
""" MARK_WEAK_INV_LOWER_CSV:
The Device class will look for the mark described by MARK_WEAK_INV_LOWER_CSV @ the core file
to replace it with the BIAS_WEAK_INV_LOWER_MARGIN_V value to build the bias_all_devices.csv
"""

MARK_WEAK_INV_UPER_CSV = "--MWIU--"
""" MARK_WEAK_INV_UPER_CSV:
The Device class will look for the mark described by MARK_WEAK_INV_UPER_CSV @ the core file
to replace it with the BIAS_WEAK_INV_UPER_MARGIN_V value to build the bias_all_devices.csv
"""

MARK_WEAK_INV_SAT_CSV = "--MWIS--"
""" MARK_WEAK_INV_SAT_CSV:
The Device class will look for the mark described by MARK_WEAK_INV_SAT_CSV @ the core file
to replace it with the BIAS_WEAK_INV_SAT_MARGIN_V value to build the bias_all_devices.csv
"""

MARK_STRONG_INV_LOWER_CSV = "--MSIL--"
""" MARK_STRONG_INV_LOWER_CSV:
The Device class will look for the mark described by MARK_STRONG_INV_LOWER_CSV @ the core file
to replace it with the BIAS_STRONG_INV_LOWER_MARGIN_V value to build the bias_all_devices.csv
"""

MARK_STRONG_INV_SAT_CSV = "--MSIS--"
""" MARK_STRONG_INV_SAT_CSV:
The Device class will look for the mark described by MARK_STRONG_INV_SAT_CSV @ the core file
to replace it with the BIAS_STRONG_INV_SAT_MARGIN_V value to build the bias_all_devices.csv
"""

#############################################################################################################
#############################################################################################################

BIAS_WEAK_INV_LOWER_MARGIN_V = "-250m"
""" BIAS_WEAK_INV_LOWER_MARGIN_V:
Is the lower margin allowed to bias a device at weak inversion region.
This can be edited here or running the generate_bias_report.sh
"""

BIAS_WEAK_INV_UPER_MARGIN_V = "80m"
""" BIAS_WEAK_INV_UPER_MARGIN_V:
Is the uper margin allowed to bias a device at weak inversion region.
This can be edited here or running the generate_bias_report.sh
"""

BIAS_STRONG_INV_LOWER_MARGIN_V = "120m"
""" BIAS_STRONG_INV_LOWER_MARGIN_V:
Is the lower margin allowed to bias a device at strong inversion region.
This can be edited here or running the generate_bias_report.sh
"""

BIAS_WEAK_INV_SAT_MARGIN_V = "120m"
""" BIAS_WEAK_INV_SAT_MARGIN_V:
Is the Vds-Vdsat margin allowed to bias a device at weak inversion region.
This can be edited here or running the generate_bias_report.sh
"""

BIAS_STRONG_INV_SAT_MARGIN_V = "100m"
""" BIAS_STRONG_INV_SAT_MARGIN_V:
Is the Vds-Vdsat margin allowed to bias a device at strong inversion region.
This can be edited here or running the generate_bias_report.sh
"""
