import pandas as pd
import matplotlib.pyplot as plt

# define constants
BJJ = "BJJ"
WRESTLE = "Wrestling"
JUDO = "Judo"

def group_techniques_by_origin(data):
    """
        :param data: This is the pandas DataFrame that was created using the csv file
        This function uses pandas and matplotlib functions to separate the data into groups based on martial art
    """

    # separate the data based on the Origin (get the rows), and then only give the Names
    bjj_tech = data[data["Origin"] == BJJ]["Name"]
    wrestling_tech = data[data["Origin"] == WRESTLE]["Name"]
    judo_tech = data[data["Origin"] == JUDO]["Name"]

    # get the number of rows for each martial art
    bjj_count = bjj_tech.shape[0]
    wrestling_count = wrestling_tech.shape[0]
    judo_count = judo_tech.shape[0]

    # display data and findings
    print("BJJ TECHNIQUE")
    print("******************")
    print(f"In this data, BJJ has {bjj_count} techniques.")
    print()

    print("WRESTLING TECHNIQUE COUNT")
    print("******************")
    print(f"In this data, Wrestling has {wrestling_count} techniques.")
    print()

    print("JUDO TECHNIQUE COUNT")
    print("******************")
    print(f"In this data, Judo has {judo_count} techniques.")
    print()

    print("RESULT/ANALYSIS of Martial Arts Technique Count")
    print("****************************************************")
    print(f"BJJ has the most techniques at {bjj_count}, while Wrestling has {wrestling_count} and Judo has {judo_count}")
    print()

    # creates a pie graph to visualize counts
    x = ["BJJ", "Wrestling", "Judo"]
    y = [bjj_count, wrestling_count, judo_count]
    plt.pie(y, labels=x)
    plt.title("Martial Art Technique Distribution")
    plt.show()


def group_techniques_by_type(data):
    """
        :param data: This is the pandas DataFrame that was created using the csv file
        This function uses pandas and matplotlib functions to separate the data into groups based on Type
    """
    
    # get all the rows in the "Type" column and set up coordinate arrays
    type_data = data["Type"]
    names = []
    counts = []

    types_dict = type_data.value_counts()
    
    # every tech is a tuple like ("Control", 1)
    for tech in types_dict.items():
        name = tech[0]
        count = tech[1]
        names.append(name)
        counts.append(count)
    
    plt.bar(names, counts)

    # xticks and tight_layout used to make the x axis labels diagonal, makes it easier to read
    plt.xticks(rotation=45)
    plt.title("Technique Types")
    plt.tight_layout()
    plt.show()


def group_techniques_by_position(data):
    """
        :param data: This is the pandas DataFrame that was created using the csv file
        This function uses pandas and matplotlib functions to separate dominant vs. defensive techniques
        for each grappling art
    """
    # get the techniques from each martial art
    bjj_tech = data[data["Origin"] == BJJ]["Position"]
    judo_tech = data[data["Origin"] == JUDO]["Position"]
    wrestling_tech = data[data["Origin"] == WRESTLE]["Position"]

    arts = [BJJ, JUDO, WRESTLE]

    # the indexes are BJJ (0), Judo (1), and Wrestling (2)
    dom_data = [0, 0, 0]
    def_data = [0, 0, 0]

    # separate each technique by martial art and position
    for tech in bjj_tech:
        if tech == "Dominant":
            dom_data[0] += 1
        elif tech == "Defensive":
            def_data[0] += 1

    for tech in judo_tech:
        if tech == "Dominant":
            dom_data[1] += 1
        elif tech == "Defensive":
            def_data[1] += 1

    for tech in wrestling_tech:
        if tech == "Dominant":
            dom_data[2] += 1
        elif tech == "Defensive":
            def_data[2] += 1

    # create grouped bar chart
    bar_width = 0.25

    # get the x-axis locations for the bar pairs
    bar_1 = [0, 1, 2]
    bar_2 = [x + bar_width for x in bar_1]
    
    plt.bar(bar_1, dom_data, width = bar_width, label="Dominant")
    plt.bar(bar_2, def_data, width = bar_width, label="Defensive")
    plt.title("Dominant vs. Defensive Techniques")
    plt.xlabel("Martial Arts")
    plt.ylabel("Number of Techniques")

    # add the martial arts labels in the appropriate locations
    plt.xticks([x + (bar_width/2) for x in range(len(bar_1))], 
               ["BJJ", "Judo", "Wrestling"])
    plt.legend()
    plt.show()
    
if __name__ == "__main__":

    try:
        # this creates a DataFrame object with all of the data from the csv file
        grappling_data = pd.read_csv("grappling_techniques.csv")

        group_techniques_by_origin(grappling_data)
        group_techniques_by_type(grappling_data)
        group_techniques_by_position(grappling_data)

    except FileNotFoundError:
        print("File does not exist in appropriate directory")