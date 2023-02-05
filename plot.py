import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
file = []
# file.append(pd.read_csv("47.88all.csv"))
# file.append(pd.read_csv("47.88alt.csv"))
# file.append(pd.read_csv("55.0all.csv"))
# file.append(pd.read_csv("55.0alt.csv"))
file.append(pd.read_csv("74.0all.csv"))
file.append(pd.read_csv("74.0alt.csv"))
# file.append(pd.read_csv("83.0all.csv"))
# file.append(pd.read_csv("83.0alt.csv"))
file.append(pd.read_csv("93.5all.csv"))
file.append(pd.read_csv("93.5alt.csv"))
name_str = ["74.0all", "74.0alt", "93.5all", "93.5alt"]

pos_diff_plot = []
for i in range(len(file)):
    partdata = {
        "TRK_Dur(hr)": file[i]["TRK_Dur(hr)"].to_list()[0:8],
        "od-1": file[i]["Drift"][file[i]["od"] == 1].to_list(),
        "od-2": file[i]["Drift"][file[i]["od"] == 2].to_list(),
        "od-3": file[i]["Drift"][file[i]["od"] == 3].to_list(),
        "od-4": file[i]["Drift"][file[i]["od"] == 4].to_list(),
        "od-5": file[i]["Drift"][file[i]["od"] == 5].to_list(),
    }
    df = pd.DataFrame(partdata)
    pos_diff_plot.append(df)
i = 0
for data_frame in pos_diff_plot:
    data_frame.plot(x="TRK_Dur(hr)", y=["od-1", "od-2", "od-3", "od-4", "od-5"], marker='^')
    plt.grid(True)
    # plt.ylim([0, 0.03])
    plt.ylabel("Drift")
    plt.title(f"{name_str[i]} Drift vs TRK_Dur(hr)")
    plt.savefig(f"./graph/{name_str[i]}.png")
    plt.show()
    i = i + 1
