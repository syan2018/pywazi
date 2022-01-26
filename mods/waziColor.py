class waziColor:
    # A true color print class for the console.
    # 一个真色彩的打印类，用于控制台。
    def __init__(self):
        super(waziColor, self).__init__()

    @staticmethod
    def HexToRGB(R, G, B):
        tr = R / 0xff * 255
        tg = G / 0xff * 255
        tb = B / 0xff * 255
        return {"R": str(int(tr)), "G": str(int(tg)), "B": str(int(tb))}

    @staticmethod
    def print(jsons):
        text = ""
        if "color" in jsons:
            text += "\x1b[38;2;" + jsons["color"]["R"] + ";"
            text += jsons["color"]["G"] + ";"
            text += jsons["color"]["B"] + "m"
        if "bgColor" in jsons:
            text += "\x1b[48;2;" + jsons["bgColor"]["R"] + ";"
            text += jsons["bgColor"]["G"] + ";"
            text += jsons["bgColor"]["B"] + "m"
        if "effects" in jsons:
            if "normal" in jsons["effects"]:
                text += "\x1b[0m"
            if "highLight" in jsons["effects"]:
                text += "\x1b[1m"
            if "lowLight" in jsons["effects"]:
                text += "\x1b[2m"
            if "itail" in jsons["effects"]:
                text += "\x1b[3m"
            if "underLine" in jsons["effects"]:
                text += "\x1b[4m"
            if "slowShine" in jsons["effects"]:
                text += "\x1b[5m"
            if "revWhite" in jsons["effects"]:
                text += "\x1b[7m"
            if "hide" in jsons["eff"]:
                text += "\x1b[8m"
            if "delLine" in jsons["eff"]:
                text += "\x1b[9m"
        text += jsons["text"] + "\x1b[0m"
        print(text)
