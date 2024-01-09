import config


class Device:
    def __init__(self, label: str, model: str, inv_reg: str) -> None:
        if "M" in label:
            self.id = int(label.replace("M", ""))
        elif "SW" in label:
            self.id = int(label.replace("SW", "")) + 1000
        self.label = label
        self.model = model
        self.inv_reg = inv_reg
        self.info_csv = self.read_info_csv()

    def read_info_csv(self) -> str:
        inv_char = self.get_char_inv()
        core_file_name = "backend/core_files/" + self.model + "_" + inv_char + ".csv"
        # Read the core file and replace the info
        with open(core_file_name, "r") as f:
            full_text = f.read()
            full_text = full_text.replace(config.MARK_DEVICE_LABEL_CSV, self.label)
            # Replace weak or strong inv values
            if inv_char == "w":
                full_text = full_text.replace(
                    config.MARK_WEAK_INV_LOWER_CSV, config.BIAS_WEAK_INV_LOWER_MARGIN_V
                )
                full_text = full_text.replace(
                    config.MARK_WEAK_INV_UPER_CSV, config.BIAS_WEAK_INV_UPER_MARGIN_V
                )
                full_text = full_text.replace(
                    config.MARK_WEAK_INV_SAT_CSV, config.BIAS_WEAK_INV_SAT_MARGIN_V
                )
            elif inv_char == "s":
                full_text = full_text.replace(
                    config.MARK_STRONG_INV_LOWER_CSV,
                    config.BIAS_STRONG_INV_LOWER_MARGIN_V,
                )
                full_text = full_text.replace(
                    config.MARK_STRONG_INV_SAT_CSV, config.BIAS_STRONG_INV_SAT_MARGIN_V
                )

        return full_text

    def get_char_inv(self) -> str:
        if self.inv_reg in config.WEAK_INV_REG_VALID_OPTIONS:
            return "w"
        elif self.inv_reg in config.STRONG_INV_REG_VALID_OPTIONS:
            return "s"
        else:  # Error handling for this is @ write_all_devices
            return "ERROR"

    def __str__(self) -> str:
        return "{};{};{}".format(self.label, self.model, self.inv_reg)
