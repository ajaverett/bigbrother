people = people
people[["f","l"]] = (people["name"].str.split(" ", expand=True))
people["f"] = people["f"].str.slice(0,1)
people["email"] = ((people["f"] + people["l"] + "@byui.edu")
    .str.lower()
    .drop(columns = ["f","l"]))


