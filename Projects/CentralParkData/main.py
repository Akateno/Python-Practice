import pandas

data =  pandas.read_csv("squirrel_count.csv")
gray_fur_color=len(data[data['Primary Fur Color']=="Gray"])
red_fur_color=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_fur_color=len(data[data["Primary Fur Color"] == "Black"])
print(gray_fur_color, red_fur_color,black_fur_color)

data_dict = {
    "Fur Color": ['Gray', "Cinnamon", "Black"],
    "Count": [gray_fur_color,red_fur_color,black_fur_color]
}

df=pandas.DataFrame(data_dict)
df.to_csv("Squirrel_color_count.csv")